#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publica el informe 'Datacenters en Patagonia' en propios.json (+ rota el más viejo)."""
import json, os

BASE = "/Users/jm/Desktop/CLAUDCODE/GLOBAL PATAGONIA"
PROPIOS = f"{BASE}/propios.json"
HISTORIAL = f"{BASE}/propios_historial.json"
MAX_ACTIVOS = 7

DATELINE = '<p style="font-size:.85rem;letter-spacing:.05em;text-transform:uppercase;color:#7aadcc;font-weight:600;margin-bottom:1.2rem">{txt}</p>'

VIDEO1 = '<div style="margin:2rem 0"><iframe width="100%" height="400" src="https://www.youtube.com/embed/r473fEO-ojg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius:6px"></iframe></div>'
VIDEO2 = '<div style="margin:2rem 0"><iframe width="100%" height="400" src="https://www.youtube.com/embed/MoFKsFuCdsE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius:6px"></iframe></div>'

def fig(src, cap, alt):
    return (f'<figure style="margin:2.2rem 0"><img src="{src}" alt="{alt}" '
            f'style="width:100%;border-radius:6px;display:block">'
            f'<figcaption style="font-size:.85rem;color:#8c6b4a;margin-top:.5rem">{cap}</figcaption></figure>')

def statbox(title, rows, source):
    tr = "".join(
        f'<tr style="border-bottom:1px solid rgba(122,173,204,.22)"><td style="padding:.6rem 0;opacity:.82">{k}</td>'
        f'<td style="padding:.6rem 0;text-align:right;font-weight:600">{v}</td></tr>'
        for k, v in rows)
    return (f'<div style="background:#1c2d3d;color:#f0ede8;border-radius:8px;padding:1.4rem 1.7rem;margin:2.3rem 0">'
            f'<div style="font-family:\'Playfair Display\',serif;font-size:1.15rem;font-weight:700;color:#7aadcc;margin-bottom:.9rem">{title}</div>'
            f'<table style="width:100%;border-collapse:collapse;font-size:1rem">{tr}</table>'
            f'<div style="font-size:.78rem;opacity:.6;margin-top:.9rem">{source}</div></div>')

