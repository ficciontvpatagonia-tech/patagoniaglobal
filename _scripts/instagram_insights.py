#!/usr/bin/env python3
"""
instagram_insights.py — Reporte de métricas propias de Instagram (@global.patagonia)
Corre en GitHub Actions (necesita FACEBOOK_PAGE_TOKEN + INSTAGRAM_BUSINESS_ACCOUNT_ID
como secrets; el token no vive local). Uso a demanda vía workflow_dispatch, igual que
analytics_oauth.py para GA4.

Uso: python3 _scripts/instagram_insights.py [--days N]
"""
import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone

API = "https://graph.facebook.com/v21.0"

ap = argparse.ArgumentParser()
ap.add_argument("--days", type=int, default=30)
args = ap.parse_args()

TOKEN = os.environ.get("FACEBOOK_PAGE_TOKEN", "")
IG_ID = os.environ.get("INSTAGRAM_BUSINESS_ACCOUNT_ID", "")
if not TOKEN or not IG_ID:
    print("ERROR: faltan FACEBOOK_PAGE_TOKEN o INSTAGRAM_BUSINESS_ACCOUNT_ID en el entorno.")
    sys.exit(1)

end = datetime.now(timezone.utc)
start = end - timedelta(days=args.days)
since_ts = int(start.timestamp())
until_ts = int(end.timestamp())


def get(url):
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try:
            return {"HTTPError": e.code, "body": json.loads(e.read().decode())}
        except Exception:
            return {"HTTPError": e.code, "body": e.read().decode("utf-8", errors="replace")}


print("=" * 70)
print(f"INSTAGRAM @global.patagonia — reporte {start.date()} a {end.date()}")
print("=" * 70)

print("\n## PERFIL (totales actuales, sin histórico)")
r = get(f"{API}/{IG_ID}?fields=username,name,followers_count,follows_count,media_count&access_token={TOKEN}")
print(json.dumps(r, ensure_ascii=False, indent=2))

print("\n## SERIE DIARIA — reach + follower_count")
r2 = get(f"{API}/{IG_ID}/insights?metric=reach,follower_count&period=day&metric_type=time_series"
          f"&since={since_ts}&until={until_ts}&access_token={TOKEN}")
print(json.dumps(r2, ensure_ascii=False, indent=2))

print("\n## SERIE DIARIA — engagement (accounts_engaged, total_interactions, views, likes, comments, shares, saves)")
r3 = get(f"{API}/{IG_ID}/insights?metric=accounts_engaged,total_interactions,views,likes,comments,shares,saves"
          f"&period=day&metric_type=time_series&since={since_ts}&until={until_ts}&access_token={TOKEN}")
print(json.dumps(r3, ensure_ascii=False, indent=2))

# --- Resumen antes/después del 12/09/2026 (reactivación de la cuenta) ---
CORTE = datetime(2026, 9, 12, tzinfo=timezone.utc).date()


def resumen_serie(resp):
    out = {}
    for m in resp.get("data", []):
        name = m.get("name")
        vals = m.get("values", [])
        antes, despues = 0, 0
        for v in vals:
            d = v.get("end_time", "")[:10]
            try:
                fecha = datetime.strptime(d, "%Y-%m-%d").date()
            except ValueError:
                continue
            val = v.get("value", 0) or 0
            if fecha < CORTE:
                antes += val
            else:
                despues += val
        out[name] = (antes, despues)
    return out


print("\n" + "=" * 70)
print(f"RESUMEN ANTES/DESPUÉS DEL {CORTE} (reactivación de @global.patagonia)")
print("=" * 70)
for resp, label in [(r2, "reach/follower_count"), (r3, "engagement")]:
    if "data" in resp:
        for name, (antes, despues) in resumen_serie(resp).items():
            print(f"  {name:<22} antes: {antes:<8} después: {despues}")
    else:
        print(f"  ({label}: sin datos o error, ver bloque JSON arriba)")

print("\n" + "=" * 70)
