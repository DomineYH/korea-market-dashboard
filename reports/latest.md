# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-09-03T20:59:00+09:00`
- 단기 판정: **중립/상승 경계** / 신뢰도: 중간
- 중기 판정: **상승 우세** / 신뢰도: 중간~높음
- 총점: **1.33** = 상승 4.5 + 하락 -3.17

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 6,579.48 | 2026-09-03 18:52 |
| KOSDAQ | 790.21 | 2026-09-03 18:52 |
| USD/KRW | 1,357.52 | 1M -4.96% |
| SOX | 1W -2.34% | 1M -6.90% |
| VIX | 15.33 | 위험선호/공포 지표 |
| WTI | 93.03 | 1M 23.68% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 중립/상승 경계 | 상승 우세 | 1.33 | 4.5 | -3.17 |
| KOSDAQ | 중립/하락 경계 | 중립/상승 경계 | -0.67 | 4.0 | -4.67 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M +3.47%, 3M -23.84%, 6M +13.60% | 상승 | 0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D -38,686억, 10D -115,092억 | 하락 | -1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 10,805억, 기관 5D -37,271억 | 중립 | 0.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,357.52, 1M -4.96% | 하락 | 0.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -2.34%, 1M -6.90% | 하락 | 0.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.796%, 1M +3.65% | 하락 | -1.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 15.33 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 93.03달러, 1M +23.68% | 하락 | -1.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 +0.00% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=neutral, 실제=bearish(-0.85%) | 하락 | -0.17 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 219 | 60.27% | 1.69% | 0.21 | 모멘텀 롱 |
| KOSDAQ | 219 | 54.79% | 0.10% | 0.10 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.17**
- 누적 표본: 75
- 누적 적중률: 40.00%
- 최근 피드백: 전일 09시 예측 불일치: 예측=neutral, 실제=bearish(-0.85%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [환율 1415.9원으로 ‘뚝’…코스피·코스닥도 동반 상승 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTE13Z09JcUdJYnhhODJWRTlJVWhRN3dJUXo4T3lVWXlrendsMXF6dVRmN1ZxQmJTSzBkNGJWSkkxVHdSOVFmeTdDaDR0YlRIMkZ2U0gzTXRuMkdBQjBPRDBTUElCS0tvV043Zm8wa1E4bE5lbDjSAXdBVV95cUxPeXJYZk0yZGNaYmpacHZTclFlSk5obW1oQXVsTGhWZlRHVEdJQTgweHVEVWU1b3g4b1lKcUN4ZV9rX0JjWWliaE9OQVJOd0k3N2VKZ0hMWVJBYk9YNWlqU0Q1Q2E2OGFFYTNCb3hMem81Ui1oRGRJSQ?oc=5) — 스트레이트뉴스
- ['D램 달러 시대', 외국인 폭풍 매도에 원달러 환율 1,600원대 '폭풍 질주' - ytn.co.kr](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9ZWFpFRXR6dE1ta3JzaXhEUEdDbEg3ajRaWDhOdHU1TDFUdHBXcjdVQW05MXNjUTl4OG82VVNaZklpdWJUQ2dsLVUydVd3M21PX1VBQVNIbV9qWS1nVVE?oc=5) — ytn.co.kr
- [[AI MY 증시전망] 반도체가 이끈다…코스피 상승 기대 속 외국인 수급 '촉각' - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBVUGF2dUtPN05SS1ZKQ1BvdGE0SFVINGViRnpPdnBqbjlqZGZ4aXI3d2dhTmtLM3JvR2FQcEVSNjh5a2hMMVNLdURhX2pzaVF3WDFFSTlGZDlKTm5K?oc=5) — 뉴스핌
- [[주간증시전망] 사상 최고치 찍고 급락한 코스피…반도체 조정 속 순환매 올까 - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fVU40UjdSLUxkNUs5UzJSeTB0alYydVdkQXRXd1ZyS3VUUUtnWF9kOFdtalNNUEZWbDRXVERfLW9kdUdhcXJwTkZ6M3dfdlR6dU1DeGVnb0N3QdIBWEFVX3lxTFBDeGRIM1BLZE1XaGdGcHZ5S1N0ZGMyWDgzN0QtRmVkbmt1SVZRN3lqWm0zNERaWTdZMUpWT254b0RNVWs0V1kySjlkaTdFSG42aHlnZ3lnOXQ?oc=5) — 아주경제
- [[주간증시] 유가·환율·반도체 ‘삼각 변수’…박스권 내 ‘조건부 장세’ - 에너지경제신문](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5ELURYY1NNRnUxN2tPMnRrdzRRZFdSd3V4bU9QR3BnNDNObHpUV3lKM0JhOU8tWm1MRDIxQzRUWWI0SFJ6MHh5MHhoTngtcGo2WkhiRkpFWm9pQlU?oc=5) — 에너지경제신문
- [골드만삭스가 한국 증시를 찍은 이유…반도체 실적이 바꾼 코스피 전망 - christiandaily.co.kr](https://news.google.com/rss/articles/CBMiV0FVX3lxTE04Tk1CY1p6OEc3VDhoaUNiNllxczhRNDJWcDFpdjJMOFMtV2V2Q2hlakRVTjdOMmIwYzc4eTZHbkFtaXJ5eXdKdlpONXZhS3d0anJVXzUyONIBXEFVX3lxTE9CSWVPNV9FclUzYW9Wc19pMlc0eE5FVjF0amhFSWdvRjVqV3hqOGxTOERBb0F5NzA1aGs3VkM2Wi1FQzZFMXNzdTM0aTB3X01NYUdBRmpxU21SYUlE?oc=5) — christiandaily.co.kr
- ["코스피 7500 간다"... KB증권, 반도체 힘입어 외국인 자금 유입 기대 - 인포스탁데일리](https://news.google.com/rss/articles/CBMidkFVX3lxTFBkRHR4anpGQm1MRjN0YzFiUnROR3NxcFg1bk5jY1R5Sy1SRGJ4aXBTVldyRHd1VVFQeFN6Yml2SlNZOVk4YzJSQ1ZodGNFcEtwb25rS202YUJfVHVnVVlTbHB2WXdETWlieE0wMUNQV3BMb2xoZlE?oc=5) — 인포스탁데일리
- [코스피 '꿈의 8000선' 뚫었다…한국 증시 사상 첫 신기원 - mstoday.co.kr](https://news.google.com/rss/articles/CBMibEFVX3lxTFAtc2VMWG9GYzFnUjI2OVhPMzRsd2ZRMllIUXpIREpGcHZjbVpTMFZJVkppX3R5WC1kNDFGcURhTzYxeHZXVFk5OXlrZjFlZ0NCTHZ4NHkyeVZhS012QTlkQXBILWJFcGttdEZ6UQ?oc=5) — mstoday.co.kr

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