# ════════════════════════════════════════════════ ESPAÑOL
cuerpo_es = "\n\n".join([
DATELINE.format(txt="Neuquén, Patagonia — 29 de junio de 2026"),
'<p>El <strong>10 de octubre de 2025</strong>, a quince días de las elecciones de medio término, el gobierno de Javier Milei celebró con bombos y platillos lo que presentó como la mayor inversión tecnológica de la historia argentina: <strong>OpenAI</strong>, la creadora de ChatGPT, y la empresa local <strong>Sur Energy</strong> habían firmado una carta de intención para levantar un mega datacenter de inteligencia artificial en la Patagonia. Lo bautizaron <strong>"Stargate Argentina"</strong>.</p>',
'<p>La cifra era de las que cambian una conversación: hasta <strong>US$ 25.000 millones</strong> de inversión y una capacidad de <strong>500 megavatios</strong> (MW). Para dimensionarlo, el mayor centro de datos de América Latina, en San Pablo, tiene 61 MW; y los 45 datacenters que hoy funcionan en todo el país, sumados, no llegan a esa potencia. Sam Altman, CEO de OpenAI, lo difundió en un video: "Estamos orgullosos de anunciar los planes para lanzar Stargate Argentina". El proyecto entraría al RIGI, el régimen de beneficios fiscales por 30 años que Milei lanzó en 2024.</p>',
'<p>Ocho meses después, ese anuncio sigue siendo apenas eso: un anuncio. <strong>No se presentó formalmente, no tiene ubicación definitiva, ni plazos ni montos confirmados.</strong> El propio Ministerio de Economía reconoció que no hay nada que respalde la declaración de intención. Darío Clemente, investigador del CONICET y del Observatorio del RIGI de la fundación FARN, lo resume sin vueltas: de los 17 proyectos aprobados y 23 en evaluación bajo el régimen, <strong>ninguno es Stargate</strong>. "No hay información actualizada confiable más allá de aquel anuncio electoral", señala. Las versiones más optimistas hablan de empezar a construir recién en 2027.</p>',
VIDEO1,
'<h3>Lo que sí avanzó: el "Súper RIGI" ya tiene media sanción</h3>',
'<p>Aunque el datacenter no se concretó, el anuncio cumplió su función política: cambió la escala de la discusión y habilitó un nuevo marco legal. La madrugada del <strong>miércoles 24 de junio de 2026</strong> —apenas días atrás— la Cámara de Diputados le dio <strong>media sanción al "Súper RIGI"</strong> por <strong>130 votos a favor, 106 en contra y 7 abstenciones</strong>. Ahora la iniciativa espera al Senado para convertirse en ley.</p>',
'<p>El régimen apunta de lleno a las "industrias del futuro": <strong>inteligencia artificial, centros de datos, baterías de litio, paneles solares, turbinas eólicas y la cadena de valor del uranio</strong>. Y ofrece beneficios excepcionales: una alícuota de Ganancias del <strong>15%</strong>, estabilidad tributaria, aduanera y cambiaria por <strong>30 años</strong>, exenciones a la importación, amortización acelerada, baja de contribuciones patronales y libre disponibilidad de divisas que llega al 100% desde el tercer año. Elimina, además, la obligación de contratar proveedores locales que el RIGI original fijaba en 20%, y habilita a las empresas a demandar al país ante el <strong>CIADI</strong> si el Estado cambia las reglas.</p>',
'<p>El abogado Pablo Cerdan fue tajante: "Es la ley de datacenters. Energía y trabajo subsidiado para grandes tecnológicas que facturan más que el PBI argentino y van a pagar menos impuestos que una pyme del conurbano".</p>',
'<h3>¿Por qué la Patagonia?</h3>',
'<p>La elección no es casual. La investigación del <strong>Pulitzer Center</strong>, en alianza con Chequeado, identifica cuatro razones: tierra disponible, energía barata, acceso a agua y bajas temperaturas que abaratan el enfriamiento. En noviembre de 2025, el gobierno neuquino presentó una "microrregión" tecnológica que se extiende desde la zona de Vaca Muerta —Añelo y Tratayén— hasta el río Limay, en la localidad de Arroyito, cerca de la represa El Chocón. Rubén Etcheverry, del Consejo de Planificación de Neuquén, lo vende como un "microclima ideal para industrias tecnológicas".</p>',
'<p>El suministro está encaminado: <strong>Sur Energy</strong> ya firmó acuerdos con Genneia —la mayor generadora renovable del país— y Central Puerto. La empresa, fundada por Emiliano Kargieman (también CEO de Satellogic, la firma de nanosatélites que cotiza en Wall Street) y el fallecido Mat Travizano, sería la desarrolladora de la infraestructura, mientras OpenAI se compromete a comprar toda la potencia de cómputo <strong>sin poner un dólar en la construcción</strong>.</p>',
fig("fotos/datacenter-ia-racks.webp",
    "El corazón de la máquina: pasillos de servidores que demandan energía y agua las 24 horas. El cuello de botella de la IA ya no es el chip, sino la electricidad que lo alimenta. <em>(Foto de referencia)</em>",
    "Interior de un datacenter: pasillos de servidores con refrigeración"),
'<h3>La sed digital: lo que no se anuncia</h3>',
'<p>Detrás del brillo del cómputo hay una huella física enorme. Según estimaciones usadas para Estados Unidos, un datacenter necesita <strong>7,1 m³ de agua por cada MWh</strong> consumido —contando uso directo e indirecto en la generación eléctrica—, lo que equivale a <strong>más de 2,5 millones de litros al año por cada megavatio</strong> de potencia. Llevado a Stargate: un centro de <strong>500 MW consume agua y electricidad equivalentes a las de una ciudad mediana</strong>. A escala global, los datacenters ya se llevan el 1,5% de la electricidad del planeta (unos 415 TWh en 2024), y la demanda se duplicaría hacia 2030.</p>',
statbox("La huella de un datacenter de 500 MW",
        [("Agua por MWh consumido", "7,1 m³"),
         ("Agua al año por cada MW", "+2,5 millones de litros"),
         ("Consumo de un centro de 500 MW", "≈ una ciudad mediana"),
         ("Datacenters en el mundo (2024)", "1,5% de la electricidad global")],
        "Datos: Pulitzer Center / Chequeado"),
'<p>El problema es <em>dónde</em> caería esa sed. En la región de Vaca Muerta, donde cada pozo de fracking puede consumir hasta 60.000 m³ de agua al año y en 2025 ya había 17.300 pozos —más de 1.038 millones de m³ en total—, el recurso hídrico está bajo presión. Allí se registran unos 56 incidentes ambientales por día; el último derrame, en el lago Mari Menuco, afectó 50.000 m². A una región exprimida por el petróleo, ahora se le sumaría una nueva sed: la digital.</p>',
'<h3>Unblock: el enclave que ya existe</h3>',
'<p>No hace falta imaginar el futuro. Entre Rincón de los Sauces y Añelo ya funciona <strong>Unblock</strong>, un datacenter de <strong>27 MW</strong> que proyecta duplicar su capacidad… y que emplea a unas <strong>20 personas</strong>. Es la radiografía perfecta de lo que los especialistas llaman "economías de enclave": mucha energía, mucha inversión, casi ningún empleo permanente. Su CEO, Tomás Ocampo, lo plantea con crudeza: "El futuro de la IA estará condicionado por el costo de la energía".</p>',
fig("fotos/datacenter-anelo-vaca-muerta.webp",
    "Añelo, corazón de Vaca Muerta: instalaciones industriales sobre la estepa y el cartel que da la bienvenida al pueblo que ya conoce el precio de las grandes inversiones. Aquí ya opera el primer enclave de cómputo.",
    "Instalación industrial sobre la estepa neuquina y el cartel de bienvenida a Añelo"),
'<p>Y OpenAI no es la única que mira al sur. Según reveló Infobae, Tesla, de Elon Musk, también evalúa un datacenter en el país de la mano de YPF Luz; y el gobierno ya recibió a ejecutivos de Google, Meta y Apple. La Patagonia se volvió, de pronto, la góndola energética del mundo.</p>',
'<h3>La zona de sacrificio</h3>',
'<p>Mientras los gobiernos celebran, las comunidades miran con preocupación. Liliana Romero, lonko de la comunidad mapuche Fvta Trayén, en Añelo, resume el clima: "Ya no tenemos la misma tranquilidad. Acá hay mucha contaminación". El werkén Diego Rosales va más lejos y describe la dependencia que ya impone la industria: "Dependemos de pedirle agua a la industria". Y Lefxaru Nawel, vocero mapuche de Neuquén, denuncia el método: las comunidades se enteran de los proyectos "cuando ya entran a los territorios, cuando están licitadas las obras, ilegalmente autorizadas, sin hacer una consulta".</p>',
'<p>La investigadora Irina Sternik lo llama <strong>"zonas de sacrificio digital"</strong>: territorios socialmente excluidos donde se descargan infraestructuras de altísimo costo ambiental, sin actores con peso político que las frenen. Para Alan Rocha, del Observatorio Petrolero Sur, el RIGI es justamente un marco "regresivo en términos de control ambiental".</p>',
VIDEO2,
'<h3>El vacío que todos los vecinos ya llenaron</h3>',
'<p>El dato más alarmante es regulatorio: <strong>Argentina no tiene normas específicas —comerciales, impositivas ni ambientales— para este tipo de infraestructura</strong>. El único marco es el RIGI, que otorga beneficios y prioridad en el uso de recursos, pero no fija contrapesos. La propia Secretaría de Ambiente de Neuquén lo admite: "De momento, no hay normativas específicas".</p>',
'<p>El contraste con la región es elocuente. <strong>Brasil</strong> sancionó en 2025 su régimen Redata, que combina incentivos con exigencias de sostenibilidad: 100% de energía limpia, eficiencia hídrica y compromisos de investigación. <strong>Chile</strong> tiene un Plan Nacional de Data Centers 2024-2030 orientado a renovables e integración territorial. En el ranking latinoamericano por cantidad de centros de datos, Argentina es <strong>cuarta</strong>, detrás de Brasil, Chile y México: los vecinos ya regulan; acá todavía no hay con qué.</p>',
'<p>Y la promesa económica, por ahora, no aparece ni siquiera para el sector privado local. Fernando Zurita, titular de la Federación de Entidades Empresarias de Neuquén, lo dice sin militancia: "Aún no se produjo un impacto económico real y tangible". Afuera, las señales de alerta se multiplican: en Estados Unidos, Erin Brockovich lanzó una plataforma para mapear datacenters y Bernie Sanders pidió una "pausa"; en Paraguay, la localidad de Villarrica lleva años peleando contra una granja de criptominería que consumió en seis meses lo que 47.464 familias gastarían en un año.</p>',
'<h3>La pregunta que queda</h3>',
'<p>Como plantea Bea Busaniche, de la Fundación Vía Libre, el dilema no es <em>datacenter sí o no</em>, sino <strong>datacenter cómo y para quién</strong>. Cualquier país que quiera desarrollar tecnología necesita capacidad de cómputo. La pregunta es si esa capacidad se construye con regulación, consulta a las comunidades y beneficios compartidos, o si se instala como un nuevo enclave extractivista, con el agua y la energía de la Patagonia como moneda de cambio por la promesa —todavía incierta— del progreso digital.</p>',
'<p>Por ahora hay un anuncio que no se concretó y una ley a un paso del Senado. El espejismo de los datos sigue brillando en el horizonte patagónico. Falta saber si, cuando llegue, traerá agua o sólo más sed.</p>',
])

