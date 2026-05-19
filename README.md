# Korea Market Direction Dashboard

한국 주식시장(KOSPI/KOSDAQ)의 단기·중기 방향성을 공개 데이터 기반 휴리스틱 모델로 점수화한 정적 리포트/대시보드입니다.

## Links

- Dashboard: https://domineyh.github.io/korea-market-dashboard/
- Latest report: [`reports/latest.md`](reports/latest.md)
- 09:00 prediction report: [`reports/morning-prediction.md`](reports/morning-prediction.md)
- 16:00 close analysis report: [`reports/close-analysis.md`](reports/close-analysis.md)
- Backtest report: [`reports/backtest.md`](reports/backtest.md)
- Machine-readable payload: [`data/latest.json`](data/latest.json)

## Daily Schedule

| KST | UTC cron | Phase | Output |
|---:|---|---|---|
| 09:00 | `0 0 * * 1-5` | Morning prediction | `reports/morning-prediction.md`, `data/morning.json`, latest dashboard |
| 16:00 | `0 7 * * 1-5` | Same-day close analysis + correction | `reports/close-analysis.md`, `data/close-analysis.json`, latest dashboard |

The 16:00 run loads the saved 09:00 prediction, compares it with the same-day KOSPI/KOSDAQ movement, records hit/miss, and applies the close data by recalculating `latest` report/dashboard artifacts.

## Current Features

1. **Twice-daily auto-update**
   - GitHub Actions workflow: [`.github/workflows/auto-update.yml`](.github/workflows/auto-update.yml)
   - 09:00 KST: public data collection + opening prediction.
   - 16:00 KST: same-day close analysis, prediction-vs-actual review, and latest dashboard correction.
   - Workflow dispatch supports `phase=auto|morning|close`.

2. **Prediction model table**
   - Signals are scored from `-2.0` to `+2.0`.
   - Inputs include foreign/retail/institution flows, USD/KRW, SOX, U.S. rates, VIX, WTI, sectors, BOK base rate, and news headlines.
   - Produces aggregate short-term and medium-term verdicts.

3. **Intraday review**
   - `src/korea_market_dashboard/intraday.py` compares the 09:00 prediction with the 16:00 market state.
   - It records KOSPI/KOSDAQ intraday changes, primary hit/miss, and the correction action.

4. **Close-analysis feedback loop**
   - `src/korea_market_dashboard/feedback.py` persists the 16:00 prediction-vs-actual result to `data/feedback.json`.
   - The next 09:00/manual run loads that state, adds a dynamic feedback signal, and slightly adjusts the short-term score.
   - Stale, missing, or duplicate same-day close analyses are skipped so the persistent sample count is not polluted by retries.
   - Reports and dashboard cards show whether feedback was applied, the adjustment size, sample count, hit rate, and latest feedback summary.

5. **Backtest**
   - Uses historical Yahoo Finance KOSPI/KOSDAQ price series.
   - Current baseline is a transparent 20-session momentum rule with 5-session forward horizon.
   - Outputs hit rate, average forward return, and suggested model weight.

6. **Alerts**
   - `scripts/update.py` compares the previous and current short-term verdict.
   - If the verdict bias changes and `DISCORD_WEBHOOK_URL` exists as a GitHub Actions secret, it posts a Discord webhook alert.
   - Configure secret:
     ```bash
     gh secret set DISCORD_WEBHOOK_URL --repo DomineYH/korea-market-dashboard --body 'https://discord.com/api/webhooks/...'
     ```

7. **Enhanced dashboard**
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

### Generate a 09:00 prediction phase artifact

```bash
PYTHONPATH=src uv run python scripts/update.py --phase morning --no-alert
```

### Generate a 16:00 close analysis phase artifact

```bash
PYTHONPATH=src uv run python scripts/update.py --phase close --no-alert
```

### Generate from a saved snapshot

```bash
PYTHONPATH=src uv run python scripts/generate.py --input /path/to/snapshot.json --phase manual
```

## Tests

```bash
PYTHONPATH=src uv run python -m unittest discover -s tests -p 'test_*.py' -v
```

## Outputs

- `docs/index.html` — GitHub Pages dashboard
- `reports/latest.md` — latest Markdown market report
- `reports/morning-prediction.md` — 09:00 prediction report
- `reports/close-analysis.md` — 16:00 same-day analysis and correction report
- `reports/backtest.md` — backtest report
- `data/latest.json` — snapshot + prediction payload
- `data/morning.json` — saved 09:00 prediction payload
- `data/close-analysis.json` — same-day prediction-vs-actual analysis
- `data/feedback.json` — persistent close-analysis feedback used by the next prediction run
- `data/backtest.json` — backtest metrics

## Disclaimer

This repository is for research and monitoring only. It is not financial advice. The model is heuristic and should be validated with deeper backtesting before capital allocation.
