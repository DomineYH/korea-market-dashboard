# 오전 9시 예측 리포트

- 생성 시각: `2026-06-23T09:54:45+09:00`
- 단기 판정: **중립/상승 경계** / 신뢰도: 중간
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **1.0** = 상승 6.0 + 하락 -5.0

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 8,984.90 | 2026-06-23 09:50 |
| KOSDAQ | 934.16 | 2026-06-23 09:07 |
| USD/KRW | 1,538.77 | 1M 1.71% |
| SOX | 1W 9.45% | 1M 23.88% |
| VIX | 17.28 | 위험선호/공포 지표 |
| WTI | 74.06 | 1M -24.63% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 중립/상승 경계 | 조건부 상승 | 1.0 | 6.0 | -5.0 |
| KOSDAQ | 상승 우세 | 상승 우세 | 2.5 | 5.5 | -3.0 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M +24.72%, 3M +56.01%, 6M +118.73% | 상승 | 2.0 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D -41,466억, 10D -35,692억 | 하락 | -1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 57,601억, 기관 5D -14,405억 | 하락 | -1.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,538.77, 1M +1.71% | 하락 | -1.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W +9.45%, 1M +23.88% | 하락 | 1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.509%, 1M -1.38% | 하락 | 0.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 17.28 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 74.06달러, 1M -24.63% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 -4.97% | 하락 | -1.0 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=bullish, 실제=bearish(-0.40%) | 하락 | -0.5 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 219 | 60.73% | 2.52% | 0.21 | 모멘텀 롱 |
| KOSDAQ | 219 | 53.88% | 0.57% | 0.08 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.50**
- 누적 표본: 25
- 누적 적중률: 44.00%
- 최근 피드백: 전일 09시 예측 불일치: 예측=bullish, 실제=bearish(-0.40%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [Kospi Hits Another Record High to Close at 9,114 Amid Iran Negotiations - SBS 뉴스](https://news.google.com/rss/articles/CBMiakFVX3lxTFBET1gwT3drSk9NQXMtaU1jR092ZmpUQXdodWdvZV9XNFJXcWNaYTNNS1d5MURhY2RkQzdDQXJkRUxYNmpyakFDMXVPNldiWDRKS0tmTk94SVVESjBSamJPUmVjR2lVTDNkM1E?oc=5) — SBS 뉴스
- [KOSPI Surges 3.7% to Close at 8788.38 Amid AI Stock Rally and Jensen Huang's Visit - Aju Press](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9pQ2J1V1BCWHdmdnFhSzhvR3B6SHdhVlRTZ0FkcnlWakJfdXREQkI4ZzkxWi1Mel9zbWtBMW0tRXEza1JiVTFxLVZUNkpMZngwU05KbkJRQmtrU1k?oc=5) — Aju Press
- [Nikkei Breaks 67,000 for the First Time, Samsung Soars 7.7%: Why Asia-Pacific Stocks Exploded Higher - TMGM](https://news.google.com/rss/articles/CBMisgFBVV95cUxNR1lUcnJfSUpGa05VWXNMX2t2SWxZTlhoejRnWXI3NXo0RldVMk1BbWMxRG5vR2dKMS1FTnk3cGRIOXNLZ1RZUDZ1YXVBakE4cHoycWZ6N2MtQmItZ2ZNTzQzb0dkRGRjU2dUWFNFWk1yV3gwUFNwaG4wTnRCbzA2V2FqZTJOTXhBVjZZOGlLci15RlRkYlhTc3JGQXRpY2M4Y2QtU3RRVEFKYWJLd283S1Zn?oc=5) — TMGM
- [[Market Insight] Korea Stocks Face Middle East Shock, but Brokers See Volatility as an Entry Point - 한국면세뉴스](https://news.google.com/rss/articles/CBMiakFVX3lxTE9vUnphSi1TMGh2LW16VlRFZV9tZGVGOUhaOVgzZHo1WXZmbEJ4Q0RaY3FiOHZBWmhnWTdlTEZFZmhIR2JESjhPeGIwR0k5T3JnaFk3QU5MelFrODFCOXRTUmdkTDNHZV8zNlE?oc=5) — 한국면세뉴스
- [Korean Cosmetics Stocks Surge on Export Growth and Policy Support - 뷰티경제](https://news.google.com/rss/articles/CBMiakFVX3lxTFAycnYwaWFYOHlBa2hBcDdKZExncHNPV1ZwUTd3Y2IxTFVWaFBUc2lLTmR5QWFja3F6RDMtZXpDc0FGZ3pUdjBOdTZBME0wY1ZybHpYeVh3d3JuTUdJLU9fSmhtZDlPQUxHQnc?oc=5) — 뷰티경제
- [Even amid war, KOSPI reclaims 6000 again···SK hynix sets ‘all-time high’ after a month and a half - 경향신문](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1uUHR4eUFLM0tMeHhJTkR0OXdpQVhId0JZMERvZHBuYVVGMWQwc0hZWVlGOFgwMXZ1TGxiMHlxZFFIMHFWVlNqRGRuQWkzOUlrMzUtT21nanJxLTJvSGc?oc=5) — 경향신문
- [AJP Market Watch: AI boom runs into debt and FX markets in Korea, Japan - 네이트](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9BNnBEazlWbG5ndzFtNTBqMFhtOElJUXRTYVBXRURMa3M0VHRLR1pKRXRSdmk5bGxET2ozb0U2VE1wbWdLUjVnSWdhb2E4LVJBRDhJ?oc=5) — 네이트
- [KOSPI shatters 7,300, outpacing Asia as foreign buying floods chip stocks - 네이트](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9VSmtaNi0xLVFpQXpLNFh2ajBWLWFkTng1UmVFekhPN0ZLcWFKSTFHdUxvWTk1VXgza0dWbW9FenYyejk4VW0zVFE2YWRZa2FVWGww?oc=5) — 네이트

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
