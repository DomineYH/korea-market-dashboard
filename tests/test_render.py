import json
import unittest

from korea_market_dashboard.render import render_dashboard_html, render_report_markdown


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.snapshot = {
            "generated_kst": "2026-05-19T09:14:52+09:00",
            "naver_indices": {"KOSPI": {"now_value": "7,372.94"}, "KOSDAQ": {"now_value": "1,112.04"}},
            "investor_flows_억원": {"KOSPI": {"sums_억원": {"5d": {"foreign": -160693}}}},
            "yahoo_market": {
                "KOSPI": {"history": [{"date": "2026-05-15", "close": 7493.18}, {"date": "2026-05-18", "close": 7372.94}]},
                "KOSDAQ": {"history": [{"date": "2026-05-15", "close": 1129.82}, {"date": "2026-05-18", "close": 1112.04}]},
                "KRW per USD": {"latest": 1496.68},
                "Philadelphia SOX": {"1w_change_pct": -6.44},
            },
            "sectors": {"top": [{"sector": "우주항공과국방", "change_pct": 5.38}], "bottom": [{"sector": "반도체와반도체장비", "change_pct": -2.57}]},
        }
        self.prediction = {
            "total_score": -1.6,
            "short_term": {"label": "중립/하락 경계", "confidence": "중간"},
            "medium_term": {"label": "조건부 상승", "confidence": "중간"},
            "signals": [
                {"id": "foreign_kospi_flow", "category": "수급", "factor": "KOSPI 외국인 순매수", "observed": "5D -160,693억", "direction": "하락", "score": -2.0, "weight": "매우 높음", "rationale": "외국인 매도"},
                {"id": "feedback_next_session_adjustment", "category": "피드백", "factor": "전일 09시 예측 vs 마감 장세", "observed": "전일 불일치", "direction": "상승", "score": 0.9, "weight": "동적", "rationale": "전일 실제 상승을 다음 예측에 반영"},
            ],
            "market_models": {
                "KOSPI": {"total_score": -1.6, "short_term": {"label": "중립/하락 경계"}},
                "KOSDAQ": {"total_score": -0.5, "short_term": {"label": "중립/하락 경계"}},
            },
            "backtest": {"markets": {"KOSPI": {"hit_rate": 0.55, "samples": 40, "suggested_weight": 0.4, "best_signal_label": "모멘텀 롱"}}},
            "feedback": {"applied": True, "score_adjustment": 0.9, "summary": "전일 예측 불일치 → 상승 보정"},
        }

    def test_report_markdown_contains_model_table_feedback_and_verdict(self):
        md = render_report_markdown(self.snapshot, self.prediction)
        self.assertIn("# 한국 주식시장 방향성 리포트", md)
        self.assertIn("중립/하락 경계", md)
        self.assertIn("전일 09시 예측 vs 마감 장세", md)
        self.assertIn("조건부 상승", md)
        self.assertIn("## KOSPI/KOSDAQ 분리 모델", md)
        self.assertIn("## 피드백 반영", md)
        self.assertIn("전일 예측 불일치", md)

    def test_dashboard_html_embeds_snapshot_json_model_table_and_feedback(self):
        html = render_dashboard_html(self.snapshot, self.prediction)
        self.assertIn("한국 주식시장 방향성 대시보드", html)
        self.assertIn("window.MARKET_DATA", html)
        self.assertIn("feedback_next_session_adjustment", html)
        self.assertIn("marketChart", html)
        self.assertIn("KOSPI 모델", html)
        self.assertIn("KOSDAQ 모델", html)
        self.assertIn("섹터 신호표", html)
        self.assertIn("피드백 반영", html)
        embedded = html.split("window.MARKET_DATA = ", 1)[1].split(";", 1)[0]
        parsed = json.loads(embedded)
        self.assertEqual(parsed["prediction"]["feedback"]["score_adjustment"], 0.9)


if __name__ == "__main__":
    unittest.main()
