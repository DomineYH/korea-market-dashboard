# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-06-05T17:25:52+09:00`
- 단기 판정: **중립/상승 경계** / 신뢰도: 중간
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **0.54** = 상승 6.04 + 하락 -5.5

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 8,160.59 | 2026-06-05 16:56 |
| KOSDAQ | 1,002.44 | 2026-06-05 16:10 |
| USD/KRW | 1,538.48 | 1M 6.51% |
| SOX | 1W 6.15% | 1M 24.01% |
| VIX | 15.74 | 위험선호/공포 지표 |
| WTI | 92.64 | 1M -2.57% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 중립/상승 경계 | 조건부 상승 | 0.54 | 6.04 | -5.5 |
| KOSDAQ | 상승 우세 | 조건부 상승 | 3.04 | 5.54 | -2.5 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M +17.64%, 3M +60.21%, 6M +106.03% | 상승 | 2.0 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D -203,548억, 10D -256,209억 | 하락 | -2.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 145,721억, 기관 5D 53,389억 | 하락 | -1.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,538.48, 1M +6.51% | 하락 | -1.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W +6.15%, 1M +24.01% | 하락 | 1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.477%, 1M +1.38% | 하락 | 0.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 15.74 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 92.64달러, 1M -2.57% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 -7.61%, 자동차 +0.00% | 하락 | -1.0 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=mild_bullish, 실제=neutral(-0.08%) | 상승 | 0.04 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 219 | 62.56% | 2.46% | 0.25 | 모멘텀 롱 |
| KOSDAQ | 218 | 55.05% | 0.77% | 0.10 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **+0.04**
- 누적 표본: 13
- 누적 적중률: 38.46%
- 최근 피드백: 전일 09시 예측 불일치: 예측=mild_bullish, 실제=neutral(-0.08%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [환율 1540원·외인 매도 폭탄…코스피 5% 급락 - mstoday.co.kr](https://news.google.com/rss/articles/CBMibEFVX3lxTE5Cc056NXd2Q1NQZ0hJOFFXcVVMNlJqaXl2MUNwZGx0X1BzUXNzbnk1c2Z1ckJSN0lTUjdJbzV4eE1SQnBmNnc0QWFrVmlySnVIdVZSWFRfbkZ2ejlEbnlKRVJBZlgyS2JHaG04dw?oc=5) — mstoday.co.kr
- [외국인 20일째 매도 폭탄에 코스피 5%대 급락…반도체 쇼크와 고환율 직격탄 - 2news.co.kr](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBhSFplenl5VnZGRFJ6c25TOWExM1RuN1lJSGlKMlFHYmpDLVZHOUZRQ2xBcWZRR3VsanhIcUt5akpPUFRuYi05cVZOOFBJUzV5WXJyaFFXbWk1VHRIREd5RFNYRzZIWVE?oc=5) — 2news.co.kr
- [[증시전망대] 美 기술주 휘청·환율 1,530원 돌파…‘젠슨 황 효과’로 코스피 버틸까 - 뉴스로드](https://news.google.com/rss/articles/CBMibEFVX3lxTE1PMzRuNzlOZklUMW05akNkVktOcUMta3E4RzJucnRnM1pwTzF0aUZja1Jrbl9BTWdpYS01U2syeGxHd2JYWm4wS0FaVDZnVHZqSzVCTk1kVHN5Q3R0QWdBUjFFQWR4c0szOVZPRNIBb0FVX3lxTE5fSS1hdGNiMFhESl9PNm5xdFFpWUlYRGRkYzY1eDlsRHJSaFl1RF9iVTF5UUxXSkNJdUxhSGhuTnU2V3A5Z00zenY5REE0NFdWM1oxNHdfVWhBa2ZneUF1MDdqZ1VJTVpmM0w0ZmJGQQ?oc=5) — 뉴스로드
- [외국인 19일간 '66조 코스피' 매도···1530원 고환율에 수급 불안 가중 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1CZC1NVWFUeGVtdUlMRmxWQTJ3R1NzZlNsN0dWNmxVMU9jdmNNdjBnTTlkMTJsakdWYTFtSU9VSFQ0djFWRnFXMGJReFVENTdXSWZwTlhMb1NrQm9z?oc=5) — 뉴스핌
- [코스피, 8000 찍고 급등락…“코스피 고평가 vs 저평가” 혼란 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTFBfT1FjSllZbVVFT2I5cVRDdlE3b2djUW5WWXNlWkJSSlJJY3Z1elFzdnZ5MHVzOWVNeVlWbjJEaVVOcGVYTDlvTGVONVZmcDFFaEVjTy1TTHNJeTBpcjlzUVA4ZnhtSEVsMU1QOW45TzVvbTjSAXdBVV95cUxQRENENzh0eE5NWlhKbjdYNWFzMGRNTXVPOHdEZXdJa3VvN1c2amFmSnYxVWhuNmN2M3g4OFlkZXhIZDFRaTMtc0hJVGRRZGxtM3ZBUW1EOGNLQ2ZTbnFnVHB5NzRLZnhXUWlwdld6WE5tRmtEX3pSRQ?oc=5) — 스트레이트뉴스
- [100조 투매에도 지분율은 상승… 코스피 불장이 만든 ‘외인 지분 미스터리’ - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUm1oVVVsV3FfeXFOTzk1UnJyamRVMWRPS09LVjhSWFEtbHNBUkY2eVJINm1jSmlmLWx0OGhQcGZFUTdmR2x3YzdHNVE4MkNlcE9YMnBtdXlyb0p3bXRuNXRpaXQ0aXNKUHE4M1lWT3E0eDRQaHVvSkNTaFlZVGFqektvX3BNS1Jm0gGcAUFVX3lxTFBlMWpZVlNWRzJrTHlzX25hRXV0dUNkaTFNZHZ0cDd1WVJuaE5SM0VEbnhNR1lmY2dyQkVaUnotY1ppT0hRN2RSenRxenJ3X24wQkNSRWZtQ0FKaDJTX2F4NWhqa2EtMVZ6LUgzNDhGRk9tNGhqTDFXa0RXeXRwVmpVeEZ6QmdYQVlDbHBMQkpxZmxmR2hPODhaaTBpcA?oc=5) — Chosunbiz
- [코스피 13조 던진 외국인, 유턴 필수 조건은 환율·금리·AI - 뉴스1](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBhNlZWN01CRFVkYWFrTWVpZFMxNXBqUXVnQUN4NzEyZGg1UTB0aTRBZzU1VzNfbTZiLWFJMEFGZnR2UDN1aTJKWmtPbmNqbjV6OU5PUWxlV29MWnFOVDM4?oc=5) — 뉴스1
- [해외 투자기관은 왜 한국 반도체를 다시 보나…삼성전자·SK하이닉스 전망 분석 - christiandaily.co.kr](https://news.google.com/rss/articles/CBMiV0FVX3lxTE84MTkwOVczNlhEc2VUYzF4WGhVZWdLSUMtVXNTTTdUQVZYbVF2eDBmS3hsLURpeUtkSFJxbnZwYmhRZjZxLVFKUWVacC0xeElweFduMEZYSdIBXEFVX3lxTFBCeXU1ZlM1bURQYjVIMTFCcWpkMjd5MHRacTZ0SWNlbUdCVU83YklLVFZZcjdyV1VUb3poLUlQUVdnamIzS1g5eThsV0FETFdKTEhtM0JMYzJmWTFF?oc=5) — christiandaily.co.kr

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
