#!/usr/bin/env python3
import json, os

BASE = "/Users/jm/Desktop/CLAUDCODE/GLOBAL PATAGONIA"
PROPIOS = f"{BASE}/propios.json"
HISTORIAL = f"{BASE}/propios_historial.json"
MAX_ACTIVOS = 7

cuerpo = (
    "<h3>Una obra que redefine el mapa patagónico</h3>\n\n"
    "El Puente Chacao es la obra vial más ambiciosa de la historia de Chile. Sus 2,75 kilómetros de longitud se dividen en dos vanos principales: 1.155 metros del lado de Chiloé y 1.055 metros del lado continental, con un vano central libre de 300 metros sobre el canal. Su gálibo de 54,9 metros sobre la marea media garantizará el paso sin restricciones de grandes embarcaciones por el Canal de Chacao, una de las vías marítimas más activas del sur austral.\n\n"
    "Según el Ministerio de Obras Públicas de Chile, la obra registra un avance del 63% a febrero de 2026 y su inauguración está prevista para octubre de 2028. Una vez terminado, la Ruta 5 quedará unida de forma ininterrumpida desde Arica hasta Quellón, integrando definitivamente al archipiélago con el resto del territorio nacional. El costo total del proyecto ronda los 1.100 millones de dólares.\n\n"
    "<h3>De 50 minutos de ferry a tres minutos de puente</h3>\n\n"
    "El cambio más concreto y palpable para los isleños será la eliminación del transbordador como único vínculo con el continente. Hoy, el cruce del Canal de Chacao demanda cerca de 50 minutos de travesía, más largas esperas que en temporada alta —verano austral y vacaciones de invierno— pueden extenderse entre dos y tres horas, sujetas al clima, las mareas y la capacidad operativa de los ferries. El puente reducirá ese recorrido a apenas tres minutos, disponibles las 24 horas, los 365 días del año.\n\n"
    "Para las familias de Chiloé, la conexión permanente significa poder trasladar a un paciente al hospital del continente sin depender de las mareas, acceder a la educación superior sin planificar el horario de los barcos y recibir insumos básicos en plena tormenta patagónica. El puente no es solo infraestructura: es la posibilidad de vivir mejor sin tener que emigrar.\n\n"
    "<h3>El corredor que también transforma la Patagonia argentina</h3>\n\n"
    "El impacto del Puente Chacao no se detiene en la orilla chilena. Para la Patagonia argentina, la obra abre una dimensión nueva en el corredor bioceánico del sur: por primera vez, la Ruta 5 chilena llegará por tierra hasta Quellón, en el extremo sur de la Isla Grande, completando un eje vial que une el Atlántico con el Pacífico sin interrupciones. Eso significa rutas comerciales más directas, mayor fluidez para el turismo binacional y una revalorización de los pasos fronterizos patagónicos.\n\n"
    "Para las provincias de Neuquén, Río Negro y Chubut, el puente potencia la integración regional que hace décadas los gobiernos de ambos países vienen impulsando. Los productos patagónicos argentinos —lana, frutos, madera, hidrocarburos— tendrán un corredor más fluido hacia los puertos del Pacífico. En términos geopolíticos, el sur austral dejará de ser una periferia para afirmarse como un nodo estratégico de conectividad continental.\n\n"
    "<h3>El despegue económico que espera Chiloé</h3>\n\n"
    "En lo económico, la conexión terrestre potenciará el turismo, uno de los motores de la isla. Se proyecta que el flujo de visitantes se duplique, impulsando la creación de hoteles, restaurantes y servicios. Los productos locales —pescados, mariscos, lácteos y artesanías— podrán salir más rápido y a menor costo hacia los mercados del norte. Empresarios de la zona comparan el potencial impacto con el que tuvo la construcción del aeropuerto de Mocopulli, pero a una escala incomparablemente mayor.\n\n"
    "<h3>Las voces que piden cuidar la \"isla interior\"</h3>\n\n"
    "No todos celebran la conexión con el mismo entusiasmo. En Chiloé convive una resistencia callada pero constante, articulada en torno a preguntas que el entusiasmo oficial no siempre responde: ¿qué Chiloé llegará al otro lado del puente?\n\n"
    "<div style=\"background:#fff8f2;border-left:4px solid #8c6b4a;border-radius:0 6px 6px 0;padding:16px 20px;margin:20px 0;font-size:15px;line-height:1.7\">"
    "<strong style=\"color:#8c6b4a\">Fauna marina bajo presión.</strong> El Canal de Chacao es uno de los corredores de alimentación más importantes de la ballena azul en el Pacífico Sur. Organizaciones ambientales y científicos de la Universidad Austral de Chile advirtieron que las vibraciones del tráfico permanente y la alteración de las corrientes submarinas por los pilotes podrían afectar los patrones de migración de cetáceos, delfines y lobos marinos que habitan el canal. El Servicio de Evaluación Ambiental exigió planes de monitoreo, pero los ecologistas consideran que son insuficientes."
    "</div>\n\n"
    "<div style=\"background:#fff8f2;border-left:4px solid #8c6b4a;border-radius:0 6px 6px 0;padding:16px 20px;margin:20px 0;font-size:15px;line-height:1.7\">"
    "<strong style=\"color:#8c6b4a\">Comunidades Huilliche: territorio e identidad.</strong> Los pueblos originarios de Chiloé señalaron que el trazado del puente y las obras de acceso atraviesan zonas con significado cultural y espiritual para sus comunidades. Organizaciones como el Consejo de Caciques de Chiloé demandaron una consulta indígena más amplia, argumentando que el Estado cumplió el trámite pero no el espíritu del Convenio 169 de la OIT. Sus inquietudes sobre el impacto en la pesca artesanal y en territorios ancestrales nunca fueron resueltas del todo."
    "</div>\n\n"
    "<div style=\"background:#fff8f2;border-left:4px solid #8c6b4a;border-radius:0 6px 6px 0;padding:16px 20px;margin:20px 0;font-size:15px;line-height:1.7\">"
    "<strong style=\"color:#8c6b4a\">El miedo a la \"continentalización\".</strong> Escritores, artistas y activistas chilenos temen lo que algunos llaman la \"continentalización\" de la isla: la llegada masiva de cadenas comerciales, el encarecimiento del suelo que expulsa a los residentes históricos y la dilución de la cultura local —la mitología del Trauco y la Pincoya, la arquitectura de tejuelas, la gastronomía del curanto— bajo la presión del turismo masivo. \"No queremos convertirnos en otro Puerto Montt\", es la frase que resume ese temor. La especulación inmobiliaria ya es visible: el precio de los terrenos en Ancud y Castro aumentó significativamente desde que el proyecto fue confirmado."
    "</div>\n\n"
    "<div style=\"background:#fff8f2;border-left:4px solid #8c6b4a;border-radius:0 6px 6px 0;padding:16px 20px;margin:20px 0;font-size:15px;line-height:1.7\">"
    "<strong style=\"color:#8c6b4a\">Los trabajadores del ferry.</strong> Las empresas de transbordadores emplean directamente a cientos de familias en Pargua y en Chacao. Cuando el puente entre en operaciones, los ferries perderán la mayor parte de su carga. Los gremios de trabajadores han pedido al gobierno planes de reconversión laboral concretos, pero hasta ahora las respuestas han sido genéricas. Es la herida más silenciosa que dejará la obra."
    "</div>\n\n"
    "El gobierno ha respondido a estas preocupaciones con planes de ordenamiento territorial, regulaciones de protección de humedales y compromisos de monitoreo ambiental. Pero para muchos en el archipiélago, la pregunta central sigue en el aire: ¿quién diseñó el Chiloé del otro lado del puente?\n\n"
    "<h3>Los desafíos que marcaron el camino</h3>\n\n"
    "En 2019, el consorcio constructor liderado por Hyundai solicitó un pago adicional de 300 millones de dólares; tras una tensa negociación, el Estado chileno acordó en 2020 un desembolso extra de 138,5 millones, muy por debajo de lo pedido. Las condiciones extremas del Canal de Chacao —fuertes corrientes, vientos huracanados y mareas que desafían cualquier ingeniería— también obligaron a reprogramar plazos: la fecha original de 2020 se corrió varias veces, y hoy el cronograma oficial apunta a octubre de 2028, con estimaciones conservadoras que extienden la posibilidad hasta 2030.\n\n"
    "<h3>Un puente que mira al futuro</h3>\n\n"
    "Cuando en 2028 se corte la cinta inaugural, Chiloé dejará de ser una isla en el sentido geográfico, pero seguirá siendo el mismo territorio de mitos, curantos y cultura única. Solo que ahora con una conexión firme al resto del país —y con el sur de la Patagonia argentina un poco más cerca también. Las controversias, los sobrecostos y las demoras no pudieron frenar un avance que ya supera el sesenta por ciento. Es el símbolo de cómo la región austral encara proyectos monumentales para unir a su gente, aprendiendo de los obstáculos del camino. Y esa es, sin duda, una buena noticia para toda la Patagonia."
)

