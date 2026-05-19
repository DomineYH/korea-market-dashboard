import unittest

from korea_market_dashboard.model import build_prediction_table, classify_score


class PredictionModelTests(unittest.TestCase):
    def test_classify_score_maps_ranges_to_market_direction(self):
        self.assertEqual(classify_score(3.0)["label"], "상승 우세")
        self.assertEqual(classify_score(0.75)["label"], "중립/상승 경계")
        self.assertEqual(classify_score(-0.75)["label"], "중립/하락 경계")
        self.assertEqual(classify_score(-3.0)["label"], "하락/조정 우세")

    def test_build_prediction_table_scores_known_signals_from_snapshot(self):
        snapshot = {
            "investor_flows_억원": {
                "KOSPI": {
                    "sums_억원": {
                        "5d": {"foreign": -160693, "individual": 140730, "institution_total": 15767},
                        "10d": {"foreign": -333799, "individual": 330134, "institution_total": 1736},
                    }
                },
                "KOSDAQ": {"sums_억원": {"5d": {"foreign": -1428, "institution_total": -3163}}},
            },
            "yahoo_market": {
                "KOSPI": {"1m_change_pct": 25.56, "3m_change_pct": 41.43, "6m_change_pct": 89.52},
                "KRW per USD": {"latest": 1496.68, "1m_change_pct": 2.15},
                "Philadelphia SOX": {"1w_change_pct": -6.44, "1m_change_pct": 18.28},
                "US 10Y yield": {"latest": 4.623, "1m_change_pct": 8.88},
                "VIX": {"latest": 17.82},
                "WTI crude": {"latest": 102.7, "1m_change_pct": 22.48},
            },
            "sectors": {
                "bottom": [
                    {"sector": "반도체와반도체장비", "change_pct": -2.57},
                    {"sector": "자동차", "change_pct": -4.88},
                ],
                "top": [{"sector": "우주항공과국방", "change_pct": 5.38}],
            },
            "bok_base_rate": {"latest": 2.5},
            "news": [
                {"items": [{"title": "반도체 수출 4월 수출 859억 달러 HBM 공급난"}]},
                {"items": [{"title": "원달러 환율 1500원"}]},
            ],
        }

        result = build_prediction_table(snapshot)

        self.assertLess(result["total_score"], 0)
        self.assertEqual(result["short_term"]["label"], "하락/조정 우세")
        self.assertEqual(result["medium_term"]["label"], "조건부 상승")
        self.assertTrue(any(row["id"] == "foreign_kospi_flow" and row["score"] < 0 for row in result["signals"]))
        self.assertTrue(any(row["id"] == "semiconductor_exports_news" and row["score"] > 0 for row in result["signals"]))
        self.assertGreaterEqual(len(result["signals"]), 10)


if __name__ == "__main__":
    unittest.main()
