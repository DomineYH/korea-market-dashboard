#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from korea_market_dashboard.collector import collect_snapshot  # noqa: E402
from korea_market_dashboard.site import build_site  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the Korea market dashboard from a snapshot JSON file or live public data.")
    parser.add_argument("--input", default="", help="Path to collected market snapshot JSON. If omitted, live public data is collected.")
    parser.add_argument("--phase", choices=["manual", "morning", "close"], default="manual", help="Output phase label and phase-specific artifacts")
    parser.add_argument("--root", default=str(ROOT), help="Project root where docs/reports/data are written")
    args = parser.parse_args()

    if args.input:
        input_path = Path(args.input)
        if not input_path.exists():
            raise SystemExit(f"Input snapshot not found: {input_path}")
        snapshot = json.loads(input_path.read_text(encoding="utf-8"))
    else:
        snapshot = collect_snapshot()
    written = build_site(snapshot, Path(args.root), phase=args.phase)
    print(json.dumps(written, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
