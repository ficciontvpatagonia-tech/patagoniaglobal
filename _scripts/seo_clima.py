#!/usr/bin/env python3
"""
seo_clima.py — Inyecta contenido SEO indexable en las páginas clima-CIUDAD.html.

Problema que resuelve: el pronóstico se renderiza por JS (Open-Meteo), así que
Google ve una página casi vacía → posiciones 40-70, casi 0 clics pese a muchas
impresiones. Este script agrega, por ciudad:
  1. Un bloque <section class="clima-seo"> con texto real (clima por estación,
     mejor época, FAQ) → contenido crawleable.
  2. JSON-LD FAQPage → chance de rich results.
  3. Arregla el H1 duplicado (deja un solo H1 visible por página).
  4. Enlace interno a la guía de viaje de la ciudad.

Idempotente: si la página ya tiene el bloque (marca 'clima-seo'), la saltea.
Correr desde la raíz del repo:  python3 _scripts/seo_clima.py
"""
import os, json, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# guía de viaje a la que enlaza cada ciudad (None → guía general Patagonia)
GUIA_GENERAL = ("notas/guia-patagonia-argentina-chile.html", "Guía Patagonia Argentina y Chile")

CITIES = {
    "clima-bariloche.html": {
        "ciudad": "Bariloche", "lugar": "San Carlos de Bariloche, Río Negro (Argentina)",
        "guia": ("notas/guia-bariloche.html", "Guía de viaje de Bariloche"),
        "intro": [
            "Bariloche tiene un <strong>clima templado frío de montaña</strong>, marcado por los Andes patagónicos, los grandes lagos y el bosque andino. Es de los pocos destinos argentinos donde el paisaje y la actividad cambian por completo según la estación: lagos y trekking en verano, bosques dorados en otoño y nieve para esquiar en invierno.",
            "Las temperaturas son suaves en verano y frías en invierno, con viento frecuente del oeste y nevadas entre junio y septiembre. Antes de viajar conviene mirar el pronóstico de los próximos 7 días —arriba en esta misma página— porque el tiempo en la cordillera puede cambiar de un momento a otro.",
        ],
        "estaciones": {
            "☀️ Verano (dic–feb)": "Días templados de 20 a 24 °C y noches frescas cerca de 8–10 °C. Es la mejor época para los lagos, el Circuito Chico y el trekking. Sol fuerte: llevá protección UV.",
            "🍂 Otoño (mar–may)": "Temperaturas de 10 a 15 °C y los bosques de lenga se tiñen de rojo y dorado. Aumentan las lluvias. Temporada tranquila y muy fotogénica.",
            "❄️ Invierno (jun–ago)": "Frío: de 2 a 7 °C de día y bajo cero de noche. Nieve en altura y temporada de esquí en el Cerro Catedral. Llevá abrigo técnico y calzado impermeable.",
            "🌸 Primavera (sep–nov)": "Deshielo y reverdecer del bosque, de 12 a 18 °C, con viento. Buena época para ver cascadas con caudal y evitar las multitudes.",
        },
        "mejor": "La mejor época para visitar Bariloche depende de qué busques: <strong>diciembre a marzo</strong> para lagos, kayak y trekking con días largos; <strong>julio a septiembre</strong> para esquiar en el Cerro Catedral. Otoño y primavera son ideales si preferís precios más bajos y menos gente.",
        "faq": [
            ("¿Qué temperatura hace hoy en Bariloche?", "Arriba en esta página podés ver la temperatura actual y el pronóstico de los próximos 7 días, con datos de los modelos ECMWF y GFS actualizados cada hora."),
            ("¿Cuándo nieva en Bariloche?", "La temporada de nieve va de junio a septiembre, con el pico en julio y agosto. En esos meses funciona el centro de esquí del Cerro Catedral."),
            ("¿Cuál es la mejor época para visitar Bariloche?", "Diciembre a marzo para actividades de verano (lagos y trekking) y julio a septiembre para esquí. Otoño ofrece los bosques dorados con menos turistas."),
            ("¿Hace mucho viento en Bariloche?", "Sí, el viento del oeste es habitual durante todo el año y se intensifica en primavera. En la montaña conviene revisar siempre el pronóstico antes de salir."),
        ],
    },
    "clima-ushuaia.html": {
        "ciudad": "Ushuaia", "lugar": "Ushuaia, Tierra del Fuego (Argentina)",
        "guia": ("notas/guia-ushuaia.html", "Guía de viaje de Ushuaia"),
        "intro": [
            "Ushuaia, la ciudad más austral del mundo, tiene un <strong>clima subpolar oceánico</strong>: fresco durante todo el año, húmedo y muy ventoso. No hay temperaturas extremas, pero el tiempo es cambiante y puede pasar del sol a la lluvia o la nieve en pocas horas, incluso en pleno verano.",
            "El gran contraste no es tanto la temperatura como la luz: en verano los días duran hasta 17 horas y en invierno apenas 7. Antes de salir al Parque Nacional Tierra del Fuego o navegar el Canal Beagle, mirá el pronóstico de 7 días que aparece arriba en esta página.",
        ],
        "estaciones": {
            "☀️ Verano (dic–feb)": "De 9 a 15 °C, días larguísimos y la mejor ventana para navegar el Beagle y hacer trekking. Aun así, llevá abrigo e impermeable: el viento enfría.",
            "🍂 Otoño (mar–may)": "De 4 a 10 °C, bosques de colores y primeras nevadas en altura. Temporada tranquila y luz suave para fotos.",
            "❄️ Invierno (jun–ago)": "De 0 a 5 °C, nieve y días cortos. Temporada de esquí en el Cerro Castor y de actividades sobre nieve.",
            "🌸 Primavera (sep–nov)": "De 3 a 10 °C, viento fuerte y deshielo. Empiezan a alargarse los días y a abrir las excursiones de temporada.",
        },
        "mejor": "La mejor época para visitar Ushuaia es de <strong>noviembre a marzo</strong>, con temperaturas más amables y días largos para navegar el Canal Beagle, recorrer el Parque Nacional y hacer trekking. Para esquí y paisajes nevados, el invierno (julio–agosto) es la temporada.",
        "faq": [
            ("¿Qué temperatura hace hoy en Ushuaia?", "Arriba en esta página podés ver la temperatura actual y el pronóstico de 7 días, con sensación térmica, viento y precipitaciones."),
            ("¿Hace mucho frío en Ushuaia en verano?", "No tanto: en verano ronda los 9 a 15 °C. El frío lo da el viento, así que conviene llevar abrigo y ropa impermeable aunque sea diciembre."),
            ("¿Cuándo nieva en Ushuaia?", "La nieve es habitual de junio a septiembre, cuando funciona el centro de esquí del Cerro Castor. En altura puede nevar incluso fuera del invierno."),
            ("¿Cuál es la mejor época para visitar Ushuaia?", "De noviembre a marzo por el clima más suave y los días largos. El invierno es ideal si buscás nieve y deportes blancos."),
        ],
    },
    "clima-el-calafate.html": {
        "ciudad": "El Calafate", "lugar": "El Calafate, Santa Cruz (Argentina)",
        "guia": ("notas/guia-calafate.html", "Guía de viaje de El Calafate"),
        "intro": [
            "El Calafate tiene un <strong>clima árido de estepa patagónica</strong>: seco, con poca lluvia y mucho viento. Es la puerta de entrada al Glaciar Perito Moreno y al Parque Nacional Los Glaciares, así que el clima define buena parte de la experiencia frente al hielo.",
            "Los veranos son frescos y ventosos y los inviernos fríos, con nevadas ocasionales. El viento del oeste es casi constante. Revisá el pronóstico de 7 días que aparece arriba antes de salir a las pasarelas del glaciar o a navegar entre témpanos.",
        ],
        "estaciones": {
            "☀️ Verano (dic–feb)": "De 15 a 22 °C, días largos y mucho viento. La temporada alta para visitar el Perito Moreno y navegar el Lago Argentino.",
            "🍂 Otoño (mar–may)": "De 6 a 14 °C, menos viento y la estepa con tonos ocres. Temporada de transición, más tranquila.",
            "❄️ Invierno (jun–ago)": "De 0 a 6 °C, con nevadas ocasionales y menos servicios abiertos. El glaciar con nieve alrededor ofrece postales únicas.",
            "🌸 Primavera (sep–nov)": "De 8 a 16 °C y viento fuerte. Reabren las excursiones y crecen las horas de luz.",
        },
        "mejor": "La mejor época para visitar El Calafate es de <strong>octubre a abril</strong>, con días largos y todas las excursiones operativas (pasarelas, minitrekking sobre el hielo y navegación). El verano es alto en gente; primavera y otoño ofrecen buen clima con menos multitudes.",
        "faq": [
            ("¿Qué temperatura hace hoy en El Calafate?", "Arriba en esta página tenés la temperatura actual y el pronóstico de 7 días, con viento y sensación térmica —clave en una zona tan ventosa."),
            ("¿Hace mucho viento en El Calafate?", "Sí. El viento del oeste es casi permanente y puede ser intenso, sobre todo en primavera y verano. Llevá rompevientos para las pasarelas del glaciar."),
            ("¿Cuál es la mejor época para ver el Glaciar Perito Moreno?", "De octubre a abril, con días largos y todas las excursiones operativas. En invierno el entorno nevado es espectacular pero hay menos servicios."),
            ("¿Llueve mucho en El Calafate?", "No: es una zona árida con escasas precipitaciones. El factor a vigilar no es la lluvia sino el viento y la amplitud térmica entre día y noche."),
        ],
    },
    "clima-el-chalten.html": {
        "ciudad": "El Chaltén", "lugar": "El Chaltén, Santa Cruz (Argentina)",
        "guia": ("notas/guia-chalten.html", "Guía de viaje de El Chaltén"),
        "intro": [
            "El Chaltén, la capital nacional del trekking, tiene un <strong>clima de montaña patagónica</strong> muy ventoso y notablemente cambiante. Al pie del Cerro Fitz Roy, el tiempo puede ofrecer sol, viento, lluvia y nieve en un mismo día, incluso en verano.",
            "No hay estación 'mala', pero sí ventanas más estables. Por eso, para subir a la Laguna de los Tres o la Laguna Torre, mirar el pronóstico de 7 días —arriba en esta página— es parte imprescindible de la planificación.",
        ],
        "estaciones": {
            "☀️ Verano (dic–feb)": "De 10 a 18 °C, días largos y la temporada alta del trekking. Aun así el viento puede ser fuerte: llevá capas y rompevientos.",
            "🍂 Otoño (mar–may)": "De 4 a 12 °C, bosques rojizos y senderos más tranquilos. Buena luz para fotografía, con jornadas más cortas.",
            "❄️ Invierno (jun–ago)": "De -2 a 6 °C, nieve y muchos servicios cerrados. Solo para quienes buscan paisaje invernal y experiencia.",
            "🌸 Primavera (sep–nov)": "De 6 a 14 °C, viento muy fuerte y clima inestable. Reabren las excursiones hacia fin de temporada.",
        },
        "mejor": "La mejor época para visitar El Chaltén es de <strong>noviembre a marzo</strong>, cuando el trekking está en plena temporada y los días son largos. Diciembre y febrero suelen dar las ventanas más estables para ver el Fitz Roy despejado, aunque nunca está garantizado.",
        "faq": [
            ("¿Qué temperatura hace hoy en El Chaltén?", "Arriba en esta página podés ver la temperatura actual y el pronóstico de 7 días, fundamental para planificar las caminatas a las lagunas."),
            ("¿Por qué cambia tanto el clima en El Chaltén?", "Por su ubicación al pie de los Andes y la influencia de los campos de hielo: la montaña genera tiempo propio y muy variable, con viento fuerte casi permanente."),
            ("¿Cuál es la mejor época para hacer trekking en El Chaltén?", "De noviembre a marzo. Diciembre y febrero suelen ofrecer las mejores ventanas para ver el Fitz Roy despejado."),
            ("¿Se puede visitar El Chaltén en invierno?", "Sí, pero con muchos servicios cerrados, nieve y días cortos. Es para viajeros experimentados que buscan paisaje invernal."),
        ],
    },
    "clima-neuquen.html": {
        "ciudad": "Neuquén", "lugar": "Neuquén capital (Argentina)",
        "guia": GUIA_GENERAL,
        "intro": [
            "La ciudad de Neuquén tiene un <strong>clima semiárido y seco</strong>, con gran amplitud térmica: veranos calurosos e inviernos fríos, poca lluvia y aire limpio. A diferencia de la cordillera, acá domina la estepa del Alto Valle del río Negro y Limay.",
            "Es una ciudad de servicios y puerta hacia destinos como Vaca Muerta, San Martín de los Andes y la Ruta del Vino patagónica. Para moverte por la región, conviene mirar el pronóstico de 7 días que aparece arriba en esta página.",
        ],
        "estaciones": {
            "☀️ Verano (dic–feb)": "Caluroso y seco, de 30 a 33 °C de máxima. Conviene hidratarse y evitar el sol del mediodía. Noches más frescas.",
            "🍂 Otoño (mar–may)": "Temperaturas agradables de 12 a 22 °C, el Alto Valle con tonos dorados y la cosecha de fruta y vino.",
            "❄️ Invierno (jun–ago)": "Frío y seco, de 2 a 12 °C, con heladas matinales. Cielos despejados y poca nieve en la ciudad.",
            "🌸 Primavera (sep–nov)": "De 14 a 26 °C, viento y la floración de los frutales del Alto Valle. Época muy agradable.",
        },
        "mejor": "La mejor época para visitar Neuquén es <strong>primavera (sep–nov) y otoño (mar–may)</strong>, con temperaturas templadas y paisajes del Alto Valle en su mejor momento. El verano es ideal si tu plan incluye los lagos cordilleranos cercanos.",
        "faq": [
            ("¿Qué temperatura hace hoy en Neuquén?", "Arriba en esta página tenés la temperatura actual y el pronóstico de 7 días para la ciudad de Neuquén y el Alto Valle."),
            ("¿Hace mucho calor en Neuquén en verano?", "Sí: en verano las máximas suelen rondar los 30 a 33 °C, con ambiente seco. Conviene hidratarse bien y evitar la exposición al sol del mediodía."),
            ("¿Nieva en la ciudad de Neuquén?", "Muy poco. El invierno es frío y seco, con heladas frecuentes, pero la nieve en la ciudad es excepcional. La nieve está en la cordillera, más al oeste."),
            ("¿Cuál es la mejor época para visitar Neuquén?", "Primavera y otoño, por el clima templado. El verano sirve si vas a combinar con los lagos y la montaña de la zona andina."),
        ],
    },
    "clima-puerto-madryn.html": {
        "ciudad": "Puerto Madryn", "lugar": "Puerto Madryn, Chubut (Argentina)",
        "guia": GUIA_GENERAL,
        "intro": [
            "Puerto Madryn tiene un <strong>clima árido costero de estepa</strong>: templado, seco y ventoso, con la influencia moderadora del mar. Es la base para visitar Península Valdés y uno de los mejores lugares del mundo para ver fauna marina.",
            "El clima acompaña la temporada de avistaje: la ballena franca austral llega entre junio y diciembre. Antes de salir a la costa o a la península, revisá el pronóstico de 7 días que aparece arriba en esta página, porque el viento condiciona las navegaciones.",
        ],
        "estaciones": {
            "☀️ Verano (dic–feb)": "Caluroso y seco, de 25 a 30 °C, ideal para playa, snorkel y buceo. Mucho sol: llevá protección.",
            "🍂 Otoño (mar–may)": "De 12 a 20 °C, agradable y con menos gente. Empiezan a llegar las primeras ballenas hacia el final.",
            "❄️ Invierno (jun–ago)": "Templado-frío, de 6 a 14 °C. Plena temporada de ballena franca austral en Península Valdés.",
            "🌸 Primavera (sep–nov)": "De 14 a 24 °C, viento fuerte y el pico del avistaje de ballenas, con crías incluidas.",
        },
        "mejor": "La mejor época para visitar Puerto Madryn depende del plan: <strong>junio a diciembre</strong> para el avistaje de ballenas (pico en septiembre–noviembre) y <strong>diciembre a marzo</strong> para playa, buceo y pingüinos. El viento es un factor todo el año.",
        "faq": [
            ("¿Qué temperatura hace hoy en Puerto Madryn?", "Arriba en esta página podés ver la temperatura actual y el pronóstico de 7 días, con viento y sensación térmica."),
            ("¿Cuándo se ven ballenas en Puerto Madryn?", "La ballena franca austral está presente de junio a diciembre, con el pico de avistaje entre septiembre y noviembre en Península Valdés."),
            ("¿Hace mucho viento en Puerto Madryn?", "Sí, el viento es habitual durante todo el año y se intensifica en primavera. Puede afectar las navegaciones de avistaje, así que conviene mirar el pronóstico."),
            ("¿Cuál es la mejor época para ir a la playa en Puerto Madryn?", "El verano (diciembre a marzo), con máximas de 25 a 30 °C, es ideal para playa, snorkel y buceo en Golfo Nuevo."),
        ],
    },
    "clima-punta-arenas.html": {
        "ciudad": "Punta Arenas", "lugar": "Punta Arenas, Magallanes (Chile)",
        "guia": GUIA_GENERAL,
        "intro": [
            "Punta Arenas, a orillas del Estrecho de Magallanes, tiene un <strong>clima subpolar oceánico</strong>: fresco todo el año, húmedo y con uno de los regímenes de viento más intensos de la Patagonia. Es la puerta de entrada a Torres del Paine, la Antártica y la Tierra del Fuego chilena.",
            "Las temperaturas son moderadas pero el viento marca la sensación térmica real. Antes de cruzar a la isla Magdalena (pingüinos) o salir hacia el Paine, mirá el pronóstico de 7 días que aparece arriba en esta página.",
        ],
        "estaciones": {
            "☀️ Verano (dic–feb)": "De 11 a 15 °C, días muy largos y la mejor ventana para excursiones. El viento puede ser fuerte: llevá cortavientos.",
            "🍂 Otoño (mar–may)": "De 6 a 11 °C, colores otoñales y menos turistas. Empieza a bajar la temperatura y a acortarse el día.",
            "❄️ Invierno (jun–ago)": "De 0 a 4 °C, con nieve y días cortos. Temporada baja, ideal para ver el paisaje magallánico nevado.",
            "🌸 Primavera (sep–nov)": "De 4 a 11 °C y viento muy fuerte. Reabren las excursiones y vuelven los pingüinos a la isla Magdalena.",
        },
        "mejor": "La mejor época para visitar Punta Arenas es de <strong>octubre a marzo</strong>, con días largos y todas las excursiones operativas: pingüineras, navegaciones por el Estrecho y conexión con Torres del Paine. El viento es intenso casi todo el año, sobre todo en primavera.",
        "faq": [
            ("¿Qué temperatura hace hoy en Punta Arenas?", "Arriba en esta página tenés la temperatura actual y el pronóstico de 7 días, con viento y sensación térmica —clave en una ciudad tan ventosa."),
            ("¿Por qué hace tanto viento en Punta Arenas?", "Por su ubicación frente al Estrecho de Magallanes, en la zona de los vientos del oeste del extremo sur. El viento es intenso todo el año y máximo en primavera."),
            ("¿Cuándo se pueden ver pingüinos cerca de Punta Arenas?", "De octubre a marzo, cuando la colonia de pingüinos de Magallanes ocupa la isla Magdalena. Las navegaciones operan en esa temporada."),
            ("¿Cuál es la mejor época para visitar Punta Arenas?", "De octubre a marzo, por los días largos y las excursiones operativas hacia Torres del Paine, la isla Magdalena y el Estrecho de Magallanes."),
        ],
    },
    "clima-puerto-montt.html": {
        "ciudad": "Puerto Montt", "lugar": "Puerto Montt, Los Lagos (Chile)",
        "guia": GUIA_GENERAL,
        "intro": [
            "Puerto Montt tiene un <strong>clima oceánico templado lluvioso</strong>: fresco todo el año, muy húmedo y con lluvias frecuentes en casi cualquier estación. A orillas del seno de Reloncaví, es la puerta de entrada a Chiloé, la Carretera Austral y la Patagonia chilena de los lagos y volcanes.",
            "Acá la lluvia es protagonista más que el frío: no hay temperaturas extremas, pero sí muchos días nublados y cambios rápidos. Antes de cruzar a Chiloé o salir hacia Puerto Varas y el Volcán Osorno, revisá el pronóstico de 7 días que aparece arriba en esta página.",
        ],
        "estaciones": {
            "☀️ Verano (dic–feb)": "De 11 a 19 °C, la época más seca y luminosa. La mejor ventana para navegar, recorrer Chiloé y la Carretera Austral. Aun así, llevá impermeable.",
            "🍂 Otoño (mar–may)": "De 8 a 14 °C, vuelven las lluvias y los bosques toman color. Paisajes verdes y menos turistas.",
            "❄️ Invierno (jun–ago)": "De 4 a 10 °C, muy lluvioso y con días cortos. Rara vez nieva en la ciudad; la nieve está en los volcanes cercanos.",
            "🌸 Primavera (sep–nov)": "De 7 a 15 °C, clima inestable que alterna sol y lluvia. Reverdece todo y reabren las excursiones de temporada.",
        },
        "mejor": "La mejor época para visitar Puerto Montt es de <strong>diciembre a marzo</strong>, los meses más secos y de días largos para recorrer Chiloé, Puerto Varas, el Volcán Osorno y la Carretera Austral. El resto del año es verde y hermoso, pero hay que ir preparado para la lluvia.",
        "faq": [
            ("¿Qué temperatura hace hoy en Puerto Montt?", "Arriba en esta página podés ver la temperatura actual y el pronóstico de los próximos 7 días, con lluvia, viento y sensación térmica, datos de los modelos ECMWF y GFS actualizados cada hora."),
            ("¿Llueve mucho en Puerto Montt?", "Sí. Es una de las zonas más lluviosas de Chile, con precipitaciones repartidas casi todo el año. El verano (diciembre a marzo) es la temporada más seca, pero conviene llevar siempre ropa impermeable."),
            ("¿Cuál es la mejor época para visitar Puerto Montt?", "De diciembre a marzo, por ser los meses más secos y de días largos, ideales para Chiloé, Puerto Varas y la Carretera Austral."),
            ("¿Nieva en Puerto Montt?", "En la ciudad la nieve es excepcional: el invierno es lluvioso más que nevado. La nieve aparece en los volcanes y la cordillera cercana."),
        ],
    },
    "clima-comodoro.html": {
        "ciudad": "Comodoro Rivadavia", "lugar": "Comodoro Rivadavia, Chubut (Argentina)",
        "guia": GUIA_GENERAL,
        "intro": [
            "Comodoro Rivadavia tiene un <strong>clima árido frío y extremadamente ventoso</strong>: seco, con poca lluvia y rachas de viento de las más fuertes de la Patagonia. Sobre el Golfo San Jorge, es la principal ciudad petrolera del país y un nudo de servicios del sur de Chubut y norte de Santa Cruz.",
            "El viento del oeste es el rasgo que define el día a día y puede superar los 100 km/h. Las temperaturas son moderadas por el mar, pero la sensación térmica la marca el viento. Antes de salir a la ruta o a la costa, mirá el pronóstico de 7 días que aparece arriba en esta página.",
        ],
        "estaciones": {
            "☀️ Verano (dic–feb)": "De 18 a 26 °C y viento intenso, sobre todo a la tarde. Días largos; buena época para la costa y el Cerro Chenque, siempre con cortavientos.",
            "🍂 Otoño (mar–may)": "De 10 a 18 °C, el viento amaina un poco y baja la temperatura. Temporada más tranquila y luz suave.",
            "❄️ Invierno (jun–ago)": "De 4 a 11 °C, frío seco con heladas y nieve ocasional. Días cortos y viento que acentúa el frío.",
            "🌸 Primavera (sep–nov)": "De 9 a 18 °C y el pico del viento patagónico, con rachas muy fuertes. Vuelven las jornadas largas.",
        },
        "mejor": "La mejor época para visitar Comodoro Rivadavia es <strong>verano (diciembre a marzo)</strong>, con temperaturas templadas y días largos para la costa del Golfo San Jorge y la Reserva Punta del Marqués. El viento es un factor todo el año: conviene revisar siempre el pronóstico.",
        "faq": [
            ("¿Qué temperatura hace hoy en Comodoro Rivadavia?", "Arriba en esta página tenés la temperatura actual y el pronóstico de 7 días, con viento y sensación térmica —clave en una de las ciudades más ventosas del país."),
            ("¿Por qué hace tanto viento en Comodoro Rivadavia?", "Por su ubicación en la costa patagónica, plena zona de los vientos del oeste. Las rachas pueden superar los 100 km/h, sobre todo en primavera y verano."),
            ("¿Cuál es la mejor época para visitar Comodoro Rivadavia?", "El verano (diciembre a marzo), por las temperaturas más templadas y los días largos para recorrer la costa y los museos del petróleo."),
            ("¿Nieva en Comodoro Rivadavia?", "Poco: el invierno es frío y seco, con heladas frecuentes y nevadas ocasionales que no suelen acumular en la ciudad."),
        ],
    },
}

