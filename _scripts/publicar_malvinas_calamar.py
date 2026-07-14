#!/usr/bin/env python3
# Publica el informe "El pequeño animal que paga las cuentas de Malvinas"
# en propios.json (modelo: publicar_puente_chacao.py + ARA San Juan para HTML/idiomas)
import json

BASE = "/Users/jm/Desktop/CLAUDCODE/GLOBAL PATAGONIA"
PROPIOS = f"{BASE}/propios.json"
HISTORIAL = f"{BASE}/propios_historial.json"
MAX_ACTIVOS = 7

DATELINE = '<p style="font-size:.85rem;letter-spacing:.05em;text-transform:uppercase;color:#7aadcc;font-weight:600;margin-bottom:1.2rem">{}</p>'

def img_block(src, alt, cap):
    return ('<div style="margin:2rem 0"><img src="' + src + '" alt="' + alt +
            '" loading="lazy" decoding="async" style="width:100%;border-radius:6px;display:block">'
            '<div style="font-size:.8rem;color:#777;margin-top:.45rem">' + cap + '</div></div>')

def datos_box(titulo, items):
    lis = "".join(f"<li style=\"margin-bottom:.45rem\">{i}</li>" for i in items)
    return ('<div style="background:rgba(140,107,74,.08);border-left:4px solid #8c6b4a;border-radius:0 8px 8px 0;padding:1.4rem 1.6rem;margin:2.2rem 0">'
            f'<div style="font-weight:700;font-size:1.1rem;margin-bottom:.8rem;color:#16222e">{titulo}</div>'
            f'<ul style="margin:0;padding-left:1.1rem;font-size:.98rem">{lis}</ul></div>')

IMG_PLATO = "fotos/plato-anillas-calamar-salsa.webp"
IMG_POTEROS = "fotos/foto-20260617-santa-cruz-pesquero-barcos.webp"
IMG_PA = "fotos/puerto-argentino-stanley-muelle.webp"

