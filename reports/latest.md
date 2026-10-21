# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-10-21T21:46:26+09:00`
- 단기 판정: **중립/상승 경계** / 신뢰도: 중간
- 중기 판정: **상승 우세** / 신뢰도: 중간~높음
- 총점: **1.32** = 상승 5.0 + 하락 -3.68

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | N/A |  |
| KOSDAQ | N/A |  |
| USD/KRW | 1,325.90 | 1M -3.48% |
| SOX | 1W -7.58% | 1M -9.24% |
| VIX | 17.27 | 위험선호/공포 지표 |
| WTI | 97.76 | 1M 3.35% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 중립/상승 경계 | 상승 우세 | 1.32 | 5.0 | -3.68 |
| KOSDAQ | 중립/상승 경계 | 상승 우세 | 1.32 | 5.0 | -3.68 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M -14.62%, 3M -15.91%, 6M -3.89% | 하락 | -0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D 0억, 10D 0억 | 상승 | 1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 0억, 기관 5D 0억 | 중립 | 0.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,325.90, 1M -3.48% | 하락 | 0.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -7.58%, 1M -9.24% | 하락 | -1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 5.098%, 1M +2.62% | 하락 | -1.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 17.27 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 97.76달러, 1M +3.35% | 하락 | -1.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 +0.00% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=bullish, 실제=neutral(-0.11%) | 하락 | -0.18 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 220 | 55.91% | 1.10% | 0.12 | 모멘텀 롱 |
| KOSDAQ | 220 | 50.45% | -0.02% | 0.01 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.18**
- 누적 표본: 80
- 누적 적중률: 40.00%
- 최근 피드백: 전일 09시 예측 불일치: 예측=bullish, 실제=neutral(-0.11%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [코스피 전망, 美 반도체 8일째 급락…외국인 수급 시험대 - 톱스타뉴스](https://news.google.com/rss/articles/CBMickFVX3lxTE1iQjdTY2wxeWpKN2JNRDdFZGJXT09KUXhrMFR2Y2xIdUJOMXFSM2w3cnhPdkxqdmE4ZFZROFptOHpVYUozUFJkb0hxWE51dmNEQ21VRW5EeUgzNkdmTWphQnRUYlR6b29ZQkR4SXBieWE1QQ?oc=5) — 톱스타뉴스
- [원화는 2년 만에 강세, 코스피는 급락…엇갈린 금융시장 - 엠에스투데이](https://news.google.com/rss/articles/CBMibEFVX3lxTFBleGZ3UTY1VU9QSnd6U2laaDZNTWk3aDJJQXZoblFkUXVmU0txYjJsUlBQc2FGVkNGLVFxMTkwb3RWX0d5T1B1azdfeTRPcmpTMW9vY2E0ckZjZ3ozUVRLQVpHcF9TQldnelBpbtIBcEFVX3lxTE9zb3M1VmZqZjByMDJrY3YySVFIUTI2eEhJX0M4S2h1MDZLUDJ3TVB1R3RQQVQwX1VxR0MzaXgtREVQeVBYSWNhZkp1VHZUMDRqQ3ZKTm1uWHhEMFFyLUpqWGN4RURwUnBlRkhWYlZrUEo?oc=5) — 엠에스투데이
- [환율 1,550원 육박...코스피 '검은 금요일' - YTN](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1TLTZEWFpQYUdFQkU3eTAwUk5TMnpRV09BaTJHOVE2RWJBd3VBb2E1NXhBQkdnLVFHTzg3blpUbXdEMU9QcEM5VG5QdHRfQmRTTWdUa0RvVTh0TDUzd1E?oc=5) — YTN
- [7000피 아슬아슬한데 "1만2000 간다"…외국인 돌아온 코스피, 복병은 - 머니투데이 - 머니투데이](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBtYk1BaU5NLUlPdWlyUTFldGdmX2NJbm9IVjBnaG1oTllIVXNIMUstX1JFRDZBOG0yVFFROWZNb3Q4TmI4V3ZUT2JQdjE2dWNQY1ZFMUxzQkduNGVDVUZORzZ2Q184WGZI0gFuQVVfeXFMUHpoR3RYWHJtNG04SWtxS25pajJGZFBFTktlRWZBb0dTdzNibV8ybXFrSndDbjBiWi0zN01zY3R6RVVablQ5eU1KT3RXamxadHR4bnNSb0J3b2dYUjhBQy1KT3JIOHo4SEl1YlhNYXc?oc=5) — 머니투데이
- [환율 1415.9원으로 ‘뚝’…코스피·코스닥도 동반 상승 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTE13Z09JcUdJYnhhODJWRTlJVWhRN3dJUXo4T3lVWXlrendsMXF6dVRmN1ZxQmJTSzBkNGJWSkkxVHdSOVFmeTdDaDR0YlRIMkZ2U0gzTXRuMkdBQjBPRDBTUElCS0tvV043Zm8wa1E4bE5lbDjSAXdBVV95cUxPeXJYZk0yZGNaYmpacHZTclFlSk5obW1oQXVsTGhWZlRHVEdJQTgweHVEVWU1b3g4b1lKcUN4ZV9rX0JjWWliaE9OQVJOd0k3N2VKZ0hMWVJBYk9YNWlqU0Q1Q2E2OGFFYTNCb3hMem81Ui1oRGRJSQ?oc=5) — 스트레이트뉴스
- [[AI MY 증시전망] "하루 만에 뒤집힌 흐름, 코스피 반등 시도" - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1UQkZTR3dQQjktWkRIM0JpZ3dmTjVHcWJrOGdqOHlOU05MR216eHN1TFRCQ2taUUZUNUU3R0d3c1djRlRlUFVwaVMyeXhwbU40bURhU1JfT0l6MEVx?oc=5) — 뉴스핌
- [코스피 다음주 전망, 외국인 귀환보다 AI 실적이 관건 - TopStarNews](https://news.google.com/rss/articles/CBMickFVX3lxTFBhaWsyUGlnMzZ4MTZYTldabXhfdDM4cW1SWTY4ODEyZnJ6ckF1MjF6ZjJYaXNWbnVBSnhZRlg2LUE0Qzg0ZGtyMm5VQlFfd2tDM1I1eGV5QzRIazI1cW8wbmkzNFZLLWpyNXBsT3JvWW8tdw?oc=5) — TopStarNews
- [외국인 20일째 "팔자"… 코스피 한때 8000선까지 급락 - 조선일보](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbWpfWFdxa242eEg2ZUNhUXpZWlE5TTBDaVBWTE1Jam9Mc0gzYWdCbDFsSUVYNmdvQW9MS29hUmNBX1lOTlJHU3BYUFJjblp1WngyZzdFN2tuVGd0UWdQOFZzcDVqdnhrNkpfUkZCYi1vemloOVc3d0lvMVdkQkNIdg?oc=5) — 조선일보

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
