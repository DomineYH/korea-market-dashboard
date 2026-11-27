# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-11-27T09:14:52+09:00`
- 단기 판정: **중립/상승 경계** / 신뢰도: 중간
- 중기 판정: **상승 우세** / 신뢰도: 중간~높음
- 총점: **1.23** = 상승 4.0 + 하락 -2.77

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | N/A |  |
| KOSDAQ | N/A |  |
| USD/KRW | 1,344.18 | 1M 0.29% |
| SOX | 1W -9.10% | 1M -23.58% |
| VIX | 26.80 | 위험선호/공포 지표 |
| WTI | 85.01 | 1M -17.29% |

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
| 환율 | USD/KRW | 1,344.18, 1M +0.29% | 하락 | 0.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -9.10%, 1M -23.58% | 하락 | -1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.848%, 1M -2.90% | 하락 | 0.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 26.80 | 상승 | -1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 85.01달러, 1M -17.29% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 +0.00% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=mild_bullish, 실제=bearish(-0.23%) | 하락 | -0.27 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 218 | 57.80% | 0.59% | 0.16 | 모멘텀 롱 |
| KOSDAQ | 218 | 53.67% | -0.58% | 0.07 | 모멘텀 숏 |

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

- [[오늘 증시 전망] 코스피 4,700선 회복했지만 상승폭 축소…27일 외국인 수급·환율이 관건 - 업코리아](https://news.google.com/rss/articles/CBMibkFVX3lxTE9CMkFEdXBqQ3dRX0x4c3Y4M00tU1Z3LWxqcjJEWkFIbTNOR2JNUDNXZFllMExnYkdxVUFDNmQybTJSM2VhQWl4MS1WTDdmYmVDMGMzMUZPWC1WN0pYRmdPWFZCWXVxR0M4a1YwSW93?oc=5) — 업코리아
- ["코스피 4200선까지 밀릴 수도"…최악의 전망 나왔다 - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5pb2RVSF9udHV4RHpfdUQxbno4aWVTbDZZazZxbTk5RzZ2Q05YNWp1NEZhM2Ffd1N3bHZMakZDX3BJaVhtVHU5MUI1MWFxSHpKR05VTUl3SEwtZw?oc=5) — 한국경제
- [[오늘 증시 전망] 코스피 6.16% 급락, 4,700선 붕괴…오늘 한국은행 금리 결정에 시장 촉각 - 업코리아](https://news.google.com/rss/articles/CBMibkFVX3lxTFBtcUtXVjF3UDBKY1prbUdmZVJVQmd6X2VOQWw0Q2FselBKZ2dnUkVNZGxmeVRPeHktMTZDMEZ0dm03ZDJzMzF1bzMwSDhMYThkSFJpaC1NT2V3M3FZTFZZVkhoVFNNOXA0RlY5bXlB?oc=5) — 업코리아
- [환율 1,550원 육박...코스피 '검은 금요일' - YTN](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1TLTZEWFpQYUdFQkU3eTAwUk5TMnpRV09BaTJHOVE2RWJBd3VBb2E1NXhBQkdnLVFHTzg3blpUbXdEMU9QcEM5VG5QdHRfQmRTTWdUa0RvVTh0TDUzd1E?oc=5) — YTN
- [[데일리 시장해부] 코스피 급락 왜? 외국인 매도와 환율이 흔든 한국 증시 - 네이버 프리미엄콘텐츠](https://news.google.com/rss/articles/CBMikgFBVV95cUxOd1JYSDd1cnRIcjNUdUtDc3czRUdzb1ZqTXNBZnpCNGJLY3hwcVBsRURneV96SEUyQjEzcUQ4RG9BcWFRUVJ6b2wxT3lDTzRNNTNoOEFWcjZRekFJcDFEQVpOUS1rTk1JNWZpUTBtSkJWN0xLNWpBRFY2dXdXNHVfSEpXaHRKOWhaS1RtZV9ReEY1Zw?oc=5) — 네이버 프리미엄콘텐츠
- [[AI MY 증시전망] "코스피 보합권 숨고르기…순환매 확산 주목" - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5WcGI0TmhEUjk3SVVlS2FlcHBuMk5aN2kxdFZHQkhhUzBvaHZFQzI4bHhtZUNiZDJzOG5EWVUxUk9ZSkUwV0xFSEVQdkJ6aERSc0FGaDZzcWRiaGJo?oc=5) — 뉴스핌
- [코스피, 8000 찍고 급등락…“코스피 고평가 vs 저평가” 혼란 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTFBfT1FjSllZbVVFT2I5cVRDdlE3b2djUW5WWXNlWkJSSlJJY3Z1elFzdnZ5MHVzOWVNeVlWbjJEaVVOcGVYTDlvTGVONVZmcDFFaEVjTy1TTHNJeTBpcjlzUVA4ZnhtSEVsMU1QOW45TzVvbTjSAXdBVV95cUxQRENENzh0eE5NWlhKbjdYNWFzMGRNTXVPOHdEZXdJa3VvN1c2amFmSnYxVWhuNmN2M3g4OFlkZXhIZDFRaTMtc0hJVGRRZGxtM3ZBUW1EOGNLQ2ZTbnFnVHB5NzRLZnhXUWlwdld6WE5tRmtEX3pSRQ?oc=5) — 스트레이트뉴스
- [[증시 레이더] 코스피, 반도체 반등에 8,470선 회복⋯환율 1,549원대 부담은 지속 - 포커스온경제](https://news.google.com/rss/articles/CBMiYEFVX3lxTE50MzduX3YtZm5XOGdGWVNydUdITkNaMnBody1LeXNzUTI0N2NNaE0wSTkyMkFaS1QzV3A0SmlHXzl2cVpVUEJzWEdqdkp4Y0ZKU2Y1MkNMb0N1WUxZeDNodg?oc=5) — 포커스온경제

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
