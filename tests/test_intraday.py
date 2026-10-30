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
        self.assertTrue(analysis["feedback_eligible"])
        self.assertEqual(analysis["trading_date"], "2026-05-19")
        self.assertTrue(analysis["primary_hit"])
        self.assertEqual(analysis["markets"]["KOSPI"]["change_pct"], -2.0)
        self.assertEqual(analysis["markets"]["KOSDAQ"]["change_pct"], 0.5)
        self.assertIn("유지", analysis["adjustment"]["action"])

    def test_build_close_analysis_marks_missing_morning_payload_ineligible(self):
        close = {
            "snapshot": {
                "generated_kst": "2026-05-19T16:00:00+09:00",
                "naver_indices": {"KOSPI": {"now_value": "98.00"}, "KOSDAQ": {"now_value": "201.00"}},
            },
            "prediction": {"short_term": {"label": "하락/조정 우세", "bias": "bearish"}, "total_score": -2.0},
        }

        analysis = build_close_analysis(None, close)

        self.assertFalse(analysis["feedback_eligible"])
        self.assertFalse(analysis["adjustment"]["applied"])
        self.assertIn("payload", analysis["feedback_reason"])

    def test_build_close_analysis_marks_stale_morning_payload_ineligible(self):
        morning = {
            "snapshot": {
                "generated_kst": "2026-05-18T09:00:00+09:00",
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

        self.assertFalse(analysis["feedback_eligible"])
        self.assertFalse(analysis["adjustment"]["applied"])
        self.assertIn("달라", analysis["feedback_reason"])

    def test_render_close_analysis_markdown_contains_prediction_and_result(self):
        analysis = {
            "phase": "close",
            "morning_generated_kst": "2026-05-19T09:00:00+09:00",
            "close_generated_kst": "2026-05-19T16:00:00+09:00",
            "morning_prediction_label": "하락/조정 우세",
            "primary_market": "KOSPI",
            "primary_hit": True,
            "feedback_eligible": True,
            "feedback_reason": "동일 거래일 오전 예측과 마감 데이터를 비교했습니다.",
            "markets": {"KOSPI": {"morning": 100.0, "close": 98.0, "change_pct": -2.0}},
            "adjustment": {"action": "가중치 유지", "reason": "예측 적중"},
        }

        md = render_close_analysis_markdown(analysis)

        self.assertIn("# 오후 4시 당일 장세 분석", md)
        self.assertIn("오전 9시 예측", md)
        self.assertIn("적중", md)
        self.assertIn("피드백 반영 가능 여부", md)
        self.assertIn("가중치 유지", md)


class IntradayHardeningTests(unittest.TestCase):
    """2026-10-30 감사 반영: 중립 판정 보류, 변화율 0.0% 가드, Yahoo 폴백, 중립 밴드 확장."""

    @staticmethod
    def _payload(bias, label, kospi_value=None, yahoo_history=None, generated="2026-05-19T09:00:00+09:00"):
        snap = {"generated_kst": generated}
        if kospi_value is not None:
            snap["naver_indices"] = {"KOSPI": {"now_value": kospi_value}, "KOSDAQ": {"now_value": "200.00"}}
        if yahoo_history is not None:
            snap["yahoo_market"] = {
                "KOSPI": {"history": yahoo_history},
                "KOSDAQ": {"history": [{"date": "2026-05-19", "close": 200.0}]},
            }
        return {"snapshot": snap, "prediction": {"short_term": {"label": label, "bias": bias}, "total_score": 0.0}}

    def test_neutral_prediction_is_feedback_hold(self):
        morning = self._payload("neutral", "중립", kospi_value="100.00")
        close = self._payload("bearish", "하락/조정 우세", kospi_value="98.00", generated="2026-05-19T16:00:00+09:00")

        analysis = build_close_analysis(morning, close)

        self.assertFalse(analysis["feedback_eligible"])
        self.assertFalse(analysis["primary_hit"])
        self.assertFalse(analysis["adjustment"]["applied"])
        self.assertIn("중립", analysis["feedback_reason"])

    def test_zero_change_pct_is_ineligible(self):
        morning = self._payload("bullish", "상승 우세", kospi_value="100.00")
        close = self._payload("bullish", "상승 우세", kospi_value="100.00", generated="2026-05-19T16:00:00+09:00")

        analysis = build_close_analysis(morning, close)

        self.assertEqual(analysis["markets"]["KOSPI"]["change_pct"], 0.0)
        self.assertFalse(analysis["feedback_eligible"])
        self.assertIn("0.00%", analysis["feedback_reason"])

    def test_yahoo_history_fallback_when_naver_missing(self):
        morning = self._payload(
            "bearish", "하락/조정 우세",
            yahoo_history=[{"date": "2026-05-16", "close": 99.0}, {"date": "2026-05-19", "close": 100.0}],
        )
        close = self._payload(
            "bearish", "하락/조정 우세",
            yahoo_history=[{"date": "2026-05-19", "close": 98.0}],
            generated="2026-05-19T16:00:00+09:00",
        )

        analysis = build_close_analysis(morning, close)

        self.assertEqual(analysis["markets"]["KOSPI"]["morning"], 100.0)
        self.assertEqual(analysis["markets"]["KOSPI"]["close"], 98.0)
        self.assertEqual(analysis["markets"]["KOSPI"]["change_pct"], -2.0)
        self.assertTrue(analysis["feedback_eligible"])
        self.assertTrue(analysis["primary_hit"])

    def test_neutral_hit_band_widened(self):
        from korea_market_dashboard.intraday import _hit_for_bias

        self.assertTrue(_hit_for_bias("neutral", 0.4))
        self.assertTrue(_hit_for_bias("neutral", -0.49))
        self.assertFalse(_hit_for_bias("neutral", 0.51))
        self.assertFalse(_hit_for_bias("neutral", -0.6))
        self.assertTrue(_hit_for_bias("bullish", 0.01))
        self.assertTrue(_hit_for_bias("bearish", -0.01))


if __name__ == "__main__":
    unittest.main()
