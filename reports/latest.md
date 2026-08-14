# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-08-14T17:17:03+09:00`
- 단기 판정: **상승 우세** / 신뢰도: 중간~높음
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **4.23** = 상승 6.0 + 하락 -1.77

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 6,977.94 | 2026-08-14 17:11 |
| KOSDAQ | 864.65 | 2026-08-14 16:09 |
| USD/KRW | 1,413.58 | 1M -4.89% |
| SOX | 1W 3.38% | 1M 0.46% |
| VIX | 14.64 | 위험선호/공포 지표 |
| WTI | 82.84 | 1M 4.93% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 상승 우세 | 조건부 상승 | 4.23 | 6.0 | -1.77 |
| KOSDAQ | 중립/하락 경계 | 중립/상승 경계 | -0.77 | 4.5 | -5.27 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M -4.21%, 3M -12.57%, 6M +37.11% | 상승 | 0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D 65,469억, 10D 6,453억 | 상승 | 1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D -70,846억, 기관 5D 7,719억 | 중립 | 0.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,413.58, 1M -4.89% | 하락 | -0.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W +3.38%, 1M +0.46% | 하락 | 1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.641%, 1M +2.11% | 하락 | -1.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 14.64 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 82.84달러, 1M +4.93% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 +6.20% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=bullish, 실제=bearish(-0.59%) | 하락 | -0.27 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 219 | 63.01% | 1.73% | 0.26 | 모멘텀 롱 |
| KOSDAQ | 219 | 57.08% | 0.22% | 0.14 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.27**
- 누적 표본: 63
- 누적 적중률: 39.68%
- 최근 피드백: 전일 09시 예측 불일치: 예측=bullish, 실제=bearish(-0.59%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [환율 1415.9원으로 ‘뚝’…코스피·코스닥도 동반 상승 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTE13Z09JcUdJYnhhODJWRTlJVWhRN3dJUXo4T3lVWXlrendsMXF6dVRmN1ZxQmJTSzBkNGJWSkkxVHdSOVFmeTdDaDR0YlRIMkZ2U0gzTXRuMkdBQjBPRDBTUElCS0tvV043Zm8wa1E4bE5lbDjSAXdBVV95cUxPeXJYZk0yZGNaYmpacHZTclFlSk5obW1oQXVsTGhWZlRHVEdJQTgweHVEVWU1b3g4b1lKcUN4ZV9rX0JjWWliaE9OQVJOd0k3N2VKZ0hMWVJBYk9YNWlqU0Q1Q2E2OGFFYTNCb3hMem81Ui1oRGRJSQ?oc=5) — 스트레이트뉴스
- [환율 1,550원 육박...코스피 '검은 금요일' - YTN](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1TLTZEWFpQYUdFQkU3eTAwUk5TMnpRV09BaTJHOVE2RWJBd3VBb2E1NXhBQkdnLVFHTzg3blpUbXdEMU9QcEM5VG5QdHRfQmRTTWdUa0RvVTh0TDUzd1E?oc=5) — YTN
- [[AI MY 증시전망] 반도체가 이끈다…코스피 상승 기대 속 외국인 수급 '촉각' - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBVUGF2dUtPN05SS1ZKQ1BvdGE0SFVINGViRnpPdnBqbjlqZGZ4aXI3d2dhTmtLM3JvR2FQcEVSNjh5a2hMMVNLdURhX2pzaVF3WDFFSTlGZDlKTm5K?oc=5) — 뉴스핌
- [외국인 20일째 "팔자"… 코스피 한때 8000선까지 급락 - 조선일보](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbWpfWFdxa242eEg2ZUNhUXpZWlE5TTBDaVBWTE1Jam9Mc0gzYWdCbDFsSUVYNmdvQW9MS29hUmNBX1lOTlJHU3BYUFJjblp1WngyZzdFN2tuVGd0UWdQOFZzcDVqdnhrNkpfUkZCYi1vemloOVc3d0lvMVdkQkNIdg?oc=5) — 조선일보
- [코스피 전망은 밝다지만…개인투자자가 한국 주식 살 때 봐야 할 변수 - christiandaily.co.kr](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9TZTVYNUF2QWdSTzlzRkVtN3V3dzZERE1mRnNkZDN1R040X3ZjSzlSUkxITFN4NDlpMnNDYklRMV91cnFNR3dEVERZcXUyNkVBWVhXUDcwb9IBXEFVX3lxTE9NMGJVVjdrVXJ3OVhTSTk2UC1rSHNDdkhCYXdSNVc4RENVLXpvSW9ueWl2azBMUU1zN2VOOFY5c3Zudnp5cUxjcHJBMEFHWnRKa2UtYUpCVlRrSW5o?oc=5) — christiandaily.co.kr
- [코스피 장중 급락, 삼성전자·SK하이닉스 지금 팔아야 할까? - 네이버 프리미엄콘텐츠](https://news.google.com/rss/articles/CBMifkFVX3lxTE5PV2dfOWFTOWV4RFl4WmotU202dHRnVWwxQTQ3N0Q0bThFSFRodmE0Q3JtUml1NnJNbzFNbVJ0SXdvME1ZSlpBdTM0SHhLQUg3WXVFZFJqNV8tNFVyaEdaeXRGTm1PTXZIQTVsczlabk01RklsVXRVSENsOXFPQQ?oc=5) — 네이버 프리미엄콘텐츠
- [코스피 '꿈의 8000선' 뚫었다…한국 증시 사상 첫 신기원 - mstoday.co.kr](https://news.google.com/rss/articles/CBMibEFVX3lxTFAtc2VMWG9GYzFnUjI2OVhPMzRsd2ZRMllIUXpIREpGcHZjbVpTMFZJVkppX3R5WC1kNDFGcURhTzYxeHZXVFk5OXlrZjFlZ0NCTHZ4NHkyeVZhS012QTlkQXBILWJFcGttdEZ6UQ?oc=5) — mstoday.co.kr
- ["코스피 7500 간다"... KB증권, 반도체 힘입어 외국인 자금 유입 기대 - 인포스탁데일리](https://news.google.com/rss/articles/CBMidkFVX3lxTFBkRHR4anpGQm1MRjN0YzFiUnROR3NxcFg1bk5jY1R5Sy1SRGJ4aXBTVldyRHd1VVFQeFN6Yml2SlNZOVk4YzJSQ1ZodGNFcEtwb25rS202YUJfVHVnVVlTbHB2WXdETWlieE0wMUNQV3BMb2xoZlE?oc=5) — 인포스탁데일리

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
