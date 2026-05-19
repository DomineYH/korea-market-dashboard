import json
import tempfile
import unittest
from pathlib import Path

from korea_market_dashboard.alerts import build_alert, load_previous_payload, should_alert


class AlertTests(unittest.TestCase):
    def test_should_alert_when_short_term_bias_changes(self):
        previous = {"prediction": {"short_term": {"label": "하락/조정 우세", "bias": "bearish"}}}
        current = {"prediction": {"short_term": {"label": "상승 우세", "bias": "bullish"}}}

        self.assertTrue(should_alert(previous, current))

    def test_should_not_alert_when_bias_is_unchanged(self):
        previous = {"prediction": {"short_term": {"label": "하락/조정 우세", "bias": "bearish"}}}
        current = {"prediction": {"short_term": {"label": "하락/조정 우세", "bias": "bearish"}}}

        self.assertFalse(should_alert(previous, current))

    def test_build_alert_contains_verdicts_and_dashboard_url(self):
        previous = {"prediction": {"short_term": {"label": "중립", "bias": "neutral"}}}
        current = {"prediction": {"short_term": {"label": "상승 우세", "bias": "bullish"}, "total_score": 3.0}}

        message = build_alert(previous, current, "https://example.com")

        self.assertIn("중립 → 상승 우세", message["content"])
        self.assertIn("https://example.com", message["content"])
        self.assertIn("3.0", message["content"])

    def test_load_previous_payload_returns_none_when_missing_and_json_when_present(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "latest.json"
            self.assertIsNone(load_previous_payload(path))
            path.write_text(json.dumps({"prediction": {"total_score": 1}}), encoding="utf-8")
            self.assertEqual(load_previous_payload(path)["prediction"]["total_score"], 1)


if __name__ == "__main__":
    unittest.main()
