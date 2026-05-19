from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .backtest import render_backtest_markdown, run_momentum_backtest
from .model import build_market_prediction_tables, build_prediction_table
from .render import render_dashboard_html, render_report_markdown


def _history_by_market(snapshot: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    market = snapshot.get("yahoo_market") or {}
    return {
        "KOSPI": (market.get("KOSPI") or {}).get("history", []) or [],
        "KOSDAQ": (market.get("KOSDAQ") or {}).get("history", []) or [],
    }


def build_site(snapshot: dict[str, Any], root: str | Path) -> dict[str, str]:
    """Build dashboard, Markdown report, backtest report, and data files."""
    project_root = Path(root)
    docs_dir = project_root / "docs"
    reports_dir = project_root / "reports"
    data_dir = project_root / "data"
    docs_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)

    prediction = build_prediction_table(snapshot)
    prediction["market_models"] = build_market_prediction_tables(snapshot)
    backtest = run_momentum_backtest(_history_by_market(snapshot), lookback=20, horizon=5)
    prediction["backtest"] = backtest
    payload = {"snapshot": snapshot, "prediction": prediction}

    data_path = data_dir / "latest.json"
    backtest_data_path = data_dir / "backtest.json"
    report_path = reports_dir / "latest.md"
    backtest_report_path = reports_dir / "backtest.md"
    dashboard_path = docs_dir / "index.html"

    data_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    backtest_data_path.write_text(json.dumps(backtest, ensure_ascii=False, indent=2), encoding="utf-8")
    report_path.write_text(render_report_markdown(snapshot, prediction), encoding="utf-8")
    backtest_report_path.write_text(render_backtest_markdown(backtest), encoding="utf-8")
    dashboard_path.write_text(render_dashboard_html(snapshot, prediction), encoding="utf-8")

    return {
        "dashboard": str(dashboard_path),
        "report": str(report_path),
        "data": str(data_path),
        "backtest_report": str(backtest_report_path),
        "backtest_data": str(backtest_data_path),
    }
