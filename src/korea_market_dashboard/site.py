from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .backtest import render_backtest_markdown, run_momentum_backtest
from .feedback import apply_feedback_to_prediction, default_feedback_state, update_feedback_state
from .intraday import build_close_analysis, render_close_analysis_markdown
from .model import build_market_prediction_tables, build_prediction_table
from .render import render_dashboard_html, render_report_markdown


PHASE_LABELS = {
    "manual": "수동 갱신",
    "morning": "오전 9시 예측",
    "close": "오후 4시 당일 장세 분석 및 수정 적용",
}


def _history_by_market(snapshot: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    market = snapshot.get("yahoo_market") or {}
    return {
        "KOSPI": (market.get("KOSPI") or {}).get("history", []) or [],
        "KOSDAQ": (market.get("KOSDAQ") or {}).get("history", []) or [],
    }


def _load_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def _load_morning_payload(data_dir: Path) -> dict[str, Any] | None:
    return _load_json(data_dir / "morning.json")


def _load_feedback_state(data_dir: Path) -> dict[str, Any]:
    return _load_json(data_dir / "feedback.json") or default_feedback_state()


def _prefixed_report(title: str, body: str) -> str:
    return f"# {title}\n\n" + body.removeprefix("# 한국 주식시장 방향성 리포트\n\n")


def _build_prediction_with_feedback(snapshot: dict[str, Any], feedback_state: dict[str, Any]) -> dict[str, Any]:
    prediction = apply_feedback_to_prediction(build_prediction_table(snapshot), feedback_state)
    prediction["market_models"] = {
        market: apply_feedback_to_prediction(model, feedback_state)
        for market, model in build_market_prediction_tables(snapshot).items()
    }
    return prediction


def build_site(snapshot: dict[str, Any], root: str | Path, phase: str = "manual", morning_payload: dict[str, Any] | None = None) -> dict[str, str]:
    """Build dashboard, Markdown report, phase reports, feedback state, backtest report, and data files."""
    project_root = Path(root)
    docs_dir = project_root / "docs"
    reports_dir = project_root / "reports"
    data_dir = project_root / "data"
    docs_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)

    phase = phase if phase in PHASE_LABELS else "manual"
    snapshot = dict(snapshot)
    snapshot["run_phase"] = phase
    snapshot["run_phase_label"] = PHASE_LABELS[phase]

    feedback_state = _load_feedback_state(data_dir)
    prediction = _build_prediction_with_feedback(snapshot, feedback_state)
    backtest = run_momentum_backtest(_history_by_market(snapshot), lookback=20, horizon=5)
    prediction["backtest"] = backtest
    prediction["run_phase"] = phase
    prediction["run_phase_label"] = PHASE_LABELS[phase]
    payload = {"snapshot": snapshot, "prediction": prediction}

    next_feedback_state: dict[str, Any] | None = None
    if phase == "close":
        morning_payload = morning_payload or _load_morning_payload(data_dir)
        close_analysis = build_close_analysis(morning_payload, payload)
        next_feedback_state = update_feedback_state(feedback_state, close_analysis)
        prediction["intraday_review"] = close_analysis
        prediction["next_feedback"] = next_feedback_state
        payload = {"snapshot": snapshot, "prediction": prediction}

    data_path = data_dir / "latest.json"
    backtest_data_path = data_dir / "backtest.json"
    report_path = reports_dir / "latest.md"
    backtest_report_path = reports_dir / "backtest.md"
    dashboard_path = docs_dir / "index.html"

    report_markdown = render_report_markdown(snapshot, prediction)
    data_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    backtest_data_path.write_text(json.dumps(backtest, ensure_ascii=False, indent=2), encoding="utf-8")
    report_path.write_text(report_markdown, encoding="utf-8")
    backtest_report_path.write_text(render_backtest_markdown(backtest), encoding="utf-8")
    dashboard_path.write_text(render_dashboard_html(snapshot, prediction), encoding="utf-8")

    written = {
        "dashboard": str(dashboard_path),
        "report": str(report_path),
        "data": str(data_path),
        "backtest_report": str(backtest_report_path),
        "backtest_data": str(backtest_data_path),
    }

    if phase == "morning":
        morning_data_path = data_dir / "morning.json"
        morning_report_path = reports_dir / "morning-prediction.md"
        morning_data_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        morning_report_path.write_text(_prefixed_report("오전 9시 예측 리포트", report_markdown), encoding="utf-8")
        written["morning_data"] = str(morning_data_path)
        written["morning_report"] = str(morning_report_path)

    if phase == "close":
        analysis = prediction["intraday_review"]
        close_data_path = data_dir / "close-analysis.json"
        close_report_path = reports_dir / "close-analysis.md"
        feedback_data_path = data_dir / "feedback.json"
        close_data_path.write_text(json.dumps(analysis, ensure_ascii=False, indent=2), encoding="utf-8")
        close_report_path.write_text(render_close_analysis_markdown(analysis, next_feedback_state), encoding="utf-8")
        feedback_data_path.write_text(json.dumps(next_feedback_state, ensure_ascii=False, indent=2), encoding="utf-8")
        written["close_analysis_data"] = str(close_data_path)
        written["close_analysis_report"] = str(close_report_path)
        written["feedback_data"] = str(feedback_data_path)

    return written