CSS_MARK = "/* ── BLOQUE SEO CLIMA ── */"
CSS_BLOCK = CSS_MARK + """
.clima-seo { max-width:920px; margin:10px auto 40px; padding:0 20px; line-height:1.7; }
.clima-seo h2 { font-family:'Playfair Display',serif; color:var(--verde); font-size:26px; margin:32px 0 16px; }
.clima-seo h3 { font-family:'Playfair Display',serif; color:var(--verde-medio); font-size:19px; margin:24px 0 8px; }
.clima-seo p { color:var(--gris-oscuro); margin-bottom:14px; font-size:16px; }
.clima-estaciones { display:grid; grid-template-columns:repeat(2,1fr); gap:14px; margin:18px 0 8px; }
.ce-card { background:#fff; border:1px solid #e3ddd3; border-radius:12px; padding:16px 18px; }
.ce-card h3 { margin:0 0 6px; font-family:'Inter',sans-serif; font-size:16px; color:var(--verde); }
.ce-card p { margin:0; font-size:14.5px; color:#4a4a4a; }
.clima-faq { margin-top:28px; }
.clima-faq details { background:#fff; border:1px solid #e3ddd3; border-radius:10px; padding:4px 18px; margin-bottom:10px; }
.clima-faq summary { font-weight:600; color:var(--verde); cursor:pointer; padding:12px 0; font-size:15.5px; list-style:none; }
.clima-faq summary::-webkit-details-marker { display:none; }
.clima-faq summary::after { content:'+'; float:right; color:var(--verde-claro); font-size:20px; line-height:1; }
.clima-faq details[open] summary::after { content:'–'; }
.clima-faq details p { padding:0 0 14px; margin:0; font-size:15px; color:#4a4a4a; }
.clima-guia-link { display:inline-block; margin-top:18px; background:var(--verde); color:#fff; text-decoration:none; padding:12px 22px; border-radius:999px; font-weight:600; font-size:15px; }
.clima-guia-link:hover { background:var(--verde-medio); }
@media(max-width:640px){ .clima-estaciones{ grid-template-columns:1fr; } .clima-seo h2{ font-size:22px; } }
"""


