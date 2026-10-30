#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mapa propio del Circuito Austral (El Calafate – Torres del Paine – Puerto Natales – Punta Arenas – Ushuaia).
Datos © colaboradores de OpenStreetMap (ODbL): costa, frontera y rutas vía Overpass. Requiere shapely + matplotlib.
Uso: python mapa_circuito_austral.py <carpeta_datos> <salida.png>   (carpeta con coast_simpl.json, border.json, roads.json, lakes.json)"""
import json, math, sys, heapq
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import matplotlib.patheffects as pe
from shapely.geometry import LineString, Polygon, MultiPolygon, Point, box
from shapely.ops import unary_union, polygonize
from shapely import STRtree

DATA, OUT = sys.argv[1], sys.argv[2]
X0, X1, Y0, Y1 = -74.2, -66.7, -55.15, -49.95
LAT = -52.5; K = 1 / math.cos(math.radians(abs(LAT)))
CREMA="#f0ede8"; TIERRA="#e7e1d3"; AGUA="#a9cde3"; AGUA_E="#86b4d0"; AZUL="#1c2d3d"; RUTA="#c0562b"; BORDE="#6a5a8a"; ARCILLA="#8c6b4a"

# ---------- tierra / mar desde la línea de costa (tierra a la izquierda) ----------
coast = [LineString(w) for w in json.load(open(f"{DATA}/coast_simpl.json")) if len(w) > 1]
BB = box(-75.5, -55.4, -66.5, -49.8)
lines = unary_union(coast + [BB.exterior])
faces = list(polygonize(lines))
tree = STRtree(coast)
def es_tierra(poly):
    p = poly.representative_point()
    i = tree.nearest(p)
    ln = coast[i]; d = ln.project(p)
    a = ln.interpolate(max(d - 1e-4, 0)); b = ln.interpolate(min(d + 1e-4, ln.length))
    cross = (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)
    return cross > 0
land = [f for f in faces if es_tierra(f)]
print("caras", len(faces), "tierra", len(land))

def patch(geoms, fc, ec, lw=0.4, z=2):
    verts, codes = [], []
    for g in geoms:
        for poly in (g.geoms if isinstance(g, MultiPolygon) else [g]):
            for ring in [poly.exterior] + list(poly.interiors):
                c = list(ring.coords); verts += c; codes += [Path.MOVETO] + [Path.LINETO]*(len(c)-2) + [Path.CLOSEPOLY]
    return PathPatch(Path(verts, codes), fc=fc, ec=ec, lw=lw, zorder=z)

fig = plt.figure(figsize=(10, 10*((Y1-Y0))/((X1-X0)/K)), dpi=200)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(X0, X1); ax.set_ylim(Y0, Y1); ax.set_aspect(K); ax.axis("off")
fig.patch.set_facecolor(CREMA)
ax.add_patch(plt.Rectangle((X0, Y0), X1-X0, Y1-Y0, fc=AGUA, ec="none", zorder=0))
ax.add_patch(patch(land, TIERRA, AGUA_E, 0.35, 1))

# ---------- lagos ----------
lk = json.load(open(f"{DATA}/lakes.json"))
lag = []
for e in lk["elements"]:
    if e["type"] == "way" and e.get("geometry"):
        g = [(p["lon"], p["lat"]) for p in e["geometry"]]
        if len(g) > 3 and g[0] == g[-1]: lag.append(Polygon(g).buffer(0))
    elif e["type"] == "relation":
        segs = [LineString([(p["lon"], p["lat"]) for p in m["geometry"]]) for m in e.get("members", [])
                if m.get("role") == "outer" and m.get("geometry") and len(m["geometry"]) > 1]
        if segs: lag += list(polygonize(unary_union(segs)))
ax.add_patch(patch(lag, AGUA, AGUA_E, 0.4, 2))
print("lagos", len(lag))

# ---------- frontera ----------
bd = json.load(open(f"{DATA}/border.json"))
bl = []
for e in bd["elements"]:
    g = e.get("geometry", [])
    if e.get("tags", {}).get("maritime") == "yes": continue
    if len(g) > 1: bl.append(LineString([(p["lon"], p["lat"]) for p in g]))
for l in bl:
    ax.plot(*l.xy, color=BORDE, lw=0.9, ls=(0, (6, 3)), zorder=3, alpha=.75)

# ---------- grafo de rutas ----------
rd = json.load(open(f"{DATA}/roads.json"))
def key(p): return (round(p["lon"], 5), round(p["lat"], 5))
adj = {}
def hav(a, b):
    return math.hypot((a[0]-b[0])*math.cos(math.radians(abs(a[1]))), a[1]-b[1])
for e in rd["elements"]:
    g = e.get("geometry", [])
    ks = [key(p) for p in g]
    for a, b in zip(ks, ks[1:]):
        if a == b: continue
        d = hav(a, b); adj.setdefault(a, {})[b] = d; adj.setdefault(b, {})[a] = d
nodes = list(adj)
def snap(lat, lon):
    return min(nodes, key=lambda n: hav(n, (lon, lat)))
def dijk(s, t):
    dist = {s: 0}; prev = {}; pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if u == t: break
        if d > dist.get(u, 1e9): continue
        for v, w in adj[u].items():
            nd = d + w
            if nd < dist.get(v, 1e9): dist[v] = nd; prev[v] = u; heapq.heappush(pq, (nd, v))
    if t not in dist: return None
    path = [t]
    while path[-1] != s: path.append(prev[path[-1]])
    return path[::-1]

P = {"calafate": (-50.340, -72.277), "natales": (-51.730, -72.497), "paine": (-51.005, -72.940),
     "arenas": (-53.163, -70.909), "ushuaia": (-54.807, -68.304)}
# cruce del Estrecho (Primera Angostura): Punta Delgada (continente) -> Bahía Azul (Tierra del Fuego)
pd_ = snap(-52.456, -69.470); ba = snap(-52.78, -69.60)
adj.setdefault(pd_, {})[ba] = 0.05; adj.setdefault(ba, {})[pd_] = 0.05
print("ferry", pd_, ba)
def ruta(a, b):
    r = dijk(snap(*P[a]), snap(*P[b]))
    print(a, "->", b, "ok" if r else "SIN RUTA", len(r) if r else "")
    return r
tramos = [("calafate", "natales"), ("natales", "arenas"), ("arenas", "ushuaia")]
for a, b in tramos:
    r = ruta(a, b)
    if r:
        xs = [p[0] for p in r]; ys = [p[1] for p in r]
        ax.plot(xs, ys, color="white", lw=4.2, zorder=4, solid_capstyle="round")
        ax.plot(xs, ys, color=RUTA, lw=2.4, zorder=5, solid_capstyle="round")
        ls = LineString(list(zip(xs, ys)))
        for bline in bl:
            x = ls.intersection(bline)
            pts = [x] if x.geom_type == "Point" else (list(x.geoms) if hasattr(x, "geoms") else [])
            for q in pts:
                if q.geom_type == "Point":
                    ax.scatter([q.x], [q.y], s=70, marker="D", c="#ffffff", edgecolors=BORDE, linewidths=1.6, zorder=6)
                    print("frontera", round(q.y, 3), round(q.x, 3))
    else:
        ax.plot([P[a][1], P[b][1]], [P[a][0], P[b][0]], color=RUTA, lw=2, ls=":", zorder=5)
# excursión a Torres del Paine desde Puerto Natales
r = ruta("natales", "paine")
if r:
    ax.plot([p[0] for p in r] + [P["paine"][1]], [p[1] for p in r] + [P["paine"][0]], color=RUTA, lw=2, ls=(0, (2, 2)), zorder=5)
else:
    ax.plot([P["natales"][1], P["paine"][1]], [P["natales"][0], P["paine"][0]], color=RUTA, lw=2, ls=(0, (2, 2)), zorder=5)

# ---------- paradas ----------
stops = [("calafate", "1", "El Calafate", (0, 24), "center"), ("paine", "2", "Torres del Paine", (-8, 6), "right"),
         ("natales", "3", "Puerto Natales", (-10, -4), "right"), ("arenas", "4", "Punta Arenas", (-12, -2), "right"),
         ("ushuaia", "5", "Ushuaia", (0, 24), "center")]
halo = [pe.withStroke(linewidth=3, foreground="white")]
for k, n, nombre, off, ha in stops:
    la, lo = P[k]
    ax.scatter([lo], [la], s=520, c=AZUL, edgecolors="white", linewidths=2, zorder=8)
    ax.text(lo, la, n, color="white", fontsize=11, fontweight="bold", ha="center", va="center", zorder=9)
    ax.annotate(nombre, (lo, la), xytext=off, textcoords="offset points", ha=ha, va="center", fontsize=10.5,
                fontweight="bold", color=AZUL, path_effects=halo, zorder=9)

def lab(x, y, t, **kw):
    ax.text(x, y, t, ha="center", va="center", path_effects=halo, zorder=7, **kw)
lab(-69.0, -50.8, "ARGENTINA", fontsize=15, color="#8a7a64", fontweight="bold", alpha=.8)
lab(-73.55, -52.2, "CHILE", fontsize=15, color="#8a7a64", fontweight="bold", alpha=.8)
lab(-67.4, -52.25, "Océano\nAtlántico", fontsize=9.5, color="#4f7f9f", style="italic")
lab(-70.3, -52.55, "Estrecho de Magallanes", fontsize=8.5, color="#4f7f9f", style="italic")
lab(-67.6, -54.97, "Canal Beagle", fontsize=8.5, color="#4f7f9f", style="italic")
lab(-69.2, -53.9, "TIERRA DEL FUEGO", fontsize=9.5, color="#8a7a64", fontweight="bold", alpha=.85)

# leyenda
lx, ly = X0 + 0.2, Y0 + 0.5
ax.add_patch(plt.Rectangle((X0 + 0.08, Y0 + 0.08), 2.3, 0.56, fc="white", ec="#c8d4dc", alpha=.92, zorder=9))
ax.plot([lx, lx + 0.4], [ly + 0.06, ly + 0.06], color=RUTA, lw=2.4, zorder=10)
ax.text(lx + 0.5, ly + 0.06, "Ruta del circuito", fontsize=8, va="center", color=AZUL, zorder=10)
ax.plot([lx, lx + 0.4], [ly - 0.1, ly - 0.1], color=RUTA, lw=2, ls=(0, (2, 2)), zorder=10)
ax.text(lx + 0.5, ly - 0.1, "Excursión desde Puerto Natales", fontsize=8, va="center", color=AZUL, zorder=10)
ax.scatter([lx + 0.2], [ly - 0.26], s=40, marker="D", c="white", edgecolors=BORDE, linewidths=1.4, zorder=10)
ax.text(lx + 0.5, ly - 0.26, "Cruce de frontera", fontsize=8, va="center", color=AZUL, zorder=10)
ax.text(X1 - 0.08, Y1 - 0.08, "Mapa propio de GLOBALpatagonia · © colaboradores de OpenStreetMap (ODbL)", fontsize=6.5,
        ha="right", va="top", color="#6a6a6a", zorder=10, path_effects=[pe.withStroke(linewidth=2, foreground=CREMA)])
fig.savefig(OUT, dpi=200, facecolor=CREMA)
print("OK", OUT)
