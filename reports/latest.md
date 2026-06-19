# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-06-19T17:50:24+09:00`
- 단기 판정: **상승 우세** / 신뢰도: 중간~높음
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **6.15** = 상승 7.65 + 하락 -1.5

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 9,052.42 | 2026-06-19 16:41 |
| KOSDAQ | 966.59 | 2026-06-19 16:15 |
| USD/KRW | 1,531.50 | 1M 2.12% |
| SOX | 1W 10.41% | 1M 19.24% |
| VIX | 16.90 | 위험선호/공포 지표 |
| WTI | 75.81 | 1M -22.85% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 상승 우세 | 조건부 상승 | 6.15 | 7.65 | -1.5 |
| KOSDAQ | 중립/상승 경계 | 상승 우세 | 0.65 | 5.15 | -4.5 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M +20.44%, 3M +60.49%, 6M +118.47% | 상승 | 2.0 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D 25,434억, 10D -17,627억 | 상승 | 1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D -19,389억, 기관 5D -2,470억 | 중립 | 0.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,531.50, 1M +2.12% | 하락 | -1.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W +10.41%, 1M +19.24% | 하락 | 1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.487%, 1M +0.13% | 하락 | 0.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 16.90 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 75.81달러, 1M -22.85% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 +0.52% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 적중: 예측=bullish, 실제=bullish(+1.81%) | 상승 | 0.15 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 219 | 60.27% | 2.45% | 0.21 | 모멘텀 롱 |
| KOSDAQ | 219 | 53.42% | 0.61% | 0.07 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **+0.15**
- 누적 표본: 23
- 누적 적중률: 47.83%
- 최근 피드백: 전일 09시 예측 적중: 예측=bullish, 실제=bullish(+1.81%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [[AI MY 증시전망] "반도체 조정 여파 속 유가 안정에 낙폭 제한 전망" - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBwa2lZYzd0QWtzeGs3UHBzZkliY2JOcUdiVk5wczBoMWZhX2hSeTcwd20wdXNIcmlMWWNTd1BoTXI5cm05aHRtT3BKakU0dlcxcXpUTXFPRkhUOC1F?oc=5) — 뉴스핌
- [코스피, 8800선 탈환…‘9000피’ 열쇠는 외국인 수급 확산 - 직썰](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5kUE4xclpmV0hON0p2YjRxQXUyOEZ1QkluRjcybm1fMnE4TDF2dVVMcE9wSFJ2d3dkcVkxMXRvNEVHMHN4Sm9oNWNmZWdVOXF2aV9vS2R3Q1pkYmhuLTd0VE5mM2Q2Z3g10gFsQVVfeXFMTTJXWkdiVHlzUWplR2M0cGJjNGM2NURIRmV2aGpkemlzNmo4NWxSR09xaWNwQ3ZzRVBNRlJQVWlERWVGRnVjTlN1X3BBVXVkWmx4MVI1R2VjVmRpVE9YS2hqc19LZG5EUFFXcHlY?oc=5) — 직썰
- [韓 증시, 월요일 환율 급등·반도체 충격 긴장 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTE1jWHFkaXM0YjNRRTFMR2ZpM2NBZkpFSEt5VU5WUWNsOFVSTjdXOFVnanJucHl6ZG9LUWp3UmhnTWN0cUxHSkhMWER4LVpGenBTcFBsajNldE54Xy0wWDZLTGlKamFpeGJOTWFlRWJPbFVLNzTSAXdBVV95cUxQMUVYS1RYdGJ1aWZjdWVzS05DTWtRYjVxSlFZUGx2aFVsVEVHclRvWF9BcVMyekg1MFZGeEs0WWN4MGY0dVB4cTN2Y3l0b0p3MDFwZE5mRFIxRGRDM282ODFyM0duZTZGUEQ2cF9yN09YOHQwU09sWQ?oc=5) — 스트레이트뉴스
- [환율 1540원·외인 매도 폭탄…코스피 5% 급락 - mstoday.co.kr](https://news.google.com/rss/articles/CBMicEFVX3lxTFBEeW96akVVTDNYa2RQUVN3aVBzeF84djBGbjFrQlhMZ1Robjk0YTRsN01ia0o0Qi1WNDdWaGFqSkxDaFdSQmVOVHlvcUNfNHJmQl9GZDlfSEN6Mmd4bUJsQy1IellOTGZrcG1EMG9BWGY?oc=5) — mstoday.co.kr
- [코스피, '검은 월요일' 오나?…주말 美 반도체 급락에 고환율 덮쳤다 - 한국일보](https://news.google.com/rss/articles/CBMibkFVX3lxTE5tWkc4cmNUODU3anotR0FVYk83NUVNdE1wbU9NYW5XTVVGZV9Ib2pqSkk1aHVuNUtHQzNjLWVsSUlJRlRvS0E2aW1nZDhMcHVHWFpiSERJR05zREtvZXJHeWwtQjFjTUl2b0pCZ2tn0gFzQVVfeXFMTVQtakFqeXdIY01HQlJvcGxHbmdudFpQVE1yZVAxRFFKVkIwQmttODhpVU85cUJCdWZOaDVXNWNwV3dyUWV2YVEzYVZKSEpuOXVhRmN2QTJ6Ny12WEQya296RTFpV1hWaXFEM0s2b0tzaGtlcw?oc=5) — 한국일보
- [외국인 20일째 매도 폭탄에 코스피 5%대 급락…반도체 쇼크와 고환율 직격탄 - 2news.co.kr](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBhSFplenl5VnZGRFJ6c25TOWExM1RuN1lJSGlKMlFHYmpDLVZHOUZRQ2xBcWZRR3VsanhIcUt5akpPUFRuYi05cVZOOFBJUzV5WXJyaFFXbWk1VHRIREd5RFNYRzZIWVE?oc=5) — 2news.co.kr
- [100조 투매에도 지분율은 상승… 코스피 불장이 만든 ‘외인 지분 미스터리’ - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUm1oVVVsV3FfeXFOTzk1UnJyamRVMWRPS09LVjhSWFEtbHNBUkY2eVJINm1jSmlmLWx0OGhQcGZFUTdmR2x3YzdHNVE4MkNlcE9YMnBtdXlyb0p3bXRuNXRpaXQ0aXNKUHE4M1lWT3E0eDRQaHVvSkNTaFlZVGFqektvX3BNS1Jm0gGcAUFVX3lxTFBlMWpZVlNWRzJrTHlzX25hRXV0dUNkaTFNZHZ0cDd1WVJuaE5SM0VEbnhNR1lmY2dyQkVaUnotY1ppT0hRN2RSenRxenJ3X24wQkNSRWZtQ0FKaDJTX2F4NWhqa2EtMVZ6LUgzNDhGRk9tNGhqTDFXa0RXeXRwVmpVeEZ6QmdYQVlDbHBMQkpxZmxmR2hPODhaaTBpcA?oc=5) — Chosunbiz
- [코스피 전망은 밝다지만…개인투자자가 한국 주식 살 때 봐야 할 변수 - christiandaily.co.kr](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9TZTVYNUF2QWdSTzlzRkVtN3V3dzZERE1mRnNkZDN1R040X3ZjSzlSUkxITFN4NDlpMnNDYklRMV91cnFNR3dEVERZcXUyNkVBWVhXUDcwb9IBXEFVX3lxTE9NMGJVVjdrVXJ3OVhTSTk2UC1rSHNDdkhCYXdSNVc4RENVLXpvSW9ueWl2azBMUU1zN2VOOFY5c3Zudnp5cUxjcHJBMEFHWnRKa2UtYUpCVlRrSW5o?oc=5) — christiandaily.co.kr

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