nueva_entrada = {
    "id": "20260531-propio-puente-chacao",
    "titulo": "Chiloé dejará de ser isla: el megapuente que une el sur de Chile de punta a punta",
    "bajada": "Después de más de medio siglo de sueños postergados, el Puente Chacao avanza hacia su inauguración en 2028. Con 2,75 kilómetros de longitud y un gálibo de 54,9 metros, transformará un cruce de 50 minutos en ferry en apenas tres minutos de puente — y pondrá fin a siglos de aislamiento geográfico del archipiélago más austral de Chile.",
    "cuerpo": cuerpo,
    "tag": "🌉 Infraestructura",
    "categoria": "infraestructura|chile|patagonia",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "chile",
    "imagen": "fotos/CIUDADES/puente-chacao-render.webp",
    "imagen_keywords": "puente chacao chiloé canal infraestructura chile patagonia",
    "meta": "31 de Mayo de 2026 · J. Martineau",
    "excluir_feed": True,
    "galeria": [
        "fotos/CIUDADES/puente-chacao-obra.webp",
        "fotos/CIUDADES/puente-chacao-infografia.webp"
    ]
}

with open(PROPIOS, "r", encoding="utf-8") as f:
    propios = json.load(f)

with open(HISTORIAL, "r", encoding="utf-8") as f:
    historial = json.load(f)

# Si ya hay MAX_ACTIVOS, mover el más antiguo al historial
if len(propios) >= MAX_ACTIVOS:
    mas_antiguo = propios.pop()  # último = más antiguo
    historial.insert(0, mas_antiguo)
    print(f"Movido al historial: {mas_antiguo['id']}")

# Insertar nuevo al inicio
propios.insert(0, nueva_entrada)
print(f"Nuevo informe en propios[0]: {nueva_entrada['id']}")
print(f"Total activos: {len(propios)}")

with open(PROPIOS, "w", encoding="utf-8") as f:
    json.dump(propios, f, ensure_ascii=False, indent=2)

with open(HISTORIAL, "w", encoding="utf-8") as f:
    json.dump(historial, f, ensure_ascii=False, indent=2)

print("OK — propios.json y propios_historial.json actualizados.")
