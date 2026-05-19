from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .model import build_prediction_table
from .render import render_dashboard_html, render_report_markdown


def build_site(snapshot: dict[str, Any], root: str | Path) -> dict[str, str]:
    """Build dashboard, Markdown report, and machine-readable data files."""
    project_root = Path(root)
    docs_dir = project_root / "docs"
    reports_dir = project_root / "reports"
    data_dir = project_root / "data"
    docs_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)

    prediction = build_prediction_table(snapshot)
    payload = {"snapshot": snapshot, "prediction": prediction}

    data_path = data_dir / "latest.json"
    report_path = reports_dir / "latest.md"
    dashboard_path = docs_dir / "index.html"

    data_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    report_path.write_text(render_report_markdown(snapshot, prediction), encoding="utf-8")
    dashboard_path.write_text(render_dashboard_html(snapshot, prediction), encoding="utf-8")

    return {"dashboard": str(dashboard_path), "report": str(report_path), "data": str(data_path)}
