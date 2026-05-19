from __future__ import annotations

import csv
import datetime as dt
import html
import io
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Any, Callable

UA = {"User-Agent": "Mozilla/5.0 (compatible; korea-market-dashboard/1.0)"}


def fetch_url(url: str, timeout: int = 20) -> bytes:
    request = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(request, timeout=timeout).read()


def _clean(text: str | None) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def _num(value: Any, default: float | None = None) -> float | None:
    if value is None:
        return default
    try:
        return float(str(value).replace(",", "").replace("%", "").strip())
    except (TypeError, ValueError):
        return default


def _pct(first: float, last: float) -> float:
    return round((last / first - 1.0) * 100.0, 2) if first else 0.0


def parse_yahoo_chart(payload: dict[str, Any]) -> dict[str, Any]:
    result = payload["chart"]["result"][0]
    meta = result.get("meta", {})
    timestamps = result.get("timestamp") or []
    closes = (result.get("indicators", {}).get("quote") or [{}])[0].get("close") or []
    history: list[dict[str, Any]] = []
    for timestamp, close in zip(timestamps, closes):
        if close is None:
            continue
        history.append({"date": dt.datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d"), "close": round(float(close), 4)})
    out: dict[str, Any] = {
        "currency": meta.get("currency"),
        "exchange": meta.get("exchangeName"),
        "regularMarketPrice": meta.get("regularMarketPrice"),
        "history": history,
    }
    if history:
        out["latest_date"] = history[-1]["date"]
        out["latest"] = history[-1]["close"]
        for days, label in [(1, "1d"), (5, "1w"), (21, "1m"), (63, "3m"), (126, "6m"), (252, "1y")]:
            if len(history) > days:
                out[f"{label}_change_pct"] = _pct(history[-days - 1]["close"], history[-1]["close"])
            elif label == "1w" and len(history) >= 2:
                out[f"{label}_change_pct"] = _pct(history[0]["close"], history[-1]["close"])
    return out


def yahoo_chart(symbol: str, fetcher: Callable[[str], bytes] = fetch_url, range_: str = "1y") -> dict[str, Any]:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol, safe='')}?range={range_}&interval=1d"
    try:
        parsed = parse_yahoo_chart(json.loads(fetcher(url).decode("utf-8")))
        parsed["symbol"] = symbol
        parsed["source"] = url
        return parsed
    except Exception as exc:  # network sources are best-effort
        return {"symbol": symbol, "source": url, "error": repr(exc), "history": []}


def parse_google_news_rss(xml_bytes: bytes, limit: int = 8) -> list[dict[str, str | None]]:
    root = ET.fromstring(xml_bytes)
    items: list[dict[str, str | None]] = []
    for item in root.findall(".//item")[:limit]:
        source = item.find("source")
        items.append({
            "title": _clean(item.findtext("title")),
            "source": source.text if source is not None else None,
            "pubDate": item.findtext("pubDate"),
            "link": item.findtext("link"),
        })
    return items


def google_news(query: str, fetcher: Callable[[str], bytes] = fetch_url, limit: int = 8) -> dict[str, Any]:
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode({"q": query, "hl": "ko", "gl": "KR", "ceid": "KR:ko"})
    try:
        return {"query": query, "source": url, "items": parse_google_news_rss(fetcher(url), limit=limit)}
    except Exception as exc:
        return {"query": query, "source": url, "error": repr(exc), "items": []}


def naver_index(code: str, fetcher: Callable[[str], bytes] = fetch_url) -> dict[str, Any]:
    url = f"https://finance.naver.com/sise/sise_index.naver?code={code}"
    try:
        text = fetcher(url).decode("euc-kr", "ignore")
    except Exception as exc:
        return {"source": url, "error": repr(exc)}
    out: dict[str, Any] = {"source": url}
    for element_id in ["now_value", "change_value_and_rate", "quant", "amount", "high_value", "low_value"]:
        match = re.search(r"id\s*=\s*['\"]%s['\"][^>]*>(.*?)</" % re.escape(element_id), text, re.S)
        if match:
            out[element_id] = _clean(match.group(1))
    qmatch = re.search(r"<div class=\"quotient ([^\"]+)\"", text)
    if qmatch:
        out["direction_class"] = qmatch.group(1)
    dmatch = re.search(r"<span class=\"date\">(.*?)</span>", text, re.S)
    if dmatch:
        out["timestamp_text"] = _clean(dmatch.group(1))
    pmatch = re.search(r"([+-]\d+(?:\.\d+)?)%", out.get("change_value_and_rate", ""))
    if pmatch:
        out["change_pct"] = pmatch.group(1) + "%"
    return out