# ════════════════════════════════════════════════ ENGLISH
cuerpo_en = "\n\n".join([
DATELINE.format(txt="Neuquén, Patagonia — June 29, 2026"),
'<p>On <strong>October 10, 2025</strong>, fifteen days before the midterm elections, Javier Milei\'s government trumpeted what it billed as the largest technology investment in Argentine history: <strong>OpenAI</strong>, the maker of ChatGPT, and the local firm <strong>Sur Energy</strong> had signed a letter of intent to build a mega AI data center in Patagonia. They named it <strong>"Stargate Argentina."</strong></p>',
'<p>The numbers were the kind that change a conversation: up to <strong>US$25 billion</strong> in investment and a capacity of <strong>500 megawatts</strong> (MW). For scale, Latin America\'s largest data center, in São Paulo, runs at 61 MW; and the 45 data centers operating across the country today do not, combined, reach that figure. OpenAI CEO Sam Altman put out a video: "We are proud to announce plans to launch Stargate Argentina." The project would enter the RIGI, the 30-year tax-incentive regime Milei launched in 2024.</p>',
'<p>Eight months on, that announcement is still just that: an announcement. <strong>It was never formally filed, has no definitive location, and no confirmed timeline or figures.</strong> The Economy Ministry itself acknowledged there is nothing backing the declaration of intent. Darío Clemente, a researcher at CONICET and at the RIGI Observatory of the FARN foundation, sums it up bluntly: of the 17 approved projects and 23 under review in the regime, <strong>none is Stargate</strong>. "There is no reliable updated information beyond that electoral announcement," he says. The most optimistic versions speak of breaking ground only in 2027.</p>',
VIDEO1,
'<h3>What did move forward: the "Super RIGI" already has half-sanction</h3>',
'<p>Even though the data center never materialized, the announcement served its political purpose: it shifted the scale of the debate and opened the door to a new legal framework. In the early hours of <strong>Wednesday, June 24, 2026</strong> —just days ago— the Chamber of Deputies granted <strong>half-sanction to the "Super RIGI"</strong> by <strong>130 votes in favor, 106 against and 7 abstentions</strong>. The bill now awaits the Senate to become law.</p>',
'<p>The regime takes direct aim at the "industries of the future": <strong>artificial intelligence, data centers, lithium batteries, solar panels, wind turbines and the uranium value chain</strong>. And it offers exceptional benefits: a <strong>15%</strong> income-tax rate, tax, customs and foreign-exchange stability for <strong>30 years</strong>, import exemptions, accelerated depreciation, lower payroll contributions, and free availability of foreign currency reaching 100% from the third year. It also scraps the obligation to hire local suppliers that the original RIGI set at 20%, and lets companies sue the country before <strong>ICSID</strong> if the State changes the rules.</p>',
'<p>Lawyer Pablo Cerdan was blunt: "It\'s the data-center law. Subsidized energy and labor for big tech firms that bill more than Argentina\'s GDP and will pay less tax than a small business in the suburbs."</p>',
'<h3>Why Patagonia?</h3>',
'<p>The choice is no accident. The investigation by the <strong>Pulitzer Center</strong>, in partnership with Chequeado, identifies four reasons: available land, cheap energy, access to water, and low temperatures that cut cooling costs. In November 2025, the Neuquén government unveiled a tech "micro-region" stretching from the Vaca Muerta area —Añelo and Tratayén— to the Limay River, in the town of Arroyito, near the El Chocón dam. Rubén Etcheverry, of Neuquén\'s Planning Council, sells it as an "ideal microclimate for technology industries."</p>',
'<p>Supply is already lined up: <strong>Sur Energy</strong> has signed deals with Genneia —the country\'s largest renewable generator— and Central Puerto. The company, founded by Emiliano Kargieman (also CEO of Satellogic, the nanosatellite firm listed on Wall Street) and the late Mat Travizano, would develop the infrastructure, while OpenAI commits to buying all the computing power <strong>without putting a single dollar into construction</strong>.</p>',
fig("fotos/datacenter-ia-racks.webp",
    "The heart of the machine: server aisles that demand power and water around the clock. The bottleneck of AI is no longer the chip, but the electricity that feeds it. <em>(Stock photo)</em>",
    "Inside a data center: server aisles with cooling"),
'<h3>The digital thirst: what the announcement leaves out</h3>',
'<p>Behind the shine of computing lies an enormous physical footprint. According to estimates used for the United States, a data center needs <strong>7.1 m³ of water per MWh</strong> consumed —counting direct use and indirect use in power generation— equal to <strong>more than 2.5 million liters per year for every megawatt</strong> of capacity. Applied to Stargate: a <strong>500 MW facility consumes water and electricity equivalent to a mid-sized city</strong>. Globally, data centers already take 1.5% of the planet\'s electricity (about 415 TWh in 2024), and demand is set to double by 2030.</p>',
statbox("The footprint of a 500 MW data center",
        [("Water per MWh consumed", "7.1 m³"),
         ("Water per year for each MW", "+2.5 million liters"),
         ("Consumption of a 500 MW facility", "≈ a mid-sized city"),
         ("Data centers worldwide (2024)", "1.5% of global electricity")],
        "Source: Pulitzer Center / Chequeado"),
'<p>The problem is <em>where</em> that thirst would land. In the Vaca Muerta region —where each fracking well can use up to 60,000 m³ of water a year and by 2025 there were already 17,300 wells, more than 1.038 billion m³ in total— water is under strain. The area logs some 56 environmental incidents a day; the latest spill, at Lake Mari Menuco, affected 50,000 m². To a region already squeezed by oil, a new thirst would now be added: the digital one.</p>',
'<h3>Unblock: the enclave that already exists</h3>',
'<p>There is no need to imagine the future. Between Rincón de los Sauces and Añelo, <strong>Unblock</strong> already operates —a <strong>27 MW</strong> data center planning to double its capacity… and employing some <strong>20 people</strong>. It is the perfect snapshot of what specialists call "enclave economies": lots of energy, lots of investment, almost no permanent jobs. Its CEO, Tomás Ocampo, puts it bluntly: "The future of AI will be conditioned by the cost of energy."</p>',
fig("fotos/datacenter-anelo-vaca-muerta.webp",
    "Añelo, the heart of Vaca Muerta: industrial facilities on the steppe and the sign welcoming visitors to a town that already knows the price of big investments. The first computing enclave is already running here.",
    "Industrial facility on the Neuquén steppe and the welcome sign to Añelo"),
'<p>And OpenAI is not the only one looking south. As Infobae revealed, Elon Musk\'s Tesla is also weighing a data center in the country alongside YPF Luz; and the government has already received executives from Google, Meta and Apple. Patagonia has suddenly become the world\'s energy aisle.</p>',
'<h3>The sacrifice zone</h3>',
'<p>While governments celebrate, communities watch with concern. Liliana Romero, lonko of the Mapuche community Fvta Trayén, in Añelo, sums up the mood: "We no longer have the same peace. There\'s a lot of pollution here." The werkén Diego Rosales goes further, describing the dependence the industry already imposes: "We depend on asking the industry for water." And Lefxaru Nawel, a Mapuche spokesman in Neuquén, denounces the method: communities learn of the projects "once they\'re already on the territory, once the works are tendered, illegally authorized, with no consultation."</p>',
'<p>Researcher Irina Sternik calls them <strong>"digital sacrifice zones"</strong>: socially excluded territories where infrastructure of enormous environmental cost is dumped, with no politically powerful actors to stop it. For Alan Rocha, of the Southern Oil Observatory, the RIGI is precisely a framework that is "regressive in terms of environmental control."</p>',
VIDEO2,
'<h3>The void every neighbor has already filled</h3>',
'<p>The most alarming fact is regulatory: <strong>Argentina has no specific rules —commercial, tax or environmental— for this kind of infrastructure</strong>. The only framework is the RIGI, which grants benefits and priority access to resources but sets no counterweights. Neuquén\'s own Environment Secretariat admits it: "For now, there are no specific regulations."</p>',
'<p>The contrast with the region is striking. <strong>Brazil</strong> enacted its Redata regime in 2025, combining incentives with sustainability requirements: 100% clean energy, water efficiency and research commitments. <strong>Chile</strong> has a National Data Center Plan 2024-2030 geared toward renewables and territorial integration. In the Latin American ranking by number of data centers, Argentina is <strong>fourth</strong>, behind Brazil, Chile and Mexico: the neighbors already regulate; here there is still nothing to regulate with.</p>',
'<p>And the economic promise, so far, fails to appear even for the local private sector. Fernando Zurita, head of the Federation of Business Entities of Neuquén, says it without partisanship: "There has been no real, tangible economic impact yet." Abroad, the warning signs multiply: in the United States, Erin Brockovich launched a platform to map data centers and Bernie Sanders called for a "pause"; in Paraguay, the town of Villarrica has spent years fighting a crypto-mining farm that consumed in six months what 47,464 families would use in a year.</p>',
'<h3>The question that remains</h3>',
'<p>As Bea Busaniche, of the Vía Libre Foundation, puts it, the dilemma is not <em>data center yes or no</em>, but <strong>data center how and for whom</strong>. Any country that wants to develop technology needs computing capacity. The question is whether that capacity is built with regulation, community consultation and shared benefits, or installed as a new extractive enclave, with Patagonia\'s water and energy as the bargaining chip for the still-uncertain promise of digital progress.</p>',
'<p>For now there is an announcement that never materialized and a law one step from the Senate. The mirage of data still shimmers on the Patagonian horizon. It remains to be seen whether, when it arrives, it will bring water —or only more thirst.</p>',
])

