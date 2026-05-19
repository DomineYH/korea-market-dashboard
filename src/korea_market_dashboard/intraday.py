from __future__ import annotations

from datetime import datetime
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


def _date_part(value: str) -> str | None:
    if not value or value == "N/A":
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        match = re.search(r"\d{4}-\d{2}-\d{2}", value)
        return match.group(0) if match else None


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


def _feedback_eligibility(
    morning_payload: dict[str, Any],
    morning_generated: str,
    close_generated: str,
    morning_label: str,
    markets: dict[str, dict[str, Any]],
) -> tuple[bool, str, str | None]:
    morning_date = _date_part(morning_generated)
    close_date = _date_part(close_generated)
    kospi = markets.get("KOSPI") or {}
    if not morning_payload:
        return False, "저장된 오전 9시 예측 payload가 없어 피드백 표본에 반영하지 않았습니다.", close_date
    if morning_label == "N/A":
        return False, "오전 9시 예측 판정이 없어 피드백 표본에 반영하지 않았습니다.", close_date
    if kospi.get("morning") is None or kospi.get("close") is None:
        return False, "KOSPI 오전/마감 지수 값이 불완전해 피드백 표본에 반영하지 않았습니다.", close_date
    if not morning_date or not close_date:
        return False, "오전/마감 생성일을 확인할 수 없어 피드백 표본에 반영하지 않았습니다.", close_date
    if morning_date != close_date:
        return False, f"오전 예측일({morning_date})과 마감 분석일({close_date})이 달라 피드백 표본에 반영하지 않았습니다.", close_date
    return True, "동일 거래일 오전 예측과 마감 데이터를 비교했습니다.", close_date


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

    morning_generated = _generated(morning_payload)
    close_generated = _generated(close_payload)
    morning_label = _prediction_label(morning_payload)
    bias = _prediction_bias(morning_payload)
    primary_market = "KOSPI"
    eligible, feedback_reason, trading_date = _feedback_eligibility(morning_payload, morning_generated, close_generated, morning_label, markets)
    primary_hit = _hit_for_bias(bias, float(markets[primary_market]["change_pct"])) if eligible else False
    if not eligible:
        adjustment = {
            "action": "피드백 보류",
            "reason": feedback_reason,
            "applied": False,
        }
    elif primary_hit:
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
        "morning_generated_kst": morning_generated,
        "close_generated_kst": close_generated,
        "trading_date": trading_date,
        "morning_prediction_label": morning_label,
        "morning_prediction_bias": bias,
        "close_prediction_label": _prediction_label(close_payload),
        "primary_market": primary_market,
        "primary_hit": primary_hit,
        "feedback_eligible": eligible,
        "feedback_reason": feedback_reason,
        "markets": markets,
        "adjustment": adjustment,
    }


def render_close_analysis_markdown(analysis: dict[str, Any], next_feedback_state: dict[str, Any] | None = None) -> str:
    if analysis.get("feedback_eligible") is False:
        result = "피드백 보류"
    else:
        result = "적중" if analysis.get("primary_hit") else "불일치"
    lines = [
        "# 오후 4시 당일 장세 분석",
        "",
        f"- 오전 9시 예측 시각: `{analysis.get('morning_generated_kst', 'N/A')}`",
        f"- 오후 4시 분석 시각: `{analysis.get('close_generated_kst', 'N/A')}`",
        f"- 오전 9시 예측: **{analysis.get('morning_prediction_label', 'N/A')}**",
        f"- 오후 4시 재계산 판정: **{analysis.get('close_prediction_label', 'N/A')}**",
        f"- 1차 판정 결과: **{result}**",
        f"- 피드백 반영 가능 여부: **{'가능' if analysis.get('feedback_eligible', True) else '보류'}**",
        f"- 피드백 상태: {analysis.get('feedback_reason', '동일 거래일 오전 예측과 마감 데이터를 비교했습니다.')}",
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
    ])
    if next_feedback_state:
        lines.extend([
            "",
            "## 다음 장세 피드백 반영값",
            "",
            f"- 누적 표본: {next_feedback_state.get('samples', 0)}",
            f"- 누적 적중률: {float(next_feedback_state.get('hit_rate', 0)):.2%}",
            f"- 다음 예측 점수 보정: **{float(next_feedback_state.get('next_session_score_adjustment', 0)):+.2f}**",
            f"- 최근 피드백: {next_feedback_state.get('last_feedback', {}).get('summary', 'N/A')}",
        ])
    lines.extend([
        "",
        "오후 4시 run은 당일 장세를 반영해 `latest` 리포트/대시보드를 다시 계산하고, `data/feedback.json`을 다음 오전 9시 예측에 투입합니다.",
    ])
    return "\n".join(lines) + "\n"
