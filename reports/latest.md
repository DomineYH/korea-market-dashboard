# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-05-20T09:56:52+09:00`
- 단기 판정: **하락/조정 우세** / 신뢰도: 중간~높음
- 중기 판정: **조건부 상승** / 신뢰도: 중간
- 총점: **-2.12** = 상승 5.5 + 하락 -7.62

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | 7,201.47 | 2026-05-20 09:46 |
| KOSDAQ | 1,058.12 | 2026-05-20 09:44 |
| USD/KRW | 1,511.28 | 1M 2.86% |
| SOX | 1W -3.51% | 1M 17.78% |
| VIX | 18.06 | 위험선호/공포 지표 |
| WTI | 103.84 | 1M 15.88% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 하락/조정 우세 | 조건부 상승 | -2.12 | 5.5 | -7.62 |
| KOSDAQ | 중립 | 조건부 상승 | 0.38 | 5.0 | -4.62 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M +16.39%, 3M +30.50%, 6M +73.63% | 상승 | 2.0 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D -183,217억, 10D -424,635억 | 하락 | -2.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 173,979억, 기관 5D 7,204억 | 하락 | -1.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,511.28, 1M +2.86% | 하락 | -1.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W -3.51%, 1M +17.78% | 하락 | -1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 4.667%, 1M +9.81% | 하락 | -1.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 18.06 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 103.84달러, 1M +15.88% | 하락 | -1.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 -0.13%, 자동차 +0.00% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 적중: 예측=bearish, 실제=bearish(-0.19%) | 하락 | -0.12 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 220 | 61.82% | 2.17% | 0.24 | 모멘텀 롱 |
| KOSDAQ | 219 | 55.25% | 0.90% | 0.10 | 모멘텀 롱 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.12**
- 누적 표본: 1
- 누적 적중률: 100.00%
- 최근 피드백: 전일 09시 예측 적중: 예측=bearish, 실제=bearish(-0.19%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [[AI MY 증시전망] 코스피, 외국인 6조 매도 충격…반도체·금리 변수 속 변동성 지속 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9UOEh3YWFhSzk4QmQ2UVo3bklUaWFwaFV1Q1JGWm9wV2tWREVOOTZHaGFBeGtfbzhuUFRhWWlXb2M4cDV4MmdyN05yRzM5UlprU3JYc1ZUWFVOM1F0?oc=5) — 뉴스핌
- [코스피 8000 찍고 급등락…“코스피 고평가 vs 저평가” 혼란 - 스트레이트뉴스](https://news.google.com/rss/articles/CBMid0FVX3lxTFBEQ0Q3OHR4Tk1aWEpuN1g1YXMwZE1NdU84d0Rld0lrdW83VzZqYWZKdjFVaG42Y3YzeDg4WWRleEhkMVFpMy1zSElUZFFkbG0zdkFRbUQ4Y0tDZlNucWdUcHk3NEtmeFdRaXB2V3pYTm1Ga0RfelJF0gF3QVVfeXFMUERDRDc4dHhOTVpYSm43WDVhczBkTU11Tzh3RGV3SWt1bzdXNmphZkp2MVVobjZjdjN4ODhZZGV4SGQxUWkzLXNISVRkUWRsbTN2QVFtRDhjS0NmU25xZ1RweTc0S2Z4V1FpcHZXelhObUZrRF96UkU?oc=5) — 스트레이트뉴스
- [[증시전망] 변동성 커진 코스피...반도체 '숨고르기' 속 방향성 탐색 - 디지털투데이](https://news.google.com/rss/articles/CBMic0FVX3lxTE1SUlZhVUtNc2xHZ3lfbm10TzYtbG9uRzZfZUpka281eHA1WlhxNE9SVHFicFdIX3FvZElxMFRPOXc2alJfQkF0cFBkNWUwZlVKRXlBbWdmZ1JZQ0Fqei1DSW8zRzQ0SDRZNDVJd29jTWVDTGs?oc=5) — 디지털투데이
- [코스피 '꿈의 8000선' 뚫었다…한국 증시 사상 첫 신기원 - mstoday.co.kr](https://news.google.com/rss/articles/CBMibEFVX3lxTFAtc2VMWG9GYzFnUjI2OVhPMzRsd2ZRMllIUXpIREpGcHZjbVpTMFZJVkppX3R5WC1kNDFGcURhTzYxeHZXVFk5OXlrZjFlZ0NCTHZ4NHkyeVZhS012QTlkQXBILWJFcGttdEZ6UQ?oc=5) — mstoday.co.kr
- [[데일리 경제 분석] (5월 13일) 반도체가 밀어 올린 성장 전망, 환율·유가·수급 불안이 시장의 체력을 시험하다 - 미디어피아](https://news.google.com/rss/articles/CBMibEFVX3lxTE0taThuUHBaYV9GbVRDdGdaclB2T3dXREtVZmxYZWVyQXZHMnpvRkxtdE1sdmRsY0VFM3RVZmZ3ZnlSajVfdHVpaFZFQThLSzdCdm9ubEwyWm9NVHNXQTJsMGpVemI3M3BnSDNWdA?oc=5) — 미디어피아
- [[주간증시] 유가·환율·반도체 ‘삼각 변수’…박스권 내 ‘조건부 장세’ - 에너지경제신문](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5ELURYY1NNRnUxN2tPMnRrdzRRZFdSd3V4bU9QR3BnNDNObHpUV3lKM0JhOU8tWm1MRDIxQzRUWWI0SFJ6MHh5MHhoTngtcGo2WkhiRkpFWm9pQlU?oc=5) — 에너지경제신문
- [중동 리스크, 아직 실적 충격은 아니다…“코스피 조정 본질은 외국인 베타 축소” - 마켓인](https://news.google.com/rss/articles/CBMic0FVX3lxTE1CUnNyN3NXdzYwVkJHQUxYOXFYTWV1TUl1VVBCVXpKMFVNYjRudFZZbFM0d2RSNHRLeHR0a2Y5bDUzNmZ5VGkwMm1KLVNNVGppZmtSbVlQejlLR3l4TF9XdUZ4Z0Rkd3p1QkZCVWlGcmJwQ1U?oc=5) — 마켓인
- [코스피 13조 던진 외국인, 유턴 필수 조건은 환율·금리·AI - 뉴스1](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBhNlZWN01CRFVkYWFrTWVpZFMxNXBqUXVnQUN4NzEyZGg1UTB0aTRBZzU1VzNfbTZiLWFJMEFGZnR2UDN1aTJKWmtPbmNqbjV6OU5PUWxlV29MWnFOVDM4?oc=5) — 뉴스1

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