# ============================== ESPAÑOL ==============================
cuerpo = "\n\n".join([
    DATELINE.format("Atlántico Sur — Informe GLOBALpatagonia"),

    "<p>Pocas economías del mundo dependen tanto de un solo animal. El <strong>Illex argentinus</strong> —el calamar argentino— vive alrededor de doce meses: nace, migra, se reproduce y muere en un único ciclo que arranca en aguas de la plataforma continental argentina y termina, en buena parte, dentro de la zona que el gobierno británico de las islas Malvinas administra y licencia como propia. Cada verano austral, ese animal breve y errático define si a las islas les cierran o no las cuentas.</p>",

    "<p>La administración isleña vive de vender <strong>licencias de pesca</strong>. Es, desde 1987, su principal fuente de ingresos genuinos: un promedio histórico de unos <strong>20 millones de libras por año</strong>, que llegó a financiar entre el 50% y el 75% de todo su gasto corriente y de capital. Más de la mitad de esa recaudación viene del calamar. El petróleo de Malvinas, del que tanto se habla, sigue siendo una promesa; el calamar es la caja real, la que paga sueldos, obras y también parte del andamiaje que sostiene la ocupación británica del archipiélago.</p>",

    "<h3>Dos calamares, dos flotas</h3>",

    "<p>El negocio tiene dos patas. La primera es el <strong>Illex</strong>, que se pesca con buques poteros —los barcos de luces que se ven de noche como ciudades flotantes—. Las licencias tipo B las compran sobre todo <strong>flotas de Taiwán y Corea del Sur</strong>, las mismas banderas que dominan la pesquería en toda la región. Este año el gobierno isleño otorgó <strong>105 licencias</strong> para la zafra de calamar, permisos que para la legislación argentina son lisa y llanamente ilegales: se emiten sobre aguas en disputa de soberanía, donde la Argentina no puede ejercer control.</p>",

    "<p>La segunda pata es menos conocida y más jugosa por tonelada: el <strong>calamar patagónico</strong> o Loligo (<em>Doryteuthis gahi</em>), el \"calamarete\" que Europa consume como <em>calamari</em>. Ahí no hay poteros asiáticos sino <strong>arrastreros congeladores de capital español</strong>. Al menos siete empresas gallegas —Lanzal, Grupo Pereira, Pescapuerta, Copemar, Ferralmes, Hermanos Touza y Moradiña— operan desde hace décadas mediante <em>joint ventures</em> con firmas registradas en las islas. El esquema les permite abanderar sus buques como isleños y acceder a las licencias que emite Puerto Argentino (Stanley).</p>",

    img_block(IMG_PLATO, "Plato de anillas de calamar en su salsa",
              "Del Atlántico Sur a las mesas de Europa: el calamar patagónico —el <em>calamari</em> de los restaurantes europeos— es el premio mayor de las flotas gallegas con licencia isleña. (Foto de referencia)"),

    "<p>Los números de esa sociedad explican por qué nadie quiere soltarla. En la primera campaña de Loligo de 2026, los <strong>16 arrastreros</strong> del régimen mixto capturaron más de <strong>42.000 toneladas en 64 días</strong>, una zafra valuada por la prensa especializada en cerca de <strong>500 millones de dólares</strong> puesta en el mercado europeo. Por las licencias de este año, las empresas españolas pagarán al gobierno isleño unos <strong>13,4 millones de euros</strong>. El margen del negocio es elocuente: por cada euro de licencia, decenas de euros de calamar.</p>",

    img_block(IMG_POTEROS, "Buques poteros amarrados en un puerto patagónico al amanecer",
              "Poteros amarrados en un puerto de Santa Cruz. Del otro lado de la línea, más de un centenar de buques extranjeros pescan el mismo calamar con licencia isleña. (Archivo GLOBALpatagonia)"),

    "<h3>Un recurso que ya mostró que puede desaparecer</h3>",

    "<p>Todo el andamiaje descansa, sin embargo, sobre una biología frágil. El calamar vive un año: no hay stock acumulado, no hay reservas nadando de una temporada a la otra. Cada zafra depende de que la generación nueva aparezca. Y en <strong>2024 no apareció</strong>: por primera vez en la historia de la pesquería, la temporada de Loligo se canceló completa por falta de biomasa. Un hecho inédito desde que las islas empezaron a licenciar la pesca.</p>",

    "<p>La zafra volvió en 2026 —el relevamiento científico de febrero estimó una biomasa central de <strong>41.725 toneladas</strong> y la temporada se abrió con normalidad—, pero el susto dejó marca en las cuentas públicas isleñas. El presupuesto 2026/27, aprobado hace semanas, es el retrato de una economía tensionada: una apropiación total de <strong>216,3 millones de libras</strong> (unos 290 millones de dólares), con la recaudación por impuesto corporativo pesquero en caída por las zafras débiles de Loligo y un superávit operativo previsto que no llega a <strong>300.000 dólares</strong>. Las reservas del gobierno isleño, que equivalían a 3,1 veces su gasto departamental, caerían a apenas 1,2 veces en 2027/28, mientras las islas se endeudan con un préstamo de 150 millones de libras para infraestructura.</p>",

    img_block(IMG_PA, "Vista del muelle de Puerto Argentino (Stanley), capital de las islas Malvinas",
              "Puerto Argentino (Stanley), sede del gobierno británico que administra las islas. Su presupuesto depende, zafra a zafra, de las licencias pesqueras. (Archivo)"),

    datos_box("El negocio en números", [
        "<strong>~£20 millones/año</strong>: promedio histórico de recaudación isleña por licencias de pesca (en años recientes cayó a £12–15 millones).",
        "<strong>105 licencias</strong> de calamar otorgadas en 2026, consideradas ilegales por la Argentina.",
        "<strong>7 empresas gallegas</strong> operan Loligo vía joint ventures; 16 arrastreros, 42.000 toneladas, ~US$ 500 millones en la primera campaña 2026.",
        "<strong>€13,4 millones</strong> pagarán las españolas por sus licencias este año.",
        "<strong>2024:</strong> primera cancelación total de una zafra de Loligo en la historia.",
        "<strong>156.813 toneladas</strong> descargó la flota potera argentina en 2026: segundo récord consecutivo.",
    ]),

    "<h3>Del otro lado de la línea</h3>",

    "<p>Mientras tanto, del lado argentino el mismo calamar vive un momento inesperadamente dulce. La zafra 2026 de la flota potera nacional cerró con <strong>156.813 toneladas descargadas</strong>, el segundo año récord consecutivo. La abundancia dentro de la Zona Económica Exclusiva tuvo un efecto lateral revelador: la famosa flota extranjera de la <strong>milla 201</strong> —el borde exterior de la ZEE donde cada verano se agolpan cientos de buques sin licencia de nadie— se achicó a ojos vista, porque el calamar, este año, estaba adentro.</p>",

    "<p>Esa flota de la milla 201 es la tercera pata silenciosa del negocio: cerca del <strong>50% de los buques están vinculados a empresas chinas</strong>, muchos bajo banderas de conveniencia de Vanuatu, Tanzania o Kenia, y casi un 30% son españoles. Pescan gratis lo que las islas licencian y la Argentina regula: el mismo recurso, tres regímenes distintos, un solo cardumen.</p>",

    "<p>Buenos Aires, por su parte, decidió jugar a capturar el calamar antes de que migre: el Consejo Federal Pesquero lanzó este año una convocatoria para incorporar <strong>18 nuevos buques poteros</strong> a la matrícula nacional, la mayor ampliación de la flota en décadas. La lógica es simple y algo cruda: el Illex nace y engorda en aguas argentinas; cada tonelada que se pesca dentro de la ZEE es una tonelada que no llegará a pagar licencia en Puerto Argentino ni a llenar bodegas chinas en la milla 201.</p>",

    "<h3>La paradoja del cardumen</h3>",

    "<p>El resultado es una de las paradojas económicas más singulares del Atlántico Sur: un animal de un año de vida, que no reconoce líneas en el agua, financia a la vez a la flota argentina, a las pesqueras de Galicia, a los armadores de Taiwán y al presupuesto del gobierno británico que administra un territorio que la Argentina reclama. Cuando el calamar abunda, todos ganan y nadie discute. Cuando falta —como en 2024—, las islas descubren en sus propias cuentas lo que la biología repite cada temporada: su economía depende de un recurso que no controlan, que no nace en sus aguas y cuya suerte se decide, cardumen a cardumen, en el mar argentino.</p>",

    "<p><em>Con datos del Fisheries Department isleño, presupuesto 2026/27 de las islas, Consejo Federal Pesquero, Revista Puerto, Pescare, MercoPress y prensa especializada del sector.</em></p>",
])

