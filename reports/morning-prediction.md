# 오전 9시 예측 리포트

- 생성 시각: `2026-07-03T12:21:45+09:00`
- 단기 판정: **중립/하락 경계** / 신뢰도: 중간
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **-1.56** = 상승 4.0 + 하락 -5.56

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 7,863.94 | 2026-07-03 11:59 |
| KOSDAQ | 841.94 | 2026-07-03 09:50 |
| USD/KRW | 1,542.88 | 1M 0.83% |
| SOX | 1W -9.43% | 1M -8.01% |
| VIX | 16.15 | 위험선호/공포 지표 |
| WTI | 69.06 | 1M -28.08% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 중립/하락 경계 | 조건부 상승 | -1.56 | 4.0 | -5.56 |
| KOSDAQ | 중립/하락 경계 | 중립/상승 경계 | -0.56 | 3.5 | -4.06 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M -8.88%, 3M +43.68%, 6M +91.60% | 상승 | 0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D -190,522억, 10D -356,241억 | 하락 | -2.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 127,913억, 기관 5D 57,122억 | 하락 | -1.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,542.88, 1M +0.83% | 하락 | -1.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -9.43%, 1M -8.01% | 하락 | -1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.485%, 1M +0.67% | 하락 | 0.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 16.15 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 69.06달러, 1M -28.08% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +4.91%, 자동차 +0.00% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 적중: 예측=mild_bearish, 실제=bearish(-2.18%) | 하락 | -0.06 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 220 | 59.55% | 2.31% | 0.19 | 모멘텀 롱 |
| KOSDAQ | 220 | 56.82% | 0.40% | 0.14 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.06**
- 누적 표본: 33
- 누적 적중률: 45.45%
- 최근 피드백: 전일 09시 예측 적중: 예측=mild_bearish, 실제=bearish(-2.18%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [[AI MY 증시전망] 반도체가 이끈다…코스피 상승 기대 속 외국인 수급 '촉각' - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBVUGF2dUtPN05SS1ZKQ1BvdGE0SFVINGViRnpPdnBqbjlqZGZ4aXI3d2dhTmtLM3JvR2FQcEVSNjh5a2hMMVNLdURhX2pzaVF3WDFFSTlGZDlKTm5K?oc=5) — 뉴스핌
- [코스피, 반도체주 약세에 8300선 후퇴…환율 1550원대 마감 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTFBXREdDejJHa2JkY0ltMTlMUGE1Mm45cTFNR2dhamh6Zl82aXN2bE1uUmRUeG9Ya2UxVUktSGt2MlNWQnM1aW9ROHVQQUJvcUNDdXhqMWNiLXhZcmlIcTVzMzhvZW5ITHg3eVdXZFAtSEZKX0HSAXdBVV95cUxPWlZRQU5fYk1naDBUeWtTbW9xaGU1TlZpMUhsZVMzT0diMGVSZHdSVjZ4MzMwSG9qZjRwWjE5aGRHRTNZdTJaeW5rc0RBd2hCeE5MRUR5Z1ZZYlQ0Tmxocm45SGxQZXI5a1NJWkFEOXJhSEU2TjJyVQ?oc=5) — 스트레이트뉴스
- [올해 외국인 코스피 149조 원 순매도…하반기에도 매도세 이어질까? - 내외뉴스통신](https://news.google.com/rss/articles/CBMibkFVX3lxTE9Pc1lncExhTWYyX3FabHl4cHIzYWwwRUo4U1lDZXFwd1pLMFhrSnJITHU1aTNPcXd4RUlnLTZpUDJ6STlaTXNtRzRBTmpmYnN0bG5xSHc1SE9nci1JcGxFUTZNcHZ0cTlKOUlBaW9R0gFwQVVfeXFMTkxfYU45Zm04ZHZacE5fLWxhLUp1ajJJRmJzUkRBYXNibUJhZzFMUTh4OXUtY0JjQnVoT21WQ3dXR2tnZFIxY05lNmpnanF2Z3JfLWtYQlNpcTVTaTZwRzNUWGZzRXNyaXBfTWd4QkhNbQ?oc=5) — 내외뉴스통신
- [외국인 48조 매도에도 "한국 떠난 건 아니다"…복귀 조건은 실적·주주환원 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1lNXZkLUF2QTNlaEE4bWRWU0s4R0tlUFRidmZXT0NiYVI0WHBZZWtiOEo3TWFnQkttOWNBZ3ZabDZhMkxpb3pmdnA2VGcxUm9XcVVHb0U5dXUwVV9i?oc=5) — 뉴스핌
- [환율 1,550원 육박...코스피 '검은 금요일' - YTN](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1TLTZEWFpQYUdFQkU3eTAwUk5TMnpRV09BaTJHOVE2RWJBd3VBb2E1NXhBQkdnLVFHTzg3blpUbXdEMU9QcEM5VG5QdHRfQmRTTWdUa0RvVTh0TDUzd1E?oc=5) — YTN
- [코스피, '검은 월요일' 오나?…주말 美 반도체 급락에 고환율 덮쳤다 - 한국일보](https://news.google.com/rss/articles/CBMibkFVX3lxTE5tWkc4cmNUODU3anotR0FVYk83NUVNdE1wbU9NYW5XTVVGZV9Ib2pqSkk1aHVuNUtHQzNjLWVsSUlJRlRvS0E2aW1nZDhMcHVHWFpiSERJR05zREtvZXJHeWwtQjFjTUl2b0pCZ2tn0gFzQVVfeXFMTVQtakFqeXdIY01HQlJvcGxHbmdudFpQVE1yZVAxRFFKVkIwQmttODhpVU85cUJCdWZOaDVXNWNwV3dyUWV2YVEzYVZKSEpuOXVhRmN2QTJ6Ny12WEQya296RTFpV1hWaXFEM0s2b0tzaGtlcw?oc=5) — 한국일보
- [외국인 20일째 매도 폭탄에 코스피 5%대 급락…반도체 쇼크와 고환율 직격탄 - 2news.co.kr](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBhSFplenl5VnZGRFJ6c25TOWExM1RuN1lJSGlKMlFHYmpDLVZHOUZRQ2xBcWZRR3VsanhIcUt5akpPUFRuYi05cVZOOFBJUzV5WXJyaFFXbWk1VHRIREd5RFNYRzZIWVE?oc=5) — 2news.co.kr
- [환율 1540원·외인 매도 폭탄…코스피 5% 급락 - mstoday.co.kr](https://news.google.com/rss/articles/CBMibEFVX3lxTE5Cc056NXd2Q1NQZ0hJOFFXcVVMNlJqaXl2MUNwZGx0X1BzUXNzbnk1c2Z1ckJSN0lTUjdJbzV4eE1SQnBmNnc0QWFrVmlySnVIdVZSWFRfbkZ2ejlEbnlKRVJBZlgyS2JHaG04dw?oc=5) — mstoday.co.kr

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
