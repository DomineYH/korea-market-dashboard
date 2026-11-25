# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-11-25T16:21:46+09:00`
- 단기 판정: **중립/상승 경계** / 신뢰도: 중간
- 중기 판정: **상승 우세** / 신뢰도: 중간~높음
- 총점: **1.23** = 상승 4.0 + 하락 -2.77

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | N/A |  |
| KOSDAQ | N/A |  |
| USD/KRW | 1,342 | 1M 1.30% |
| SOX | 1W -8.40% | 1M -20.31% |
| VIX | 26.36 | 위험선호/공포 지표 |
| WTI | 80.68 | 1M -19.24% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 중립/상승 경계 | 상승 우세 | 1.23 | 4.0 | -2.77 |
| KOSDAQ | 중립/상승 경계 | 상승 우세 | 1.23 | 4.0 | -2.77 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M -16.69%, 3M -29.86%, 6M -39.90% | 하락 | -0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D 0억, 10D 0억 | 상승 | 1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 0억, 기관 5D 0억 | 중립 | 0.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,342.00, 1M +1.30% | 하락 | 0.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -8.40%, 1M -20.31% | 하락 | -1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.904%, 1M -1.64% | 하락 | 0.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 26.36 | 상승 | -1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 80.68달러, 1M -19.24% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 +0.00% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=mild_bullish, 실제=bearish(-0.23%) | 하락 | -0.27 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 220 | 58.18% | 0.64% | 0.16 | 모멘텀 롱 |
| KOSDAQ | 220 | 54.09% | -0.54% | 0.08 | 모멘텀 숏 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.27**
- 누적 표본: 95
- 누적 적중률: 40.00%
- 최근 피드백: 전일 09시 예측 불일치: 예측=mild_bullish, 실제=bearish(-0.23%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [[주간시황] AI 투심 냉각에 나스닥 7.7% 급락…코스피도 반도체 약세에 '휘청' : 네이버 블로그 - Naver Blog](https://news.google.com/rss/articles/CBMijwFBVV95cUxPdGJIb2pYZWV0bnFRRXBLTEFrNlo1WE51b2xsMlJRTWt3a3lWTThWSWhuaXVoUlVZNTN3UXl2M3U0eUJTU1JYYXhKRVdPbEh6RS1vaTB6RlBubGltY3ZuanRZajNHMnQwUGdrUklBOTVZTDIyenpnWmIyamNYT1dseGoybVZuUXB1bThDR2RKYw?oc=5) — Naver Blog
- [[오늘 증시 전망] 코스피 5,100선 회복했지만 뉴욕증시 급락…20일 외국인 수급이 관건 - 업코리아](https://news.google.com/rss/articles/CBMibkFVX3lxTE1VTmVVYWxLVkxmSVlWa3NydEVRMkVSNmdBUGowTXBOV3FtTmZEdEZTWXpMWU9OVGNKRGt6QndkR2std2FOWi11T21VOTNkYy03V1k0bHBSeUZzOVp2WFVWc3M4T3lJVVR3TWZBQmZ3?oc=5) — 업코리아
- [환율 1,550원 육박...코스피 '검은 금요일' - YTN](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1TLTZEWFpQYUdFQkU3eTAwUk5TMnpRV09BaTJHOVE2RWJBd3VBb2E1NXhBQkdnLVFHTzg3blpUbXdEMU9QcEM5VG5QdHRfQmRTTWdUa0RvVTh0TDUzd1E?oc=5) — YTN
- [[주간증시전망] 코스피 한 주 11.71% 급락…미 반도체 반등, 5000선 지킬까 - 강릉뉴스](https://news.google.com/rss/articles/CBMib0FVX3lxTFBpUUc3V19CbFdVVkhxRkRzSDVmcjZmUkd3d0R2bklNd24tZlFIa2MyVjJteTJMMER5Zi1rczJXdG1VS3cwUURKSmQ5THI2MUVpU0RUZTU5LXN3TnF0Qi1fQkV1eml2M3NmTG1OSHV1aw?oc=5) — 강릉뉴스
- [[심층분석] ‘삼전닉스’ 17조 덜어낸 외국인…실적·금리 개선이 복귀 가른다 - 굿모닝경제](https://news.google.com/rss/articles/CBMibEFVX3lxTE5yLWw2WndSa0pWTXlvRktRZ3NQd2lTQlRHNGpXLVQzYWgzdkdTZVhCakVzcktOZTcyeXlUcHFvcDdiaEZfSXhUb21yUUhSVFRFOWFmd19aaGs5b19uUkRZRXc3MElST2tNeG05SA?oc=5) — 굿모닝경제
- [7000피 아슬아슬한데 "1만2000 간다"…외국인 돌아온 코스피, 복병은 - 머니투데이 - 머니투데이](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBtYk1BaU5NLUlPdWlyUTFldGdmX2NJbm9IVjBnaG1oTllIVXNIMUstX1JFRDZBOG0yVFFROWZNb3Q4TmI4V3ZUT2JQdjE2dWNQY1ZFMUxzQkduNGVDVUZORzZ2Q184WGZI0gFuQVVfeXFMUHpoR3RYWHJtNG04SWtxS25pajJGZFBFTktlRWZBb0dTdzNibV8ybXFrSndDbjBiWi0zN01zY3R6RVVablQ5eU1KT3RXamxadHR4bnNSb0J3b2dYUjhBQy1KT3JIOHo4SEl1YlhNYXc?oc=5) — 머니투데이
- [외국인 20일째 "팔자"… 코스피 한때 8000선까지 급락 - 조선일보](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbWpfWFdxa242eEg2ZUNhUXpZWlE5TTBDaVBWTE1Jam9Mc0gzYWdCbDFsSUVYNmdvQW9MS29hUmNBX1lOTlJHU3BYUFJjblp1WngyZzdFN2tuVGd0UWdQOFZzcDVqdnhrNkpfUkZCYi1vemloOVc3d0lvMVdkQkNIdg?oc=5) — 조선일보
- [[AI MY 증시전망] "하루 만에 뒤집힌 흐름, 코스피 반등 시도" - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1UQkZTR3dQQjktWkRIM0JpZ3dmTjVHcWJrOGdqOHlOU05MR216eHN1TFRCQ2taUUZUNUU3R0d3c1djRlRlUFVwaVMyeXhwbU40bURhU1JfT0l6MEVx?oc=5) — 뉴스핌

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
