# Korea Market Direction Dashboard

한국 주식시장(KOSPI/KOSDAQ)의 단기·중기 방향성을 공개 데이터 기반 휴리스틱 모델로 점수화한 정적 리포트/대시보드입니다.

## Links

- Dashboard: https://domineyh.github.io/korea-market-dashboard/
- Latest report: [`reports/latest.md`](reports/latest.md)
- Backtest report: [`reports/backtest.md`](reports/backtest.md)
- Machine-readable payload: [`data/latest.json`](data/latest.json)

## Current Features

1. **Daily auto-update**
   - GitHub Actions workflow: [`.github/workflows/auto-update.yml`](.github/workflows/auto-update.yml)
   - Schedule: `0 7 * * 1-5` = 16:00 KST on weekdays, after the 15:30 Korean market close
   - Collects public data, rebuilds `docs/index.html`, `reports/*.md`, `data/*.json`, commits, and pushes.

2. **Prediction model table**
   - Signals are scored from `-2.0` to `+2.0`.
   - Inputs include foreign/retail/institution flows, USD/KRW, SOX, U.S. rates, VIX, WTI, sectors, BOK base rate, and news headlines.
   - Produces aggregate short-term and medium-term verdicts.

3. **Backtest**
   - Uses historical Yahoo Finance KOSPI/KOSDAQ price series.
   - Current baseline is a transparent 20-session momentum rule with 5-session forward horizon.
   - Outputs hit rate, average forward return, and suggested model weight.

4. **Alerts**
   - `scripts/update.py` compares the previous and current short-term verdict.
   - If the verdict bias changes and `DISCORD_WEBHOOK_URL` exists as a GitHub Actions secret, it posts a Discord webhook alert.
   - Configure secret:
     ```bash
     gh secret set DISCORD_WEBHOOK_URL --repo DomineYH/korea-market-dashboard --body 'https://discord.com/api/webhooks/...'
     ```

5. **Enhanced dashboard**
   - Canvas price chart for KOSPI/KOSDAQ.
   - Separate KOSPI and KOSDAQ model cards.
   - Sector signal table.
   - Backtest summary table.

## Data Sources

- Naver Finance: indices, investor flows, sector movement
- Yahoo Finance Chart API: global indices, FX, commodities, Korean equities, historical prices
- FRED: FX, U.S. rates, VIX, credit spread
- BOK ECOS sample API: Korean base rate
- Google News RSS: Korean market, semiconductor, FX, exports, rate headlines

## Local Usage

### Generate from live public data

```bash
PYTHONPATH=src uv run python scripts/generate.py
```

### Generate from a saved snapshot

```bash
PYTHONPATH=src uv run python scripts/generate.py --input /path/to/snapshot.json
```

### Full auto-update path locally

```bash
PYTHONPATH=src uv run python scripts/update.py --no-alert
```

## Tests

```bash
PYTHONPATH=src uv run python -m unittest discover -s tests -p 'test_*.py' -v
```

## Outputs

- `docs/index.html` — GitHub Pages dashboard
- `reports/latest.md` — Markdown market report
- `reports/backtest.md` — Backtest report
- `data/latest.json` — Snapshot + prediction payload
- `data/backtest.json` — Backtest metrics

## Disclaimer

This repository is for research and monitoring only. It is not financial advice. The model is heuristic and should be validated with deeper backtesting before capital allocation.