# ════════════════════════════════════════════════ PORTUGUÊS
cuerpo_pt = "\n\n".join([
DATELINE.format(txt="Neuquén, Patagônia — 29 de junho de 2026"),
'<p>Em <strong>10 de outubro de 2025</strong>, a quinze dias das eleições de meio de mandato, o governo de Javier Milei celebrou aos brados o que apresentou como o maior investimento tecnológico da história argentina: a <strong>OpenAI</strong>, criadora do ChatGPT, e a empresa local <strong>Sur Energy</strong> haviam assinado uma carta de intenção para erguer um mega data center de inteligência artificial na Patagônia. Batizaram-no de <strong>"Stargate Argentina"</strong>.</p>',
'<p>Os números eram do tipo que muda uma conversa: até <strong>US$ 25 bilhões</strong> de investimento e uma capacidade de <strong>500 megawatts</strong> (MW). Para dimensionar, o maior data center da América Latina, em São Paulo, tem 61 MW; e os 45 data centers que hoje funcionam em todo o país, somados, não chegam a essa potência. Sam Altman, CEO da OpenAI, divulgou um vídeo: "Estamos orgulhosos de anunciar os planos para lançar a Stargate Argentina". O projeto entraria no RIGI, o regime de benefícios fiscais por 30 anos que Milei lançou em 2024.</p>',
'<p>Oito meses depois, esse anúncio continua sendo apenas isso: um anúncio. <strong>Não foi apresentado formalmente, não tem localização definitiva, nem prazos nem valores confirmados.</strong> O próprio Ministério da Economia reconheceu que não há nada que respalde a declaração de intenção. Darío Clemente, pesquisador do CONICET e do Observatório do RIGI da fundação FARN, resume sem rodeios: dos 17 projetos aprovados e 23 em avaliação no regime, <strong>nenhum é o Stargate</strong>. "Não há informação atualizada confiável além daquele anúncio eleitoral", afirma. As versões mais otimistas falam em começar a construir apenas em 2027.</p>',
VIDEO1,
'<h3>O que de fato avançou: o "Super RIGI" já tem sanção parcial</h3>',
'<p>Embora o data center não tenha se concretizado, o anúncio cumpriu sua função política: mudou a escala da discussão e abriu caminho para um novo marco legal. Na madrugada de <strong>quarta-feira, 24 de junho de 2026</strong> —poucos dias atrás— a Câmara dos Deputados deu <strong>sanção parcial ao "Super RIGI"</strong> por <strong>130 votos a favor, 106 contra e 7 abstenções</strong>. Agora o projeto aguarda o Senado para virar lei.</p>',
'<p>O regime mira diretamente as "indústrias do futuro": <strong>inteligência artificial, data centers, baterias de lítio, painéis solares, turbinas eólicas e a cadeia de valor do urânio</strong>. E oferece benefícios excepcionais: alíquota de Imposto de Renda de <strong>15%</strong>, estabilidade tributária, aduaneira e cambial por <strong>30 anos</strong>, isenções à importação, depreciação acelerada, redução de contribuições patronais e livre disponibilidade de divisas que chega a 100% a partir do terceiro ano. Elimina, ainda, a obrigação de contratar fornecedores locais que o RIGI original fixava em 20%, e permite às empresas processar o país no <strong>CIADI</strong> se o Estado mudar as regras.</p>',
'<p>O advogado Pablo Cerdan foi taxativo: "É a lei dos data centers. Energia e trabalho subsidiados para grandes tecnológicas que faturam mais que o PIB argentino e vão pagar menos impostos que uma pequena empresa da periferia".</p>',
'<h3>Por que a Patagônia?</h3>',
'<p>A escolha não é casual. A investigação do <strong>Pulitzer Center</strong>, em parceria com o Chequeado, identifica quatro razões: terra disponível, energia barata, acesso à água e baixas temperaturas que reduzem os custos de resfriamento. Em novembro de 2025, o governo de Neuquén apresentou uma "micro-região" tecnológica que se estende da área de Vaca Muerta —Añelo e Tratayén— até o rio Limay, na localidade de Arroyito, perto da represa El Chocón. Rubén Etcheverry, do Conselho de Planejamento de Neuquén, a vende como um "microclima ideal para indústrias tecnológicas".</p>',
'<p>O fornecimento já está encaminhado: a <strong>Sur Energy</strong> assinou acordos com a Genneia —a maior geradora renovável do país— e a Central Puerto. A empresa, fundada por Emiliano Kargieman (também CEO da Satellogic, a firma de nanossatélites listada em Wall Street) e pelo falecido Mat Travizano, seria a desenvolvedora da infraestrutura, enquanto a OpenAI se compromete a comprar toda a potência de computação <strong>sem investir um dólar na construção</strong>.</p>',
fig("fotos/datacenter-ia-racks.webp",
    "O coração da máquina: corredores de servidores que exigem energia e água 24 horas por dia. O gargalo da IA já não é o chip, mas a eletricidade que o alimenta. <em>(Foto ilustrativa)</em>",
    "Interior de um data center: corredores de servidores com refrigeração"),
'<h3>A sede digital: o que não se anuncia</h3>',
'<p>Por trás do brilho da computação há uma pegada física enorme. Segundo estimativas usadas para os Estados Unidos, um data center precisa de <strong>7,1 m³ de água por MWh</strong> consumido —contando uso direto e indireto na geração elétrica—, o equivalente a <strong>mais de 2,5 milhões de litros por ano para cada megawatt</strong> de potência. Aplicado à Stargate: um centro de <strong>500 MW consome água e eletricidade equivalentes às de uma cidade de porte médio</strong>. Em escala global, os data centers já consomem 1,5% da eletricidade do planeta (cerca de 415 TWh em 2024), e a demanda deve dobrar até 2030.</p>',
statbox("A pegada de um data center de 500 MW",
        [("Água por MWh consumido", "7,1 m³"),
         ("Água por ano para cada MW", "+2,5 milhões de litros"),
         ("Consumo de um centro de 500 MW", "≈ uma cidade média"),
         ("Data centers no mundo (2024)", "1,5% da eletricidade global")],
        "Dados: Pulitzer Center / Chequeado"),
'<p>O problema é <em>onde</em> cairia essa sede. Na região de Vaca Muerta —onde cada poço de fracking pode consumir até 60.000 m³ de água por ano e em 2025 já havia 17.300 poços, mais de 1,038 bilhão de m³ no total— o recurso hídrico está sob pressão. Ali se registram cerca de 56 incidentes ambientais por dia; o último vazamento, no lago Mari Menuco, afetou 50.000 m². A uma região já espremida pelo petróleo, somar-se-ia agora uma nova sede: a digital.</p>',
'<h3>Unblock: o enclave que já existe</h3>',
'<p>Não é preciso imaginar o futuro. Entre Rincón de los Sauces e Añelo já funciona a <strong>Unblock</strong>, um data center de <strong>27 MW</strong> que projeta dobrar sua capacidade… e que emprega cerca de <strong>20 pessoas</strong>. É o retrato perfeito do que os especialistas chamam de "economias de enclave": muita energia, muito investimento, quase nenhum emprego permanente. Seu CEO, Tomás Ocampo, coloca sem rodeios: "O futuro da IA estará condicionado ao custo da energia".</p>',
fig("fotos/datacenter-anelo-vaca-muerta.webp",
    "Añelo, coração de Vaca Muerta: instalações industriais sobre a estepe e a placa que dá as boas-vindas ao povoado que já conhece o preço dos grandes investimentos. Aqui já opera o primeiro enclave de computação.",
    "Instalação industrial sobre a estepe de Neuquén e a placa de boas-vindas a Añelo"),
'<p>E a OpenAI não é a única a olhar para o sul. Segundo revelou o Infobae, a Tesla, de Elon Musk, também avalia um data center no país ao lado da YPF Luz; e o governo já recebeu executivos de Google, Meta e Apple. A Patagônia virou, de repente, a prateleira energética do mundo.</p>',
'<h3>A zona de sacrifício</h3>',
'<p>Enquanto os governos comemoram, as comunidades observam com preocupação. Liliana Romero, lonko da comunidade mapuche Fvta Trayén, em Añelo, resume o clima: "Já não temos a mesma tranquilidade. Aqui há muita contaminação". O werkén Diego Rosales vai além e descreve a dependência que a indústria já impõe: "Dependemos de pedir água à indústria". E Lefxaru Nawel, porta-voz mapuche de Neuquén, denuncia o método: as comunidades ficam sabendo dos projetos "quando já entram nos territórios, quando as obras já estão licitadas, ilegalmente autorizadas, sem fazer uma consulta".</p>',
'<p>A pesquisadora Irina Sternik as chama de <strong>"zonas de sacrifício digital"</strong>: territórios socialmente excluídos onde se despejam infraestruturas de altíssimo custo ambiental, sem atores com peso político para freá-las. Para Alan Rocha, do Observatório Petroleiro Sul, o RIGI é justamente um marco "regressivo em termos de controle ambiental".</p>',
VIDEO2,
'<h3>O vazio que todos os vizinhos já preencheram</h3>',
'<p>O dado mais alarmante é regulatório: <strong>a Argentina não tem normas específicas —comerciais, tributárias ou ambientais— para esse tipo de infraestrutura</strong>. O único marco é o RIGI, que concede benefícios e prioridade no uso de recursos, mas não fixa contrapesos. A própria Secretaria de Ambiente de Neuquén admite: "Por enquanto, não há normativas específicas".</p>',
'<p>O contraste com a região é eloquente. O <strong>Brasil</strong> sancionou em 2025 seu regime Redata, que combina incentivos com exigências de sustentabilidade: 100% de energia limpa, eficiência hídrica e compromissos de pesquisa. O <strong>Chile</strong> tem um Plano Nacional de Data Centers 2024-2030 voltado a renováveis e integração territorial. No ranking latino-americano por quantidade de data centers, a Argentina é a <strong>quarta</strong>, atrás de Brasil, Chile e México: os vizinhos já regulam; aqui ainda não há com o quê.</p>',
'<p>E a promessa econômica, por ora, não aparece nem mesmo para o setor privado local. Fernando Zurita, titular da Federação de Entidades Empresariais de Neuquén, diz sem militância: "Ainda não houve um impacto econômico real e tangível". Lá fora, os sinais de alerta se multiplicam: nos Estados Unidos, Erin Brockovich lançou uma plataforma para mapear data centers e Bernie Sanders pediu uma "pausa"; no Paraguai, a localidade de Villarrica passa anos lutando contra uma fazenda de criptomineração que consumiu em seis meses o que 47.464 famílias gastariam em um ano.</p>',
'<h3>A pergunta que fica</h3>',
'<p>Como propõe Bea Busaniche, da Fundação Vía Libre, o dilema não é <em>data center sim ou não</em>, mas <strong>data center como e para quem</strong>. Qualquer país que queira desenvolver tecnologia precisa de capacidade de computação. A pergunta é se essa capacidade se constrói com regulação, consulta às comunidades e benefícios compartilhados, ou se se instala como um novo enclave extrativista, com a água e a energia da Patagônia como moeda de troca pela promessa —ainda incerta— do progresso digital.</p>',
'<p>Por ora há um anúncio que não se concretizou e uma lei a um passo do Senado. A miragem dos dados segue brilhando no horizonte patagônico. Falta saber se, quando chegar, trará água ou apenas mais sede.</p>',
])

