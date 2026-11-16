# 한국 주식시장 방향성 리포트

- 생성 시각: `2026-11-16T14:11:04+09:00`
- 단기 판정: **상승 우세** / 신뢰도: 중간~높음
- 중기 판정: **상승 우세** / 신뢰도: 중간~높음
- 총점: **4.13** = 상승 6.0 + 하락 -1.87

## 핵심 시장 지표

| 항목 | 값 | 비고 |
|---|---:|---|
| KOSPI | N/A |  |
| KOSDAQ | N/A |  |
| USD/KRW | 1,333.78 | 1M -0.53% |
| SOX | 1W 8.05% | 1M -12.39% |
| VIX | 19.30 | 위험선호/공포 지표 |
| WTI | 88.37 | 1M -12.86% |

## KOSPI/KOSDAQ 분리 모델

| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |
|---|---|---|---:|---:|---:|
| KOSPI | 상승 우세 | 상승 우세 | 4.13 | 6.0 | -1.87 |
| KOSDAQ | 상승 우세 | 상승 우세 | 4.13 | 6.0 | -1.87 |

## 예측 모델표

| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |
|---|---|---|---|---:|---|---|
| 가격/추세 | KOSPI 중기 모멘텀 | 1M -9.90%, 3M -22.38%, 6M -33.19% | 하락 | -0.5 | 높음 | 지수 자체의 중기 추세가 강하면 급락보다 눌림 후 재상승 확률이 커진다. |
| 수급 | KOSPI 외국인 순매수 | 5D 0억, 10D 0억 | 상승 | 1.0 | 매우 높음 | 한국 시장은 외국인 매매가 단기 방향을 지배하는 경우가 많다. |
| 수급 | KOSPI 개인 순매수 방어 | 개인 5D 0억, 기관 5D 0억 | 중립 | 0.0 | 중간 | 외국인 매도를 개인이 받아내는 구조는 단기 과열/분산 매물 신호가 될 수 있다. |
| 환율 | USD/KRW | 1,333.78, 1M -0.53% | 하락 | 0.5 | 높음 | 원화 약세는 외국인 환차손 우려와 할인율 부담을 높인다. |
| 글로벌/반도체 | Philadelphia SOX 단기 흐름 | 1W +8.05%, 1M -12.39% | 하락 | 1.0 | 높음 | 한국 반도체 대형주는 미국 반도체 지수와 단기 연동성이 높다. |
| 펀더멘털 | 반도체/HBM·수출 뉴스 | 수출·반도체·HBM 긍정 키워드 확인 | 상승 | 1.5 | 높음 | 한국 지수의 이익 개선은 반도체 수출 사이클에 크게 의존한다. |
| 금리 | 미국 10년물 | 5.154%, 1M +1.28% | 하락 | -1.0 | 중간~높음 | 미 장기금리 상승은 성장주와 고PER 반도체 밸류에이션을 압박한다. |
| 리스크 | VIX | 19.30 | 상승 | 1.0 | 중간 | VIX 20 이하에서는 위기성 급락보다 일반 조정일 가능성이 커진다. |
| 원자재 | WTI 유가 | 88.37달러, 1M -12.86% | 하락 | 0.0 | 중간 | 고유가는 한국의 비용·무역수지·물가 부담을 키운다. |
| 업종 | 반도체/자동차 장중 흐름 | 반도체 +0.00%, 자동차 +0.00% | 상승 | 0.5 | 높음 | KOSPI 지수 기여도가 큰 업종이 밀리면 지수 조정 압력이 커진다. |
| 국내금리 | 한국은행 기준금리 | 2.50% | 상승 | 0.5 | 중간 | 국내 기준금리 안정은 밸류에이션 하방을 일부 완충한다. |
| 피드백 | 전일 09시 예측 vs 마감 장세 | 전일 09시 예측 불일치: 예측=bullish, 실제=bearish(-0.22%) | 하락 | -0.37 | 동적 | 전일 오전 예측과 마감 장세의 적중/불일치 결과를 다음 장세 예측 점수에 반영한다. |

## 백테스트 요약

| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |
|---|---:|---:|---:|---:|---|
| KOSPI | 219 | 57.99% | 0.89% | 0.16 | 모멘텀 롱 |
| KOSDAQ | 219 | 53.42% | -0.43% | 0.07 | 모멘텀 숏 |

## 피드백 반영

- 적용 여부: 적용
- 점수 보정: **-0.37**
- 누적 표본: 90
- 누적 적중률: 40.00%
- 최근 피드백: 전일 09시 예측 불일치: 예측=bullish, 실제=bearish(-0.22%)

