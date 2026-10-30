#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera notas/guia-torres-del-paine.html (ES) a partir de la estructura de guia-esquel.html.
Preview local: NO publica. Cuerpo = lista de bloques; head/pie se heredan de Esquel."""
import re, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
esq = open(f"{BASE}/notas/guia-esquel.html", encoding="utf-8").read()

SLUG = "guia-torres-del-paine"
TITLE = "Torres del Paine: guía de viaje — Circuitos W y O, glaciares y fauna — GLOBALpatagonia"
DESC = ("Guía de Torres del Paine, Patagonia chilena: cuándo ir, cómo llegar desde Puerto Natales y El Calafate, "
        "circuito W y O, Base de las Torres, Glaciar Grey, dónde dormir y consejos prácticos. Con mapa propio.")
HERO = "fotos/CIUDADES/torres-del-paine-hero.webp"
HERO_ABS = "https://globalpatagonia.org/" + HERO

# ---- cabeza: reemplazos sobre la de Esquel
head = esq[:esq.index('<div class="hero">')]
head = head.replace("Esquel: guía de viaje — La puerta de la Patagonia — GLOBALpatagonia", TITLE)
head = re.sub(r'Esquel es una ciudad tranquila[^"]*?Trevelin\.', DESC, head)
head = head.replace("guia-esquel", SLUG)
head = head.replace("https://globalpatagonia.org/fotos/CIUDADES/esquel-trochita-nieve.webp", HERO_ABS)
head = head.replace("https://globalpatagonia.org/fotos/CIUDADES/esquel-trochita-nieve.jpg", HERO_ABS)
head = head.replace('"@type":"TouristDestination","name":"Esquel"', '"@type":"TouristDestination","name":"Parque Nacional Torres del Paine"')
head = head.replace('es_AR', 'es_CL')
# CSS extra: mapa y tabla
extra_css = """
    .mapa-wrap{margin:8px 0 8px;background:white;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.07);overflow:hidden;}
    .mapa-wrap img{width:100%;height:auto;display:block;}
    .mapa-cap{font-size:12px;color:#7a7a7a;font-style:italic;padding:10px 16px 12px;}
    .tabla-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;}
    .gp-tabla{width:100%;border-collapse:collapse;background:white;border-radius:6px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.07);font-size:14px;}
    .gp-tabla th{background:var(--verde);color:white;text-align:left;padding:12px 14px;font-size:12px;letter-spacing:1px;text-transform:uppercase;}
    .gp-tabla td{padding:12px 14px;border-bottom:1px solid #e8e5e0;vertical-align:top;line-height:1.5;color:#2a2a2a;}
    .gp-tabla tr:last-child td{border-bottom:none;}
    .gp-tabla td:first-child{font-weight:700;color:var(--verde);}
    .aviso-salud{background:#fff7e6;border:1px solid #f0d9a8;border-left:6px solid #e59500;border-radius:6px;padding:22px 24px;margin-top:6px;box-shadow:0 2px 8px rgba(0,0,0,0.05);}
    .aviso-salud h3{font-family:'Playfair Display',serif;font-size:20px;color:#7a4a00;margin-bottom:10px;}
    .aviso-salud p{font-size:15px;line-height:1.7;color:#3a3a3a;margin:0 0 10px;}
    .aviso-salud ul{margin:6px 0 12px 20px;}
    .aviso-salud li{font-size:15px;line-height:1.65;color:#3a3a3a;margin-bottom:6px;}
    .aviso-salud .fin{font-size:13px;color:#7a5a20;margin:10px 0 0;}
    .nota-oficial{font-size:13px;color:#5a6070;background:#e9f1f6;border-left:4px solid #8ab8d4;padding:12px 16px;border-radius:3px;margin-top:14px;line-height:1.6;}
"""
head = head.replace("  </style>", extra_css + "  </style>", 1)

def img(src, alt, pos=None):
    st = f' style="object-position:{pos};"' if pos else ""
    return f'<div class="foto-ratio"><img src="../fotos/CIUDADES/{src}" alt="{alt}" loading="lazy"{st}/></div>'
def item(src, alt, h, p):
    return f'''    <div class="guia-item">
      {img(src, alt)}
      <div class="guia-item-body">
        <h3>{h}</h3>
        <p>{p}</p>
      </div>
    </div>
'''

hero = f'''<div class="hero">
  <img src="../{HERO}" alt="Las tres torres de granito del Parque Nacional Torres del Paine bajo un cielo de nubes en la Patagonia chilena"/>
  <div class="hero-overlay">
    <div class="hero-tag">🗺️ Guía de viaje</div>
    <div class="hero-titulo">Torres del Paine</div>
    <div class="hero-tagline">El corazón de granito de la Patagonia chilena</div>
  </div>
</div>

<div class="container">
  <a href="../" class="volver">← Inicio</a>
    <div class="lang-switcher">
      <a href="{SLUG}.html" class="active">🇨🇱 ES</a>
      <a href="{SLUG}-en.html">🇬🇧 EN</a>
      <a href="{SLUG}-pt.html">🇧🇷 PT</a>
      <a href="{SLUG}-zh.html">🇨🇳 中文</a>
    </div>

  <p class="guia-intro">Torres del Paine es el parque más famoso de la Patagonia chilena y una Reserva de la Biosfera de la UNESCO desde 1978. En unas 240.000 hectáreas de la región de Magallanes, a unos 110 km de Puerto Natales, se juntan torres de granito, glaciares, lagos turquesa y una fauna que se deja ver: guanacos, cóndores y pumas en libertad. Se recorre en una caminata de un día o en circuitos de varios días.</p>

  <!-- ¿CUÁNDO IR? -->
  <div class="guia-seccion">
    <h2>¿Cuándo ir?</h2>
    <div class="cuando-grid">
      <div class="cuando-card">
        <div class="mes">Oct · Nov</div>
        <div class="titulo-cuando">Primavera: menos gente</div>
        <p>Deshielo, flores y senderos más tranquilos. El viento ya es fuerte y algunos servicios y el circuito O recién empiezan la temporada: confirmá fechas antes de reservar.</p>
      </div>
      <div class="cuando-card">
        <div class="mes">Dic · Feb</div>
        <div class="titulo-cuando">Verano: temporada alta</div>
        <p>Días larguísimos y el mejor clima, pero también el pico de visitantes. Los refugios y campings se agotan con meses de anticipación.</p>
      </div>
      <div class="cuando-card">
        <div class="mes">Mar · Abr</div>
        <div class="titulo-cuando">Otoño: colores y calma</div>
        <p>El bosque se pone rojizo y amarillo, con menos gente y noches frías. Un momento muy buscado por fotógrafos.</p>
      </div>
    </div>
    <div class="nota-oficial">En invierno rige un reglamento especial: el circuito W y el sendero a la Base de las Torres exigen un <strong>guía habilitado por CONAF</strong>.</div>
  </div>

  <!-- CÓMO LLEGAR -->
  <div class="guia-seccion">
    <h2>Cómo llegar</h2>
    <div class="llegar-grid">
      <div class="llegar-item">
        <div class="icono">✈️</div>
        <h4>Avión</h4>
        <p>Lo habitual es volar a Punta Arenas o a El Calafate (Argentina) y seguir por tierra hasta Puerto Natales, la base más cómoda para visitar el parque.</p>
      </div>
      <div class="llegar-item">
        <div class="icono">🚌</div>
        <h4>Desde Puerto Natales</h4>
        <p>Unos 110 km hasta la Portería Laguna Amarga: dos horas en bus o auto, con servicios diarios en temporada alta.</p>
      </div>
      <div class="llegar-item">
        <div class="icono">🛂</div>
        <h4>Desde El Calafate</h4>
        <p>Bus con cruce de frontera: entre 4 y 7 horas hasta Puerto Natales, con menos salidas en invierno. Llevá el pasaporte o documento habilitado.</p>
      </div>
      <div class="llegar-item">
        <div class="icono">⛴️</div>
        <h4>Catamarán Pudeto – Paine Grande</h4>
        <p>Cruza el lago Pehoé y es la puerta de entrada al circuito W por el oeste. Depende del clima y del viento: confirmá horarios en el momento.</p>
      </div>
    </div>
    <div class="nota-oficial"><strong>Entradas:</strong> desde el 1 de mayo de 2026 rige un nuevo sistema (entrada diaria o por 2 días o más, válida hasta 10 días seguidos). La compra es anticipada y obligatoria en <strong>pasesparques.cl</strong> y se presenta el código QR en el acceso. Los valores para extranjeros cambian: consultalos en el sitio oficial.</div>
  </div>

  <!-- MAPA -->
  <div class="guia-seccion">
    <h2>El mapa: circuitos W y O</h2>
    <div class="mapa-wrap">
      <img src="../fotos/CIUDADES/torres-del-paine-mapa-circuitos-w-o.webp" alt="Mapa de Torres del Paine con los circuitos W y O, campamentos, miradores, lagos y glaciares" loading="lazy"/>
      <div class="mapa-cap">Mapa propio de GLOBALpatagonia con datos de OpenStreetMap. El W (azul) termina en el glaciar Grey; el O (naranja) lo rodea todo por el paso John Gardner.</div>
    </div>
  </div>

  <!-- ELEGIR CIRCUITO -->
  <div class="guia-seccion">
    <h2>¿Cuál recorrido elegir?</h2>
    <div class="tabla-scroll">
      <table class="gp-tabla">
        <thead><tr><th>Recorrido</th><th>Duración aprox.</th><th>Para quién</th><th>Reserva</th></tr></thead>
        <tbody>
          <tr><td>Base de las Torres</td><td>1 día (8 a 10 h ida y vuelta)</td><td>Quien tiene poco tiempo y buen estado físico</td><td>Entrada al parque</td></tr>
          <tr><td>Circuito W</td><td>4 a 5 días</td><td>El clásico: glaciar Grey, Valle del Francés y Torres</td><td>Refugios o campings, con anticipación</td></tr>
          <tr><td>Circuito O</td><td>7 a 9 días</td><td>Trekking completo alrededor del macizo, con paso John Gardner</td><td>Refugios o campings, con anticipación</td></tr>
        </tbody>
      </table>
    </div>
    <div class="nota-oficial">Duraciones aproximadas. Para armar el viaje, usá siempre el boletín oficial del parque y confirmá las fechas de apertura de cada temporada.</div>
  </div>

  <!-- QUÉ HACER -->
  <div class="guia-seccion">
    <h2>Qué hacer</h2>

''' + item("torres-del-paine-base-torres-laguna.webp", "Laguna turquesa a los pies de las Torres del Paine, con dos caminantes en la orilla",
    "Base de las Torres", "La postal del parque. Se llega desde el Hotel Las Torres por un sendero de unos 20 km ida y vuelta, que se hace en 8 a 10 horas. El último tramo, una subida por morrena, es el más exigente. Arriba esperan las tres torres de granito sobre una laguna de color turquesa. Para ver el amanecer rojizo hay que dormir en el campamento más cercano a la base y subir de madrugada.") \
 + item("torres-del-paine-torres-lago-atardecer.webp", "Torres del Paine al atardecer con los picos iluminados de rojo sobre la laguna",
    "El circuito W", "La caminata más famosa, en forma de W: glaciar Grey, Valle del Francés con el mirador Británico y la Base de las Torres. Se hace en 4 o 5 días, con refugios o campings en el camino. Muchos empiezan en Paine Grande, adonde se llega en catamarán desde Pudeto, y terminan en la Base de las Torres; también se hace al revés.") \
 + item("torres-del-paine-paso-john-gardner.webp", "Dos caminantes con mochila bajan del paso John Gardner frente al glaciar Grey y el Campo de Hielo Sur",
    "El circuito O y el paso John Gardner", "Es el circuito completo alrededor del macizo Paine: suma el tramo norte del W y cruza el paso John Gardner (más de 1.200 m), con vista al Campo de Hielo Sur. Son 7 a 9 días en lugares mucho menos concurridos. Como el W, exige reservar el alojamiento con anticipación.") \
 + item("torres-del-paine-glaciar-grey.webp", "Frente del glaciar Grey con témpanos azules sobre el lago Grey",
    "Glaciar Grey", "Un frente de hielo azul de más de 6 km sobre el lago Grey, parte del Campo de Hielo Patagónico Sur. Se ve desde los miradores del sendero (unas 3 a 4 horas desde Paine Grande) o navegando hasta el frente. Es el extremo oeste del circuito W.") \
 + item("torres-del-paine-lago-pehoe-atardecer.webp", "Atardecer rosado sobre el lago Pehoé con los Cuernos del Paine reflejados",
    "Lago Pehoé y los Cuernos del Paine", "Para quien no camina varios días: desde el camino principal se llega a los miradores del lago Pehoé y del Salto Grande, con los Cuernos del Paine de fondo. Es la foto clásica del parque y se puede hacer en un día de auto desde Puerto Natales.") \
 + item("torres-del-paine-cuernos-lago.webp", "Los Cuernos del Paine con nieve sobre el lago Nordenskjöld",
    "Los Cuernos y el lago Nordenskjöld", "Entre el Valle del Francés y las Torres, el circuito W bordea el lago Nordenskjöld, con los Cuernos del Paine como telón. Los campamentos de Los Cuernos y Francés quedan sobre este tramo.") \
 + item("torres-del-paine-guanacos.webp", "Dos guanacos en una loma con las agujas de granito del macizo Paine detrás",
    "Fauna: guanacos, cóndores y pumas", "El parque es uno de los mejores lugares del mundo para ver fauna patagónica sin rejas: manadas de guanacos en la estepa, cóndores sobre los acantilados, ñandúes y, con suerte, pumas, sobre todo en las zonas del lago Sarmiento y Laguna Amarga. Mantené siempre la distancia.") \
 + '''  </div>

  <!-- DÓNDE DORMIR -->
  <div class="guia-seccion">
    <h2>Dónde dormir</h2>
    <div class="comer-foto-wrap">
      <img src="../fotos/CIUDADES/torres-del-paine-campamento-arcoiris.webp" alt="Carpas amarillas en un campamento de Torres del Paine con un arcoíris sobre las montañas" loading="lazy"/>
    </div>
    <div class="comer-grid">
      <div class="comer-item">
        <div class="comer-item-body">
          <h4>Refugios y campings del W y del O</h4>
          <div class="comer-dir">Dentro del parque</div>
          <p>Los operan concesionarios privados y CONAF. Para recorrer el W o el O, la reserva anticipada de alojamiento es obligatoria: sin ella no se puede entrar a la zona de montaña.</p>
        </div>
      </div>
      <div class="comer-item">
        <div class="comer-item-body">
          <h4>Refugio Paine Grande</h4>
          <div class="comer-dir">Extremo oeste del Pehoé</div>
          <p>Es el punto de partida del W y de llegada del catamarán. Camas, comidas y camping.</p>
        </div>
      </div>
      <div class="comer-item">
        <div class="comer-item-body">
          <h4>Hotel Las Torres</h4>
          <div class="comer-dir">Acceso a la Base de las Torres</div>
          <p>El hotel más cercano al sendero clásico. Reabrió su temporada el 1 de octubre de 2026.</p>
        </div>
      </div>
      <div class="comer-item">
        <div class="comer-item-body">
          <h4>Hostería Pehoé y Hotel Lago Grey</h4>
          <div class="comer-dir">Lago Pehoé · Lago Grey</div>
          <p>Opciones con camas para quien prefiere dormir bajo techo sin hacer los circuitos.</p>
        </div>
      </div>
      <div class="comer-item" style="grid-column:1/-1;">
        <div class="comer-item-body">
          <h4>Puerto Natales</h4>
          <div class="comer-dir">A unos 110 km del parque</div>
          <p>La base más práctica: hostales, hoteles, restaurantes y tiendas de equipo. Desde ahí salen los buses diarios al parque y se arman excursiones de un día.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- CONSEJOS PRÁCTICOS -->
  <div class="guia-seccion">
    <h2>Consejos prácticos</h2>
    <div class="consejo-grid">
      <div class="consejo-item" style="grid-column:1/-1;">Hacete un control médico antes de viajar y entrená con anticipación: las caminatas del W y del O son exigentes. Mirá el aviso al final de la guía: <strong>Exigencia física y preparación</strong>.</div>
      <div class="consejo-item">Comprá la entrada con anticipación en pasesparques.cl y guardá el QR: se pide en el acceso.</div>
      <div class="consejo-item">Reservá refugios y campings apenas definas las fechas. Para el W y el O es obligatorio, y en verano se agotan con meses de anticipación.</div>
      <div class="consejo-item">El viento puede superar los 100 km/h y el clima cambia en horas. Llevá capas, impermeable y gorro aunque sea verano.</div>
      <div class="consejo-item">Está prohibido hacer fuego fuera de las áreas habilitadas. Los incendios arrasaron el parque en el pasado.</div>
      <div class="consejo-item">Llevá efectivo en pesos chilenos: dentro del parque los pagos con tarjeta no siempre funcionan.</div>
      <div class="consejo-item">Consultá siempre las fuentes oficiales antes de salir: parquetorresdelpaine.cl, conaf.cl y pasesparques.cl. Precios, horarios y fechas de apertura cambian cada temporada.</div>
    </div>
  </div>

  <!-- EXIGENCIA Y PREPARACIÓN -->
  <div class="guia-seccion">
    <h2>Exigencia física y preparación</h2>
    <div class="aviso-salud">
      <h3>⚠️ Antes de reservar, evaluá si estás en condiciones</h3>
      <p>Las caminatas de Torres del Paine son exigentes: son muchas horas por día con mochila, desniveles, terreno de piedra y barro, viento fuerte y clima que cambia rápido. Los servicios médicos están lejos, y un problema de salud en medio del circuito puede complicarse.</p>
      <ul>
        <li><strong>Hacete un control médico completo antes de viajar</strong> y consultá si tu estado de salud es adecuado para caminatas largas y exigentes. Es especialmente importante si tenés problemas cardíacos o de presión, respiratorios, de rodillas o columna, diabetes, o si tomás medicación.</li>
        <li><strong>Entrená con anticipación:</strong> caminatas largas con mochila cargada y escaleras o cuestas durante varias semanas antes del viaje.</li>
        <li><strong>Considerá ir con guía habilitado</strong>, sobre todo si es tu primera caminata de varios días o si vas en invierno, cuando es obligatorio en el W y en la Base de las Torres.</li>
        <li><strong>Contratá un seguro de viaje con cobertura médica y de rescate.</strong> Revisá que incluya actividades de trekking.</li>
        <li><strong>Avisá tu recorrido</strong> a alguien y respetá el cupo y las fechas de tus reservas. Hay zonas con poca o ninguna señal de celular.</li>
        <li><strong>Escuchá a tu cuerpo:</strong> si no te sentís bien, volvé. La montaña no se va.</li>
      </ul>
      <p class="fin">Esta guía es informativa y no reemplaza la opinión de un médico ni de un guía profesional. Cada persona debe evaluar su propio estado y el de quienes viajen con ella.</p>
    </div>
  </div>

  <div class="relacionadas">
    <div class="relacionadas-titulo">También te puede interesar</div>
    <div class="relacionadas-grid">
      <a class="rel-card" href="/notas/guia-calafate.html">
        <img class="rel-img" src="https://globalpatagonia.org/fotos/CIUDADES/Calafate.webp" alt="El Calafate"/>
        <div class="rel-body"><div class="rel-tag">Guías</div><div class="rel-titulo">El Calafate: la puerta al Glaciar Perito Moreno</div></div>
      </a>
      <a class="rel-card" href="/notas/guia-patagonia-argentina-chile.html">
        <img class="rel-img" src="https://globalpatagonia.org/fotos/guia-patagonia-argentina-chile-hero.webp" alt="Patagonia Argentina y Chile"/>
        <div class="rel-body"><div class="rel-tag">Guías</div><div class="rel-titulo">Patagonia Argentina y Chile: cómo visitar los dos países en un viaje</div></div>
      </a>
      <a class="rel-card" href="/notas/guia-ushuaia.html">
        <img class="rel-img" src="https://globalpatagonia.org/fotos/CIUDADES/ushuaia-laguna-esmeralda.webp" alt="Ushuaia"/>
        <div class="rel-body"><div class="rel-tag">Guías</div><div class="rel-titulo">Ushuaia: donde el mundo termina y la aventura empieza</div></div>
      </a>
    </div>
  </div>

  <div class="compartir-bloque" id="compartir-bloque"></div>
  <a href="../#sec-turismo" class="ver-mas">← Más guías en GLOBALpatagonia</a>
</div>

'''
tail = esq[esq.index('<div class="divider-footer">'):]
out = head + hero + tail
open(f"{BASE}/notas/{SLUG}.html", "w", encoding="utf-8").write(out)
print(f"OK notas/{SLUG}.html", len(out))
