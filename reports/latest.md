# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-07-17T18:11:00+09:00`
- 단기 판정: **중립/하락 경계** / 신뢰도: 중간
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **-1.15** = 상승 3.5 + 하락 -4.65

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 6,820.60 | 2026-07-17 10:01 |
| KOSDAQ | 791.84 | 2026-07-17 17:57 |
| USD/KRW | 1,485.19 | 1M -2.64% |
| SOX | 1W -8.43% | 1M -15.83% |
| VIX | 18.40 | 위험선호/공포 지표 |
| WTI | 79.40 | 1M 4.40% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 중립/하락 경계 | 조건부 상승 | -1.15 | 3.5 | -4.65 |
| KOSDAQ | 하락/조정 우세 | 중립/하락 경계 | -3.15 | 3.0 | -6.15 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M -23.05%, 3M +14.29%, 6M +48.72% | 상승 | 0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D -1,002억, 10D -60,288억 | 하락 | -1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 1,634억, 기관 5D -746억 | 중립 | 0.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,485.19, 1M -2.64% | 하락 | -0.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -8.43%, 1M -15.83% | 하락 | -1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.569%, 1M +2.24% | 하락 | -1.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 18.40 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 79.40달러, 1M +4.40% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 -10.07%, 자동차 +0.00% | 하락 | -1.0 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=mild_bullish, 실제=neutral(-0.07%) | 하락 | -0.15 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 220 | 60.91% | 2.00% | 0.22 | 모멘텀 롱 |
| KOSDAQ | 220 | 57.27% | 0.17% | 0.15 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.15**
- 누적 표본: 43
- 누적 적중률: 37.21%
- 최근 피드백: 전일 09시 예측 불일치: 예측=mild_bullish, 실제=neutral(-0.07%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [외국인 48조 매도에도 "한국 떠난 건 아니다"…복귀 조건은 실적·주주환원 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1lNXZkLUF2QTNlaEE4bWRWU0s4R0tlUFRidmZXT0NiYVI0WHBZZWtiOEo3TWFnQkttOWNBZ3ZabDZhMkxpb3pmdnA2VGcxUm9XcVVHb0U5dXUwVV9i?oc=5) — 뉴스핌
- [환율 1,550원 육박...코스피 '검은 금요일' - YTN](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1TLTZEWFpQYUdFQkU3eTAwUk5TMnpRV09BaTJHOVE2RWJBd3VBb2E1NXhBQkdnLVFHTzg3blpUbXdEMU9QcEM5VG5QdHRfQmRTTWdUa0RvVTh0TDUzd1E?oc=5) — YTN
- [韓 증시, 월요일 환율 급등·반도체 충격 긴장 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTE1jWHFkaXM0YjNRRTFMR2ZpM2NBZkpFSEt5VU5WUWNsOFVSTjdXOFVnanJucHl6ZG9LUWp3UmhnTWN0cUxHSkhMWER4LVpGenBTcFBsajNldE54Xy0wWDZLTGlKamFpeGJOTWFlRWJPbFVLNzTSAXdBVV95cUxQMUVYS1RYdGJ1aWZjdWVzS05DTWtRYjVxSlFZUGx2aFVsVEVHclRvWF9BcVMyekg1MFZGeEs0WWN4MGY0dVB4cTN2Y3l0b0p3MDFwZE5mRFIxRGRDM282ODFyM0duZTZGUEQ2cF9yN09YOHQwU09sWQ?oc=5) — 스트레이트뉴스
- [외국인 20일째 매도 폭탄에 코스피 5%대 급락…반도체 쇼크와 고환율 직격탄 - 2news.co.kr](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBhSFplenl5VnZGRFJ6c25TOWExM1RuN1lJSGlKMlFHYmpDLVZHOUZRQ2xBcWZRR3VsanhIcUt5akpPUFRuYi05cVZOOFBJUzV5WXJyaFFXbWk1VHRIREd5RFNYRzZIWVE?oc=5) — 2news.co.kr
- [코스피 전망은 밝다지만…개인투자자가 한국 주식 살 때 봐야 할 변수 - christiandaily.co.kr](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9TZTVYNUF2QWdSTzlzRkVtN3V3dzZERE1mRnNkZDN1R040X3ZjSzlSUkxITFN4NDlpMnNDYklRMV91cnFNR3dEVERZcXUyNkVBWVhXUDcwb9IBXEFVX3lxTE9NMGJVVjdrVXJ3OVhTSTk2UC1rSHNDdkhCYXdSNVc4RENVLXpvSW9ueWl2azBMUU1zN2VOOFY5c3Zudnp5cUxjcHJBMEFHWnRKa2UtYUpCVlRrSW5o?oc=5) — christiandaily.co.kr
- [코스피 장중 급락, 삼성전자·SK하이닉스 지금 팔아야 할까? - 네이버 프리미엄콘텐츠](https://news.google.com/rss/articles/CBMifkFVX3lxTE5PV2dfOWFTOWV4RFl4WmotU202dHRnVWwxQTQ3N0Q0bThFSFRodmE0Q3JtUml1NnJNbzFNbVJ0SXdvME1ZSlpBdTM0SHhLQUg3WXVFZFJqNV8tNFVyaEdaeXRGTm1PTXZIQTVsczlabk01RklsVXRVSENsOXFPQQ?oc=5) — 네이버 프리미엄콘텐츠
- [코스피, '검은 월요일' 오나?…주말 美 반도체 급락에 고환율 덮쳤다 - 한국일보](https://news.google.com/rss/articles/CBMibkFVX3lxTE5tWkc4cmNUODU3anotR0FVYk83NUVNdE1wbU9NYW5XTVVGZV9Ib2pqSkk1aHVuNUtHQzNjLWVsSUlJRlRvS0E2aW1nZDhMcHVHWFpiSERJR05zREtvZXJHeWwtQjFjTUl2b0pCZ2tn0gFzQVVfeXFMTVQtakFqeXdIY01HQlJvcGxHbmdudFpQVE1yZVAxRFFKVkIwQmttODhpVU85cUJCdWZOaDVXNWNwV3dyUWV2YVEzYVZKSEpuOXVhRmN2QTJ6Ny12WEQya296RTFpV1hWaXFEM0s2b0tzaGtlcw?oc=5) — 한국일보
- ["코스피 7500 간다"... KB증권, 반도체 힘입어 외국인 자금 유입 기대 - 인포스탁데일리](https://news.google.com/rss/articles/CBMidkFVX3lxTFBkRHR4anpGQm1MRjN0YzFiUnROR3NxcFg1bk5jY1R5Sy1SRGJ4aXBTVldyRHd1VVFQeFN6Yml2SlNZOVk4YzJSQ1ZodGNFcEtwb25rS202YUJfVHVnVVlTbHB2WXdETWlieE0wMUNQV3BMb2xoZlE?oc=5) — 인포스탁데일리

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
