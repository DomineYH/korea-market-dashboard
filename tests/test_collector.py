import unittest

from korea_market_dashboard.collector import parse_google_news_rss, parse_yahoo_chart


class CollectorTests(unittest.TestCase):
    def test_parse_yahoo_chart_computes_changes_and_history(self):
        payload = {
            "chart": {
                "result": [
                    {
                        "meta": {"currency": "KRW", "exchangeName": "KSC", "regularMarketPrice": 130.0},
                        "timestamp": [1700000000, 1700086400, 1700172800, 1700259200, 1700345600, 1700432000],
                        "indicators": {"quote": [{"close": [100.0, 104.0, None, 108.0, 120.0, 130.0]}]},
                    }
                ]
            }
        }

        parsed = parse_yahoo_chart(payload)

        self.assertEqual(parsed["latest"], 130.0)
        self.assertEqual(parsed["1d_change_pct"], 8.33)
        self.assertEqual(parsed["1w_change_pct"], 30.0)
        self.assertEqual(len(parsed["history"]), 5)
        self.assertEqual(parsed["history"][0]["close"], 100.0)

    def test_parse_google_news_rss_extracts_titles_sources_and_links(self):
        xml = """<?xml version='1.0'?><rss><channel>
        <item><title>반도체 수출 호조</title><source>테스트뉴스</source><link>https://example.com/a</link><pubDate>Tue, 19 May 2026 08:00:00 GMT</pubDate></item>
        </channel></rss>""".encode()

        items = parse_google_news_rss(xml, limit=3)

        self.assertEqual(items[0]["title"], "반도체 수출 호조")
        self.assertEqual(items[0]["source"], "테스트뉴스")
        self.assertEqual(items[0]["link"], "https://example.com/a")


if __name__ == "__main__":
    unittest.main()
