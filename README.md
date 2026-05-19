# Korea Market Direction Dashboard

한국 주식시장(KOSPI/KOSDAQ)의 단기·중기 방향성을 공개 데이터 기반 휴리스틱 모델로 점수화한 정적 리포트/대시보드입니다.

## 현재 판정

- **단기(1~5거래일): 하락/조정 우세**
- **중기(1~3개월): 조건부 상승**
- 최신 리포트: [`reports/latest.md`](reports/latest.md)
- 대시보드: GitHub Pages 배포 후 `https://domineyh.github.io/korea-market-dashboard/`

## 데이터 소스

- Naver Finance: 지수, 수급, 업종, 시가총액 상위 종목
- Yahoo Finance Chart API: 글로벌 지수, 환율, 원자재, 주요 한국 종목
- FRED: 환율, 미국 금리, VIX, 신용스프레드 등
- BOK ECOS: 한국은행 기준금리
- MOTIR/산업통상부: 수출입 동향 보도자료
- Google News RSS: 한국 증시/반도체/환율/금리 뉴스 헤드라인

## 모델 구조

각 신호를 `-2.0 ~ +2.0` 범위로 점수화합니다.

- 상승 신호: KOSPI 중기 추세, 반도체/HBM·수출 뉴스, 낮은 VIX, 국내 기준금리 안정 등
- 하락 신호: 외국인 KOSPI 순매도, 원화 약세, SOX 단기 조정, 미국 장기금리 상승, 유가 급등, 핵심 업종 약세 등

모델은 투명성을 우선한 휴리스틱입니다. 실제 투자 적용 전에는 백테스트와 리밸런싱 규칙 보정이 필요합니다.

## 로컬 생성

```bash
PYTHONPATH=src uv run python scripts/generate.py --input /tmp/korea_market_research_2026-05-19.json
```

## 테스트

```bash
PYTHONPATH=src uv run python -m unittest discover -s tests -p 'test_*.py' -v
```

## 산출물

- `docs/index.html` — GitHub Pages용 정적 대시보드
- `reports/latest.md` — Markdown 리포트
- `data/latest.json` — 원자료 스냅샷 + 예측 결과

## 면책

본 프로젝트는 정보 수집 및 연구 목적이며 투자 조언이 아닙니다.
