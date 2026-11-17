# 오전 9시 예측 리포트

- 생성 시각: `2026-11-17T15:55:14+09:00`
- 단기 판정: **중립/상승 경계** / 신뢰도: 중간
- 중기 판정: **상승 우세** / 신뢰도: 중간~높음
- 총점: **1.3** = 상승 4.0 + 하락 -2.7

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | N/A |  |
| KOSDAQ | N/A |  |
| USD/KRW | 1,337.06 | 1M 0.27% |
| SOX | 1W -4.22% | 1M -13.71% |
| VIX | 22.91 | 위험선호/공포 지표 |
| WTI | 85.09 | 1M -17.91% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 중립/상승 경계 | 상승 우세 | 1.3 | 4.0 | -2.7 |
| KOSDAQ | 중립/상승 경계 | 상승 우세 | 1.3 | 4.0 | -2.7 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M -13.86%, 3M -27.08%, 6M -36.66% | 하락 | -0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D 0억, 10D 0억 | 상승 | 1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 0억, 기관 5D 0억 | 중립 | 0.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,337.06, 1M +0.27% | 하락 | 0.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -4.22%, 1M -13.71% | 하락 | -1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 5.121%, 1M +0.45% | 하락 | -1.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 22.91 | 상승 | 0.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 85.09달러, 1M -17.91% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 +0.00% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=bullish, 실제=neutral(-0.12%) | 하락 | -0.2 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 220 | 58.18% | 0.86% | 0.16 | 모멘텀 롱 |
| KOSDAQ | 220 | 53.64% | -0.44% | 0.07 | 모멘텀 숏 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.20**
- 누적 표본: 91
- 누적 적중률: 39.56%
- 최근 피드백: 전일 09시 예측 불일치: 예측=bullish, 실제=neutral(-0.12%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [South Korea’s Stock Market Plunges as President Lee Marks 500 Days in Office - 최보식의언론](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1LZ1B0clhRelR5LWhNVWJaZElwM0Q1aHlLaXpORGoxZVQwT3ZiRWRzNFdKQzJXZ2pteGpSRjJXZUhxMjRRZG5rV05ZaFIyMkhZVUk3X0RYdFJqWDJPQmljN0ZrMm7SAWhBVV95cUxOaWxMdUgyMFBRN1JtRVEyWE92SzVZV0FyclpPb0ktWG9welVOMHkyalQ3aWRzWDZ4cV9Rd2h2enBxanM1cnQ4cGxMWDlVUzIxaFJlczBQN1ZRR1VFem5RazBzTUNBa193bA?oc=5) — 최보식의언론
- [Will the won-dollar rate fall into the 1,200-won range, or return to the 1,400s? - 경향신문](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9wR284bkpIU2hwUUpVMkV1WjBmWmcydTJpZkZxdHVNSzJXcHM1RmtxSnZhNHRxd0RpdmVyRWxwSVVObE5oSnpCTmJkb3FfSFoyRnBPWnlmMU0zNEdWaVE?oc=5) — 경향신문
- [[Park Su-jin's Money Watch] KOSPI Falls Below 6800 on Sharp Semiconductor Selloff…Analysts Expect Another Push Toward 7000 Next Week - 뉴스워치](https://news.google.com/rss/articles/CBMiakFVX3lxTFBTVmZ0RVl1cUlENG10ajZoUzU5d0FRMXNQUHpoT3RKUFRzcGRxMVI2SVcyQzN2aGNFOW9TVjBydFRVVmNYeFJUSmltSngzaGpUbUk3UjViTEY3LW1GVUdfcG9ObG5sOUVqQUE?oc=5) — 뉴스워치
- [KOSPI closes below 7,000 as foreign selloff outweighs chip exports - 네이트](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5Yb2VseUNiZmdtVHlBdXh0dU1RZUlkYmE1NlVwZmtHN2g5WjBwYUNCbG9BRnZsWWFHd2hoZFFHc1dDQzF2enp4dGQ5VnptS0xndFI0?oc=5) — 네이트
- [Democratic Sweep Boosts Won, Keeps Banks on Alert - IT조선](https://news.google.com/rss/articles/CBMicEFVX3lxTE5lbndpSlc2dHFhN2VxX1c3RWMwQUNKMU5lcl9VOGpSSGlBSHZNMG9UZEk0TUt6aU5zYnFzaC1OQzZ0UEk1dG04NUQzVFliYnpmTVVFeGhjRVl5YUpnOXVSSktIU3hVVjd0T3dobkZGTEXSAXRBVV95cUxPa1JRVTItVkN6cDFuc0p1UnlvREZSYlpPYllkUy1GaElJWnpOSkh2MzNvV3l6NE9Zd3VZWUt5VlB3TU03M0RqRDY4WGNtSk9PVmhwYkRFanRlTVVRb2NsS2dsejlfQjFyeUxXc3E2ZTFRdEJ5Sg?oc=5) — IT조선
- [KOSPI Crashes Below 5,000 Amid U.S. “Blue Tsunami” - 최보식의언론](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9YYWlTNm0zTWQtOUk1T0NBc1RscERZZlNMQ05acjNJREk4Z2x3cmNETzlqXzhwWGI0UmJKRG8wcDNaTUNnVm8zaEx6N0FaWTRNNVJTNFhVZV81MkNWV1RrOHdkZUrSAWhBVV95cUxNV1NURlA2UmRsQklaVXloVGw2dDRFU3pMVmtMcVlrdGFUZXVMY3I4S1RvZ1I0NDVNZzQ2OXczdTBnN0YwTmgzR1V2QlIyMkk0b0lZNUJwZTV0Y3ZKbUdXNlBLdmFnUWJwcw?oc=5) — 최보식의언론
- [KOSPI Tops 3,800 for the First Time Signs of an Improving Korean Economy? - 뷰티경제](https://news.google.com/rss/articles/CBMiakFVX3lxTE5jaHBvd3l1SDQySDZMbHhhOEM5OHZ2czltaWVxNVA2bk9Bb1NwbUw3ZnBUYkdpQXFMeXZqN2lGTXg3MVJiZGhKYWRhbG9xb2UyLTdoSU1NX205WFM2RE5xWE5SanlNMTlJYlE?oc=5) — 뷰티경제
- [이재명 대통령 취임에 코스피 랠리, 허니문 끝나도 이어질까 - Korea JoongAng Daily](https://news.google.com/rss/articles/CBMiYkFVX3lxTFAyUGZQZ2RMZnB4Zm5IOERtemJWNjd1OWdNbFg4aVRpV0huaVlIQU9NMmFNbEJsUjIyUW5BTVZtb25PY2RqTGxhVzNkT2hCZ1ZVM1lqQW1IWi1PSlgtN3Nrb25B?oc=5) — Korea JoongAng Daily

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
