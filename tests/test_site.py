import json
import tempfile
import unittest
from pathlib import Path

from korea_market_dashboard.site import build_site


def snapshot(kospi="7,372.94", kosdaq="1,112.04", generated="2026-05-19T09:14:52+09:00"):
    return {
        "generated_kst": generated,
        "naver_indices": {"KOSPI": {"now_value": kospi}, "KOSDAQ": {"now_value": kosdaq}},
        "investor_flows_억원": {
            "KOSPI": {"sums_억원": {"5d": {"foreign": -160693, "individual": 140730}, "10d": {"foreign": -333799}}},
            "KOSDAQ": {"sums_억원": {"5d": {"foreign": -1428, "individual": 5704}, "10d": {"foreign": 10126}}},
        },
        "yahoo_market": {
            "KOSPI": {"1m_change_pct": 25.56, "3m_change_pct": 41.43, "6m_change_pct": 89.52, "history": [{"date": f"2026-01-{i:02d}", "close": 100 + i} for i in range(1, 80)]},
            "KOSDAQ": {"1m_change_pct": 0.71, "3m_change_pct": 0.2, "6m_change_pct": 28.86, "history": [{"date": f"2026-01-{i:02d}", "close": 200 - i} for i in range(1, 80)]},
            "KRW per USD": {"latest": 1496.68, "1m_change_pct": 2.15},
            "Philadelphia SOX": {"1w_change_pct": -6.44, "1m_change_pct": 18.28},
            "US 10Y yield": {"latest": 4.623, "1m_change_pct": 8.88},
            "VIX": {"latest": 17.82},
            "WTI crude": {"latest": 102.7, "1m_change_pct": 22.48},
        },
        "sectors": {"top": [{"sector": "우주항공과국방", "change_pct": 5.38}], "bottom": [{"sector": "반도체와반도체장비", "change_pct": -2.57}]},
        "bok_base_rate": {"latest": 2.5},
        "news": [{"items": [{"title": "반도체 수출 HBM", "link": "https://example.com", "source": "example"}]}],
    }


class SiteBuildTests(unittest.TestCase):
    def test_build_site_writes_common_dashboard_report_data_backtest_and_state(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            written = build_site(snapshot(), root)
            self.assertTrue((root / "docs" / "index.html").exists())
            self.assertTrue((root / "reports" / "latest.md").exists())
            self.assertTrue((root / "reports" / "backtest.md").exists())
            self.assertTrue((root / "data" / "latest.json").exists())
            self.assertTrue((root / "data" / "backtest.json").exists())
            self.assertEqual(set(written), {"dashboard", "report", "data", "backtest_report", "backtest_data"})
            data = json.loads((root / "data" / "latest.json").read_text(encoding="utf-8"))
            self.assertIn("prediction", data)
            self.assertIn("market_models", data["prediction"])
            self.assertIn("backtest", data["prediction"])
            self.assertLess(data["prediction"]["total_score"], 0)

    def test_build_site_morning_phase_writes_morning_prediction_copy(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            written = build_site(snapshot(generated="2026-05-19T09:00:00+09:00"), root, phase="morning")
            self.assertTrue((root / "reports" / "morning-prediction.md").exists())
            self.assertTrue((root / "data" / "morning.json").exists())
            self.assertIn("morning_report", written)
            payload = json.loads((root / "data" / "morning.json").read_text(encoding="utf-8"))
            self.assertEqual(payload["snapshot"]["run_phase"], "morning")

    def test_build_site_close_phase_writes_close_analysis_and_feedback_state(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            morning_written = build_site(snapshot(kospi="100.00", kosdaq="200.00", generated="2026-05-19T09:00:00+09:00"), root, phase="morning")
            morning_payload = json.loads(Path(morning_written["morning_data"]).read_text(encoding="utf-8"))
            written = build_site(snapshot(kospi="98.00", kosdaq="201.00", generated="2026-05-19T16:00:00+09:00"), root, phase="close", morning_payload=morning_payload)
            self.assertTrue((root / "reports" / "close-analysis.md").exists())
            self.assertTrue((root / "data" / "close-analysis.json").exists())
            self.assertTrue((root / "data" / "feedback.json").exists())
            self.assertIn("feedback_data", written)
            analysis = json.loads((root / "data" / "close-analysis.json").read_text(encoding="utf-8"))
            self.assertEqual(analysis["phase"], "close")
            self.assertTrue(analysis["feedback_eligible"])
            self.assertIn("primary_hit", analysis)
            feedback = json.loads((root / "data" / "feedback.json").read_text(encoding="utf-8"))
            self.assertEqual(feedback["samples"], 1)
            self.assertIn("next_session_score_adjustment", feedback)

    def test_build_site_close_phase_does_not_count_stale_or_duplicate_feedback(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            stale_morning_payload = {
                "snapshot": {"generated_kst": "2026-05-18T09:00:00+09:00", "naver_indices": {"KOSPI": {"now_value": "100.00"}, "KOSDAQ": {"now_value": "200.00"}}},
                "prediction": {"short_term": {"label": "하락/조정 우세", "bias": "bearish"}, "total_score": -3.0},
            }
            build_site(snapshot(kospi="98.00", kosdaq="201.00", generated="2026-05-19T16:00:00+09:00"), root, phase="close", morning_payload=stale_morning_payload)
            feedback = json.loads((root / "data" / "feedback.json").read_text(encoding="utf-8"))
            self.assertEqual(feedback["samples"], 0)
            self.assertIn("last_skipped_feedback", feedback)

            morning_payload = {
                "snapshot": {"generated_kst": "2026-05-19T09:00:00+09:00", "naver_indices": {"KOSPI": {"now_value": "100.00"}, "KOSDAQ": {"now_value": "200.00"}}},
                "prediction": {"short_term": {"label": "하락/조정 우세", "bias": "bearish"}, "total_score": -3.0},
            }
            build_site(snapshot(kospi="98.00", kosdaq="201.00", generated="2026-05-19T16:00:00+09:00"), root, phase="close", morning_payload=morning_payload)
            build_site(snapshot(kospi="97.00", kosdaq="202.00", generated="2026-05-19T16:30:00+09:00"), root, phase="close", morning_payload=morning_payload)
            feedback = json.loads((root / "data" / "feedback.json").read_text(encoding="utf-8"))
            self.assertEqual(feedback["samples"], 1)

    def test_next_morning_applies_feedback_from_previous_close(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            # Create a missed bearish prediction, so feedback should push the next session score upward.
            morning_payload = {
                "snapshot": {"generated_kst": "2026-05-19T09:00:00+09:00", "naver_indices": {"KOSPI": {"now_value": "100.00"}, "KOSDAQ": {"now_value": "200.00"}}},
                "prediction": {"short_term": {"label": "하락/조정 우세", "bias": "bearish"}, "total_score": -3.0},
            }
            build_site(snapshot(kospi="102.00", kosdaq="202.00", generated="2026-05-19T16:00:00+09:00"), root, phase="close", morning_payload=morning_payload)
            written = build_site(snapshot(generated="2026-05-20T09:00:00+09:00"), root, phase="morning")
            payload = json.loads(Path(written["morning_data"]).read_text(encoding="utf-8"))
            self.assertTrue(payload["prediction"]["feedback"]["applied"])
            self.assertGreater(payload["prediction"]["feedback"]["score_adjustment"], 0)
            self.assertTrue(any(row["id"] == "feedback_next_session_adjustment" for row in payload["prediction"]["signals"]))


if __name__ == "__main__":
    unittest.main()