# ============================== ENGLISH ==============================
cuerpo_en = "\n\n".join([
    DATELINE.format("South Atlantic — GLOBALpatagonia Report"),

    "<p>Few economies in the world depend so heavily on a single animal. The <strong>Illex argentinus</strong> — the Argentine shortfin squid — lives about twelve months: it hatches, migrates, spawns and dies in a single cycle that begins in the waters of Argentina's continental shelf and ends, to a large extent, inside the zone that the British government of the Malvinas Islands administers and licenses as its own. Every austral summer, that brief, erratic creature decides whether the islands' books balance or not.</p>",

    "<p>The island administration lives off selling <strong>fishing licences</strong>. Since 1987 they have been its main source of genuine revenue: a historical average of about <strong>£20 million a year</strong>, which at times funded between 50% and 75% of all its operating and capital spending. More than half of that revenue comes from squid. Malvinas oil, so often talked about, remains a promise; squid is the real cash box — the one that pays salaries, public works, and part of the scaffolding that sustains the British occupation of the archipelago.</p>",

    "<h3>Two squids, two fleets</h3>",

    "<p>The business stands on two legs. The first is <strong>Illex</strong>, caught by jigger vessels — the light-covered ships that glow at night like floating cities. Type B licences are bought mostly by <strong>fleets from Taiwan and South Korea</strong>, the same flags that dominate the fishery across the region. This year the island government issued <strong>105 licences</strong> for the squid season — permits that under Argentine law are plainly illegal: they are issued over waters under a sovereignty dispute, where Argentina cannot exercise control.</p>",

    "<p>The second leg is less known and more lucrative per tonne: the <strong>Patagonian squid</strong> or Loligo (<em>Doryteuthis gahi</em>), the small squid Europe eats as <em>calamari</em>. There are no Asian jiggers here but <strong>freezer trawlers backed by Spanish capital</strong>. At least seven Galician companies — Lanzal, Grupo Pereira, Pescapuerta, Copemar, Ferralmes, Hermanos Touza and Moradiña — have operated for decades through <em>joint ventures</em> with firms registered in the islands. The scheme lets them flag their vessels as islanders and access the licences issued in Puerto Argentino (Stanley).</p>",

    img_block(IMG_PLATO, "Plate of squid rings in sauce",
              "From the South Atlantic to Europe's tables: Patagonian squid — the <em>calamari</em> of European restaurants — is the top prize for the Galician fleets fishing under island licences. (Reference photo)"),

    "<p>The numbers of that partnership explain why nobody wants to let it go. In the first Loligo campaign of 2026, the <strong>16 trawlers</strong> of the joint-venture regime caught more than <strong>42,000 tonnes in 64 days</strong>, a season valued by the trade press at close to <strong>US$500 million</strong> once placed on the European market. For this year's licences, the Spanish companies will pay the island government some <strong>€13.4 million</strong>. The margin speaks for itself: for every euro in licences, dozens of euros in squid.</p>",

    img_block(IMG_POTEROS, "Jigger vessels moored in a Patagonian port at dawn",
              "Jiggers moored in a Santa Cruz port. On the other side of the line, more than a hundred foreign vessels catch the same squid under island licences. (GLOBALpatagonia archive)"),

    "<h3>A resource that has already shown it can vanish</h3>",

    "<p>The whole structure rests, however, on fragile biology. Squid live one year: there is no accumulated stock, no reserves swimming from one season to the next. Every season depends on the new generation showing up. And in <strong>2024 it didn't</strong>: for the first time in the fishery's history, the Loligo season was cancelled entirely for lack of biomass — unprecedented since the islands began licensing fishing.</p>",

    "<p>The season returned in 2026 — the February scientific survey estimated a central biomass of <strong>41,725 tonnes</strong> and fishing opened normally — but the scare left its mark on the islands' public accounts. The 2026/27 budget, approved weeks ago, is the portrait of a strained economy: a total appropriation of <strong>£216.3 million</strong> (about US$290 million), with fishing-sector corporate tax revenue falling after the weak Loligo seasons and a projected operating surplus of less than <strong>US$300,000</strong>. The island government's reserves, once worth 3.1 times its departmental spending, would fall to just 1.2 times by 2027/28, while the islands take on a £150 million infrastructure loan.</p>",

    img_block(IMG_PA, "View of the waterfront of Puerto Argentino (Stanley), capital of the Malvinas Islands",
              "Puerto Argentino (Stanley), seat of the British government that administers the islands. Its budget depends, season by season, on fishing licences. (Archive)"),

    datos_box("The business in numbers", [
        "<strong>~£20 million/year</strong>: historical average of island revenue from fishing licences (down to £12–15 million in recent years).",
        "<strong>105 squid licences</strong> issued in 2026, considered illegal by Argentina.",
        "<strong>7 Galician companies</strong> run the Loligo fishery via joint ventures; 16 trawlers, 42,000 tonnes, ~US$500 million in the first 2026 campaign.",
        "<strong>€13.4 million</strong> is what the Spanish firms will pay for this year's licences.",
        "<strong>2024:</strong> first full cancellation of a Loligo season in history.",
        "<strong>156,813 tonnes</strong> landed by Argentina's jigger fleet in 2026: a second consecutive record.",
    ]),

    "<h3>On the other side of the line</h3>",

    "<p>Meanwhile, on the Argentine side, the same squid is enjoying an unexpectedly sweet moment. The 2026 season of the national jigger fleet closed with <strong>156,813 tonnes landed</strong>, the second record year in a row. Abundance inside the Exclusive Economic Zone had a revealing side effect: the famous foreign fleet at <strong>mile 201</strong> — the outer edge of the EEZ where hundreds of vessels with no licence from anyone crowd every summer — visibly shrank, because this year the squid was inside.</p>",

    "<p>That mile-201 fleet is the silent third leg of the business: about <strong>50% of the vessels are linked to Chinese companies</strong>, many under flags of convenience from Vanuatu, Tanzania or Kenya, and nearly 30% are Spanish. They catch for free what the islands license and Argentina regulates: the same resource, three different regimes, a single school of squid.</p>",

    "<p>Buenos Aires, for its part, has decided to play at catching the squid before it migrates: the Federal Fisheries Council launched a call this year to add <strong>18 new jigger vessels</strong> to the national registry, the biggest fleet expansion in decades. The logic is simple and somewhat raw: Illex hatches and fattens in Argentine waters; every tonne caught inside the EEZ is a tonne that will never pay a licence in Puerto Argentino nor fill Chinese holds at mile 201.</p>",

    "<h3>The paradox of the school</h3>",

    "<p>The result is one of the South Atlantic's most singular economic paradoxes: a one-year-old animal that recognizes no lines in the water simultaneously finances Argentina's fleet, Galicia's fishing companies, Taiwan's shipowners and the budget of the British government that administers a territory Argentina claims. When squid is plentiful, everyone wins and nobody argues. When it fails — as in 2024 — the islands discover in their own accounts what biology repeats every season: their economy depends on a resource they do not control, that is not born in their waters, and whose fate is decided, school by school, in the Argentine sea.</p>",

    "<p><em>Based on data from the islands' Fisheries Department, the islands' 2026/27 budget, Argentina's Federal Fisheries Council, Revista Puerto, Pescare, MercoPress and specialized trade press.</em></p>",
])