# ════════════════════════════════════════════════ 中文
cuerpo_zh = "\n\n".join([
DATELINE.format(txt="内乌肯，巴塔哥尼亚 — 2026年6月29日"),
'<p><strong>2025年10月10日</strong>，在中期选举前十五天，哈维尔·米莱政府高调宣布了它所称的阿根廷史上最大科技投资：ChatGPT的开发商<strong>OpenAI</strong>与本地企业<strong>Sur Energy</strong>签署了一份意向书，将在巴塔哥尼亚建造一座人工智能超级数据中心。他们将其命名为<strong>"星际之门阿根廷"（Stargate Argentina）</strong>。</p>',
'<p>这些数字足以改变讨论的格局：投资额最高达<strong>250亿美元</strong>，容量达<strong>500兆瓦</strong>（MW）。作为对比，拉丁美洲最大的数据中心位于圣保罗，容量为61兆瓦；而目前全国运营的45座数据中心加起来也达不到这一规模。OpenAI首席执行官萨姆·奥尔特曼发布视频称："我们自豪地宣布启动星际之门阿根廷的计划。"该项目将纳入RIGI——米莱于2024年推出的为期30年的税收优惠制度。</p>',
'<p>八个月过去，这一宣布仍然只是一个宣布。<strong>它从未正式提交，没有确定的选址，也没有确认的时间表或金额。</strong>经济部本身也承认，没有任何东西能支撑那份意向声明。CONICET研究员、FARN基金会RIGI观察站成员达里奥·克莱门特直言不讳地总结道：在该制度下获批的17个项目和评估中的23个项目里，<strong>没有一个是星际之门</strong>。"除了那次选举宣布之外，没有可靠的最新信息，"他指出。最乐观的说法也只是称要到2027年才动工。</p>',
VIDEO1,
'<h3>真正推进的："超级RIGI"已获半数通过</h3>',
'<p>尽管数据中心从未落地，这次宣布却实现了它的政治目的：改变了讨论的规模，并为新的法律框架打开了大门。<strong>2026年6月24日（周三）凌晨</strong>——就在几天前——众议院以<strong>130票赞成、106票反对、7票弃权</strong>，对<strong>"超级RIGI"给予半数通过</strong>。该法案现等待参议院表决以成为法律。</p>',
'<p>该制度直指"未来产业"：<strong>人工智能、数据中心、锂电池、太阳能板、风力涡轮机以及铀价值链</strong>。它提供了极为优厚的待遇：所得税税率<strong>15%</strong>，税收、海关和外汇稳定期长达<strong>30年</strong>，进口免税、加速折旧、降低雇主缴费，以及从第三年起达到100%的外汇自由支配权。它还取消了原RIGI规定的20%本地供应商雇用义务，并允许企业在国家改变规则时向<strong>ICSID（解决投资争端国际中心）</strong>起诉该国。</p>',
'<p>律师巴勃罗·塞尔丹一针见血："这是数据中心法。给那些营业额超过阿根廷GDP的科技巨头提供补贴的能源和劳动力，而它们缴的税却比郊区的一家小企业还少。"</p>',
'<h3>为什么是巴塔哥尼亚？</h3>',
'<p>这一选择并非偶然。<strong>普利策中心</strong>与Chequeado合作的调查指出了四个原因：可用的土地、廉价的能源、水资源的获取，以及降低冷却成本的低温。2025年11月，内乌肯政府公布了一个科技"微区域"，从瓦卡穆埃尔塔地区（阿涅洛和特拉塔延）一直延伸到利迈河畔的阿罗约托镇，靠近埃尔乔孔水坝。内乌肯规划委员会的鲁本·埃切韦里把它推销为"科技产业的理想小气候"。</p>',
'<p>供应已经安排妥当：<strong>Sur Energy</strong>已与Genneia（该国最大的可再生能源发电商）和Central Puerto签署协议。该公司由埃米利亚诺·卡尔吉曼（同时也是在华尔街上市的纳米卫星公司Satellogic的首席执行官）和已故的马特·特拉维扎诺创立，将负责开发基础设施，而OpenAI承诺购买全部算力，<strong>却不为建设投入一美元</strong>。</p>',
fig("fotos/datacenter-ia-racks.webp",
    "机器的核心：日夜不停消耗电力和水的服务器走廊。人工智能的瓶颈已不再是芯片，而是为其供电的电力。<em>（示意图片）</em>",
    "数据中心内部：带冷却系统的服务器走廊"),
'<h3>数字之渴：未被宣布的部分</h3>',
'<p>在算力的光环背后，是巨大的物理足迹。根据用于美国的估算，一座数据中心每消耗1兆瓦时需要<strong>7.1立方米的水</strong>——计入发电中的直接和间接用水——相当于每兆瓦容量<strong>每年超过250万升</strong>。换算到星际之门：一座<strong>500兆瓦的设施，其耗水和耗电量相当于一座中等规模的城市</strong>。在全球范围内，数据中心已占用地球1.5%的电力（2024年约415太瓦时），且需求预计到2030年将翻倍。</p>',
statbox("一座500兆瓦数据中心的足迹",
        [("每消耗1兆瓦时的用水", "7.1立方米"),
         ("每兆瓦每年的用水", "超过250万升"),
         ("一座500兆瓦设施的消耗", "≈ 一座中等城市"),
         ("全球数据中心（2024年）", "占全球电力的1.5%")],
        "数据来源：普利策中心 / Chequeado"),
'<p>问题在于这股渴求会落在<em>哪里</em>。在瓦卡穆埃尔塔地区——每口压裂井每年可耗水多达60,000立方米，到2025年已有17,300口井，总计超过10.38亿立方米——水资源已不堪重负。当地每天记录约56起环境事故；最近一次泄漏发生在马里梅努科湖，影响了50,000平方米。在一个已被石油榨干的地区，如今又将增添一种新的渴求：数字之渴。</p>',
'<h3>Unblock：早已存在的飞地</h3>',
'<p>无需想象未来。在林孔德洛斯绍塞斯与阿涅洛之间，<strong>Unblock</strong>已在运营——这是一座<strong>27兆瓦</strong>的数据中心，计划将容量翻倍……却只雇用约<strong>20人</strong>。它正是专家所称"飞地经济"的完美写照：大量能源、大量投资，几乎没有长期就业。其首席执行官托马斯·奥坎波直言："人工智能的未来将取决于能源的成本。"</p>',
fig("fotos/datacenter-anelo-vaca-muerta.webp",
    "阿涅洛，瓦卡穆埃尔塔的心脏：草原上的工业设施，以及欢迎来到这座早已尝过大型投资代价的小镇的路牌。第一个算力飞地已在此运营。",
    "内乌肯草原上的工业设施和阿涅洛的欢迎路牌"),
'<p>而OpenAI并非唯一把目光投向南方的公司。据Infobae披露，埃隆·马斯克的特斯拉也在与YPF Luz合作，考虑在该国建一座数据中心；政府还接待了谷歌、Meta和苹果的高管。巴塔哥尼亚一夜之间成了世界的能源货架。</p>',
'<h3>牺牲区</h3>',
'<p>当政府欢庆之时，社区却忧心忡忡地注视着。阿涅洛的马普切社区Fvta Trayén的lonko（首领）莉莉安娜·罗梅罗概括了这种氛围："我们不再有从前的安宁。这里污染很严重。"werkén（发言人）迭戈·罗萨莱斯说得更进一步，描述了这个行业已经强加的依赖："我们得靠向这个行业讨水。"内乌肯的马普切发言人莱夫萨鲁·纳韦尔则谴责了这种做法：社区是在"工程已经进入领地、已经招标、被非法批准、却没有任何协商"之后才得知这些项目的。</p>',
'<p>研究者伊琳娜·斯特尼克称它们为<strong>"数字牺牲区"</strong>：那些在社会上被边缘化的领地，被倾倒下环境代价极高的基础设施，却没有具备政治分量的力量来阻止。在南方石油观察站的阿兰·罗查看来，RIGI恰恰是一个"在环境管控方面倒退"的框架。</p>',
VIDEO2,
'<h3>邻国都已填补的空白</h3>',
'<p>最令人警觉的事实是监管层面的：<strong>阿根廷对此类基础设施没有专门的法规——无论是商业、税务还是环境方面</strong>。唯一的框架就是RIGI，它给予优惠和资源使用优先权，却不设任何制衡。内乌肯环境厅自己也承认："目前没有专门的规定。"</p>',
'<p>与本地区的对比十分鲜明。<strong>巴西</strong>于2025年颁布了Redata制度，将激励措施与可持续性要求相结合：100%清洁能源、用水效率和研发承诺。<strong>智利</strong>有一项2024-2030年国家数据中心计划，侧重可再生能源和区域融合。在拉美数据中心数量排名中，阿根廷位居<strong>第四</strong>，排在巴西、智利和墨西哥之后：邻国早已立规，而这里仍无规可依。</p>',
'<p>而经济上的承诺，到目前为止甚至连本地私营部门都未曾兑现。内乌肯企业实体联合会主席费尔南多·苏里塔毫无党派立场地说："至今还没有产生真实而实在的经济影响。"在国外，警示信号此起彼伏：在美国，艾琳·布罗科维奇推出了一个绘制数据中心地图的平台，伯尼·桑德斯则呼吁"暂停"；在巴拉圭，比亚里卡镇多年来一直在与一个加密货币矿场抗争，该矿场在六个月内消耗的电量相当于47,464个家庭一年的用电量。</p>',
'<h3>悬而未决的问题</h3>',
'<p>正如自由之路基金会的贝亚·布萨尼切所言，两难之处不在于<em>要不要数据中心</em>，而在于<strong>怎样建、为谁建</strong>。任何想要发展技术的国家都需要算力。问题在于，这种算力是以监管、社区协商和共享利益的方式建成，还是作为一个新的攫取式飞地被安置下来——以巴塔哥尼亚的水和能源，去换取那个仍不确定的数字进步的承诺。</p>',
'<p>眼下，有一个从未落地的宣布，和一部距参议院仅一步之遥的法律。数据的海市蜃楼依旧在巴塔哥尼亚的地平线上闪烁。尚待揭晓的是：当它真正到来时，带来的会是水，还是只有更多的渴。</p>',
])

