import unittest

from korea_market_dashboard.backtest import render_backtest_markdown, run_momentum_backtest


class BacktestTests(unittest.TestCase):
    def test_run_momentum_backtest_reports_hit_rate_and_suggested_weight(self):
        history = [{"date": f"2026-01-{i:02d}", "close": 100 + i} for i in range(1, 80)]

        result = run_momentum_backtest({"KOSPI": history}, lookback=10, horizon=5)

        kospi = result["markets"]["KOSPI"]
        self.assertGreater(kospi["samples"], 20)
        self.assertGreaterEqual(kospi["hit_rate"], 0.9)
        self.assertGreater(kospi["suggested_weight"], 0)
        self.assertIn("롱", kospi["best_signal_label"])

    def test_render_backtest_markdown_contains_market_rows(self):
        result = {
            "horizon_days": 5,
            "lookback_days": 20,
            "markets": {
                "KOSPI": {"samples": 40, "hit_rate": 0.55, "avg_forward_return": 1.2, "suggested_weight": 0.4, "best_signal_label": "모멘텀 롱"}
            },
        }

        md = render_backtest_markdown(result)

        self.assertIn("# 백테스트 리포트", md)
        self.assertIn("| KOSPI | 40 | 55.00% |", md)
        self.assertIn("모멘텀 롱", md)


if __name__ == "__main__":
    unittest.main()
