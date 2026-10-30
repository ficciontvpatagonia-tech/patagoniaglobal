import json, math, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, PathPatch
from matplotlib.path import Path
import matplotlib.patheffects as pe

D=json.load(open("/private/tmp/claude-501/-Users-jm/c835bf92-a34e-4b1a-ab41-70d155c87df8/scratchpad/osm_geom.json"))
X0,X1,Y0,Y1=-73.37,-72.70,-51.135,-50.815
LAT=-50.97; K=1/math.cos(math.radians(abs(LAT)))     # corrección de aspecto

# paleta GP
CREMA="#f0ede8"; TIERRA="#e7e1d3"; AGUA="#a9cde3"; AGUA_E="#86b4d0"; HIELO="#ffffff"; HIELO_E="#c9deea"
AZUL="#1c2d3d"; GLACIAL="#7aadcc"; ARCILLA="#8c6b4a"; W_COL="#1b78b4"; O_COL="#c0562b"

def ways_of(e):
    if e["type"]=="way": return [[(p["lon"],p["lat"]) for p in e.get("geometry",[])]]
    return [[(p["lon"],p["lat"]) for p in m["geometry"]] for m in e.get("members",[]) if m.get("geometry")]

def rings(segs):
    segs=[s[:] for s in segs if len(s)>1]; out=[]
    while segs:
        r=segs.pop(0)
        changed=True
        while changed and r[0]!=r[-1]:
            changed=False
            for i,s in enumerate(segs):
                if s[0]==r[-1]: r+=s[1:]; segs.pop(i); changed=True; break
                if s[-1]==r[-1]: r+=s[::-1][1:]; segs.pop(i); changed=True; break
                if s[-1]==r[0]: r=s[:-1]+r; segs.pop(i); changed=True; break
                if s[0]==r[0]: r=s[::-1][:-1]+r; segs.pop(i); changed=True; break
        out.append(r)
    return out

def poly_patch(rs, fc, ec, lw=0.6, z=2):
    # un solo Path compuesto (huecos por even-odd)
    verts=[];codes=[]
    for r in rs:
        if len(r)<3: continue
        verts+=r+[r[0]]; codes+=[Path.MOVETO]+[Path.LINETO]*(len(r)-1)+[Path.CLOSEPOLY]
    if not verts: return None
    return PathPatch(Path(verts,codes),fc=fc,ec=ec,lw=lw,zorder=z)

fig=plt.figure(figsize=(11,11*((Y1-Y0)*1.0)/((X1-X0)/K)),dpi=150)
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(X0,X1); ax.set_ylim(Y0,Y1); ax.set_aspect(K); ax.axis("off")
fig.patch.set_facecolor(CREMA); ax.add_patch(plt.Rectangle((X0,Y0),X1-X0,Y1-Y0,fc=TIERRA,ec="none",zorder=0))

def intersects(rs):
    for r in rs:
        for x,y in r:
            if X0-.05<x<X1+.05 and Y0-.05<y<Y1+.05: return True
    return False
for kind,fc,ec,z in (("glacier",HIELO,HIELO_E,1.5),("water",AGUA,AGUA_E,2)):
    for e in D["elements"]:
        t=e.get("tags",{})
        if t.get("natural")!=kind: continue
        rs=rings(ways_of(e))
        if not intersects(rs): continue
        xs=[x for r in rs for x,y in r]; ys=[y for r in rs for x,y in r]
        if kind=="water" and (max(xs)-min(xs))*(max(ys)-min(ys))<0.00004: continue   # lagunas diminutas
        p=poly_patch(rs,fc,ec,z=z)
        if p: ax.add_patch(p)

# senderos
def route(rel_id,col,lw,ls,z,alpha=1):
    for e in D["elements"]:
        if e["type"]=="relation" and e["id"]==rel_id:
            for m in e["members"]:
                g=m.get("geometry")
                if g and m["type"]=="way":
                    xs=[p["lon"] for p in g]; ys=[p["lat"] for p in g]
                    ax.plot(xs,ys,color=col,lw=lw,ls=ls,zorder=z,solid_capstyle="round",alpha=alpha)
