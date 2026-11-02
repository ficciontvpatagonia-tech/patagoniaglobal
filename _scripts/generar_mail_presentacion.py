#!/usr/bin/env python3
"""Genera la vista previa del mail de presentación de GLOBALpatagonia (ES/EN) en _preview/.
No envía nada. Uso: python3 _scripts/generar_mail_presentacion.py"""
import pathlib
B = "https://globalpatagonia.org"
IMG = B + "/fotos/mail/"
SUBS_FORM = B + "/#sec-newsletter"  # sección de suscripción del sitio (lista Brevo 3)

L = {
 "es": dict(
  lang="es", sfx="", pre="Toda la Patagonia Argentina – Chile en un solo lugar",
  tag="Noticias de la Patagonia argentina y chilena",
  hola="Hola,",
  intro="Te escribimos desde <b>GLOBALpatagonia</b>, un medio de noticias independiente que sigue lo que pasa en toda la Patagonia, a ambos lados de la cordillera, y también en el Pacífico sur, Malvinas, el Atlántico Sur y la Antártida: turismo, economía, ciencia, cultura, deportes, ambiente y conectividad. Publicamos en <b>español, inglés, portugués y chino</b>, con informes propios y herramientas pensadas para quien vive, viaja o trabaja en la Patagonia.",
  cta_main="Suscribirme al newsletter", cta_sub="Las noticias de la Patagonia en tu mail. Gratis, baja en un clic.",
  follow="Seguinos también en", serv_t="Servicios para viajeros y para el sector",
  serv=[("","Pronóstico","clima.html"),("","Mareas","mareas.html"),("","Vuelos","conectividad.html#vuelos"),
        ("","Estado de rutas","conectividad.html#rutas"),("","Pasos fronterizos","conectividad.html#pasos"),
        ("","Divisas","cotizaciones.html"),("","Agenda","agenda.html"),("","Informes","reports.html")],
  cards_t="Para explorar",
  cards=[],
  guias=[("Torres del Paine","notas/guia-torres-del-paine{s}.html","guia-paine"),("El Calafate","notas/guia-calafate{s}.html","guia-calafate"),("Circuito Austral","notas/guia-circuito-austral{s}.html","guia-circuito")],
  guias_t="Guías de viaje", guias_s="Paso a paso, con mapas y precios", cine_t="Cinemateca Patagónica", cine_s="Cine, documentales y directores de la región, en un solo lugar.", cine_b="Entrar a la Cinemateca", ban1="Toda la Patagonia Argentina – Chile en un solo lugar", ban2="Ambos lados de la cordillera.",
  inf_t="Informes propios destacados",
  inf=[("Argentina fue al Tribunal del Mar y Londres blindó a sus petroleras","notas/20261014-propio-malvinas-tribunal-mar-sea-lion.html","inf-tribunal"),
       ("Reino Desunido: la crisis constitucional británica y su impacto real en Malvinas","notas/20260917-propio-reino-desunido.html","inf-reino"),
       ("EEUU amenaza con soltarle la mano a Londres por Malvinas","notas/20260830-propio-malvinas-eeuu-otan.html","inf-eeuu")],
  inf_sfx="", leer="Leer",
  close_t="Conocé el portal completo", close="Noticias de toda la Patagonia, Malvinas y la Antártida, clima, mareas, vuelos, rutas, cine y guías de viaje, todo en un solo lugar.", close_b="Visitar globalpatagonia.org", qr_t="Escaneá el código con tu celular para entrar al portal",
  org_t="",
  org="Podés enviarnos gacetillas y novedades, o sumarte como auspiciante del portal.",
  b1="Publicidad", b2="Apoyanos", h1="publicidad.html", h2="apoyanos.html",
  firma="Equipo GLOBALpatagonia", motivo="Te escribimos porque tu organización está vinculada al turismo o a la Patagonia, y creemos que este portal puede resultarte útil. Si no querés recibir más mensajes, <a href=\"#BAJA\" style=\"color:#7aadcc\">dá de baja tu dirección acá</a>. <a href=\"%s/privacidad.html\" style=\"color:#7aadcc\">Privacidad</a>."%B),
 "en": dict(
  lang="en", sfx="-en", pre="All of Argentine and Chilean Patagonia in one place",
  tag="News from Argentine and Chilean Patagonia",
  hola="Hello,",
  intro="We are writing from <b>GLOBALpatagonia</b>, an independent news outlet covering all of Patagonia, on both sides of the Andes, as well as the southern Pacific, Malvinas, the South Atlantic and Antarctica: tourism, economy, science, culture, sports, environment and connectivity. We publish in <b>Spanish, English, Portuguese and Chinese</b>, with original reporting and tools for anyone who lives, travels or works in Patagonia.",
  cta_main="Subscribe to the newsletter", cta_sub="Patagonia news in your inbox. Free, one-click unsubscribe.",
  follow="Follow us on", serv_t="Services for travelers and the industry",
  serv=[("","Weather","clima.html"),("","Tides","mareas.html"),("","Flights","conectividad.html#vuelos"),
        ("","Road status","conectividad.html#rutas"),("","Border crossings","conectividad.html#pasos"),
        ("","Exchange rates","cotizaciones.html"),("","Events","agenda.html"),("","Reports","reports.html")],
  cards_t="Explore",
  cards=[],
  guias=[("Torres del Paine","notas/guia-torres-del-paine{s}.html","guia-paine"),("El Calafate","notas/guia-calafate{s}.html","guia-calafate"),("Austral Circuit","notas/guia-circuito-austral{s}.html","guia-circuito")],
  guias_t="Travel guides", guias_s="Step by step, with maps and prices", cine_t="Patagonian Cinematheque", cine_s="Films, documentaries and directors from the region, in one place.", cine_b="Enter the Cinematheque", ban1="All of Argentine and Chilean Patagonia in one place", ban2="Both sides of the Andes.",
  inf_t="Featured original reports",
  inf=[("Argentina took the Malvinas oil case to the Law of the Sea Tribunal, and London shielded its oil companies","notas/20261014-propio-malvinas-tribunal-mar-sea-lion.html","inf-tribunal"),
       ("Disunited Kingdom: Britain's constitutional crisis and its real impact on Malvinas","notas/20260917-propio-reino-desunido.html","inf-reino"),
       ("US threatens to let go of London's hand over Malvinas","notas/20260830-propio-malvinas-eeuu-otan.html","inf-eeuu")],
  inf_sfx="-en", leer="Read",
  close_t="Discover the full portal", close="News from all of Patagonia, Malvinas and Antarctica, weather, tides, flights, roads, cinema and travel guides, all in one place.", close_b="Visit globalpatagonia.org", qr_t="Scan the code with your phone to open the portal",
  org_t="",
  org="Send us your press releases and news, or join the portal as a sponsor.",
  b1="Advertise", b2="Support us", h1="publicidad.html", h2="apoyanos.html",
  firma="The GLOBALpatagonia team", motivo="You are receiving this because your organization is linked to tourism or Patagonia. If you prefer not to receive more messages, <a href=\"#BAJA\" style=\"color:#7aadcc\">unsubscribe here</a>. <a href=\"%s/privacidad.html\" style=\"color:#7aadcc\">Privacy</a>."%B),
}