# ============================== PORTUGUÊS ==============================
cuerpo_pt = "\n\n".join([
    DATELINE.format("Atlântico Sul — Relatório GLOBALpatagonia"),

    "<p>Poucas economias no mundo dependem tanto de um único animal. O <strong>Illex argentinus</strong> — a lula argentina — vive cerca de doze meses: nasce, migra, se reproduz e morre em um único ciclo que começa nas águas da plataforma continental argentina e termina, em boa parte, dentro da zona que o governo britânico das ilhas Malvinas administra e licencia como própria. A cada verão austral, esse animal breve e errático define se as contas das ilhas fecham ou não.</p>",

    "<p>A administração das ilhas vive de vender <strong>licenças de pesca</strong>. Desde 1987, elas são sua principal fonte de receita genuína: uma média histórica de cerca de <strong>20 milhões de libras por ano</strong>, que chegou a financiar entre 50% e 75% de todo o seu gasto corrente e de capital. Mais da metade dessa arrecadação vem da lula. O petróleo das Malvinas, de que tanto se fala, segue sendo uma promessa; a lula é o caixa real, o que paga salários, obras e também parte do andaime que sustenta a ocupação britânica do arquipélago.</p>",

    "<h3>Duas lulas, duas frotas</h3>",

    "<p>O negócio tem duas pernas. A primeira é o <strong>Illex</strong>, pescado com barcos poteiros — os navios de luzes que à noite parecem cidades flutuantes. As licenças tipo B são compradas sobretudo por <strong>frotas de Taiwan e da Coreia do Sul</strong>, as mesmas bandeiras que dominam a pescaria em toda a região. Este ano, o governo das ilhas outorgou <strong>105 licenças</strong> para a temporada de lula — permissões que, para a legislação argentina, são simplesmente ilegais: são emitidas sobre águas em disputa de soberania, onde a Argentina não pode exercer controle.</p>",

    "<p>A segunda perna é menos conhecida e mais lucrativa por tonelada: a <strong>lula patagônica</strong> ou Loligo (<em>Doryteuthis gahi</em>), a lula pequena que a Europa consome como <em>calamari</em>. Ali não há poteiros asiáticos, mas <strong>arrasteiros congeladores de capital espanhol</strong>. Pelo menos sete empresas galegas — Lanzal, Grupo Pereira, Pescapuerta, Copemar, Ferralmes, Hermanos Touza e Moradiña — operam há décadas por meio de <em>joint ventures</em> com firmas registradas nas ilhas. O esquema permite que abandeirem seus navios como locais e acessem as licenças emitidas em Puerto Argentino (Stanley).</p>",

    img_block(IMG_PLATO, "Prato de anéis de lula ao molho",
              "Do Atlântico Sul às mesas da Europa: a lula patagônica — o <em>calamari</em> dos restaurantes europeus — é o grande prêmio das frotas galegas com licença das ilhas. (Foto de referência)"),

    "<p>Os números dessa sociedade explicam por que ninguém quer largá-la. Na primeira campanha de Loligo de 2026, os <strong>16 arrasteiros</strong> do regime misto capturaram mais de <strong>42.000 toneladas em 64 dias</strong>, uma temporada avaliada pela imprensa especializada em cerca de <strong>US$ 500 milhões</strong> no mercado europeu. Pelas licenças deste ano, as empresas espanholas pagarão ao governo das ilhas cerca de <strong>13,4 milhões de euros</strong>. A margem do negócio é eloquente: para cada euro de licença, dezenas de euros em lula.</p>",

    img_block(IMG_POTEROS, "Barcos poteiros atracados em um porto patagônico ao amanhecer",
              "Poteiros atracados em um porto de Santa Cruz. Do outro lado da linha, mais de uma centena de navios estrangeiros pescam a mesma lula com licença das ilhas. (Arquivo GLOBALpatagonia)"),

    "<h3>Um recurso que já mostrou que pode desaparecer</h3>",

    "<p>Todo o andaime repousa, porém, sobre uma biologia frágil. A lula vive um ano: não há estoque acumulado, não há reservas nadando de uma temporada para a outra. Cada safra depende de a nova geração aparecer. E em <strong>2024 ela não apareceu</strong>: pela primeira vez na história da pescaria, a temporada de Loligo foi cancelada por completo por falta de biomassa — algo inédito desde que as ilhas começaram a licenciar a pesca.</p>",

    "<p>A temporada voltou em 2026 — o levantamento científico de fevereiro estimou uma biomassa central de <strong>41.725 toneladas</strong> e a pesca abriu normalmente —, mas o susto deixou marca nas contas públicas das ilhas. O orçamento 2026/27, aprovado há semanas, é o retrato de uma economia tensionada: uma apropriação total de <strong>216,3 milhões de libras</strong> (cerca de US$ 290 milhões), com a arrecadação do imposto corporativo pesqueiro em queda após as temporadas fracas de Loligo e um superávit operacional previsto de menos de <strong>US$ 300 mil</strong>. As reservas do governo das ilhas, que equivaliam a 3,1 vezes seu gasto departamental, cairiam a apenas 1,2 vez em 2027/28, enquanto as ilhas se endividam com um empréstimo de 150 milhões de libras para infraestrutura.</p>",

    img_block(IMG_PA, "Vista do cais de Puerto Argentino (Stanley), capital das ilhas Malvinas",
              "Puerto Argentino (Stanley), sede do governo britânico que administra as ilhas. Seu orçamento depende, safra a safra, das licenças de pesca. (Arquivo)"),

    datos_box("O negócio em números", [
        "<strong>~£20 milhões/ano</strong>: média histórica de arrecadação das ilhas com licenças de pesca (caiu para £12–15 milhões nos últimos anos).",
        "<strong>105 licenças</strong> de lula outorgadas em 2026, consideradas ilegais pela Argentina.",
        "<strong>7 empresas galegas</strong> operam o Loligo via joint ventures; 16 arrasteiros, 42.000 toneladas, ~US$ 500 milhões na primeira campanha de 2026.",
        "<strong>€13,4 milhões</strong> pagarão as espanholas por suas licenças este ano.",
        "<strong>2024:</strong> primeiro cancelamento total de uma temporada de Loligo na história.",
        "<strong>156.813 toneladas</strong> descarregou a frota poteira argentina em 2026: segundo recorde consecutivo.",
    ]),

    "<h3>Do outro lado da linha</h3>",

    "<p>Enquanto isso, do lado argentino, a mesma lula vive um momento inesperadamente doce. A temporada 2026 da frota poteira nacional fechou com <strong>156.813 toneladas descarregadas</strong>, o segundo ano recorde consecutivo. A abundância dentro da Zona Econômica Exclusiva teve um efeito colateral revelador: a famosa frota estrangeira da <strong>milha 201</strong> — a borda externa da ZEE onde centenas de navios sem licença de ninguém se aglomeram a cada verão — encolheu a olhos vistos, porque a lula, este ano, estava dentro.</p>",

    "<p>Essa frota da milha 201 é a terceira perna silenciosa do negócio: cerca de <strong>50% dos navios estão ligados a empresas chinesas</strong>, muitos sob bandeiras de conveniência de Vanuatu, Tanzânia ou Quênia, e quase 30% são espanhóis. Pescam de graça o que as ilhas licenciam e a Argentina regula: o mesmo recurso, três regimes distintos, um único cardume.</p>",

    "<p>Buenos Aires, por sua vez, decidiu apostar em capturar a lula antes que ela migre: o Conselho Federal Pesqueiro lançou este ano uma convocatória para incorporar <strong>18 novos barcos poteiros</strong> à matrícula nacional, a maior ampliação da frota em décadas. A lógica é simples e um tanto crua: o Illex nasce e engorda em águas argentinas; cada tonelada pescada dentro da ZEE é uma tonelada que não pagará licença em Puerto Argentino nem encherá porões chineses na milha 201.</p>",

    "<h3>O paradoxo do cardume</h3>",

    "<p>O resultado é um dos paradoxos econômicos mais singulares do Atlântico Sul: um animal de um ano de vida, que não reconhece linhas na água, financia ao mesmo tempo a frota argentina, as pesqueiras da Galícia, os armadores de Taiwan e o orçamento do governo britânico que administra um território que a Argentina reivindica. Quando a lula abunda, todos ganham e ninguém discute. Quando falta — como em 2024 —, as ilhas descobrem nas próprias contas o que a biologia repete a cada temporada: sua economia depende de um recurso que não controlam, que não nasce em suas águas e cuja sorte se decide, cardume a cardume, no mar argentino.</p>",

    "<p><em>Com dados do Fisheries Department das ilhas, orçamento 2026/27 das ilhas, Conselho Federal Pesqueiro argentino, Revista Puerto, Pescare, MercoPress e imprensa especializada do setor.</em></p>",
])

