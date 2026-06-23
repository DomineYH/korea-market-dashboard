# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-06-23T17:15:14+09:00`
- 단기 판정: **하락/조정 우세** / 신뢰도: 중간~높음
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **-2.5** = 상승 3.5 + 하락 -6.0

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 8,203.84 | 2026-06-23 16:48 |
| KOSDAQ | 891.52 | 2026-06-23 16:36 |
| USD/KRW | 1,537.70 | 1M 1.64% |
| SOX | 1W 9.45% | 1M 23.88% |
| VIX | 20.42 | 위험선호/공포 지표 |
| WTI | 73.49 | 1M -23.73% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 하락/조정 우세 | 조건부 상승 | -2.5 | 3.5 | -6.0 |
| KOSDAQ | 중립/상승 경계 | 상승 우세 | 0.5 | 4.0 | -3.5 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M +4.97%, 3M +41.91%, 6M +96.87% | 상승 | 0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D -67,516억, 10D -61,742억 | 하락 | -2.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 124,997억, 기관 5D -56,424억 | 하락 | -1.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,537.70, 1M +1.64% | 하락 | -1.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W +9.45%, 1M +23.88% | 하락 | 1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.451%, 1M -4.63% | 하락 | 0.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 20.42 | 상승 | 0.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 73.49달러, 1M -23.73% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 -11.93%, 자동차 -10.88% | 하락 | -1.0 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=bullish, 실제=bearish(-0.40%) | 하락 | -0.5 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 220 | 60.45% | 2.49% | 0.21 | 모멘텀 롱 |
| KOSDAQ | 220 | 54.09% | 0.52% | 0.08 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.50**
- 누적 표본: 25
- 누적 적중률: 44.00%
- 최근 피드백: 전일 09시 예측 불일치: 예측=bullish, 실제=bearish(-0.40%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [[AI MY 증시전망] "반도체 조정 여파 속 유가 안정에 낙폭 제한 전망" - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBwa2lZYzd0QWtzeGs3UHBzZkliY2JOcUdiVk5wczBoMWZhX2hSeTcwd20wdXNIcmlMWWNTd1BoTXI5cm05aHRtT3BKakU0dlcxcXpUTXFPRkhUOC1F?oc=5) — 뉴스핌
- [韓 증시, 월요일 환율 급등·반도체 충격 긴장 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTE1jWHFkaXM0YjNRRTFMR2ZpM2NBZkpFSEt5VU5WUWNsOFVSTjdXOFVnanJucHl6ZG9LUWp3UmhnTWN0cUxHSkhMWER4LVpGenBTcFBsajNldE54Xy0wWDZLTGlKamFpeGJOTWFlRWJPbFVLNzTSAXdBVV95cUxQMUVYS1RYdGJ1aWZjdWVzS05DTWtRYjVxSlFZUGx2aFVsVEVHclRvWF9BcVMyekg1MFZGeEs0WWN4MGY0dVB4cTN2Y3l0b0p3MDFwZE5mRFIxRGRDM282ODFyM0duZTZGUEQ2cF9yN09YOHQwU09sWQ?oc=5) — 스트레이트뉴스
- [환율 1540원·외인 매도 폭탄…코스피 5% 급락 - mstoday.co.kr](https://news.google.com/rss/articles/CBMibEFVX3lxTE5Cc056NXd2Q1NQZ0hJOFFXcVVMNlJqaXl2MUNwZGx0X1BzUXNzbnk1c2Z1ckJSN0lTUjdJbzV4eE1SQnBmNnc0QWFrVmlySnVIdVZSWFRfbkZ2ejlEbnlKRVJBZlgyS2JHaG04dw?oc=5) — mstoday.co.kr
- [코스피, 8800선 탈환…‘9000피’ 열쇠는 외국인 수급 확산 - 직썰](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5kUE4xclpmV0hON0p2YjRxQXUyOEZ1QkluRjcybm1fMnE4TDF2dVVMcE9wSFJ2d3dkcVkxMXRvNEVHMHN4Sm9oNWNmZWdVOXF2aV9vS2R3Q1pkYmhuLTd0VE5mM2Q2Z3g10gFsQVVfeXFMTTJXWkdiVHlzUWplR2M0cGJjNGM2NURIRmV2aGpkemlzNmo4NWxSR09xaWNwQ3ZzRVBNRlJQVWlERWVGRnVjTlN1X3BBVXVkWmx4MVI1R2VjVmRpVE9YS2hqc19LZG5EUFFXcHlY?oc=5) — 직썰
- [외국인 20일째 매도 폭탄에 코스피 5%대 급락…반도체 쇼크와 고환율 직격탄 - 2news.co.kr](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBhSFplenl5VnZGRFJ6c25TOWExM1RuN1lJSGlKMlFHYmpDLVZHOUZRQ2xBcWZRR3VsanhIcUt5akpPUFRuYi05cVZOOFBJUzV5WXJyaFFXbWk1VHRIREd5RFNYRzZIWVE?oc=5) — 2news.co.kr
- [[증시전망대] 美 기술주 휘청·환율 1,530원 돌파…‘젠슨 황 효과’로 코스피 버틸까 - 뉴스로드](https://news.google.com/rss/articles/CBMia0FVX3lxTE9ScEtFRXAzdXctaXNqdjA2aGY2Z3FQLVRvdUZ0RTV2dzZsVlVEdE1nQzJIZE14Um15VTBxMnhxeVNGVnpOUHJFTFNtTzZuT3d4WXRUY1drWGZkMUR0azNaOEJKSUdJTF9aeTgw0gFvQVVfeXFMTl9JLWF0Y2IwWERKX082bnF0UWlZSVhEZGRjNjV4OWxEclJoWXVEX2JVMXlRTFdKQ0l1TGFIaG5OdTZXcDlnTTN6djlEQTQ0V1YzWjE0d19VaEFrZmd5QXUwN2pnVUlNWmYzTDRmYkZB?oc=5) — 뉴스로드
- [100조 투매에도 지분율은 상승… 코스피 불장이 만든 ‘외인 지분 미스터리’ - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUm1oVVVsV3FfeXFOTzk1UnJyamRVMWRPS09LVjhSWFEtbHNBUkY2eVJINm1jSmlmLWx0OGhQcGZFUTdmR2x3YzdHNVE4MkNlcE9YMnBtdXlyb0p3bXRuNXRpaXQ0aXNKUHE4M1lWT3E0eDRQaHVvSkNTaFlZVGFqektvX3BNS1Jm0gGcAUFVX3lxTFBlMWpZVlNWRzJrTHlzX25hRXV0dUNkaTFNZHZ0cDd1WVJuaE5SM0VEbnhNR1lmY2dyQkVaUnotY1ppT0hRN2RSenRxenJ3X24wQkNSRWZtQ0FKaDJTX2F4NWhqa2EtMVZ6LUgzNDhGRk9tNGhqTDFXa0RXeXRwVmpVeEZ6QmdYQVlDbHBMQkpxZmxmR2hPODhaaTBpcA?oc=5) — Chosunbiz
- [[주간증시] 유가·환율·반도체 ‘삼각 변수’…박스권 내 ‘조건부 장세’ - 에너지경제신문](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5ELURYY1NNRnUxN2tPMnRrdzRRZFdSd3V4bU9QR3BnNDNObHpUV3lKM0JhOU8tWm1MRDIxQzRUWWI0SFJ6MHh5MHhoTngtcGo2WkhiRkpFWm9pQlU?oc=5) — 에너지경제신문

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
