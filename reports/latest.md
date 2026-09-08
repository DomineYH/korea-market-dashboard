# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-09-08T21:01:14+09:00`
- 단기 판정: **상승 우세** / 신뢰도: 중간~높음
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **3.55** = 상승 5.55 + 하락 -2.0

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 6,954.52 | 2026-09-08 19:25 |
| KOSDAQ | 811.88 | 2026-09-08 16:22 |
| USD/KRW | 1,341.78 | 1M -4.64% |
| SOX | 1W 2.32% | 1M -2.60% |
| VIX | 15.75 | 위험선호/공포 지표 |
| WTI | 93.90 | 1M 20.11% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 상승 우세 | 조건부 상승 | 3.55 | 5.55 | -2.0 |
| KOSDAQ | 상승 우세 | 상승 우세 | 2.55 | 5.05 | -2.5 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M +11.12%, 3M -14.11%, 6M +24.52% | 상승 | 0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D 17,885억, 10D -1,857억 | 상승 | 1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D -122,455억, 기관 5D 38,394억 | 중립 | 0.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,341.78, 1M -4.64% | 하락 | 0.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W +2.32%, 1M -2.60% | 하락 | 0.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.784%, 1M +2.44% | 하락 | -1.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 15.75 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 93.90달러, 1M +20.11% | 하락 | -1.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 +0.00% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 적중: 예측=mild_bullish, 실제=bullish(+1.43%) | 상승 | 0.05 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 219 | 59.82% | 1.64% | 0.20 | 모멘텀 롱 |
| KOSDAQ | 219 | 53.42% | 0.06% | 0.07 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **+0.05**
- 누적 표본: 78
- 누적 적중률: 41.03%
- 최근 피드백: 전일 09시 예측 적중: 예측=mild_bullish, 실제=bullish(+1.43%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [환율 1,550원 육박...코스피 '검은 금요일' - YTN](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1TLTZEWFpQYUdFQkU3eTAwUk5TMnpRV09BaTJHOVE2RWJBd3VBb2E1NXhBQkdnLVFHTzg3blpUbXdEMU9QcEM5VG5QdHRfQmRTTWdUa0RvVTh0TDUzd1E?oc=5) — YTN
- [코스피, 반도체주 약세에 8300선 후퇴…환율 1550원대 마감 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTFBXREdDejJHa2JkY0ltMTlMUGE1Mm45cTFNR2dhamh6Zl82aXN2bE1uUmRUeG9Ya2UxVUktSGt2MlNWQnM1aW9ROHVQQUJvcUNDdXhqMWNiLXhZcmlIcTVzMzhvZW5ITHg3eVdXZFAtSEZKX0HSAXdBVV95cUxPWlZRQU5fYk1naDBUeWtTbW9xaGU1TlZpMUhsZVMzT0diMGVSZHdSVjZ4MzMwSG9qZjRwWjE5aGRHRTNZdTJaeW5rc0RBd2hCeE5MRUR5Z1ZZYlQ0Tmxocm45SGxQZXI5a1NJWkFEOXJhSEU2TjJyVQ?oc=5) — 스트레이트뉴스
- [외국인 48조 매도에도 "한국 떠난 건 아니다"…복귀 조건은 실적·주주환원 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1lNXZkLUF2QTNlaEE4bWRWU0s4R0tlUFRidmZXT0NiYVI0WHBZZWtiOEo3TWFnQkttOWNBZ3ZabDZhMkxpb3pmdnA2VGcxUm9XcVVHb0U5dXUwVV9i?oc=5) — 뉴스핌
- [148조원 팔아치운 외국인…하반기엔 ‘셀 코리아’ 멈출까 - 마켓인](https://news.google.com/rss/articles/CBMic0FVX3lxTE55cm93YWVuMmZfRTBnUC1mZk5zT0xGd0tDVWxLRUJmQWJ1R2dtNlN3RFdOdF9uaElXaWVmTHZLeVNiQjF2R2FGakJMRXN0UkxTX1pYSk9VRVo5cnVjUVd6cks1ejZrdUVEM2JWV1dFeUpsd1U?oc=5) — 마켓인
- [코스피 장중 급락, 삼성전자·SK하이닉스 지금 팔아야 할까? - 네이버 프리미엄콘텐츠](https://news.google.com/rss/articles/CBMifkFVX3lxTE5PV2dfOWFTOWV4RFl4WmotU202dHRnVWwxQTQ3N0Q0bThFSFRodmE0Q3JtUml1NnJNbzFNbVJ0SXdvME1ZSlpBdTM0SHhLQUg3WXVFZFJqNV8tNFVyaEdaeXRGTm1PTXZIQTVsczlabk01RklsVXRVSENsOXFPQQ?oc=5) — 네이버 프리미엄콘텐츠
- [코스피 전망은 밝다지만…개인투자자가 한국 주식 살 때 봐야 할 변수 - christiandaily.co.kr](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9TZTVYNUF2QWdSTzlzRkVtN3V3dzZERE1mRnNkZDN1R040X3ZjSzlSUkxITFN4NDlpMnNDYklRMV91cnFNR3dEVERZcXUyNkVBWVhXUDcwb9IBXEFVX3lxTE9NMGJVVjdrVXJ3OVhTSTk2UC1rSHNDdkhCYXdSNVc4RENVLXpvSW9ueWl2azBMUU1zN2VOOFY5c3Zudnp5cUxjcHJBMEFHWnRKa2UtYUpCVlRrSW5o?oc=5) — christiandaily.co.kr
- [[주간증시] 유가·환율·반도체 ‘삼각 변수’…박스권 내 ‘조건부 장세’ - 에너지경제신문](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5ELURYY1NNRnUxN2tPMnRrdzRRZFdSd3V4bU9QR3BnNDNObHpUV3lKM0JhOU8tWm1MRDIxQzRUWWI0SFJ6MHh5MHhoTngtcGo2WkhiRkpFWm9pQlU?oc=5) — 에너지경제신문
- [코스피, '검은 월요일' 오나?…주말 美 반도체 급락에 고환율 덮쳤다 - hankookilbo.com](https://news.google.com/rss/articles/CBMibkFVX3lxTE5tWkc4cmNUODU3anotR0FVYk83NUVNdE1wbU9NYW5XTVVGZV9Ib2pqSkk1aHVuNUtHQzNjLWVsSUlJRlRvS0E2aW1nZDhMcHVHWFpiSERJR05zREtvZXJHeWwtQjFjTUl2b0pCZ2tn0gFzQVVfeXFMTVQtakFqeXdIY01HQlJvcGxHbmdudFpQVE1yZVAxRFFKVkIwQmttODhpVU85cUJCdWZOaDVXNWNwV3dyUWV2YVEzYVZKSEpuOXVhRmN2QTJ6Ny12WEQya296RTFpV1hWaXFEM0s2b0tzaGtlcw?oc=5) — hankookilbo.com

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
