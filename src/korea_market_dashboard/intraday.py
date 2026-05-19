from __future__ import annotations

import re
from typing import Any


def _num(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(re.sub(r"[^0-9.\-]", "", str(value)))
    except ValueError:
        return None


def _index_value(payload: dict[str, Any], market: str) -> float | None:
    return _num((((payload.get("snapshot") or {}).get("naver_indices") or {}).get(market) or {}).get("now_value"))


def _generated(payload: dict[str, Any]) -> str:
    return str((payload.get("snapshot") or {}).get("generated_kst") or "N/A")


def _prediction_label(payload: dict[str, Any]) -> str:
    return str(((payload.get("prediction") or {}).get("short_term") or {}).get("label") or "N/A")


def _prediction_bias(payload: dict[str, Any]) -> str:
    return str(((payload.get("prediction") or {}).get("short_term") or {}).get("bias") or "neutral")


def _hit_for_bias(bias: str, change_pct: float) -> bool:
    if "bullish" in bias:
        return change_pct > 0
    if "bearish" in bias:
        return change_pct < 0
    return abs(change_pct) <= 0.3


def build_close_analysis(morning_payload: dict[str, Any] | None, close_payload: dict[str, Any]) -> dict[str, Any]:
    """Compare the 09:00 prediction with the 16:00 same-day market move."""
    morning_payload = morning_payload or {}
    markets: dict[str, dict[str, Any]] = {}
    for market in ["KOSPI", "KOSDAQ"]:
        morning_value = _index_value(morning_payload, market)
        close_value = _index_value(close_payload, market)
        if morning_value and close_value:
            change_pct = round((close_value / morning_value - 1.0) * 100.0, 2)
        else:
            change_pct = 0.0
        markets[market] = {"morning": morning_value, "close": close_value, "change_pct": change_pct}

    bias = _prediction_bias(morning_payload)
    primary_market = "KOSPI"
    primary_hit = _hit_for_bias(bias, float(markets[primary_market]["change_pct"]))
    if primary_hit:
        adjustment = {
            "action": "가중치 유지",
            "reason": "오전 9시 예측이 KOSPI 당일 방향과 일치했습니다. 오후 4시 데이터로 최신 리포트와 대시보드를 갱신했습니다.",
            "applied": True,
        }
    else:
        adjustment = {
            "action": "수정 적용: 수급·환율·업종 가중치 재검토 플래그",
            "reason": "오전 9시 예측과 KOSPI 당일 방향이 어긋났습니다. 오후 4시 데이터로 latest 모델을 재계산하고 다음 자동 갱신의 검토 플래그로 남깁니다.",
            "applied": True,
        }

    return {
        "phase": "close",
        "morning_generated_kst": _generated(morning_payload),
        "close_generated_kst": _generated(close_payload),
        "morning_prediction_label": _prediction_label(morning_payload),
        "morning_prediction_bias": bias,
        "close_prediction_label": _prediction_label(close_payload),
        "primary_market": primary_market,
        "primary_hit": primary_hit,
        "markets": markets,
        "adjustment": adjustment,
    }


def render_close_analysis_markdown(analysis: dict[str, Any]) -> str:
    result = "적중" if analysis.get("primary_hit") else "불일치"
    lines = [
        "# 오후 4시 당일 장세 분석",
        "",
        f"- 오전 9시 예측 시각: `{analysis.get('morning_generated_kst', 'N/A')}`",
        f"- 오후 4시 분석 시각: `{analysis.get('close_generated_kst', 'N/A')}`",
        f"- 오전 9시 예측: **{analysis.get('morning_prediction_label', 'N/A')}**",
        f"- 오후 4시 재계산 판정: **{analysis.get('close_prediction_label', 'N/A')}**",
        f"- 1차 판정 결과: **{result}**",
        "",
        "## 당일 지수 변화",
        "",
        "| 시장 | 오전 9시 | 오후 4시 | 변화율 |",
        "|---|---:|---:|---:|",
    ]
    for market, row in (analysis.get("markets") or {}).items():
        lines.append(f"| {market} | {row.get('morning')} | {row.get('close')} | {float(row.get('change_pct', 0)):.2f}% |")
    adjustment = analysis.get("adjustment") or {}
    lines.extend([
        "",
        "## 수정 적용",
        "",
        f"- 조치: **{adjustment.get('action', 'N/A')}**",
        f"- 근거: {adjustment.get('reason', 'N/A')}",
        "",
        "오후 4시 run은 당일 장세를 반영해 `latest` 리포트/대시보드를 다시 계산합니다.",
    ])
    return "\n".join(lines) + "\n"
