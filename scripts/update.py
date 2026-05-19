#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from korea_market_dashboard.alerts import build_alert, load_previous_payload, send_discord_webhook, should_alert  # noqa: E402
from korea_market_dashboard.collector import collect_snapshot  # noqa: E402
from korea_market_dashboard.site import build_site  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect live public market data, rebuild dashboard, and optionally notify Discord.")
    parser.add_argument("--root", default=str(ROOT), help="Project root where docs/reports/data are written")
    parser.add_argument("--phase", choices=["manual", "morning", "close"], default="manual", help="Run phase: 09:00 prediction, 16:00 close analysis, or manual refresh")
    parser.add_argument("--dashboard-url", default="https://domineyh.github.io/korea-market-dashboard/", help="Public dashboard URL used in alerts")
    parser.add_argument("--snapshot-out", default="", help="Optional path to write raw collected snapshot JSON")
    parser.add_argument("--no-alert", action="store_true", help="Disable Discord alert even if webhook is configured")
    args = parser.parse_args()

    root = Path(args.root)
    previous = load_previous_payload(root / "data" / "latest.json")
    morning_payload = load_previous_payload(root / "data" / "morning.json") if args.phase == "close" else None
    snapshot = collect_snapshot()
    if args.snapshot_out:
        Path(args.snapshot_out).write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
    written = build_site(snapshot, root, phase=args.phase, morning_payload=morning_payload)
    current = load_previous_payload(root / "data" / "latest.json") or {}

    webhook = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    alert_sent = False
    if webhook and not args.no_alert and should_alert(previous, current):
        send_discord_webhook(webhook, build_alert(previous, current, args.dashboard_url))
        alert_sent = True

    print(json.dumps({"phase": args.phase, "written": written, "alert_sent": alert_sent}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
