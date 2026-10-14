#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Borrador v2 (solo ES) del informe Sea Lion / Tribunal del Mar, reescrito con la nota completa de Página12.
# Genera /Users/jm/Desktop/PREVIEW_sea_lion_tribunal_mar.html. NO publica nada.
import html

TITULO = "Argentina fue al Tribunal del Mar y Londres blindó a sus petroleras"
BAJADA = ("Buenos Aires pidió medidas urgentes en Hamburgo para frenar Sea Lion, el primer gran proyecto petrolero "
          "en aguas de Malvinas. Londres respondió con una ley que protege a las empresas y una carta a Interpol. "
          "Qué pidió cada lado y qué puede pasar.")

DATELINE = '<p class="dl">Malvinas — Informe GLOBALpatagonia</p>'

def img_block(src, alt, cap):
    return f'<div class="img"><img src="{src}" alt="{alt}"><div class="cap">{cap}</div></div>'

def quote(t):
    return f'<blockquote>{t}</blockquote>'

IMG = "/Users/jm/Desktop/CLAUDCODE/GLOBAL PATAGONIA/fotos/malvinas-plataforma-sea-lion.webp"

cuerpo = "\n\n".join([
    DATELINE,

    "<p>La disputa por el petróleo de Malvinas pasó de las notas diplomáticas a los tribunales internacionales. El Gobierno argentino llevó al Reino Unido ante el Tribunal Internacional del Derecho del Mar, en Hamburgo, para frenar <strong>Sea Lion</strong>, el primer gran proyecto petrolero en aguas de las islas. Horas después, Londres anunció que blindará legalmente a las empresas que lo operan y le pidió a Interpol que rechace los pedidos de detención argentinos vinculados al proyecto.</p>",

    "<h3>Qué pidió la Argentina</h3>",

    "<p>El pedido forma parte del arbitraje que el Gobierno inició el 28 de septiembre bajo la Convención de las Naciones Unidas sobre el Derecho del Mar. Ese día se le dio al Reino Unido un plazo de dos semanas para detener las actividades; venció el 12 de octubre sin respuesta favorable, y el 13 la Argentina pidió al Tribunal <strong>medidas provisionales</strong> con cuatro reclamos concretos:</p>",

    "<ul><li><strong>Sea Lion:</strong> que el Reino Unido impida el inicio o la continuación de la explotación de hidrocarburos en la Cuenca Malvinas Norte.</li>"
    "<li><strong>Datos de exploración:</strong> que no use en perjuicio de la Argentina la información obtenida durante las exploraciones.</li>"
    "<li><strong>Medio marino:</strong> que no obstaculice el cumplimiento de las obligaciones ambientales de la Convención.</li>"
    "<li><strong>Nuevos permisos:</strong> que no adopte medidas que agraven la controversia, en particular nuevas autorizaciones de explotación.</li></ul>",

    "<p>Presentar el pedido no suspende el proyecto: el Tribunal debe decidir si concede las medidas. En el caso de la Fragata Libertad, en 2012, resolvió en alrededor de un mes, por lo que una primera definición podría llegar en noviembre, aunque no hay fecha confirmada.</p>",

    img_block(IMG, "Plataforma offshore de Sea Lion en el Atlántico Sur",
              "La plataforma de Sea Lion, el proyecto en la Cuenca Malvinas Norte que la Argentina quiere frenar. Foto: archivo."),

    "<p>El canciller Pablo Quirno presentó la estrategia como “inédita” y dijo que es “la primera vez que Argentina acude a un arbitraje sobre este tema”, con la “intención pacífica de resolver una disputa que está en su corazón”. Es cierto en lo del arbitraje; no así en lo de presionar a las petroleras: ya lo habían hecho gobiernos anteriores.</p>",

    "<h3>Lo que ya se había intentado</h3>",

    "<p>La presión sobre las empresas que operan en Malvinas tiene antecedentes de más de una década:</p>",

    "<ul><li><strong>2011:</strong> ley que restringe la actividad hidrocarburífera en la zona sin autorización argentina.</li>"
    "<li><strong>2012:</strong> se declaran ilegales las operaciones de cinco petroleras.</li>"
    "<li><strong>2013:</strong> se endurecen las sanciones penales.</li>"
    "<li><strong>2015:</strong> se denuncia a empresas que exploraban en la zona y se consiguen embargos judiciales por más de 156 millones de dólares.</li></ul>",

    "<p>La diferencia ahora es el escenario: un tribunal internacional, un proyecto que ya tiene decisión de inversión y producción prevista para 2028.</p>",

    "<h3>Londres blinda a sus empresas</h3>",

    "<p>La respuesta británica tuvo tres piezas. Primero, ratificó su respaldo al desarrollo de Sea Lion y habilitó su continuidad. Esa autorización pasa por el secretario de Asuntos Exteriores, Ed Miliband, cuyo consentimiento es necesario para ciertas licencias de hidrocarburos en el archipiélago, según la Ordenanza de Minerales Costa Afuera de las Malvinas de 1994. Londres sostiene que los habitantes de las islas tienen derecho a desarrollar sus recursos naturales, y que esa facultad forma parte de su posición sobre la autodeterminación.</p>",

    "<p>Segundo, activó la legislación de <em>Protección de Intereses Comerciales</em>, que le permite prohibir a compañías y personas bajo jurisdicción británica que cumplan leyes extranjeras —en este caso, las argentinas— que impongan sanciones o restricciones a quienes operan en Malvinas. En la práctica significa que Navitas y Rockhopper seguirán operando pese a las sanciones que impulsa Buenos Aires.</p>",

    "<p>Tercero, escribió a Interpol. Según informó <em>The Guardian</em>, el Reino Unido sostiene que las “notificaciones rojas” solicitadas por la Argentina “deben considerarse motivadas por razones políticas” y las describe como “un intento de intimidar a personas y empresas para que no operen en las Malvinas”. Interpol respondió que respetará el artículo 3 de sus estatutos, que le prohíbe intervenir en asuntos de carácter político.</p>",

    quote("“Sea Lion podría triplicar el PIB del archipiélago, pero Milei ha prometido bloquearlo.”"),

    "<p style=\"font-size:.85rem;color:#777\">Argumento del gobierno británico, según la carta a Interpol citada por <em>The Guardian</em>.</p>",

    "<h3>Las empresas y el calendario</h3>",

    "<p>Sea Lion es operado por la israelí <strong>Navitas Petroleum</strong> (65%), con la británica <strong>Rockhopper Exploration</strong> (35%) como socia; Rockhopper descubrió el yacimiento en 2010. El plan contempla once pozos submarinos conectados a una unidad flotante de producción. Las perforaciones de desarrollo están previstas para 2027, el primer petróleo para el primer trimestre de 2028 y una capacidad de hasta 180.000 barriles diarios. El 7 de octubre, Rockhopper anunció una inversión de 44 millones de dólares en su participación en la sociedad dueña de esa unidad.</p>",

    "<p>La presión argentina ya tiene un primer efecto concreto: según la Presidencia, Halliburton confirmó que sus filiales no prestarán servicios al proyecto. Navitas reconoció que está reemplazando a dos contratistas, aunque dice que no espera un impacto material.</p>",

    "<h3>La contradicción británica</h3>",

    "<p>La decisión también abrió una grieta interna en el Reino Unido. El responsable de Energía del Partido Conservador, Andrew Bowie, celebró la autorización pero cuestionó al Gobierno laborista:</p>",

    quote("“¿Por qué Ed Miliband, el hombre que bloqueó las perforaciones en el Mar del Norte, está dispuesto a permitirlas en el Atlántico Sur, pero no frente a las costas de Escocia?”"),

    "<p>En el Mar del Norte, el gobierno británico impulsó por ahora el freno a nuevas exploraciones de petróleo y gas. En el Atlántico Sur, en cambio, respalda un yacimiento nuevo.</p>",

    "<h3>Qué está realmente en juego</h3>",

    "<p>El Tribunal del Mar no resuelve disputas de soberanía, y ese es el principal obstáculo jurídico de la estrategia argentina: la Convención no le da competencia general sobre quién es dueño de un territorio. Por eso el planteo se apoya en obligaciones concretas sobre recursos, ambiente y conducta de las partes mientras la controversia sigue abierta.</p>",

    "<p>Aun así, el movimiento tiene un peso político y económico evidente: lleva Sea Lion a un foro internacional, expone a las empresas a un riesgo reputacional y financiero, y obliga a Londres a mostrar cuánto está dispuesto a gastar —en leyes, en diplomacia y en cartas a Interpol— para sostener el proyecto. La decisión del Tribunal, que se espera para las próximas semanas, marcará el rumbo de la disputa petrolera en el Atlántico Sur.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Fuentes: Página12, <em>The Guardian</em> (vía Página12), Infobae, Perfil, La Gaceta, Informe Digital, Rosario3, Splash247.</p>',
])

page = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>PREVIEW — {html.escape(TITULO)}</title>
<style>
body{{background:#f0ede8;color:#252830;font:17px/1.7 Inter,system-ui,sans-serif;margin:0}}
.wrap{{max-width:720px;margin:0 auto;padding:2rem 1.2rem 4rem}}
.pv{{background:#8c6b4a;color:#fff;text-align:center;padding:.5rem;font-size:.85rem;letter-spacing:.08em}}
h1{{font-family:'Playfair Display',Georgia,serif;color:#1c2d3d;font-size:2.2rem;line-height:1.2}}
h3{{font-family:'Playfair Display',Georgia,serif;color:#1c2d3d;margin-top:2rem}}
.baj{{font-size:1.15rem;color:#555}}
.dl{{font-size:.85rem;letter-spacing:.05em;text-transform:uppercase;color:#7aadcc;font-weight:600;margin-bottom:1.2rem}}
.img{{margin:2rem 0}} .img img{{width:100%;border-radius:6px;display:block}} .cap{{font-size:.8rem;color:#777;margin-top:.45rem}}
blockquote{{border-left:4px solid #7aadcc;margin:2rem 0;padding:.4rem 0 .4rem 1.4rem;font-size:1.25rem;line-height:1.5;font-style:italic}}
.firma{{margin-top:2.5rem;padding-top:1rem;border-top:1px solid #ccc;font-weight:600}}
</style></head><body>
<div class="pv">PREVIEW — NO PUBLICADO · versión 2 (solo español)</div>
<div class="wrap"><h1>{html.escape(TITULO)}</h1><p class="baj">{html.escape(BAJADA)}</p>
{cuerpo}
<div class="firma">J. Martineau · GLOBALpatagonia</div></div></body></html>"""

open("/Users/jm/Desktop/PREVIEW_sea_lion_tribunal_mar.html", "w", encoding="utf-8").write(page)
print("OK → /Users/jm/Desktop/PREVIEW_sea_lion_tribunal_mar.html")