## 결론

- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.
- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.
- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.

## 주요 뉴스 헤드라인

- [[e마켓오프닝] 美 반도체지수 3.4% 급락···코스피 외국인 매매 향방은 - 시사저널e](https://news.google.com/rss/articles/CBMickFVX3lxTFBkMVRfaXBZZmRqZEoyeHpHUzRnVVB0NUstQllWWEFfQlFkYktQeVZ0cG1NbzdfQlpVQ2ZKMkV6ekR0ZGVienZfRHpmY3pMMWkyWEh2OHhnMHhQWGduZENXcGJuSm1CX19vLUJYeGZWQ1h5QQ?oc=5) — 시사저널e
- [[오늘 증시 전망] 코스피 5,300선 내주고 외국인 매도 전환…16일 국내 증시 방향 주목 - 업코리아](https://news.google.com/rss/articles/CBMibkFVX3lxTFBFaTVUbDU2OHJiX3R2NE1ySW13TXJ6TlBnZzNGajlFNVJQY3gxWmRHQlBzVXFBZGhEeHRuemdmUk1SU29WYXc1M0JrbjJOYnpqMWlOdHpKT0RINFV0bjNqRnFwTkRZeHVvM2xCYUR3?oc=5) — 업코리아
- [외국인, 한국 주식 193억 달러 팔았다…AI 투자 불안에 흔들리는 코스피 - 진주인터넷뉴스](https://news.google.com/rss/articles/CBMickFVX3lxTE1ETGZZQllKelgxeXpvc0VjUVIwTnRfSGlSZUtQdVpvaU45cGNiT3N3VDJZWllnOHYycTczMndyWlNkTnM0dmRKVzZmRzZmWi03WVRLOFk2ekVOVFVEM2RURU5hV3NoLTJ0aFdCQ2VoZjFGUQ?oc=5) — 진주인터넷뉴스
- [[주간증시분석] 코스피 5,500 찍고 5,290 마감…엔비디아 실적에 달린 반등의 지속력 - 강릉뉴스](https://news.google.com/rss/articles/CBMib0FVX3lxTE1SdEZsRDRxeTI0bDB2NWNxdEVKYXMzLUlSWklGZzBtNXR4X3AwcDBISG9KR1ktQVVaT2RUcWpPVjc3ZURLcHEycUh0ZmFQOG5oRXBLVWV3ZUZKUF9Fc015SEh1d0RIZ3JlMURvSUtZVQ?oc=5) — 강릉뉴스
- [[아! 코스피] ⑦ 금리·전쟁·환율 충격 같은데…한국 증시, 왜 더 흔들렸나 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE54XzM4VEhUSGJ5MmJzd09JZkN1dy1oMTJEbDJZa3V2UUxjNXZuVUJhWHBuY1EwRzEyMGFoNXJidDdMb09TZUdGRmJhZ0VtOTViZVdYQUhnM0lwQksz?oc=5) — 뉴스핌
- [“코스피, 심폐소생 가능합니까?”…전문가 3인이 꼽은 반등 조건 [증시 긴급진단①] - 매일경제 마켓](https://news.google.com/rss/articles/CBMiUkFVX3lxTE5iejFmUV92S1diUWlvMnZjc1hEeFRxQlE1OVNMc0pXSTJhTmE4cjRtSVdKU3Vhc0hnWEt1ZTVlVDk3YWpyX2pRaUU3R3lQcUZVc3c?oc=5) — 매일경제 마켓
- [환율 1,550원 육박...코스피 '검은 금요일' - YTN](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1TLTZEWFpQYUdFQkU3eTAwUk5TMnpRV09BaTJHOVE2RWJBd3VBb2E1NXhBQkdnLVFHTzg3blpUbXdEMU9QcEM5VG5QdHRfQmRTTWdUa0RvVTh0TDUzd1E?oc=5) — YTN
- [코스피 오르는데 환율도 올라…"외국인 매도의 성격이 달라졌다" - KB Think](https://news.google.com/rss/articles/CBMickFVX3lxTE1RNGlXWFBmUy1HUE5vS181RHhYZV9TdHdpcXFUZUVpWEtwQ0lhcG5IYnkyTVB0QWpTT1N5R0hzSnI0UXhQX1FIR2lPSGJaQXFZUFBTTjFVVmVHcDh6dC1aX21JTU1CNlZkSlJOaThmcUNRUQ?oc=5) — KB Think

## 방법론

각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.
