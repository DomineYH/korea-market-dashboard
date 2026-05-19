from __future__ import annotations

import html
import json
from datetime import datetime, timezone
from typing import Any


def _safe(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def _fmt(value: Any, suffix: str = "") -> str:
    if isinstance(value, (int, float)):
        return f"{value:,.2f}{suffix}" if abs(value) % 1 else f"{value:,.0f}{suffix}"
    return _safe(value)


def _top_news(snapshot: dict[str, Any], limit: int = 8) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for group in snapshot.get("news", []) or []:
        for item in group.get("items", []) or []:
            if item.get("title"):
                items.append(item)
            if len(items) >= limit:
                return items
    return items


def _market_models(prediction: dict[str, Any]) -> dict[str, Any]:
    return prediction.get("market_models") or {}


def _backtest(prediction: dict[str, Any]) -> dict[str, Any]:
    return prediction.get("backtest") or {}


def _sector_rows(snapshot: dict[str, Any]) -> list[dict[str, Any]]:
    sectors = snapshot.get("sectors") or {}
    rows: list[dict[str, Any]] = []
    for group, direction in [("top", "상승"), ("bottom", "하락")]:
        for row in sectors.get(group, []) or []:
            rows.append({**row, "direction": direction})
    return rows


def render_report_markdown(snapshot: dict[str, Any], prediction: dict[str, Any]) -> str:
    generated = snapshot.get("generated_kst") or datetime.now(timezone.utc).isoformat(timespec="seconds")
    short = prediction.get("short_term", {})
    medium = prediction.get("medium_term", {})
    kospi = snapshot.get("naver_indices", {}).get("KOSPI", {})
    kosdaq = snapshot.get("naver_indices", {}).get("KOSDAQ", {})
    fx = snapshot.get("yahoo_market", {}).get("KRW per USD", {})
    sox = snapshot.get("yahoo_market", {}).get("Philadelphia SOX", {})
    oil = snapshot.get("yahoo_market", {}).get("WTI crude", {})
    vix = snapshot.get("yahoo_market", {}).get("VIX", {})

    lines = [
        "# 한국 주식시장 방향성 리포트",
        "",
        f"- 생성 시각: `{generated}`",
        f"- 단기 판정: **{short.get('label', 'N/A')}** / 신뢰도: {short.get('confidence', 'N/A')}",
        f"- 중기 판정: **{medium.get('label', 'N/A')}** / 신뢰도: {medium.get('confidence', 'N/A')}",
        f"- 총점: **{prediction.get('total_score', 'N/A')}** = 상승 {prediction.get('positive_score', 'N/A')} + 하락 {prediction.get('negative_score', 'N/A')}",
        "",
        "## 핵심 시장 지표",
        "",
        "| 항목 | 값 | 비고 |",
        "|---|---:|---|",
        f"| KOSPI | {kospi.get('now_value', 'N/A')} | {kospi.get('timestamp_text', '')} |",
        f"| KOSDAQ | {kosdaq.get('now_value', 'N/A')} | {kosdaq.get('timestamp_text', '')} |",
        f"| USD/KRW | {_fmt(fx.get('latest'))} | 1M {_fmt(fx.get('1m_change_pct'), '%')} |",
        f"| SOX | 1W {_fmt(sox.get('1w_change_pct'), '%')} | 1M {_fmt(sox.get('1m_change_pct'), '%')} |",
        f"| VIX | {_fmt(vix.get('latest'))} | 위험선호/공포 지표 |",
        f"| WTI | {_fmt(oil.get('latest'))} | 1M {_fmt(oil.get('1m_change_pct'), '%')} |",
        "",
        "## KOSPI/KOSDAQ 분리 모델",
        "",
        "| 시장 | 단기 판정 | 중기 판정 | 총점 | 상승점수 | 하락점수 |",
        "|---|---|---|---:|---:|---:|",
    ]
    for market, model in _market_models(prediction).items():
        lines.append(
            f"| {market} | {model.get('short_term', {}).get('label', 'N/A')} | {model.get('medium_term', {}).get('label', 'N/A')} | "
            f"{model.get('total_score', 'N/A')} | {model.get('positive_score', 'N/A')} | {model.get('negative_score', 'N/A')} |"
        )
    lines.extend([
        "",
        "## 예측 모델표",
        "",
        "| 분류 | 신호 | 관측값 | 방향 | 점수 | 가중 | 해석 |",
        "|---|---|---|---|---:|---|---|",
    ])
    for row in prediction.get("signals", []) or []:
        lines.append(
            f"| {row.get('category','')} | {row.get('factor','')} | {row.get('observed','')} | "
            f"{row.get('direction','')} | {row.get('score','')} | {row.get('weight','')} | {row.get('rationale','')} |"
        )

    backtest = _backtest(prediction)
    if backtest.get("markets"):
        lines.extend([
            "",
            "## 백테스트 요약",
            "",
            "| 시장 | 표본 | 승률 | 평균 선행수익률 | 제안 가중치 | 우수 신호 |",
            "|---|---:|---:|---:|---:|---|",
        ])
        for market, row in backtest.get("markets", {}).items():
            lines.append(
                f"| {market} | {row.get('samples', 0)} | {float(row.get('hit_rate', 0)):.2%} | "
                f"{float(row.get('avg_forward_return', 0)):.2f}% | {float(row.get('suggested_weight', 0)):.2f} | {row.get('best_signal_label', '')} |"
            )

    lines.extend([
        "",
        "## 결론",
        "",
        "- **단기(1~5거래일)**: 외국인 매도, 원화 약세, SOX 단기 조정, 유가/금리 부담 때문에 조정 우위입니다.",
        "- **중기(1~3개월)**: 반도체/HBM 및 수출 사이클이 살아 있어 조건부 상승 여지는 유지됩니다.",
        "- 확인할 트리거: 외국인 KOSPI 순매수 전환, USD/KRW 1,500원 하향 안정, SOX 반등, 삼성전자/SK하이닉스 재상승.",
        "",
        "## 주요 뉴스 헤드라인",
        "",
    ])
    for item in _top_news(snapshot):
        title = item.get("title", "")
        link = item.get("link", "")
        source = item.get("source", "")
        lines.append(f"- [{title}]({link}) — {source}")
    lines.extend([
        "",
        "## 방법론",
        "",
        "각 신호를 -2.0~+2.0 범위로 점수화했습니다. 점수는 예측 모델의 투명성을 위한 휴리스틱이며, 백테스트 결과로 가중치를 보정할 수 있습니다.",
    ])
    return "\n".join(lines) + "\n"


def render_dashboard_html(snapshot: dict[str, Any], prediction: dict[str, Any]) -> str:
    payload = json.dumps({"snapshot": snapshot, "prediction": prediction}, ensure_ascii=False)
    title = "한국 주식시장 방향성 대시보드"
    signal_rows = "\n".join(
        f"<tr data-signal='{_safe(row.get('id'))}'><td>{_safe(row.get('category'))}</td><td>{_safe(row.get('factor'))}</td>"
        f"<td>{_safe(row.get('observed'))}</td><td class='dir'>{_safe(row.get('direction'))}</td>"
        f"<td class='score'>{_safe(row.get('score'))}</td><td>{_safe(row.get('weight'))}</td><td>{_safe(row.get('rationale'))}</td></tr>"
        for row in prediction.get("signals", []) or []
    )
    market_cards = "\n".join(
        f"<div class='mini-card'><div class='muted'>{_safe(market)} 모델</div><div class='metric small'>{_safe(model.get('short_term', {}).get('label'))}</div><p>총점 {_safe(model.get('total_score'))} · 중기 {_safe(model.get('medium_term', {}).get('label'))}</p></div>"
        for market, model in _market_models(prediction).items()
    )
    sector_rows = "\n".join(
        f"<tr><td>{_safe(row.get('direction'))}</td><td>{_safe(row.get('sector'))}</td><td class='score'>{_safe(row.get('change_pct'))}%</td><td>{_safe(row.get('up'))}</td><td>{_safe(row.get('down'))}</td></tr>"
        for row in _sector_rows(snapshot)
    )
    backtest_rows = "\n".join(
        f"<tr><td>{_safe(market)}</td><td>{_safe(row.get('samples'))}</td><td>{float(row.get('hit_rate', 0)):.2%}</td><td>{float(row.get('suggested_weight', 0)):.2f}</td><td>{_safe(row.get('best_signal_label'))}</td></tr>"
        for market, row in (_backtest(prediction).get("markets") or {}).items()
    )
    news_items = "\n".join(
        f"<li><a href='{_safe(item.get('link'))}' target='_blank' rel='noreferrer'>{_safe(item.get('title'))}</a><span>{_safe(item.get('source'))}</span></li>"
        for item in _top_news(snapshot, 10)
    )
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="KOSPI/KOSDAQ direction dashboard generated from public market data." />
  <style>
    :root {{ color-scheme: dark; --bg:#070b14; --card:#101827; --muted:#8ea0b8; --text:#e9f0fb; --blue:#68a7ff; --green:#47d18c; --red:#ff6b7a; --yellow:#ffd166; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: radial-gradient(circle at top left, #1f3558 0, #070b14 42%); color:var(--text); }}
    a {{ color:var(--blue); }}
    header {{ padding:42px min(6vw,72px) 24px; }}
    .eyebrow {{ color:var(--blue); letter-spacing:.14em; text-transform:uppercase; font-size:12px; font-weight:700; }}
    h1 {{ margin:.3rem 0; font-size:clamp(30px, 5vw, 56px); line-height:1.02; }}
    .subtitle {{ color:var(--muted); max-width:980px; font-size:17px; }}
    main {{ padding:0 min(6vw,72px) 56px; }}
    .grid {{ display:grid; gap:18px; grid-template-columns:repeat(12,1fr); }}
    .card {{ grid-column:span 4; background:rgba(16,24,39,.88); border:1px solid rgba(255,255,255,.08); border-radius:22px; padding:22px; box-shadow:0 18px 48px rgba(0,0,0,.25); }}
    .wide {{ grid-column:span 12; }} .half {{ grid-column:span 6; }}
    .metric {{ font-size:34px; font-weight:800; margin:.2rem 0; }} .metric.small {{ font-size:22px; }}
    .muted {{ color:var(--muted); }}
    .verdict.bearish {{ color:var(--red); }} .verdict.bullish {{ color:var(--green); }} .verdict.conditional_bullish,.verdict.mild_bullish,.verdict.mild_bearish {{ color:var(--yellow); }}
    table {{ width:100%; border-collapse:collapse; font-size:14px; }}
    th,td {{ padding:12px 10px; border-bottom:1px solid rgba(255,255,255,.08); vertical-align:top; }}
    th {{ color:#b9c7da; text-align:left; font-size:12px; text-transform:uppercase; letter-spacing:.08em; }}
    td.score {{ font-weight:800; }}
    .scorebar {{ height:18px; background:#1e293b; border-radius:999px; overflow:hidden; display:flex; }}
    .pos {{ background:linear-gradient(90deg,#1d8f5a,var(--green)); }} .neg {{ background:linear-gradient(90deg,var(--red),#9f1239); }}
    .news li {{ margin:12px 0; }} .news span {{ display:block; color:var(--muted); font-size:12px; margin-top:2px; }}
    .pill {{ display:inline-flex; padding:6px 10px; border-radius:999px; border:1px solid rgba(255,255,255,.14); color:#c8d6ea; margin:4px 6px 4px 0; font-size:12px; }}
    .mini-grid {{ display:grid; gap:12px; grid-template-columns:repeat(2,minmax(0,1fr)); }} .mini-card {{ border:1px solid rgba(255,255,255,.1); border-radius:16px; padding:16px; background:rgba(255,255,255,.03); }}
    canvas {{ width:100%; height:260px; background:#0b1220; border-radius:16px; border:1px solid rgba(255,255,255,.08); }}
    footer {{ color:var(--muted); padding:24px min(6vw,72px) 50px; border-top:1px solid rgba(255,255,255,.08); }}
    @media (max-width:900px) {{ .card,.half {{ grid-column:span 12; }} .mini-grid {{ grid-template-columns:1fr; }} table {{ font-size:12px; }} th,td {{ padding:9px 6px; }} }}
  </style>
</head>
<body>
<header>
  <div class="eyebrow">Public data · heuristic model · GitHub Pages · Auto update</div>
  <h1>{title}</h1>
  <p class="subtitle">외국인 수급, 환율, 반도체 사이클, 글로벌 금리/리스크, 업종 흐름을 투명한 점수표로 합산해 KOSPI/KOSDAQ의 단기·중기 방향성을 추정합니다.</p>
</header>
<main class="grid">
  <section class="card">
    <div class="muted">단기 전망</div>
    <div id="shortLabel" class="metric verdict">{_safe(prediction.get('short_term',{}).get('label'))}</div>
    <div class="muted">1~5거래일 · 신뢰도 {_safe(prediction.get('short_term',{}).get('confidence'))}</div>
  </section>
  <section class="card">
    <div class="muted">중기 전망</div>
    <div class="metric verdict conditional_bullish">{_safe(prediction.get('medium_term',{}).get('label'))}</div>
    <div class="muted">1~3개월 · 반도체/수출 사이클 조건부</div>
  </section>
  <section class="card">
    <div class="muted">모델 총점</div>
    <div class="metric">{_safe(prediction.get('total_score'))}</div>
    <div class="scorebar"><div class="neg" id="negbar"></div><div class="pos" id="posbar"></div></div>
  </section>
  <section class="card half">
    <h2>핵심 지표</h2>
    <p><span class="pill">KOSPI {_safe(snapshot.get('naver_indices',{}).get('KOSPI',{}).get('now_value'))}</span><span class="pill">KOSDAQ {_safe(snapshot.get('naver_indices',{}).get('KOSDAQ',{}).get('now_value'))}</span><span class="pill">USD/KRW {_safe(snapshot.get('yahoo_market',{}).get('KRW per USD',{}).get('latest'))}</span><span class="pill">VIX {_safe(snapshot.get('yahoo_market',{}).get('VIX',{}).get('latest'))}</span></p>
    <p class="muted">생성 시각: {_safe(snapshot.get('generated_kst'))}</p>
  </section>
  <section class="card half">
    <h2>KOSPI/KOSDAQ 분리 모델</h2>
    <div class="mini-grid">{market_cards}</div>
  </section>
  <section class="card wide">
    <h2>가격 차트</h2>
    <canvas id="marketChart" width="1200" height="320" aria-label="KOSPI and KOSDAQ line chart"></canvas>
  </section>
  <section class="card wide">
    <h2>예측 모델표</h2>
    <table><thead><tr><th>분류</th><th>신호</th><th>관측값</th><th>방향</th><th>점수</th><th>가중</th><th>해석</th></tr></thead><tbody>{signal_rows}</tbody></table>
  </section>
  <section class="card half">
    <h2>섹터 신호표</h2>
    <table><thead><tr><th>방향</th><th>섹터</th><th>등락</th><th>상승</th><th>하락</th></tr></thead><tbody>{sector_rows}</tbody></table>
  </section>
  <section class="card half">
    <h2>백테스트</h2>
    <table><thead><tr><th>시장</th><th>표본</th><th>승률</th><th>제안가중</th><th>우수신호</th></tr></thead><tbody>{backtest_rows}</tbody></table>
  </section>
  <section class="card wide">
    <h2>주요 뉴스</h2>
    <ul class="news">{news_items}</ul>
  </section>
</main>
<footer>Not financial advice. Data sources include Naver Finance, Yahoo Finance, FRED, BOK ECOS, MOTIR, and Google News RSS. The model is heuristic and should be backtested before capital allocation.</footer>
<script>
window.MARKET_DATA = {payload};
(function() {{
  const p = window.MARKET_DATA.prediction;
  const pos = Math.abs(Number(p.positive_score || 0));
  const neg = Math.abs(Number(p.negative_score || 0));
  const total = pos + neg || 1;
  document.getElementById('posbar').style.width = (pos / total * 100).toFixed(1) + '%';
  document.getElementById('negbar').style.width = (neg / total * 100).toFixed(1) + '%';
  const short = document.getElementById('shortLabel');
  const bias = p.short_term && p.short_term.bias;
  if (bias) short.classList.add(bias);
  document.querySelectorAll('td.score').forEach(td => {{
    const n = Number(String(td.textContent).replace('%',''));
    td.style.color = n > 0 ? 'var(--green)' : n < 0 ? 'var(--red)' : 'var(--muted)';
  }});
  const canvas = document.getElementById('marketChart');
  const ctx = canvas.getContext('2d');
  const series = [
    ['KOSPI', (window.MARKET_DATA.snapshot.yahoo_market.KOSPI || {{}}).history || [], '#68a7ff'],
    ['KOSDAQ', (window.MARKET_DATA.snapshot.yahoo_market.KOSDAQ || {{}}).history || [], '#47d18c']
  ];
  const points = series.flatMap(s => s[1].slice(-90).map(p => Number(p.close))).filter(Number.isFinite);
  const min = Math.min(...points), max = Math.max(...points);
  ctx.clearRect(0,0,canvas.width,canvas.height);
  ctx.strokeStyle = 'rgba(255,255,255,.15)'; ctx.lineWidth = 1;
  for (let i=0;i<5;i++) {{ const y = 30 + i*(canvas.height-60)/4; ctx.beginPath(); ctx.moveTo(40,y); ctx.lineTo(canvas.width-20,y); ctx.stroke(); }}
  series.forEach(([name, raw, color], idx) => {{
    const data = raw.slice(-90);
    if (data.length < 2 || !Number.isFinite(min) || !Number.isFinite(max) || max === min) return;
    ctx.strokeStyle = color; ctx.lineWidth = 3; ctx.beginPath();
    data.forEach((row, i) => {{
      const x = 40 + i * (canvas.width-70) / (data.length-1);
      const y = canvas.height - 30 - ((Number(row.close)-min)/(max-min)) * (canvas.height-60);
      if (i === 0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
    }});
    ctx.stroke(); ctx.fillStyle = color; ctx.fillText(name, 48, 28 + idx*18);
  }});
}})();
</script>
</body>
</html>
"""