def build_section(c):
    est = "".join(
        f'\n      <div class="ce-card"><h3>{k}</h3><p>{v}</p></div>'
        for k, v in c["estaciones"].items()
    )
    faq = "".join(
        f'\n      <details><summary>{q}</summary><p>{a}</p></details>'
        for q, a in c["faq"]
    )
    intro = "".join(f'\n    <p>{p}</p>' for p in c["intro"])
    guia_href, guia_txt = c["guia"]
    return f"""
<!-- clima-seo: contenido indexable (generado por _scripts/seo_clima.py) -->
<section class="clima-seo">
    <h2>El clima en {c['ciudad']}: qué esperar todo el año</h2>{intro}
    <h3>El clima de {c['ciudad']} estación por estación</h3>
    <div class="clima-estaciones">{est}
    </div>
    <h3>¿Cuál es la mejor época para visitar {c['ciudad']}?</h3>
    <p>{c['mejor']}</p>
    <div class="clima-faq">
      <h2>Preguntas frecuentes sobre el clima en {c['ciudad']}</h2>{faq}
    </div>
    <a class="clima-guia-link" href="{guia_href}">📖 {guia_txt} →</a>
</section>
"""


def build_jsonld(c):
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in c["faq"]
        ],
    }
    data = json.dumps(faq, ensure_ascii=False, indent=2)
    return f'\n  <script type="application/ld+json">\n{data}\n  </script>\n'


