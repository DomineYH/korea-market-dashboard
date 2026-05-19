#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from korea_market_dashboard.site import build_site  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the Korea market dashboard from a snapshot JSON file.")
    parser.add_argument("--input", default="/tmp/korea_market_research_2026-05-19.json", help="Path to collected market snapshot JSON")
    parser.add_argument("--root", default=str(ROOT), help="Project root where docs/reports/data are written")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"Input snapshot not found: {input_path}")
    snapshot = json.loads(input_path.read_text(encoding="utf-8"))
    written = build_site(snapshot, Path(args.root))
    print(json.dumps(written, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