# ============================== 中文 ==============================
cuerpo_zh = "\n\n".join([
    DATELINE.format("南大西洋 — GLOBALpatagonia 深度报道"),

    "<p>世界上很少有经济体如此依赖一种动物。<strong>阿根廷滑柔鱼（Illex argentinus）</strong>——阿根廷鱿鱼——寿命只有大约十二个月：它在一个周期内出生、洄游、繁殖、死亡。这个周期始于阿根廷大陆架水域，很大一部分终结于马尔维纳斯群岛英国政府自行管理并发放捕捞许可的海域。每年南半球的夏天，这种短命而漂泊的动物决定着群岛的账本能否平衡。</p>",

    "<p>群岛当局靠出售<strong>捕鱼许可证</strong>为生。自1987年以来，这是其最主要的实际收入来源：历史平均每年约<strong>2000万英镑</strong>，一度支撑其全部经常性支出和资本支出的50%到75%。其中一半以上来自鱿鱼。人们常谈论的马尔维纳斯石油仍然只是一个承诺；鱿鱼才是真正的钱柜——它支付薪水、公共工程，也支撑着英国占领该群岛的部分开销。</p>",

    "<h3>两种鱿鱼，两支船队</h3>",

    "<p>这门生意有两条腿。第一条是<strong>滑柔鱼（Illex）</strong>，由鱿钓船捕捞——那些夜里灯火通明、宛如漂浮城市的船只。B类许可证的买家主要是<strong>台湾和韩国的船队</strong>，也是主导整个区域渔业的旗帜。今年群岛政府为鱿鱼季发放了<strong>105张许可证</strong>——依照阿根廷法律，这些许可完全非法：它们发放于主权存在争议的海域，阿根廷无法在那里行使管辖。</p>",

    "<p>第二条腿知名度较低，但按吨位计更有利可图：<strong>巴塔哥尼亚枪乌贼（Loligo，学名 Doryteuthis gahi）</strong>，即欧洲餐桌上的<em>calamari</em>。这里没有亚洲鱿钓船，而是<strong>西班牙资本的冷冻拖网船</strong>。至少七家加利西亚企业——Lanzal、Grupo Pereira、Pescapuerta、Copemar、Ferralmes、Hermanos Touza 和 Moradiña——几十年来通过与注册在群岛的公司组建<em>合资企业</em>运营。这种安排让它们的船只得以悬挂群岛旗帜，获取阿根廷港（斯坦利）发放的许可证。</p>",

    img_block(IMG_PLATO, "一盘酱汁鱿鱼圈",
              "从南大西洋到欧洲餐桌：巴塔哥尼亚枪乌贼——欧洲餐厅里的calamari——是持有群岛许可证的加利西亚船队的最大奖赏。（资料图）"),

    "<p>这桩合作的数字解释了为什么没人愿意放手。在2026年第一个枪乌贼渔季中，合资体制下的<strong>16艘拖网船</strong>在<strong>64天里捕捞了超过42,000吨</strong>，行业媒体估计这一季投放欧洲市场的价值接近<strong>5亿美元</strong>。而今年的许可证费用，西班牙企业向群岛政府支付约<strong>1340万欧元</strong>。生意的利润率一目了然：每付一欧元的许可费，就能换来几十欧元的鱿鱼。</p>",

    img_block(IMG_POTEROS, "黎明时分停泊在巴塔哥尼亚港口的鱿钓船",
              "停泊在圣克鲁斯省港口的鱿钓船。在分界线的另一侧，一百多艘外国渔船凭群岛许可证捕捞同样的鱿鱼。（GLOBALpatagonia资料图）"),

    "<h3>一种已经证明会消失的资源</h3>",

    "<p>然而，整个体系建立在脆弱的生物学之上。鱿鱼只活一年：没有积累的种群，没有从一季游到下一季的储备。每个渔季都取决于新一代是否出现。而<strong>2024年它没有出现</strong>：渔业史上第一次，枪乌贼渔季因生物量不足被整季取消——这是群岛开始发放捕捞许可以来从未有过的事。</p>",

    "<p>渔季在2026年回归——2月的科学调查估计中心生物量为<strong>41,725吨</strong>，捕捞正常开始——但这场虚惊在群岛的公共账目上留下了印记。数周前通过的2026/27财政预算是一个紧绷经济体的写照：总拨款<strong>2.163亿英镑</strong>（约2.9亿美元），渔业企业税收因枪乌贼渔季疲弱而下滑，预计运营盈余不足<strong>30万美元</strong>。群岛政府的储备金曾相当于其部门支出的3.1倍，到2027/28年将降至仅1.2倍，同时群岛还背上了1.5亿英镑的基础设施贷款。</p>",

    img_block(IMG_PA, "马尔维纳斯群岛首府阿根廷港（斯坦利）码头景观",
              "阿根廷港（斯坦利），管理群岛的英国政府所在地。它的预算逐季依赖捕鱼许可证。（资料图）"),

    datos_box("数字里的生意", [
        "<strong>约2000万英镑/年</strong>：群岛捕鱼许可收入的历史平均值（近年降至1200–1500万英镑）。",
        "<strong>105张</strong>2026年发放的鱿鱼捕捞许可证，被阿根廷视为非法。",
        "<strong>7家加利西亚企业</strong>通过合资经营枪乌贼渔业；16艘拖网船，42,000吨，2026年首季约5亿美元。",
        "<strong>1340万欧元</strong>：西班牙企业今年支付的许可费。",
        "<strong>2024年</strong>：史上首次整季取消枪乌贼捕捞。",
        "<strong>156,813吨</strong>：阿根廷鱿钓船队2026年的卸货量，连续第二年创纪录。",
    ]),

    "<h3>分界线的另一侧</h3>",

    "<p>与此同时，在阿根廷一侧，同样的鱿鱼正经历一个出人意料的甜蜜时刻。阿根廷鱿钓船队的2026渔季以<strong>卸货156,813吨</strong>收官，连续第二年创下纪录。专属经济区内的丰产带来一个耐人寻味的副作用：著名的<strong>201海里</strong>外国船队——每年夏天数百艘无任何许可的渔船聚集在专属经济区外缘——肉眼可见地缩小了，因为今年鱿鱼在里面。</p>",

    "<p>201海里船队是这门生意沉默的第三条腿：约<strong>50%的船只与中国企业有关联</strong>，许多悬挂瓦努阿图、坦桑尼亚或肯尼亚的方便旗，另有近30%是西班牙船。群岛发许可、阿根廷立规管的资源，他们免费捕捞：同一种资源，三种制度，一群鱿鱼。</p>",

    "<p>布宜诺斯艾利斯则决定抢在鱿鱼洄游之前捕捞：联邦渔业委员会今年发起招标，将为国家船籍增加<strong>18艘新鱿钓船</strong>，这是几十年来最大规模的扩编。逻辑简单而直接：滑柔鱼在阿根廷水域出生长大；在专属经济区内捕捞的每一吨，都是不会去阿根廷港缴纳许可费、也不会装进201海里中国货舱的一吨。</p>",

    "<h3>鱼群的悖论</h3>",

    "<p>结果是南大西洋最奇特的经济悖论之一：一种寿命一年、不认得水中界线的动物，同时供养着阿根廷的船队、加利西亚的渔业公司、台湾的船东，以及管理着一片阿根廷主张主权领土的英国政府的预算。鱿鱼丰产时，人人受益，无人争论。鱿鱼缺席时——如2024年——群岛便会在自己的账本上发现生物学每季都在重复的事实：它们的经济依赖一种自己无法控制、不在自己水域出生的资源，而这种资源的命运，一群接一群，在阿根廷海域被决定。</p>",

    "<p><em>数据来源：群岛渔业部门、群岛2026/27财政预算、阿根廷联邦渔业委员会、Revista Puerto、Pescare、MercoPress及行业专业媒体。</em></p>",
])

