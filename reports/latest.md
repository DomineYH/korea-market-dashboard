# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-06-08T10:01:52+09:00`
- 단기 판정: **하락/조정 우세** / 신뢰도: 중간~높음
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **-4.86** = 상승 2.64 + 하락 -7.5

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 7,669.74 | 2026-06-08 09:49 |
| KOSDAQ | 945.34 | 2026-06-08 09:31 |
| USD/KRW | 1,547.98 | 1M 6.41% |
| SOX | 1W -4.74% | 1M 6.52% |
| VIX | 21.51 | 위험선호/공포 지표 |
| WTI | 92.53 | 1M -2.40% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 하락/조정 우세 | 조건부 상승 | -4.86 | 2.64 | -7.5 |
| KOSDAQ | 중립/하락 경계 | 중립/상승 경계 | -0.86 | 3.64 | -4.5 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M +3.74%, 3M +37.20%, 6M +92.15% | 상승 | 0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D -189,858억, 10D -250,728억 | 하락 | -2.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 161,122억, 기관 5D 27,704억 | 하락 | -1.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,547.98, 1M +6.41% | 하락 | -1.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -4.74%, 1M +6.52% | 하락 | -1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.536%, 1M +4.13% | 하락 | -1.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 21.51 | 상승 | 0.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 92.53달러, 1M -2.40% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 -7.29% | 하락 | -1.0 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 적중: 예측=mild_bullish, 실제=bullish(+1.09%) | 상승 | 0.14 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 219 | 62.10% | 2.40% | 0.24 | 모멘텀 롱 |
| KOSDAQ | 219 | 55.25% | 0.67% | 0.10 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **+0.14**
- 누적 표본: 14
- 누적 적중률: 42.86%
- 최근 피드백: 전일 09시 예측 적중: 예측=mild_bullish, 실제=bullish(+1.09%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [韓 증시, 월요일 환율 급등·반도체 충격 긴장 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTE1jWHFkaXM0YjNRRTFMR2ZpM2NBZkpFSEt5VU5WUWNsOFVSTjdXOFVnanJucHl6ZG9LUWp3UmhnTWN0cUxHSkhMWER4LVpGenBTcFBsajNldE54Xy0wWDZLTGlKamFpeGJOTWFlRWJPbFVLNzTSAXdBVV95cUxQMUVYS1RYdGJ1aWZjdWVzS05DTWtRYjVxSlFZUGx2aFVsVEVHclRvWF9BcVMyekg1MFZGeEs0WWN4MGY0dVB4cTN2Y3l0b0p3MDFwZE5mRFIxRGRDM282ODFyM0duZTZGUEQ2cF9yN09YOHQwU09sWQ?oc=5) — 스트레이트뉴스
- ['검은 월요일' 충격파 얼마나…美 지수선물·환율 시장 보며 '대응' - 뉴스1](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBjeF9xVkdDZTlxZl93d3M2XzNGMzBSbHU0VUhDak9POEQwSXRwMmwtb0pWbXJ2V3ljUVhGMnpYcjUybzBKUHJsY1V4U1hPTUZSRUJVMzl6MkRfTF9ESGM0dEVqNWY?oc=5) — 뉴스1
- [환율 1540원·외인 매도 폭탄…코스피 5% 급락 - mstoday.co.kr](https://news.google.com/rss/articles/CBMibEFVX3lxTE5Cc056NXd2Q1NQZ0hJOFFXcVVMNlJqaXl2MUNwZGx0X1BzUXNzbnk1c2Z1ckJSN0lTUjdJbzV4eE1SQnBmNnc0QWFrVmlySnVIdVZSWFRfbkZ2ejlEbnlKRVJBZlgyS2JHaG04dw?oc=5) — mstoday.co.kr
- [외국인 19일간 '66조 코스피' 매도···1530원 고환율에 수급 불안 가중 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1CZC1NVWFUeGVtdUlMRmxWQTJ3R1NzZlNsN0dWNmxVMU9jdmNNdjBnTTlkMTJsakdWYTFtSU9VSFQ0djFWRnFXMGJReFVENTdXSWZwTlhMb1NrQm9z?oc=5) — 뉴스핌
- [[속보] 코스피 8000선 붕괴…개장 직후 매도 사이드카 발동 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMic0FVX3lxTE5YNENEM1pvcTBORTMyeGhlcTA1LWxnY3oxU0ktcUZNVjdMN1ZDaWZWcFp3OHl3UTJKeEJ3bjFHd2ZOSUxpSEZDQXQ2bG50NzNuenE1eURSTnctcmRJRjZGa2ZBbU1BazJzZDdITkVSdVB2SmvSAXdBVV95cUxQU1lOc2hTTVRidTY3Z1Flc0NUYnVXMDZGQVlDRG5mZ0pwUWZWT2I4azUybUNjakNhc2FhdWk1ZDgxdFZFaGxYc2g1Q3VHYTJ3ZXJhZkt3ZEVsNjRzVnE1bXg0WWsyd2FIUndJdkRsZGJGbGR1ZHFRMA?oc=5) — 스트레이트뉴스
- [[증시전망대] 美 기술주 휘청·환율 1,530원 돌파…‘젠슨 황 효과’로 코스피 버틸까 - 뉴스로드](https://news.google.com/rss/articles/CBMibEFVX3lxTE1PMzRuNzlOZklUMW05akNkVktOcUMta3E4RzJucnRnM1pwTzF0aUZja1Jrbl9BTWdpYS01U2syeGxHd2JYWm4wS0FaVDZnVHZqSzVCTk1kVHN5Q3R0QWdBUjFFQWR4c0szOVZPRNIBb0FVX3lxTE5fSS1hdGNiMFhESl9PNm5xdFFpWUlYRGRkYzY1eDlsRHJSaFl1RF9iVTF5UUxXSkNJdUxhSGhuTnU2V3A5Z00zenY5REE0NFdWM1oxNHdfVWhBa2ZneUF1MDdqZ1VJTVpmM0w0ZmJGQQ?oc=5) — 뉴스로드
- [삼성전자·SK하이닉스 급락에도…골드만삭스 "코스피 12000 간다" - TopStarNews](https://news.google.com/rss/articles/CBMickFVX3lxTFBlV0Rtckg0cm5BVDQ4WF8tMmZldEwzeF9peHZmRkJtWDhvSThaSzZ2dWxtbGl4b1FJYk5PWmJnYmxvOEtuRGM4NzUzR2d4bVp2Q0U1ZDI1b0ZPMXFIRldxd0kyVEprbzE1b2E1YWU5WnpYUQ?oc=5) — TopStarNews
- [100조 투매에도 지분율은 상승… 코스피 불장이 만든 ‘외인 지분 미스터리’ - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUm1oVVVsV3FfeXFOTzk1UnJyamRVMWRPS09LVjhSWFEtbHNBUkY2eVJINm1jSmlmLWx0OGhQcGZFUTdmR2x3YzdHNVE4MkNlcE9YMnBtdXlyb0p3bXRuNXRpaXQ0aXNKUHE4M1lWT3E0eDRQaHVvSkNTaFlZVGFqektvX3BNS1Jm0gGcAUFVX3lxTFBlMWpZVlNWRzJrTHlzX25hRXV0dUNkaTFNZHZ0cDd1WVJuaE5SM0VEbnhNR1lmY2dyQkVaUnotY1ppT0hRN2RSenRxenJ3X24wQkNSRWZtQ0FKaDJTX2F4NWhqa2EtMVZ6LUgzNDhGRk9tNGhqTDFXa0RXeXRwVmpVeEZ6QmdYQVlDbHBMQkpxZmxmR2hPODhaaTBpcA?oc=5) — Chosunbiz

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
