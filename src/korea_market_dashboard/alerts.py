from __future__ import annotations

import json
import urllib.request
from pathlib import Path
from typing import Any


def load_previous_payload(path: str | Path) -> dict[str, Any] | None:
    file_path = Path(path)
    if not file_path.exists():
        return None
    try:
        return json.loads(file_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def _short_bias(payload: dict[str, Any] | None) -> str | None:
    if not payload:
        return None
    return (((payload.get("prediction") or {}).get("short_term") or {}).get("bias"))


def _short_label(payload: dict[str, Any] | None) -> str:
    if not payload:
        return "N/A"
    return str((((payload.get("prediction") or {}).get("short_term") or {}).get("label")) or "N/A")


def should_alert(previous: dict[str, Any] | None, current: dict[str, Any]) -> bool:
    """Alert only when a previous short-term bias exists and changes."""
    old_bias = _short_bias(previous)
    new_bias = _short_bias(current)
    return bool(old_bias and new_bias and old_bias != new_bias)


def build_alert(previous: dict[str, Any] | None, current: dict[str, Any], dashboard_url: str) -> dict[str, str]:
    old_label = _short_label(previous)
    new_label = _short_label(current)
    score = (current.get("prediction") or {}).get("total_score", "N/A")
    generated = ((current.get("snapshot") or {}).get("generated_kst")) or ((current.get("prediction") or {}).get("generated_at_utc")) or "N/A"
    content = (
        "📈 한국 증시 방향성 모델 판정 변화 감지\n"
        f"- 단기 판정: {old_label} → {new_label}\n"
        f"- 모델 총점: {score}\n"
        f"- 생성 시각: {generated}\n"
        f"- 대시보드: {dashboard_url}"
    )
    return {"content": content}


def send_discord_webhook(webhook_url: str, message: dict[str, str], timeout: int = 15) -> None:
    data = json.dumps(message, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(webhook_url, data=data, headers={"Content-Type": "application/json", "User-Agent": "korea-market-dashboard/1.0"}, method="POST")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        if response.status >= 300:
            raise RuntimeError(f"Discord webhook returned HTTP {response.status}")