nueva_entrada = {
    "id": "20260714-propio-malvinas-calamar",
    "titulo": "El pequeño animal que paga las cuentas de Malvinas",
    "bajada": "Vive apenas un año, nace y crece en aguas argentinas, y sostiene el presupuesto del gobierno británico que administra las islas. Flotas gallegas, taiwanesas y coreanas pagan millones por licencias que Buenos Aires considera ilegales, sobre un recurso que ya mostró que puede desaparecer: en 2024, por primera vez en la historia, hubo que cancelar una zafra entera. Radiografía del negocio que decide la suerte financiera de Malvinas.",
    "cuerpo": cuerpo,
    "titulo_en": "The Tiny Animal That Pays the Bills in the Malvinas",
    "bajada_en": "It lives barely a year, is born and grows in Argentine waters, and sustains the budget of the British government that administers the islands. Galician, Taiwanese and Korean fleets pay millions for licences Buenos Aires considers illegal, over a resource that has already shown it can vanish: in 2024, for the first time in history, an entire season had to be cancelled. An X-ray of the business that decides the islands' financial fate.",
    "cuerpo_en": cuerpo_en,
    "titulo_pt": "O pequeno animal que paga as contas das Malvinas",
    "bajada_pt": "Vive apenas um ano, nasce e cresce em águas argentinas e sustenta o orçamento do governo britânico que administra as ilhas. Frotas galegas, taiwanesas e coreanas pagam milhões por licenças que Buenos Aires considera ilegais, sobre um recurso que já mostrou que pode desaparecer: em 2024, pela primeira vez na história, uma temporada inteira teve de ser cancelada. Uma radiografia do negócio que decide a sorte financeira das Malvinas.",
    "cuerpo_pt": cuerpo_pt,
    "titulo_zh": "为马尔维纳斯群岛买单的小动物",
    "bajada_zh": "它的寿命只有一年，在阿根廷水域出生长大，却支撑着管理群岛的英国政府的预算。加利西亚、台湾和韩国的船队为布宜诺斯艾利斯视为非法的许可证支付数百万，而这种资源已经证明它会消失：2024年，历史上第一次整季捕捞被取消。深度剖析决定马尔维纳斯财政命运的这门生意。",
    "cuerpo_zh": cuerpo_zh,
    "tag": "🦑 Malvinas",
    "categoria": "economia|malvinas|pesca|soberania",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "argentina",
    "imagen": "fotos/calamar-illex-rojo.webp",
    "imagen_keywords": "calamar illex malvinas pesca licencias atlantico sur",
    "hashtags_en": "#Malvinas #Squid #SouthAtlantic #Fishing #Argentina #Patagonia",
    "meta": "14 de Julio de 2026 · J. Martineau",
    "excluir_feed": True,
    "galeria": []
}

with open(PROPIOS, "r", encoding="utf-8") as f:
    propios = json.load(f)

with open(HISTORIAL, "r", encoding="utf-8") as f:
    historial = json.load(f)

if any(p["id"] == nueva_entrada["id"] for p in propios):
    raise SystemExit("Ya existe ese id en propios.json — abortando.")

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
