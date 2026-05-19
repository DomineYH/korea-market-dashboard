import unittest

from korea_market_dashboard.feedback import apply_feedback_to_prediction, default_feedback_state, update_feedback_state


class FeedbackTests(unittest.TestCase):
    def test_update_feedback_state_strengthens_actual_direction_after_miss(self):
        analysis = {
            "primary_hit": False,
            "feedback_eligible": True,
            "trading_date": "2026-05-19",
            "morning_prediction_bias": "bearish",
            "markets": {"KOSPI": {"change_pct": 1.2}},
            "close_generated_kst": "2026-05-19T16:00:00+09:00",
        }

        state = update_feedback_state(default_feedback_state(), analysis)

        self.assertEqual(state["samples"], 1)
        self.assertEqual(state["hits"], 0)
        self.assertEqual(state["misses"], 1)
        self.assertEqual(state["last_actual_bias"], "bullish")
        self.assertEqual(state["last_feedback"]["trading_date"], "2026-05-19")
        self.assertGreater(state["next_session_score_adjustment"], 0)
        self.assertIn("불일치", state["last_feedback"]["summary"])

    def test_update_feedback_state_reinforces_bearish_hit_more_lightly(self):
        analysis = {
            "primary_hit": True,
            "feedback_eligible": True,
            "trading_date": "2026-05-19",
            "morning_prediction_bias": "bearish",
            "markets": {"KOSPI": {"change_pct": -0.8}},
            "close_generated_kst": "2026-05-19T16:00:00+09:00",
        }

        state = update_feedback_state(default_feedback_state(), analysis)

        self.assertEqual(state["hits"], 1)
        self.assertLess(state["next_session_score_adjustment"], 0)
        self.assertGreater(state["next_session_score_adjustment"], -0.3)

    def test_update_feedback_state_skips_ineligible_close_analysis(self):
        previous = default_feedback_state()
        previous["samples"] = 2
        previous["hits"] = 1
        analysis = {
            "feedback_eligible": False,
            "feedback_reason": "오전 예측일과 마감 분석일이 다름",
            "primary_hit": True,
            "markets": {"KOSPI": {"change_pct": -0.8}},
        }

        state = update_feedback_state(previous, analysis)

        self.assertEqual(state["samples"], 2)
        self.assertEqual(state["hits"], 1)
        self.assertIn("last_skipped_feedback", state)

    def test_update_feedback_state_skips_duplicate_trading_date(self):
        previous = default_feedback_state()
        previous["samples"] = 1
        previous["hits"] = 1
        previous["misses"] = 0
        previous["hit_rate"] = 1.0
        previous["next_session_score_adjustment"] = -0.12
        previous["last_feedback"] = {"summary": "already counted", "trading_date": "2026-05-19"}
        analysis = {
            "primary_hit": False,
            "feedback_eligible": True,
            "trading_date": "2026-05-19",
            "morning_prediction_bias": "bearish",
            "markets": {"KOSPI": {"change_pct": 1.2}},
            "close_generated_kst": "2026-05-19T16:30:00+09:00",
        }

        state = update_feedback_state(previous, analysis)

        self.assertEqual(state["samples"], 1)
        self.assertEqual(state["hits"], 1)
        self.assertEqual(state["next_session_score_adjustment"], -0.12)
        self.assertIn("이미 2026-05-19", state["last_skipped_feedback"]["reason"])

    def test_apply_feedback_to_prediction_adds_feedback_signal_and_reclassifies(self):
        prediction = {
            "total_score": -0.2,
            "positive_score": 1.0,
            "negative_score": -1.2,
            "short_term": {"label": "중립", "bias": "neutral"},
            "signals": [],
        }
        feedback = default_feedback_state()
        feedback["samples"] = 3
        feedback["hits"] = 1
        feedback["misses"] = 2
        feedback["hit_rate"] = 0.3333
        feedback["next_session_score_adjustment"] = 0.9
        feedback["last_actual_bias"] = "bullish"
        feedback["last_feedback"] = {"summary": "전일 예측 불일치 → 상승 보정"}

        adjusted = apply_feedback_to_prediction(prediction, feedback)

        self.assertTrue(adjusted["feedback"]["applied"])
        self.assertEqual(adjusted["feedback"]["score_adjustment"], 0.9)
        self.assertEqual(adjusted["total_score"], 0.7)
        self.assertEqual(adjusted["short_term"]["label"], "중립/상승 경계")
        self.assertTrue(any(row["id"] == "feedback_next_session_adjustment" for row in adjusted["signals"]))


if __name__ == "__main__":
    unittest.main()
