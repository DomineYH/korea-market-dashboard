import json
import tempfile
import unittest
from pathlib import Path

from korea_market_dashboard.site import build_site


class SiteBuildTests(unittest.TestCase):
    def test_build_site_writes_dashboard_report_data_backtest_and_state(self):
        snapshot = {
            "generated_kst": "2026-05-19T09:14:52+09:00",
            "naver_indices": {"KOSPI": {"now_value": "7,372.94"}, "KOSDAQ": {"now_value": "1,112.04"}},
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
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            written = build_site(snapshot, root)
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


if __name__ == "__main__":
    unittest.main()
