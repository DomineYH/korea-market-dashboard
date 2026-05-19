from __future__ import annotations

from statistics import mean
from typing import Any


def _pct(a: float, b: float) -> float:
    return (b / a - 1.0) * 100.0 if a else 0.0


def _clean_history(history: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in history or []:
        try:
            close = float(row["close"])
        except (KeyError, TypeError, ValueError):
            continue
        rows.append({"date": str(row.get("date", "")), "close": close})
    return rows


def run_momentum_backtest(history_by_market: dict[str, list[dict[str, Any]]], lookback: int = 20, horizon: int = 5) -> dict[str, Any]:
    """Backtest a transparent price-momentum rule.

    Rule: if the close is above the close `lookback` sessions ago, predict a
    positive return over `horizon` sessions; otherwise predict a negative return.
    This is intentionally simple so the model weight can be audited and later
    replaced by a richer calibration routine.
    """
    markets: dict[str, dict[str, Any]] = {}
    for market, raw_history in history_by_market.items():
        history = _clean_history(raw_history)
        hits = 0
        samples = 0
        forward_returns: list[float] = []
        long_signals = 0
        short_signals = 0
        long_hits = 0
        short_hits = 0
        for idx in range(lookback, len(history) - horizon):
            current = history[idx]["close"]
            past = history[idx - lookback]["close"]
            future = history[idx + horizon]["close"]
            momentum = _pct(past, current)
            forward = _pct(current, future)
            prediction = 1 if momentum >= 0 else -1
            actual = 1 if forward >= 0 else -1
            samples += 1
            forward_returns.append(forward)
            if prediction == 1:
                long_signals += 1
                if actual == prediction:
                    long_hits += 1
            else:
                short_signals += 1
                if actual == prediction:
                    short_hits += 1
            if actual == prediction:
                hits += 1
        hit_rate = hits / samples if samples else 0.0
        suggested_weight = max(0.0, min(1.0, (hit_rate - 0.5) * 2.0))
        if long_signals and (long_hits / long_signals) >= (short_hits / short_signals if short_signals else 0):
            best_signal_label = "모멘텀 롱"
        elif short_signals:
            best_signal_label = "모멘텀 숏"
        else:
            best_signal_label = "표본 부족"
        markets[market] = {
            "samples": samples,
            "hit_rate": round(hit_rate, 4),
            "avg_forward_return": round(mean(forward_returns), 4) if forward_returns else 0.0,
            "suggested_weight": round(suggested_weight, 4),
            "best_signal_label": best_signal_label,
            "lookback_days": lookback,
            "horizon_days": horizon,
        }
    return {"lookback_days": lookback, "horizon_days": horizon, "markets": markets}


def render_backtest_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# 백테스트 리포트",
        "",
        f"- 룩백: {result.get('lookback_days')}거래일",
        f"- 예측 기간: {result.get('horizon_days')}거래일",
        "",
        "| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for market, row in (result.get("markets") or {}).items():
        lines.append(
            f"| {market} | {row.get('samples', 0)} | {float(row.get('hit_rate', 0)):.2%} | "
            f"{float(row.get('avg_forward_return', 0)):.2f}% | {float(row.get('suggested_weight', 0)):.2f} | {row.get('best_signal_label', '')} |"
        )
    lines.extend([
        "",
        "## 해석",
        "",
        "승률이 50%를 초과할수록 해당 시장의 가격 모멘텀 신호에 더 높은 가중치를 부여할 수 있습니다. 현재 구현은 단순 모멘텀 규칙의 1차 검증이며, 향후 수급·환율·금리 신호까지 포함한 다변량 백테스트로 확장 가능합니다.",
    ])
    return "\n".join(lines) + "\n"
