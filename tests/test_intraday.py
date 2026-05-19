import unittest

from korea_market_dashboard.intraday import build_close_analysis, render_close_analysis_markdown


class IntradayAnalysisTests(unittest.TestCase):
    def test_build_close_analysis_compares_morning_prediction_with_close_move(self):
        morning = {
            "snapshot": {
                "generated_kst": "2026-05-19T09:00:00+09:00",
                "naver_indices": {"KOSPI": {"now_value": "100.00"}, "KOSDAQ": {"now_value": "200.00"}},
            },
            "prediction": {"short_term": {"label": "하락/조정 우세", "bias": "bearish"}, "total_score": -3.0},
        }
        close = {
            "snapshot": {
                "generated_kst": "2026-05-19T16:00:00+09:00",
                "naver_indices": {"KOSPI": {"now_value": "98.00"}, "KOSDAQ": {"now_value": "201.00"}},
            },
            "prediction": {"short_term": {"label": "하락/조정 우세", "bias": "bearish"}, "total_score": -2.0},
        }

        analysis = build_close_analysis(morning, close)

        self.assertEqual(analysis["phase"], "close")
        self.assertEqual(analysis["morning_prediction_label"], "하락/조정 우세")
        self.assertEqual(analysis["primary_market"], "KOSPI")
        self.assertTrue(analysis["primary_hit"])
        self.assertEqual(analysis["markets"]["KOSPI"]["change_pct"], -2.0)
        self.assertEqual(analysis["markets"]["KOSDAQ"]["change_pct"], 0.5)
        self.assertIn("유지", analysis["adjustment"]["action"])

    def test_render_close_analysis_markdown_contains_prediction_and_result(self):
        analysis = {
            "phase": "close",
            "morning_generated_kst": "2026-05-19T09:00:00+09:00",
            "close_generated_kst": "2026-05-19T16:00:00+09:00",
            "morning_prediction_label": "하락/조정 우세",
            "primary_market": "KOSPI",
            "primary_hit": True,
            "markets": {"KOSPI": {"morning": 100.0, "close": 98.0, "change_pct": -2.0}},
            "adjustment": {"action": "가중치 유지", "reason": "예측 적중"},
        }

        md = render_close_analysis_markdown(analysis)

        self.assertIn("# 오후 4시 당일 장세 분석", md)
        self.assertIn("오전 9시 예측", md)
        self.assertIn("적중", md)
        self.assertIn("가중치 유지", md)


if __name__ == "__main__":
    unittest.main()
