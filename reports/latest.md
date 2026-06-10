# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-06-10T17:26:37+09:00`
- 단기 판정: **하락/조정 우세** / 신뢰도: 중간~높음
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **-3.67** = 상승 2.83 + 하락 -6.5

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 7,730.82 | 2026-06-10 17:10 |
| KOSDAQ | 951.63 | 2026-06-10 15:37 |
| USD/KRW | 1,525.49 | 1M 3.46% |
| SOX | 1W -0.45% | 1M 15.64% |
| VIX | 20.22 | 위험선호/공포 지표 |
| WTI | 88.49 | 1M -9.77% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 하락/조정 우세 | 조건부 상승 | -3.67 | 2.83 | -6.5 |
| KOSDAQ | 중립 | 상승 우세 | 0.33 | 3.83 | -3.5 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M +3.21%, 3M +38.42%, 6M +96.88% | 상승 | 0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D -144,759억, 10D -276,341억 | 하락 | -2.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 152,479억, 기관 5D -13,340억 | 하락 | -1.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,525.49, 1M +3.46% | 하락 | -1.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -0.45%, 1M +15.64% | 하락 | 0.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.552%, 1M +3.64% | 하락 | -1.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 20.22 | 상승 | 0.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 88.49달러, 1M -9.77% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 -6.45%, 자동차 +0.00% | 하락 | -1.0 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=mild_bearish, 실제=bullish(+4.86%) | 상승 | 0.33 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 219 | 61.64% | 2.31% | 0.23 | 모멘텀 롱 |
| KOSDAQ | 219 | 55.25% | 0.60% | 0.10 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **+0.33**
- 누적 표본: 16
- 누적 적중률: 43.75%
- 최근 피드백: 전일 09시 예측 불일치: 예측=mild_bearish, 실제=bullish(+4.86%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [韓 증시, 월요일 환율 급등·반도체 충격 긴장 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTE1jWHFkaXM0YjNRRTFMR2ZpM2NBZkpFSEt5VU5WUWNsOFVSTjdXOFVnanJucHl6ZG9LUWp3UmhnTWN0cUxHSkhMWER4LVpGenBTcFBsajNldE54Xy0wWDZLTGlKamFpeGJOTWFlRWJPbFVLNzTSAXdBVV95cUxQMUVYS1RYdGJ1aWZjdWVzS05DTWtRYjVxSlFZUGx2aFVsVEVHclRvWF9BcVMyekg1MFZGeEs0WWN4MGY0dVB4cTN2Y3l0b0p3MDFwZE5mRFIxRGRDM282ODFyM0duZTZGUEQ2cF9yN09YOHQwU09sWQ?oc=5) — 스트레이트뉴스
- ['검은 월요일' 충격파 얼마나…美 지수선물·환율 시장 보며 '대응' - 뉴스1](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBjeF9xVkdDZTlxZl93d3M2XzNGMzBSbHU0VUhDak9POEQwSXRwMmwtb0pWbXJ2V3ljUVhGMnpYcjUybzBKUHJsY1V4U1hPTUZSRUJVMzl6MkRfTF9ESGM0dEVqNWY?oc=5) — 뉴스1
- [뉴욕발 반도체 급락에 코스피 7500선 공방 - mstoday.co.kr](https://news.google.com/rss/articles/CBMibEFVX3lxTE9TODBad2ItUGRGZEZqeUhQb0RWd19lWUdTbEJfTFBhQ2ZMdy1Pd3dfLUJUdk5vSHNWemlVbGtmMUxzYjdZbnJaSnNVdXhVNTlpNjZMbHF1dkZCWEtNVFR6MFpiWVJ1Wm9hSnZkNw?oc=5) — mstoday.co.kr
- [외국인 20일째 매도 폭탄에 코스피 5%대 급락…반도체 쇼크와 고환율 직격탄 - 2news.co.kr](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBhSFplenl5VnZGRFJ6c25TOWExM1RuN1lJSGlKMlFHYmpDLVZHOUZRQ2xBcWZRR3VsanhIcUt5akpPUFRuYi05cVZOOFBJUzV5WXJyaFFXbWk1VHRIREd5RFNYRzZIWVE?oc=5) — 2news.co.kr
- [외국인 19일간 '66조 코스피' 매도···1530원 고환율에 수급 불안 가중 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1CZC1NVWFUeGVtdUlMRmxWQTJ3R1NzZlNsN0dWNmxVMU9jdmNNdjBnTTlkMTJsakdWYTFtSU9VSFQ0djFWRnFXMGJReFVENTdXSWZwTlhMb1NrQm9z?oc=5) — 뉴스핌
- ["삼전·하닉 사도 원화는 안 사"…치솟는 환율, 무슨 일이 [빈난새의 빈틈없이월가] - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE4ydEc3WXlKaHNLcDRESnEzeGI0Tm9Fd0dBY2VlN29aNEZGOFZRR2REcXFqemVOdHhrWHprMEtnWHRBM3phWVJLWm5HSVItWUpwUkFLZzVXX25FQdIBVEFVX3lxTE1jZGpwVXdyTWhFbjVUZHpZMjJsVmpnRlZTSGszTW5tWEh3WmJkbWp5VTJSbjJUM2w2OE5RWHJCcjUya056Y0dfSlRXaXMzVlpjYURveg?oc=5) — 한국경제
- [환율 1540원·외인 매도 폭탄…코스피 5% 급락 - mstoday.co.kr](https://news.google.com/rss/articles/CBMib0FVX3lxTE1LQW9nSlhlMTJQcXdaWldydDljUEtzNmdEVzhESnNfUHQ5WjQwUVphdFJuT1ZFV0NvX0t5TG9GWklSOXZuaW01MG8yRV8xNnhRU1BlMjh6cTItaU1LZnRkWmZ1STRTQmt2bl9STHNBaw?oc=5) — mstoday.co.kr
- [삼성전자·SK하이닉스 급락에도…골드만삭스 "코스피 12000 간다" - TopStarNews](https://news.google.com/rss/articles/CBMickFVX3lxTFBlV0Rtckg0cm5BVDQ4WF8tMmZldEwzeF9peHZmRkJtWDhvSThaSzZ2dWxtbGl4b1FJYk5PWmJnYmxvOEtuRGM4NzUzR2d4bVp2Q0U1ZDI1b0ZPMXFIRldxd0kyVEprbzE1b2E1YWU5WnpYUQ?oc=5) — TopStarNews

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