def investor_flows(sosok: str, fetcher: Callable[[str], bytes] = fetch_url) -> dict[str, Any]:
    today = (dt.datetime.utcnow() + dt.timedelta(hours=9)).date()
    for delta in range(8):
        bizdate = (today - dt.timedelta(days=delta)).strftime("%Y%m%d")
        url = f"https://finance.naver.com/sise/investorDealTrendDay.naver?bizdate={bizdate}&sosok={sosok}"
        try:
            text = fetcher(url).decode("euc-kr", "ignore")
        except Exception:
            continue
        rows: list[dict[str, Any]] = []
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", text, re.S):
            cells = [_clean(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
            if len(cells) >= 11 and re.match(r"\d{2}\.\d{2}\.\d{2}", cells[0]):
                keys = ["date", "individual", "foreign", "institution_total", "financial_investment", "insurance", "investment_trust_private", "bank", "other_financial", "pension", "other_corporations"]
                rows.append({k: (_num(v, 0.0) if k != "date" else v) for k, v in zip(keys, cells)})
        if rows:
            sums: dict[str, dict[str, float]] = {}
            for n in [5, 10]:
                sub = rows[:n]
                sums[f"{n}d"] = {k: float(sum((row.get(k) or 0.0) for row in sub)) for k in ["individual", "foreign", "institution_total", "financial_investment", "pension", "other_corporations"]}
            return {"source": url, "rows": rows, "sums_억원": sums}
    return {"source": None, "rows": [], "sums_억원": {}}


def sectors(fetcher: Callable[[str], bytes] = fetch_url) -> dict[str, Any]:
    url = "https://finance.naver.com/sise/sise_group.naver?type=upjong"
    try:
        text = fetcher(url).decode("euc-kr", "ignore")
    except Exception as exc:
        return {"source": url, "error": repr(exc), "top": [], "bottom": [], "count": 0}
    rows: list[dict[str, Any]] = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", text, re.S):
        cells = [_clean(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if len(cells) >= 7 and cells[0] and re.match(r"[+-]?\d+(?:\.\d+)?%", cells[1]):
            rows.append({"sector": cells[0], "change_pct": _num(cells[1], 0.0), "stocks": _num(cells[2], 0.0), "up": _num(cells[3], 0.0), "flat": _num(cells[4], 0.0), "down": _num(cells[5], 0.0), "lead_pct": _num(cells[6], 0.0)})
    return {"source": url, "top": rows[:10], "bottom": rows[-10:], "count": len(rows)}


def fred_latest(series_id: str, fetcher: Callable[[str], bytes] = fetch_url) -> dict[str, Any]:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    try:
        text = fetcher(url).decode("utf-8")
        rows = [r for r in csv.DictReader(io.StringIO(text)) if r.get(series_id) not in (".", "", None)]
        latest = rows[-1]
        return {"series": series_id, "source": url, "latest_date": latest["observation_date"], "latest": _num(latest[series_id], 0.0)}
    except Exception as exc:
        return {"series": series_id, "source": url, "error": repr(exc)}


def bok_base_rate(fetcher: Callable[[str], bytes] = fetch_url) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for start, end in [(1, 10), (11, 20)]:
        url = f"https://ecos.bok.or.kr/api/StatisticSearch/sample/json/kr/{start}/{end}/722Y001/M/202501/202605/0101000"
        try:
            data = json.loads(fetcher(url).decode("utf-8"))
            rows.extend(data.get("StatisticSearch", {}).get("row", []))
        except Exception:
            continue
    if rows:
        last = rows[-1]
        return {"source": "BOK ECOS sample 722Y001/0101000", "stat": last.get("STAT_NAME"), "item": last.get("ITEM_NAME1"), "unit": last.get("UNIT_NAME"), "latest_time": last.get("TIME"), "latest": _num(last.get("DATA_VALUE"), 0.0), "recent": [(r.get("TIME"), _num(r.get("DATA_VALUE"), 0.0)) for r in rows[-8:]]}
    return {"source": "BOK ECOS sample 722Y001/0101000", "latest": 2.5, "latest_time": "fallback", "note": "Fallback used when BOK sample API is unavailable or rate-limited."}


def collect_snapshot(fetcher: Callable[[str], bytes] = fetch_url) -> dict[str, Any]:
    now_utc = dt.datetime.utcnow().replace(microsecond=0)
    now_kst = now_utc + dt.timedelta(hours=9)
    symbols = {
        "KOSPI": "^KS11",
        "KOSDAQ": "^KQ11",
        "KOSPI200": "^KS200",
        "Samsung Electronics": "005930.KS",
        "SK Hynix": "000660.KS",
        "Hyundai Motor": "005380.KS",
        "NAVER": "035420.KS",
        "KRW per USD": "KRW=X",
        "US Dollar Index": "DX-Y.NYB",
        "S&P500": "^GSPC",
        "Nasdaq": "^IXIC",
        "Philadelphia SOX": "^SOX",
        "VIX": "^VIX",
        "US 10Y yield": "^TNX",
        "WTI crude": "CL=F",
        "Gold": "GC=F",
        "iShares MSCI Korea ETF": "EWY",
    }
    return {
        "generated_utc": now_utc.isoformat() + "Z",
        "generated_kst": now_kst.isoformat() + "+09:00",
        "naver_indices": {"KOSPI": naver_index("KOSPI", fetcher), "KOSDAQ": naver_index("KOSDAQ", fetcher)},
        "investor_flows_억원": {"KOSPI": investor_flows("01", fetcher), "KOSDAQ": investor_flows("02", fetcher)},
        "sectors": sectors(fetcher),
        "yahoo_market": {name: yahoo_chart(symbol, fetcher) for name, symbol in symbols.items()},
        "fred_macro": {sid: fred_latest(sid, fetcher) for sid in ["DEXKOUS", "DGS10", "DGS2", "T10Y2Y", "VIXCLS", "BAMLH0A0HYM2"]},
        "bok_base_rate": bok_base_rate(fetcher),
        "news": [
            google_news("한국 증시 코스피 전망 외국인 환율 반도체", fetcher),
            google_news("Korea stock market outlook Kospi foreign investors won semiconductor exports", fetcher),
            google_news("한국 수출 반도체 산업통상자원부", fetcher),
            google_news("한국은행 기준금리 전망 증시 환율", fetcher),
            google_news("삼성전자 SK하이닉스 HBM 반도체 주가 전망", fetcher),
        ],
    }