route(7705906,O_COL,2.0,(0,(4,2.4)),4)        # O
route(2203617,W_COL,3.0,"-",5)                  # W
halo=[pe.withStroke(linewidth=2.6,foreground=TIERRA)]

def txt(x,y,s,size=7.5,color=AZUL,weight="normal",style="normal",ha="center",va="center",z=9,halo_=True,**kw):
    t=ax.text(x,y,s,fontsize=size,color=color,weight=weight,style=style,ha=ha,va=va,zorder=z,**kw)
    if halo_: t.set_path_effects([pe.withStroke(linewidth=2.4,foreground="white",alpha=.85)])
    return t

# lagos / glaciares (rótulos)
for s,(x,y,r) in {"Lago Grey":(-73.178,-51.06,-72),"Lago Pehoé":(-73.02,-51.097,12),"Lago Nordenskjöld":(-72.965,-51.045,0),
                  "Lago Sarmiento":(-72.80,-51.06,0),"Lago Dickson":(-73.11,-50.832,0),"Lago Paine":(-72.935,-50.84,0),
                  "Lago Skottsberg":(-73.052,-51.047,0)}.items():
    txt(x,y,s,size=7.5,color="#2b6a92",style="italic",rotation=r,halo_=False)
txt(-73.255,-50.985,"Glaciar\nGrey",size=7,color="#4c7893",style="italic",halo_=False)

# macizo / cumbres
def peak(x,y,name,size=7,dy=0.007,dx=0):
    ax.plot(x,y,marker="^",ms=6.5,color="#5a4a3a",mec="white",mew=.6,zorder=8)
    txt(x+dx,y+dy,name,size=size,color="#4a3b2c",style="italic")
peak(-72.985,-50.9497,"Las Torres",dy=-0.010,dx=-0.012)
peak(-73.006,-50.9989,"Cuernos del Paine",dy=0.010,dx=0.005)
peak(-73.087,-50.995,"Cerro Paine Grande",dy=0.009)
peak(-72.964,-50.9725,"Almirante Nieto",dy=-0.009)

# lugares
CAMP=[("Camping Serón",-72.8928,-50.8659,0.002,.008),("Camping Dickson",-73.0752,-50.8786,0.002,.008),("Camping Los Perros",-73.1343,-50.9323,0.002,.009),
      ("Camping Paso",-73.2003,-50.9581,0.002,.009),("Camping Grey",-73.1767,-51.0067,.012,-.002),("Paine Grande",-73.0938,-51.0727,0.002,.009),
      ("Campamento Italiano",-73.0404,-51.0269,-.006,-.0105),("Campamento Francés",-73.0273,-51.0261,.006,.0085),("Camping Los Cuernos",-72.9863,-51.0241,.002,-.010),
      ("Campamento Chileno",-72.9108,-50.9571,.002,.009),("Camping Las Torres",-72.8685,-50.9697,.003,-.010)]
for n,x,y,dx,dy in CAMP:
    ax.plot(x,y,marker="^",ms=8,color=AZUL,mec="white",mew=.8,zorder=8)
    ha="left" if dx>0.006 else "center"
    txt(x+dx,y+dy,n,size=6.8,ha=ha,weight="bold")
MIR=[("Mirador Base Torres",-72.9497,-50.9427,.004,.0075),("Mirador Británico",-73.0538,-50.9827,-.004,.008),("Valle del Francés",-73.0530,-51.0082,-.006,.0065),
     ("Mirador Grey",-73.1826,-51.0022,.0,.0),("Paso John Gardner",-73.1857,-50.9409,.004,.008),("Mirador Lago Skottsberg",-73.0741,-51.0511,-.004,.0)]
for n,x,y,dx,dy in MIR:
    ax.plot(x,y,marker="o",ms=5.2,color="#f1c232",mec=AZUL,mew=.9,zorder=8)
    if n in("Mirador Grey","Mirador Lago Skottsberg"): continue
    ha="left" if dx>0.003 and n.endswith("Torres") else ("right" if dx<-0.003 and "Skottsberg" in n else "center")
    txt(x+dx,y+dy,n,size=6.6,ha=ha,color="#6b5400",weight="bold")
