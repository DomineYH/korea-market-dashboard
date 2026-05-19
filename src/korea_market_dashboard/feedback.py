from __future__ import annotations

import copy
from datetime import datetime
from typing import Any

from .model import classify_score


def default_feedback_state() -> dict[str, Any]:
    return {
        "version": 1,
        "samples": 0,
        "hits": 0,
        "misses": 0,
        "hit_rate": 0.0,
        "next_session_score_adjustment": 0.0,
        "last_actual_bias": "neutral",
        "last_feedback": {"summary": "아직 피드백 표본 없음"},
    }


def _clamp(value: float, low: float = -1.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _date_part(value: str | None) -> str | None:
    if not value or value == "N/A":
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return value[:10] if len(value) >= 10 else None


def _actual_bias(change_pct: float, neutral_band: float = 0.15) -> str:
    if change_pct > neutral_band:
        return "bullish"
    if change_pct < -neutral_band:
        return "bearish"
    return "neutral"


def _unit_for_bias(bias: str) -> int:
    if "bullish" in bias:
        return 1
    if "bearish" in bias:
        return -1
    return 0


def _summary(hit: bool, predicted: str, actual: str, change_pct: float) -> str:
    result = "적중" if hit else "불일치"
    return f"전일 09시 예측 {result}: 예측={predicted}, 실제={actual}({change_pct:+.2f}%)"


def _unchanged_with_skip(previous_state: dict[str, Any] | None, reason: str) -> dict[str, Any]:
    state = {**default_feedback_state(), **(previous_state or {})}
    state["last_skipped_feedback"] = {"reason": reason}
    return state


def update_feedback_state(previous_state: dict[str, Any] | None, close_analysis: dict[str, Any]) -> dict[str, Any]:
    """Update persistent feedback from a 09:00 prediction vs close comparison.

    The next-session score adjustment is deliberately small and bounded. A hit
    reinforces the observed direction lightly; a miss corrects more strongly
    toward the actual KOSPI direction. Ineligible or duplicate close analyses do
    not increment the persistent sample count.
    """
    if close_analysis.get("feedback_eligible", True) is False:
        return _unchanged_with_skip(previous_state, str(close_analysis.get("feedback_reason") or "피드백 반영 조건을 충족하지 못했습니다."))

    state = {**default_feedback_state(), **(previous_state or {})}
    trading_date = close_analysis.get("trading_date") or _date_part(close_analysis.get("close_generated_kst"))
    previous_trading_date = (state.get("last_feedback") or {}).get("trading_date")
    if trading_date and previous_trading_date == trading_date:
        return _unchanged_with_skip(previous_state, f"이미 {trading_date} 마감 피드백을 반영했습니다.")

    change_pct = float(((close_analysis.get("markets") or {}).get("KOSPI") or {}).get("change_pct", 0.0))
    actual = _actual_bias(change_pct)
    predicted = str(close_analysis.get("morning_prediction_bias") or "neutral")
    hit = bool(close_analysis.get("primary_hit"))

    samples = int(state.get("samples", 0)) + 1
    hits = int(state.get("hits", 0)) + (1 if hit else 0)
    misses = samples - hits

    prior_adjustment = float(state.get("next_session_score_adjustment", 0.0) or 0.0)
    actual_unit = _unit_for_bias(actual)
    impulse = 0.0 if actual_unit == 0 else actual_unit * (0.12 if hit else 0.35)
    next_adjustment = round(_clamp(prior_adjustment * 0.55 + impulse), 2)

    return {
        "version": 1,
        "samples": samples,
        "hits": hits,
        "misses": misses,
        "hit_rate": round(hits / samples, 4) if samples else 0.0,
        "next_session_score_adjustment": next_adjustment,
        "last_actual_bias": actual,
        "last_feedback": {
            "summary": _summary(hit, predicted, actual, change_pct),
            "hit": hit,
            "predicted_bias": predicted,
            "actual_bias": actual,
            "kospi_change_pct": change_pct,
            "close_generated_kst": close_analysis.get("close_generated_kst"),
            "trading_date": trading_date,
        },
    }


def apply_feedback_to_prediction(prediction: dict[str, Any], feedback_state: dict[str, Any] | None) -> dict[str, Any]:
    """Apply the saved close-analysis feedback to the next prediction payload."""
    adjusted = copy.deepcopy(prediction)
    state = {**default_feedback_state(), **(feedback_state or {})}
    score_adjustment = round(float(state.get("next_session_score_adjustment", 0.0) or 0.0), 2)
    if not state.get("samples") or score_adjustment == 0:
        adjusted["feedback"] = {
            "applied": False,
            "score_adjustment": 0.0,
            "summary": "적용 가능한 전일 피드백 없음",
            "samples": int(state.get("samples", 0) or 0),
            "hit_rate": float(state.get("hit_rate", 0.0) or 0.0),
        }
        return adjusted

    direction = "상승" if score_adjustment > 0 else "하락"
    signal = {
        "id": "feedback_next_session_adjustment",
        "category": "피드백",
        "factor": "전일 09시 예측 vs 마감 장세",
        "observed": state.get("last_feedback", {}).get("summary", "전일 피드백"),
        "direction": direction,
        "score": score_adjustment,
        "weight": "동적",
        "rationale": "전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다.",
    }
    adjusted.setdefault("signals", []).append(signal)
    base_total = float(adjusted.get("total_score", 0.0) or 0.0)
    positives = float(adjusted.get("positive_score", 0.0) or 0.0)
    negatives = float(adjusted.get("negative_score", 0.0) or 0.0)
    if score_adjustment > 0:
        positives = round(positives + score_adjustment, 2)
    else:
        negatives = round(negatives + score_adjustment, 2)
    total = round(base_total + score_adjustment, 2)
    adjusted["positive_score"] = positives
    adjusted["negative_score"] = negatives
    adjusted["total_score"] = total
    adjusted["short_term"] = classify_score(total)
    adjusted["feedback"] = {
        "applied": True,
        "score_adjustment": score_adjustment,
        "summary": state.get("last_feedback", {}).get("summary", "전일 피드백 반영"),
        "samples": int(state.get("samples", 0) or 0),
        "hit_rate": float(state.get("hit_rate", 0.0) or 0.0),
        "last_actual_bias": state.get("last_actual_bias", "neutral"),
    }
    return adjusted