def process(path, c):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    if "clima-seo" in html:
        return "ya tenía bloque — saltada"

    # 1. arreglar H1 duplicado: el sr-only del header pasa a <p>
    html = html.replace(
        '<h1 class="sr-only">GLOBALpatagonia — El Tiempo en la Patagonia</h1>',
        '<p class="sr-only">GLOBALpatagonia — El Tiempo en la Patagonia</p>',
    )

    # 2. JSON-LD antes de </head>
    html = html.replace("</head>", build_jsonld(c) + "</head>", 1)

    # 3. sección de contenido antes de <footer>
    html = html.replace("<footer>", build_section(c) + "\n<footer>", 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return "OK"


def ensure_css():
    css_path = os.path.join(ROOT, "clima.css")
    with open(css_path, encoding="utf-8") as f:
        css = f.read()
    if CSS_MARK in css:
        return "CSS ya presente"
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + CSS_BLOCK)
    return "CSS agregado a clima.css"


if __name__ == "__main__":
    print(ensure_css())
    for fname, c in CITIES.items():
        path = os.path.join(ROOT, fname)
        if not os.path.exists(path):
            print(f"  {fname:<28} NO EXISTE")
            continue
        print(f"  {fname:<28} {process(path, c)}")
    print("\nListo. Revisá una página en el navegador antes de pushear.")