def btn(href, txt, bg="#1c2d3d", fg="#fff"):
    return f'<a href="{href}" style="display:inline-block;border:2px solid #1c2d3d;color:#1c2d3d;text-decoration:none;letter-spacing:1px;text-transform:uppercase;font-weight:bold;padding:13px 26px;font-family:Arial,sans-serif;font-size:13px">{txt}</a>'

def img(name, w, alt="", extra=""):
    return f'<img src="{IMG}{name}.jpg" width="{w}" alt="{alt}" style="display:block;width:100%;max-width:{w}px;height:auto;border:0;{extra}">'

CAP = {
 "es": {"clima.html":"9 ciudades patagónicas","mareas.html":"Tablas y horarios","conectividad.html#vuelos":"Arribos y partidas","conectividad.html#rutas":"Cortes y estado actual","conectividad.html#pasos":"Fronteras Argentina–Chile","cotizaciones.html":"Dólar, peso chileno y más","agenda.html":"Eventos de la región","reports.html":"Investigaciones propias"},
 "en": {"clima.html":"9 Patagonian cities","mareas.html":"Tables and schedules","conectividad.html#vuelos":"Arrivals and departures","conectividad.html#rutas":"Closures and live status","conectividad.html#pasos":"Argentina–Chile borders","cotizaciones.html":"Dollar, Chilean peso and more","agenda.html":"Regional events","reports.html":"Original investigations"}}