nueva_entrada = {
    "id": "20260629-propio-datacenter-ia-patagonia",
    "titulo": "DATACENTERS EN PATAGONIA: ¿ANUNCIO VACÍO O REALIDAD?",
    "bajada": "Stargate, el datacenter de OpenAI por US$ 25.000 millones, se anunció a quince días de las elecciones y todavía no existe en los papeles. Pero el \"Súper RIGI\" —la ley que lo haría posible— ya tiene media sanción. Detrás de la promesa: una sed de agua y energía equivalente a la de una ciudad entera, sobre una región que el fracking ya dejó al límite.",
    "cuerpo": cuerpo_es,
    "tag": "🛰️ Tecnología",
    "categoria": "ciencia|tecnologia|medio ambiente",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "argentina",
    "imagen": "fotos/datacenter-ia-patagonia-aerea.webp",
    "imagen_keywords": "datacenter inteligencia artificial patagonia stargate openai vaca muerta neuquen rigi",
    "meta": "29 de Junio de 2026 · J. Martineau",
    "excluir_feed": True,
    "galeria": [],
    "titulo_en": "DATA CENTERS IN PATAGONIA: EMPTY ANNOUNCEMENT OR REALITY?",
    "bajada_en": "Stargate, OpenAI's US$25-billion data center, was announced fifteen days before the elections and still doesn't exist on paper. But the \"Super RIGI\" —the law that would make it possible— already has half-sanction. Behind the promise: a thirst for water and energy equal to that of an entire city, over a region the fracking boom already pushed to the brink.",
    "cuerpo_en": cuerpo_en,
    "titulo_pt": "DATA CENTERS NA PATAGÔNIA: ANÚNCIO VAZIO OU REALIDADE?",
    "bajada_pt": "O Stargate, o data center da OpenAI de US$ 25 bilhões, foi anunciado a quinze dias das eleições e ainda não existe no papel. Mas o \"Super RIGI\" —a lei que o tornaria possível— já tem sanção parcial. Por trás da promessa: uma sede de água e energia equivalente à de uma cidade inteira, sobre uma região que o fracking já levou ao limite.",
    "cuerpo_pt": cuerpo_pt,
    "titulo_zh": "巴塔哥尼亚的数据中心：空头承诺还是现实？",
    "bajada_zh": "OpenAI价值250亿美元的数据中心“星际之门”在选举前十五天被宣布，至今仍停留在纸面上。但让其成为可能的法律——“超级RIGI”——已获半数通过。承诺背后：相当于一整座城市的水与能源之渴，压在一个已被压裂开采推向极限的地区之上。",
    "cuerpo_zh": cuerpo_zh,
}

with open(PROPIOS, "r", encoding="utf-8") as f:
    propios = json.load(f)
with open(HISTORIAL, "r", encoding="utf-8") as f:
    historial = json.load(f)

# Evitar duplicado si se corre dos veces
propios = [p for p in propios if p.get("id") != nueva_entrada["id"]]

if len(propios) >= MAX_ACTIVOS:
    mas_antiguo = propios.pop()
    historial.insert(0, mas_antiguo)
    print(f"Movido al historial: {mas_antiguo['id']}")

propios.insert(0, nueva_entrada)
print(f"Nuevo informe en propios[0]: {nueva_entrada['id']}")
print(f"Total activos: {len(propios)}")

with open(PROPIOS, "w", encoding="utf-8") as f:
    json.dump(propios, f, ensure_ascii=False, indent=2)
with open(HISTORIAL, "w", encoding="utf-8") as f:
    json.dump(historial, f, ensure_ascii=False, indent=2)

print("OK — propios.json y propios_historial.json actualizados.")