txt(-73.1826+.006,-51.0022+0.004,"Mirador Grey",size=6.6,ha="left",color="#6b5400",weight="bold")
# hoteles / accesos
ax.plot(-72.8750,-50.9732,marker="*",ms=11,color="#e59500",mec=AZUL,mew=.7,zorder=8); txt(-72.872,-50.9835,"Hotel Las Torres",size=6.6,ha="left")
ax.plot(-72.9898,-51.0612,marker="s",ms=6,color="#2e8b57",mec="white",mew=.8,zorder=8); txt(-72.99,-51.0535,"Pudeto\n(catamarán a Paine Grande)",size=6.4,ha="center",color="#1f5f3c",weight="bold")
ax.plot(-72.8004,-50.9795,marker="s",ms=6,color="#2e8b57",mec="white",mew=.8,zorder=8); txt(-72.8004,-50.9715,"Portería Laguna Amarga",size=6.6,color="#1f5f3c",weight="bold")
ax.plot(-72.9863,-51.1079,marker="^",ms=7,color=AZUL,mec="white",mew=.8,zorder=8); txt(-72.9863,-51.1165,"Camping Lago Pehoé\n(sobre la ruta, fuera del W)",size=6.2)

# título, leyenda, norte, escala, fuente
ax.text(X0+.012,Y1-.012,"Torres del Paine",fontsize=24,weight="bold",family="DejaVu Serif",color=AZUL,va="top",zorder=10)
ax.text(X0+.012,Y1-.045,"Circuitos W y O",fontsize=13,color=W_COL,weight="bold",va="top",zorder=10)
from matplotlib.lines import Line2D
h=[Line2D([0],[0],color=W_COL,lw=3,label="Circuito W"),
   Line2D([0],[0],color=O_COL,lw=2,ls=(0,(4,2.4)),label="Circuito O (completo)"),
   Line2D([0],[0],marker="^",color="w",mfc=AZUL,mec="white",ms=8,label="Camping / refugio"),
   Line2D([0],[0],marker="o",color="w",mfc="#f1c232",mec=AZUL,ms=6,label="Mirador"),
   Line2D([0],[0],marker="*",color="w",mfc="#e59500",mec=AZUL,ms=10,label="Hotel"),
   Line2D([0],[0],marker="s",color="w",mfc="#2e8b57",mec="white",ms=7,label="Acceso / transporte")]
lg=ax.legend(handles=h,loc="upper right",bbox_to_anchor=(.985,.985),fontsize=7.6,frameon=True,framealpha=.95,edgecolor="#c8d4dc",title="Referencias",title_fontsize=8.5)
lg.set_zorder(12)
# norte
ax.annotate("",xy=(X1-.025,Y0+.062),xytext=(X1-.025,Y0+.028),arrowprops=dict(arrowstyle="-|>",color=AZUL,lw=1.6),zorder=11)
ax.text(X1-.025,Y0+.070,"N",fontsize=9,weight="bold",color=AZUL,ha="center",zorder=11)
# escala 5 km
km_lon=5/(111.32*math.cos(math.radians(abs(LAT))))
sx=X0+.015; sy=Y0+.02
ax.plot([sx,sx+km_lon],[sy,sy],color=AZUL,lw=2.5,zorder=11); ax.text(sx+km_lon/2,sy+.006,"5 km",fontsize=7.5,ha="center",color=AZUL,zorder=11)
ax.text(X0+.015,Y0+.004,"Datos: © colaboradores de OpenStreetMap (ODbL) · Mapa: GLOBALpatagonia",fontsize=6.3,color="#5a6070",va="bottom",zorder=11)
out=sys.argv[1] if len(sys.argv)>1 else "/private/tmp/claude-501/-Users-jm/c835bf92-a34e-4b1a-ab41-70d155c87df8/scratchpad/mapa/mapa.png"
fig.savefig(out,dpi=200,facecolor=CREMA)
print(out, fig.get_size_inches())
