# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-11-20T09:14:36+09:00`
- 단기 판정: **중립** / 신뢰도: 낮음~중간
- 중기 판정: **상승 우세** / 신뢰도: 중간~높음
- 총점: **0.46** = 상승 4.06 + 하락 -3.6

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | N/A |  |
| KOSDAQ | N/A |  |
| USD/KRW | 1,336.18 | 1M 0.80% |
| SOX | 1W -10.35% | 1M -18.13% |
| VIX | 28.44 | 위험선호/공포 지표 |
| WTI | 82.85 | 1M -14.72% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 중립 | 상승 우세 | 0.46 | 4.06 | -3.6 |
| KOSDAQ | 중립 | 상승 우세 | 0.46 | 4.06 | -3.6 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M -8.74%, 3M -27.38%, 6M -36.51% | 하락 | -0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D 0억, 10D 0억 | 상승 | 1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 0억, 기관 5D 0억 | 중립 | 0.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,336.18, 1M +0.80% | 하락 | 0.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -10.35%, 1M -18.13% | 하락 | -1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 5.052%, 1M -1.83% | 하락 | 0.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 28.44 | 상승 | -1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 82.85달러, 1M -14.72% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 +0.00% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 리스크 | VIX 급등 꼬리 가드 | VIX 28.44 (임계 28) | 하락 | -1.1 | 높음 | VIX 급등 국면에서는 상승 방향 총점을 중립 상한으로 제한해 변동성 충격기의 상승 오판을 줄인다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 적중: 예측=bullish, 실제=bullish(+0.39%) | 상승 | 0.06 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 218 | 57.80% | 0.82% | 0.16 | 모멘텀 롱 |
| KOSDAQ | 218 | 53.67% | -0.47% | 0.07 | 모멘텀 숏 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **+0.06**
- 누적 표본: 93
- 누적 적중률: 39.78%
- 최근 피드백: 전일 09시 예측 적중: 예측=bullish, 실제=bullish(+0.39%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [[오늘 증시 전망] 코스피 5,100선 회복했지만 뉴욕증시 급락…20일 외국인 수급이 관건 - 업코리아](https://news.google.com/rss/articles/CBMibkFVX3lxTE1VTmVVYWxLVkxmSVlWa3NydEVRMkVSNmdBUGowTXBOV3FtTmZEdEZTWXpMWU9OVGNKRGt6QndkR2std2FOWi11T21VOTNkYy03V1k0bHBSeUZzOVp2WFVWc3M4T3lJVVR3TWZBQmZ3?oc=5) — 업코리아
- [코스피 5000선 결국 무너져.....외국인 투자자들의 대규모 매도세가 원인 - 정경시사 FOCUS](https://news.google.com/rss/articles/CBMiaEFVX3lxTE54bFlDb1l1NTIzVUZTQlhna0hXaHAwS3JkUGo0VmZKZUl1TjhOcWdDZC1FbmhqYjVoWjM3RUFwUUNscWVHSUFrMUFtc3hwLTUwNXhBVFp5Tjc0eVdVYzFndWwyLWp6Mkxu?oc=5) — 정경시사 FOCUS
- [[오늘 증시 전망] 코스피 5,000선 붕괴…외국인 1조4,000억원대 매도에 18일 증시 긴장 - 업코리아](https://news.google.com/rss/articles/CBMibkFVX3lxTE01NUQyVW5rQ3NyWU04dF81M2FYVk5PTkxXMHd1WERzTUVfN1drNHRxYjh3dGJjUDg5dzQ0MkVzamdsbTlLcFhxMnJhdldJbEFmSl84NnNRS3EwZFJVQTVuOTRlenByTnU1YmNCYkpn?oc=5) — 업코리아
- [“코스피, 심폐소생 가능합니까?”…전문가 3인이 꼽은 반등 조건 [증시 긴급진단①] - 매일경제 마켓](https://news.google.com/rss/articles/CBMiUkFVX3lxTE5iejFmUV92S1diUWlvMnZjc1hEeFRxQlE1OVNMc0pXSTJhTmE4cjRtSVdKU3Vhc0hnWEt1ZTVlVDk3YWpyX2pRaUU3R3lQcUZVc3c?oc=5) — 매일경제 마켓
- [[아! 코스피] ⑦ 금리·전쟁·환율 충격 같은데…한국 증시, 왜 더 흔들렸나 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE54XzM4VEhUSGJ5MmJzd09JZkN1dy1oMTJEbDJZa3V2UUxjNXZuVUJhWHBuY1EwRzEyMGFoNXJidDdMb09TZUdGRmJhZ0VtOTViZVdYQUhnM0lwQksz?oc=5) — 뉴스핌
- [환율 1,550원 육박...코스피 '검은 금요일' - YTN](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1TLTZEWFpQYUdFQkU3eTAwUk5TMnpRV09BaTJHOVE2RWJBd3VBb2E1NXhBQkdnLVFHTzg3blpUbXdEMU9QcEM5VG5QdHRfQmRTTWdUa0RvVTh0TDUzd1E?oc=5) — YTN
- [코스피, 8000 찍고 급등락…“코스피 고평가 vs 저평가” 혼란 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTFBfT1FjSllZbVVFT2I5cVRDdlE3b2djUW5WWXNlWkJSSlJJY3Z1elFzdnZ5MHVzOWVNeVlWbjJEaVVOcGVYTDlvTGVONVZmcDFFaEVjTy1TTHNJeTBpcjlzUVA4ZnhtSEVsMU1QOW45TzVvbTjSAXdBVV95cUxQRENENzh0eE5NWlhKbjdYNWFzMGRNTXVPOHdEZXdJa3VvN1c2amFmSnYxVWhuNmN2M3g4OFlkZXhIZDFRaTMtc0hJVGRRZGxtM3ZBUW1EOGNLQ2ZTbnFnVHB5NzRLZnhXUWlwdld6WE5tRmtEX3pSRQ?oc=5) — 스트레이트뉴스
- [[오늘 증시 전망] 코스피 5,100선까지 급락…뉴욕 나스닥 2.49% 하락에 국내 증시 긴장 - 업코리아](https://news.google.com/rss/articles/CBMibkFVX3lxTE1JQkxEOFhiWlhvMldwMkdJdHhEdnlSSDFtbS1iNTBZMThfTW9KZzVRdkdDM0RiQ1Q3SS1kLVUzM21XZ2xCbTVYcm0yMXA3bll4ZUQxTEZpY1JLaFJyZkZ5X0ZqcElfVTducnFTZ1pB?oc=5) — 업코리아

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
