import json
import unittest

from korea_market_dashboard.render import render_dashboard_html, render_report_markdown


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.snapshot = {
            "generated_kst": "2026-05-19T09:14:52+09:00",
            "naver_indices": {"KOSPI": {"now_value": "7,372.94"}, "KOSDAQ": {"now_value": "1,112.04"}},
            "investor_flows_억원": {"KOSPI": {"sums_억원": {"5d": {"foreign": -160693}}}},
            "yahoo_market": {"KRW per USD": {"latest": 1496.68}, "Philadelphia SOX": {"1w_change_pct": -6.44}},
        }
        self.prediction = {
            "total_score": -2.5,
            "short_term": {"label": "하락/조정 우세", "confidence": "중간~높음"},
            "medium_term": {"label": "조건부 상승", "confidence": "중간"},
            "signals": [
                {"id": "foreign_kospi_flow", "category": "수급", "factor": "KOSPI 외국인 순매수", "observed": "5D -160,693억", "direction": "하락", "score": -2.0, "weight": "매우 높음", "rationale": "외국인 매도"},
                {"id": "semiconductor_exports_news", "category": "펀더멘털", "factor": "반도체/HBM·수출 뉴스", "observed": "긍정", "direction": "상승", "score": 1.5, "weight": "높음", "rationale": "수출 사이클"},
            ],
        }

    def test_report_markdown_contains_model_table_and_verdict(self):
        md = render_report_markdown(self.snapshot, self.prediction)
        self.assertIn("# 한국 주식시장 방향성 리포트", md)
        self.assertIn("하락/조정 우세", md)
        self.assertIn("| 수급 | KOSPI 외국인 순매수 |", md)
        self.assertIn("조건부 상승", md)

    def test_dashboard_html_embeds_snapshot_json_and_model_table(self):
        html = render_dashboard_html(self.snapshot, self.prediction)
        self.assertIn("한국 주식시장 방향성 대시보드", html)
        self.assertIn("window.MARKET_DATA", html)
        self.assertIn("foreign_kospi_flow", html)
        embedded = html.split("window.MARKET_DATA = ", 1)[1].split(";", 1)[0]
        parsed = json.loads(embedded)
        self.assertEqual(parsed["prediction"]["total_score"], -2.5)


if __name__ == "__main__":
    unittest.main()
