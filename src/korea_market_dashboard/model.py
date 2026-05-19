from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class Signal:
    id: str
    category: str
    factor: str
    observed: str
    direction: str
    score: float
    weight: str
    rationale: str


def _num(value: Any, default: float = 0.0) -> float:
    if value is None:
        return default
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).replace(",", "").replace("%", "").strip())
    except (TypeError, ValueError):
        return default


def _path(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    cur: Any = data
    for key in keys:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def _news_text(data: dict[str, Any]) -> str:
    titles: list[str] = []
    for group in data.get("news", []) or []:
        for item in group.get("items", []) or []:
            titles.append(str(item.get("title", "")))
    return " ".join(titles)


def classify_score(score: float) -> dict[str, Any]:
    """Classify an aggregate short-term score into a human label."""
    if score >= 2.0:
        return {"label": "상승 우세", "confidence": "중간~높음", "bias": "bullish"}
    if score >= 0.5:
        return {"label": "중립/상승 경계", "confidence": "중간", "bias": "mild_bullish"}
    if score <= -2.0:
        return {"label": "하락/조정 우세", "confidence": "중간~높음", "bias": "bearish"}
    if score <= -0.5:
        return {"label": "중립/하락 경계", "confidence": "중간", "bias": "mild_bearish"}
    return {"label": "중립", "confidence": "낮음~중간", "bias": "neutral"}


def build_prediction_table(data: dict[str, Any], market: str = "KOSPI") -> dict[str, Any]:
    """Build the directional prediction table from a collected market snapshot.

    `market` may be KOSPI or KOSDAQ. The default preserves the original KOSPI-
    weighted aggregate model, while separate market models let the dashboard
    expose large-cap and growth-board direction independently.
    """
    market = market.upper()
    flow_market = market if market in {"KOSPI", "KOSDAQ"} else "KOSPI"
    flow = _path(data, "investor_flows_억원", flow_market, "sums_억원", default={}) or {}
    foreign_5d = _num(_path(flow, "5d", "foreign"))
    foreign_10d = _num(_path(flow, "10d", "foreign"))
    individual_5d = _num(_path(flow, "5d", "individual"))
    institution_5d = _num(_path(flow, "5d", "institution_total"))

    index_1m = _num(_path(data, "yahoo_market", flow_market, "1m_change_pct"))
    index_3m = _num(_path(data, "yahoo_market", flow_market, "3m_change_pct"))
    index_6m = _num(_path(data, "yahoo_market", flow_market, "6m_change_pct"))
    krw = _num(_path(data, "yahoo_market", "KRW per USD", "latest"))
    krw_1m = _num(_path(data, "yahoo_market", "KRW per USD", "1m_change_pct"))
    sox_1w = _num(_path(data, "yahoo_market", "Philadelphia SOX", "1w_change_pct"))
    sox_1m = _num(_path(data, "yahoo_market", "Philadelphia SOX", "1m_change_pct"))
    us10y = _num(_path(data, "yahoo_market", "US 10Y yield", "latest"))
    us10y_1m = _num(_path(data, "yahoo_market", "US 10Y yield", "1m_change_pct"))
    vix = _num(_path(data, "yahoo_market", "VIX", "latest"))
    oil = _num(_path(data, "yahoo_market", "WTI crude", "latest"))
    oil_1m = _num(_path(data, "yahoo_market", "WTI crude", "1m_change_pct"))
    base_rate = _num(_path(data, "bok_base_rate", "latest"))

    bottom_sectors = {str(row.get("sector")): _num(row.get("change_pct")) for row in data.get("sectors", {}).get("bottom", []) or []}
    top_sectors = {str(row.get("sector")): _num(row.get("change_pct")) for row in data.get("sectors", {}).get("top", []) or []}
    news = _news_text(data)

    signals: list[Signal] = []
    trend_score = 2.0 if index_1m > 5 and index_3m > 10 else (0.5 if index_6m > 0 else -0.5)
    signals.append(Signal(
        f"trend_{flow_market.lower()}", "가격/추세", f"{flow_market} 중기 모멘텀", f"1M {index_1m:+.2f}%, 3M {index_3m:+.2f}%, 6M {index_6m:+.2f}%",
        "상승" if trend_score > 0 else "하락", trend_score, "높음", "지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다."
    ))
    flow_threshold = -50000 if flow_market == "KOSPI" else -5000
    foreign_score = -2.0 if foreign_5d < flow_threshold else (-1.0 if foreign_5d < 0 else 1.0)
    signals.append(Signal(
        f"foreign_{flow_market.lower()}_flow", "수급", f"{flow_market} 외국인 순매수", f"5D {foreign_5d:,.0f}억, 10D {foreign_10d:,.0f}억",
        "상승" if foreign_score > 0 else "하락", foreign_score, "매우 높음", "한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다."
    ))
    retail_threshold = 50000 if flow_market == "KOSPI" else 5000
    retail_score = -1.0 if individual_5d > retail_threshold and foreign_5d < 0 else 0.0
    signals.append(Signal(
        f"retail_{flow_market.lower()}_absorption", "수급", f"{flow_market} 개인 순매수 방어", f"개인 5D {individual_5d:,.0f}억, 기관 5D {institution_5d:,.0f}억",
        "하락" if retail_score < 0 else "중립", retail_score, "중간", "외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다."
    ))
    signals.append(Signal(
        "fx_krw", "환율", "USD/KRW", f"{krw:,.2f}, 1M {krw_1m:+.2f}%",
        "하락", -1.5 if krw >= 1450 and krw_1m > 0 else (-0.5 if krw >= 1400 else 0.5), "높음", "원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다."
    ))
    signals.append(Signal(
        "sox_short_term", "글로벌/반도체", "Philadelphia SOX 단기 흐름", f"1W {sox_1w:+.2f}%, 1M {sox_1m:+.2f}%",
        "하락", -1.0 if sox_1w < -3 else (1.0 if sox_1w > 3 else 0.0), "높음", "한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다."
    ))
    signals.append(Signal(
        "semiconductor_exports_news", "펀더멘털", "반도체/HBM·수출 뉴스", "수출·반도체·HBM 긍정 키워드 확인" if any(k in news for k in ["반도체", "HBM", "수출"]) else "긍정 키워드 부족",
        "상승", 1.5 if any(k in news for k in ["반도체", "HBM", "수출"]) else 0.0, "높음", "한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다."
    ))
    signals.append(Signal(
        "us_rates", "금리", "미국 10년물", f"{us10y:.3f}%, 1M {us10y_1m:+.2f}%",
        "하락", -1.0 if us10y >= 4.5 and us10y_1m > 0 else 0.0, "중간~높음", "미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다."
    ))
    signals.append(Signal(
        "risk_vix", "리스크", "VIX", f"{vix:.2f}",
        "상승", 1.0 if 0 < vix < 20 else (-1.0 if vix >= 25 else 0.0), "중간", "VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다."
    ))
    signals.append(Signal(
        "oil", "원자재", "WTI 유가", f"{oil:.2f}달러, 1M {oil_1m:+.2f}%",
        "하락", -1.0 if oil >= 95 or oil_1m > 15 else 0.0, "중간", "고유가는 한국의 비용·무역수지·물가 부담을 키운다."
    ))
    semi_sector = bottom_sectors.get("반도체와반도체장비", top_sectors.get("반도체와반도체장비", 0.0))
    auto_sector = bottom_sectors.get("자동차", top_sectors.get("자동차", 0.0))
    signals.append(Signal(
        "domestic_lead_sectors", "업종", "반도체/자동차 장중 흐름", f"반도체 {semi_sector:+.2f}%, 자동차 {auto_sector:+.2f}%",
        "하락" if semi_sector < -1 or auto_sector < -2 else "상승", -1.0 if semi_sector < -1 or auto_sector < -2 else 0.5, "높음", "KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다."
    ))
    signals.append(Signal(
        "bok_rate", "국내금리", "한국은행 기준금리", f"{base_rate:.2f}%" if base_rate else "확인 제한",
        "상승", 0.5 if 0 < base_rate <= 2.75 else 0.0, "중간", "국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다."
    ))

    total = round(sum(s.score for s in signals), 2)
    positives = round(sum(s.score for s in signals if s.score > 0), 2)
    negatives = round(sum(s.score for s in signals if s.score < 0), 2)
    short_term = classify_score(total)

    medium_score = total + 2.0
    if any(k in news for k in ["반도체", "HBM", "수출"]) and (index_3m > 10 or index_6m > 15):
        medium = {"label": "조건부 상승", "confidence": "중간", "bias": "conditional_bullish"}
    else:
        medium = classify_score(medium_score)

    return {
        "market": flow_market,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_score": total,
        "positive_score": positives,
        "negative_score": negatives,
        "short_term": short_term,
        "medium_term": medium,
        "signals": [asdict(signal) for signal in signals],
        "method": {
            "horizon_short": "1~5거래일",
            "horizon_medium": "1~3개월",
            "score_rule": "각 신호를 -2.0~+2.0 범위로 점수화해 단기 방향성을 합산한다.",
        },
    }


def build_market_prediction_tables(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Return separate KOSPI and KOSDAQ models for dashboard comparison."""
    return {"KOSPI": build_prediction_table(data, "KOSPI"), "KOSDAQ": build_prediction_table(data, "KOSDAQ")}