def build(c):
    sfx = c["sfx"]
    cap = CAP[c["lang"]]
    cells = []
    for k, (ic, t, h) in enumerate(c["serv"]):
        cells.append(f'<td width="50%" valign="top" style="padding:5px"><a href="{B}/{h}" style="display:block;text-decoration:none;background:#f0ede8;border-left:4px solid #b03a2e;padding:16px 18px"><span style="display:block;font-family:Georgia,serif;font-size:19px;color:#1b2e42">{t} &rarr;</span><span style="display:block;font-family:Arial,sans-serif;font-size:12px;color:#6a6f7a;padding-top:4px">{cap[h]}</span></a></td>')
        if k % 2 == 1 and k < len(c["serv"]) - 1: cells.append("</tr><tr>")
    serv = "".join(cells)
    guias = "".join(
      f'<td width="33%" valign="top" style="padding:0 4px"><a href="{B}/{h.format(s=sfx)}" style="text-decoration:none">{img(g,190,t)}<div style="font-family:Georgia,serif;font-size:15px;color:#1b2e42;padding:8px 0 0;text-align:center">{t}</div></a></td>'
      for t, h, g in c["guias"])
    cine = "".join(f'<td width="25%" style="padding:0 2px">{img("cine-"+n,140,"")}</td>' for n in ["erase-patagonia","forajidos-patagonia","al-pie-de-los-andes","encuentros-fin-del-mundo"])
    inf = "".join(
      f'<tr><td width="120" valign="top" style="padding:10px 14px 10px 0;border-bottom:1px solid #e8e3da"><a href="{B}/{h.replace(".html", c["inf_sfx"]+".html")}">{img(g,120,"")}</a></td><td valign="middle" style="padding:10px 0;border-bottom:1px solid #e8e3da;font-family:Georgia,serif;font-size:17px;line-height:23px"><a href="{B}/{h.replace(".html", c["inf_sfx"]+".html")}" style="color:#1b2e42;text-decoration:none">{t}</a></td></tr>'
      for t, h, g in c["inf"])
    soc = " &nbsp;·&nbsp; ".join(f'<a href="{h}" style="color:#1c2d3d;text-decoration:none;font-weight:bold">{n}</a>' for n, h in
      [("WhatsApp","https://whatsapp.com/channel/0029VbDPKE6DJ6Gyg2eQTH2j"),("Telegram","https://t.me/globalpatagonia"),("Instagram","https://www.instagram.com/global.patagonia"),("Facebook","https://www.facebook.com/PatagoniaGLOBAL"),("RSS",B+"/feed.xml")])
    H = 'font-family:Georgia,serif;font-size:22px;color:#1b2e42;font-weight:normal'
    S = 'font-family:Arial,sans-serif;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#b03a2e'
    return f'''<!DOCTYPE html><html lang="{c["lang"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light only"><meta name="supported-color-schemes" content="light"><style>:root{{color-scheme:light only;supported-color-schemes:light}}</style><title>GLOBALpatagonia</title></head>
<body style="margin:0;background:#f0ede8"><span style="display:none;max-height:0;overflow:hidden">{c["pre"]}</span>
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f0ede8"><tr><td align="center" style="padding:0 0 24px">
<table width="640" cellpadding="0" cellspacing="0" style="max-width:640px;width:100%;background:#ffffff">
<tr><td>{img("cabecera-"+c["lang"],640,c["ban1"])}</td></tr>
<tr><td style="padding:12px 40px 8px;font-family:Georgia,serif;font-size:17px;line-height:27px;color:#3b3f48">{c["intro"]}</td></tr>
<tr><td align="center" style="padding:20px 40px 8px">{btn(SUBS_FORM, c["cta_main"], "#1c2d3d")}<div style="font-family:Arial,sans-serif;font-size:12px;color:#7a7f8a;margin-top:10px">{c["cta_sub"]}</div></td></tr>
<tr><td align="center" style="padding:16px 40px 28px;font-family:Arial,sans-serif;font-size:13px;color:#5a6070">{soc}</td></tr>
<tr><td>{img("banda-fitz-roy",640,"Fitz Roy")}</td></tr>
<tr><td align="center" style="padding:30px 30px 8px"><div style="{S}">{c["serv_t"]}</div></td></tr>
<tr><td style="padding:4px 25px 30px"><table width="100%" cellpadding="0" cellspacing="0"><tr>{serv}</tr></table></td></tr>
<tr><td style="padding:0 30px 4px"><div style="{S}">{c["guias_t"]}</div><div style="font-family:Arial,sans-serif;font-size:13px;color:#7a7f8a;padding:4px 0 12px">{c["guias_s"]}</div></td></tr>
<tr><td style="padding:0 26px 30px"><table width="100%" cellpadding="0" cellspacing="0"><tr>{guias}</tr></table></td></tr>
<tr><td style="background:#f0ede8;padding:26px 30px 28px" align="center"><div style="{S}">Cinemateca</div><div style="font-family:Georgia,serif;font-size:22px;color:#1b2e42;padding:6px 0 4px">{c["cine_t"]}</div><div style="font-family:Arial,sans-serif;font-size:13px;color:#5a6070;padding-bottom:16px">{c["cine_s"]}</div><table width="100%" cellpadding="0" cellspacing="0"><tr>{cine}</tr></table><div style="padding-top:18px">{btn(B+"/videos.html", c["cine_b"])}</div></td></tr>
<tr><td style="padding:30px 30px 2px"><div style="{S}">{c["inf_t"]}</div></td></tr>
<tr><td style="padding:6px 30px 20px"><table width="100%" cellpadding="0" cellspacing="0">{inf}</table></td></tr>
<tr><td>{img("banda-chalten",640,"El Chaltén")}</td></tr>
<tr><td align="center" style="padding:30px 40px 34px"><div style="{H}">{c["close_t"]}</div><div style="font-family:Arial,sans-serif;color:#5a6070;font-size:14px;line-height:21px;margin:8px 0 18px">{c["close"]}</div>{btn(B+"/?utm_source=mail&utm_medium=email&utm_campaign=presentacion-g1", c["close_b"])}<div style="padding-top:26px"><img src="{IMG}qr-portal.png" width="170" alt="QR globalpatagonia.org" style="display:block;margin:0 auto;width:170px;height:auto;border:0"><div style="font-family:Arial,sans-serif;font-size:12px;color:#7a7f8a;padding-top:8px">{c["qr_t"]}</div></div></td></tr>
<tr><td style="background:#f0ede8;padding:22px 30px;font-family:Arial,sans-serif;font-size:12px;line-height:18px;color:#5a6070"><b style="color:#1b2e42">{c["firma"]}</b> · <a href="{B}" style="color:#3a5a7a">globalpatagonia.org</a><br><br>{c["motivo"]}</td></tr>
</table></td></tr></table></body></html>'''

def main():
    import sys
    global IMG
    out = pathlib.Path(__file__).resolve().parent.parent / "_preview"
    if "--preview" in sys.argv:
        IMG = "../fotos/mail/"
    for k, c in L.items():
        (out / f"mail_presentacion_{k}.html").write_text(build(c), encoding="utf-8")
        print("OK", out / f"mail_presentacion_{k}.html")

if __name__ == "__main__":
    main()
