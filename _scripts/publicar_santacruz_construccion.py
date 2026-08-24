#!/usr/bin/env python3
import json, os

BASE = "/Users/jm/Desktop/CLAUDCODE/GLOBAL PATAGONIA"
PROPIOS = f"{BASE}/propios.json"
HISTORIAL = f"{BASE}/propios_historial.json"
MAX_ACTIVOS = 7

CREDITO_SATELITAL = (
    '<div style="font-size:13px;color:#8a8a8a;margin:4px 0 20px">'
    'Imagen satelital del complejo hidroeléctrico sobre el río Santa Cruz '
    '— Maxar Technologies / Google Earth, 2022.</div>\n\n'
)

cuerpo = (
    "En la Ruta 3, los carteles de “Obra Paralizada” se oxidan. Sobre el puente que cruza el río Santa Cruz, los trabajadores de la UOCRA volvieron a cortar el paso esta semana, reclamando por la reactivación de las represas del río Santa Cruz. No es una postal aislada: es el reflejo de la peor crisis del empleo en la construcción de todo el país.\n\n"
    "<h3>El derrumbe en números</h3>\n\n"
    "Según datos de IDARC, INDEC y la consultora Politikón Chaco, el empleo registrado en la construcción cayó 40% interanual durante el primer semestre de 2026 en Santa Cruz, la peor caída de todas las provincias argentinas. En términos absolutos, el sector pasó de 5.357 puestos en noviembre de 2023 a 1.587 en enero de 2026 — una pérdida de casi 3.800 empleos. Medida contra el promedio histórico 2007-2023, la caída llega al 76,2%, la brecha más profunda del país.\n\n"
    "El dato paradójico es el salario: pese al derrumbe del empleo, el salario nominal promedio de la UOCRA en Santa Cruz ($2,2 millones) es el más alto del país, producto de escalas históricamente altas en la Patagonia. Descontando inflación, sin embargo, el salario real cayó 15,9% desde noviembre de 2023.\n\n"
    "Hubo una señal de reactivación parcial: en mayo de 2026 el empleo formal subió 6% respecto de abril (de 1.586 a 1.681 registrados, según CAMARCO), y el gobierno provincial destacó la suma de casi 100 empleos formales. La magnitud de esa recuperación, sin embargo, es marginal frente a los más de 3.700 puestos perdidos desde 2023.\n\n"
    "<h3>El gigante de hormigón que se durmió (de nuevo)</h3>\n\n"
    "El corazón de la obra pesada en Santa Cruz siempre fueron las represas Néstor Kirchner (Cóndor Cliff) y Jorge Cepernic, sobre el río Santa Cruz. En enero de 2026 llegaron US$136 millones de un crédito con bancos chinos y el proyecto salió de dos años de parálisis: hoy Cóndor Cliff muestra 20% de avance y Cepernic, 42%. Terminada, la obra proyecta generar 4.000 empleos.\n\n"
    "Pero el respiro fue corto. Según la Comisión Interna de la UOCRA en Represas, un nuevo tramo de fondos —también cercano a los US$136 millones— está depositado en el Banco Central desde hace más de cinco meses sin liberarse, lo que volvió a frenar el ritmo de obra y llevó a la empresa constructora a reducir personal. Es ese freno, y no el de años anteriores, el que motivó el corte de esta semana en el puente sobre el río Santa Cruz.\n\n"
    + CREDITO_SATELITAL +
    "<h3>La delegación de las rutas nacionales</h3>\n\n"
    "En abril, el Gobierno nacional publicó el Decreto 253/2026, que delega en nueve provincias —entre ellas Santa Cruz, junto a Corrientes, Santa Fe, Córdoba, San Luis, Mendoza, Río Negro, Neuquén y San Juan— la facultad de concesionar tramos de rutas nacionales, incluidas las rutas 3 y 40. El Estado nacional conserva la titularidad; las provincias podrán licitar, adjudicar y cobrar peaje, con concesiones de hasta 30 años y la obligación de convocar a licitación dentro del año. Los fondos recaudados por peaje solo pueden destinarse al tramo concesionado, no a otras obras.\n\n"
    "En una provincia que arrastra el antecedente de Austral Construcciones y los sobreprecios en la obra pública de la década pasada, el esquema abre una pregunta legítima sobre transparencia en las licitaciones que le tocará responder al gobierno de Claudio Vidal.\n\n"
    "<h3>Lo que está en juego</h3>\n\n"
    "Con salarios reales en baja y una obra clave —las represas— sujeta a la liberación de fondos que ya están depositados, la crisis de la construcción en Santa Cruz combina dos frentes distintos: el ritmo de desembolsos del financiamiento chino y el diseño de las nuevas concesiones viales. Ambos definirán si el sector vuelve a crecer en lo que resta de 2026."
)

cuerpo_en = (
    "On Route 3, “Work Halted” signs are rusting. On the bridge crossing the Santa Cruz River, UOCRA construction workers blocked traffic again this week, demanding the reactivation of the dams on the Santa Cruz River. It's not an isolated scene — it reflects the worst construction employment crisis in the country.\n\n"
    "<h3>The collapse in numbers</h3>\n\n"
    "According to IDARC, INDEC and the Politikón Chaco consultancy, registered construction employment fell 40% year-on-year in the first half of 2026 in Santa Cruz, the steepest drop of any Argentine province. In absolute terms, the sector went from 5,357 jobs in November 2023 to 1,587 in January 2026 — a loss of nearly 3,800 jobs. Measured against the 2007-2023 historical average, the decline reaches 76.2%, the deepest gap in the country.\n\n"
    "The paradox is wages: despite the collapse in employment, the average nominal UOCRA wage in Santa Cruz ($2.2 million pesos) is the highest in the country, a legacy of historically high pay scales in Patagonia. Adjusted for inflation, however, real wages fell 15.9% since November 2023.\n\n"
    "There was a partial recovery signal: in May 2026 formal employment rose 6% versus April (from 1,586 to 1,681 registered workers, per CAMARCO), and the provincial government highlighted the addition of nearly 100 formal jobs. That recovery, however, is marginal against the more than 3,700 jobs lost since 2023.\n\n"
    "<h3>The concrete giant that fell back asleep</h3>\n\n"
    "The heart of heavy construction in Santa Cruz has always been the Néstor Kirchner (Cóndor Cliff) and Jorge Cepernic dams on the Santa Cruz River. In January 2026, US$136 million arrived from a loan with Chinese banks and the project emerged from two years of paralysis: Cóndor Cliff is now 20% complete and Cepernic 42%. Once finished, the project is expected to generate 4,000 jobs.\n\n"
    "But the relief was short-lived. According to the UOCRA's Internal Commission at the dams, a new tranche of funds — also close to US$136 million — has sat deposited at the Central Bank for more than five months without being released, which slowed construction again and led the contractor to cut staff. It is that freeze, not an earlier one, that triggered this week's blockade on the bridge over the Santa Cruz River.\n\n"
    '<div style="font-size:13px;color:#8a8a8a;margin:4px 0 20px">Satellite image of the hydroelectric complex on the Santa Cruz River — Maxar Technologies / Google Earth, 2022.</div>\n\n'
    "<h3>Handing national highways to the provinces</h3>\n\n"
    "In April, the national government issued Decree 253/2026, delegating to nine provinces — including Santa Cruz, alongside Corrientes, Santa Fe, Córdoba, San Luis, Mendoza, Río Negro, Neuquén and San Juan — the power to grant tolled concessions on stretches of national highways, including Routes 3 and 40. The national government keeps ownership; provinces can bid, award contracts and charge tolls, with concessions of up to 30 years and a requirement to launch bidding within one year. Toll revenue can only be spent on the concessioned stretch, not on other works.\n\n"
    "In a province still marked by the Austral Construcciones overpricing scandal from the previous decade, the scheme raises a legitimate question about bidding transparency that Governor Claudio Vidal's administration will have to answer.\n\n"
    "<h3>What's at stake</h3>\n\n"
    "With real wages falling and a flagship project — the dams — hostage to the release of funds that are already deposited, Santa Cruz's construction crisis combines two separate fronts: the pace of Chinese-financed disbursements and the design of the new road concessions. Both will determine whether the sector grows again for the rest of 2026."
)

cuerpo_pt = (
    "Na Rota 3, as placas de “Obra Paralisada” enferrujam. Na ponte sobre o rio Santa Cruz, os trabalhadores da UOCRA voltaram a bloquear a passagem esta semana, exigindo a reativação das represas do rio Santa Cruz. Não é um retrato isolado: reflete a pior crise de emprego na construção de todo o país.\n\n"
    "<h3>O colapso em números</h3>\n\n"
    "Segundo dados do IDARC, INDEC e da consultoria Politikón Chaco, o emprego registrado na construção caiu 40% em relação ao ano anterior no primeiro semestre de 2026 em Santa Cruz, a pior queda entre todas as províncias argentinas. Em termos absolutos, o setor passou de 5.357 postos em novembro de 2023 para 1.587 em janeiro de 2026 — uma perda de quase 3.800 empregos. Medida em relação à média histórica de 2007-2023, a queda chega a 76,2%, a maior diferença do país.\n\n"
    "O dado paradóxico é o salário: apesar do colapso do emprego, o salário nominal médio da UOCRA em Santa Cruz (2,2 milhões de pesos) é o mais alto do país, resultado de escalas historicamente altas na Patagônia. Descontada a inflação, porém, o salário real caiu 15,9% desde novembro de 2023.\n\n"
    "Houve um sinal de recuperação parcial: em maio de 2026 o emprego formal subiu 6% em relação a abril (de 1.586 para 1.681 registrados, segundo a CAMARCO), e o governo provincial destacou a criação de quase 100 empregos formais. Essa recuperação, porém, é marginal diante dos mais de 3.700 postos perdidos desde 2023.\n\n"
    "<h3>O gigante de concreto que voltou a dormir</h3>\n\n"
    "O coração da obra pesada em Santa Cruz sempre foram as represas Néstor Kirchner (Cóndor Cliff) e Jorge Cepernic, sobre o rio Santa Cruz. Em janeiro de 2026 chegaram US$ 136 milhões de um crédito com bancos chineses e o projeto saiu de dois anos de paralisação: hoje Cóndor Cliff tem 20% de avanço e Cepernic, 42%. Concluída, a obra deve gerar 4.000 empregos.\n\n"
    "Mas o alívio durou pouco. Segundo a Comissão Interna da UOCRA nas Represas, um novo lote de fundos — também próximo a US$ 136 milhões — está depositado no Banco Central há mais de cinco meses sem ser liberado, o que voltou a travar o ritmo da obra e levou a construtora a reduzir pessoal. Foi esse novo bloqueio, e não o de anos anteriores, que motivou o corte desta semana na ponte sobre o rio Santa Cruz.\n\n"
    '<div style="font-size:13px;color:#8a8a8a;margin:4px 0 20px">Imagem de satélite do complexo hidrelétrico sobre o rio Santa Cruz — Maxar Technologies / Google Earth, 2022.</div>\n\n'
    "<h3>A delegação das rodovias nacionais</h3>\n\n"
    "Em abril, o governo nacional publicou o Decreto 253/2026, que delega a nove províncias — entre elas Santa Cruz, junto com Corrientes, Santa Fe, Córdoba, San Luis, Mendoza, Río Negro, Neuquén e San Juan — o poder de conceder trechos de rodovias nacionais, incluindo as rotas 3 e 40, mediante pedágio. O Estado nacional mantém a titularidade; as províncias poderão licitar, adjudicar contratos e cobrar pedágio, com concessões de até 30 anos e a obrigação de abrir licitação dentro de um ano. Os recursos arrecadados com pedágio só podem ser usados no trecho concedido, não em outras obras.\n\n"
    "Em uma província marcada pelo antecedente da Austral Construcciones e dos superfaturamentos na obra pública da década passada, o esquema levanta uma pergunta legítima sobre transparência nas licitações, que caberá ao governo de Claudio Vidal responder.\n\n"
    "<h3>O que está em jogo</h3>\n\n"
    "Com salários reais em queda e uma obra-chave — as represas — refém da liberação de fundos que já estão depositados, a crise da construção em Santa Cruz combina duas frentes distintas: o ritmo dos desembolsos do financiamento chinês e o desenho das novas concessões rodoviárias. Ambos definirão se o setor volta a crescer no restante de 2026."
)

cuerpo_zh = (
    "在·3号公路上，“工程停工”的告示牌正在生锈。本周，在横跨圣克鲁斯河的大桥上，UOCRA建筑工会工人再次封锁道路，要求重启圣克鲁斯河大坝工程。这并非孤立场景，而是全国建筑业就业危机最为严重的写照。\n\n"
    "<h3>数字背后的崩溃</h3>\n\n"
    "根据IDARC、INDEC（阿根廷国家统计局）和Politikón Chaco咨询机构的数据，2026年上半年，圣克鲁斯省建筑业registered就业同比下降40%，是阿根廷所有省份中跌幅最大的。绝对数值上，该行业从2023年11月的5,357个岗位降至2026年1月的1,587个，损失近3,800个就业岗位。与2007-2023年历史平均水平相比，降幅达到76.2%，是全国差距最深的省份。\n\n"
    "矛盾的是工资数据：尽管就业市场崩溃，圣克鲁斯省UOCRA工人的平均名义工资（220万比索）却是全国最高，这得益于巴塔哥尼亚地区历来较高的工资标准。但剔除通胀因素后，自2023年11月以来实际工资下降了15.9%。\n\n"
    "市场出现部分回暖迹象：据CAMARCO（阿根廷建筑商会）数据，2026年5月正规就业环比4月增长6%（从1,586人增至1,681人），省政府也强调新增了近100个正规就业岗位。然而，相较于2023年以来流失的3,700多个岗位，这一回升幅度微不足道。\n\n"
    "<h3>再度沉睡的混凝土巨人</h3>\n\n"
    "圣克鲁斯省重型工程建设的核心，一直是位于圣克鲁斯河上的内斯托尔·基什内尔（孔多尔崖）和豪尔赫·塞佩尔尼克两座大坝。2026年1月，一笔来自中国银行贷款的1.36亿美元资金到位，项目结束了长达两年的停滞：目前孔多尔崖大坝工程进度为20%，塞佩尔尼克大坝为42%。工程完工后预计将创造4,000个就业岗位。\n\n"
    "但喘息期十分短暂。据UOCRA大坝工程内部委员会称，另一笔同样约1.36亿美元的资金已在阿根廷中央银行存放超过五个月未予拨付，这再次拖慢了工程进度，并促使承建企业裁减人员。正是这笔新的资金冻结，而非此前年份的旧问题，引发了本周在圣克鲁斯河大桥上的封路行动。\n\n"
    '<div style="font-size:13px;color:#8a8a8a;margin:4px 0 20px">圣克鲁斯河水电综合体卫星图像 — Maxar Technologies / 谷歌地球，2022年。</div>\n\n'
    "<h3>国道管理权下放</h3>\n\n"
    "今年4月，阿根廷国家政府颁布了253/2026号法令，将包括圣克鲁斯省在内的九个省份——科连特斯、圣菲、科尔多瓦、圣路易斯、门多莎、里奥内格罗、内乌肯和圣胡安——授权可对国道路段（包括3号和40号公路）实行收费特许经营。国家政府保留路权所有权；各省可组织招标、授予合同并收取通行费，特许经营期最长可达30年，并须在一年内启动招标。通行费收入只能用于所特许经营的路段，不得挪作他用。\n\n"
    "这个省份仍背负着上个十年“奥斯特拉尔建筑公司”（Austral Construcciones）公共工程超支丑闻的历史包袱，该方案由此引发了关于招标透明度的合理质疑，克劳迪奥·比达尔省长领导的政府将不得不对此作出回应。\n\n"
    "<h3>利害攸关</h3>\n\n"
    "实际工资持续下滑，而关键工程——大坝——的命运又系于已存入但尚未拨付的资金能否释放，圣克鲁斯省的建筑业危机由此交织着两条不同的战线：中国融资的拨付节奏，以及新公路特许经营方案的设计。这两者将共同决定该行业在2026年剩余时间能否重新实现增长。"
)

nueva_entrada = {
    "id": "20260824-propio-santa-cruz-construccion",
    "titulo": "Santa Cruz: la construcción registra la peor caída de todo el país",
    "bajada": "El empleo en la industria cayó 40% interanual en el primer semestre de 2026 — la peor performance del país — y acumula la brecha más profunda respecto al promedio histórico. La UOCRA volvió a cortar la Ruta 3 esta semana por el freno a los fondos de las represas del río Santa Cruz.",
    "cuerpo": cuerpo,
    "tag": "🏗️ Empleo & Obra Pública",
    "categoria": "economia|empleo|construccion|santa-cruz|obra-publica",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "argentina",
    "imagen": "fotos/ENERGIA/protesta-uocra-obra-publica-2026.webp",
    "imagen_keywords": "uocra protesta construccion santa cruz obra publica empleo",
    "meta": "24 de Agosto de 2026 · J. Martineau",
    "excluir_feed": True,
    "galeria": [
        "fotos/ENERGIA/protesta-uocra-corte-ruta-nacional.webp",
        "fotos/ENERGIA/represa-jorge-cepernic-satelital.webp"
    ],
    "titulo_en": "Santa Cruz: Argentina's Sharpest Construction Collapse",
    "bajada_en": "Construction employment fell 40% year-on-year in the first half of 2026 — the worst performance in the country — marking the deepest gap versus the historical average. The UOCRA union blocked Route 3 again this week over stalled dam funding on the Santa Cruz River.",
    "cuerpo_en": cuerpo_en,
    "titulo_pt": "Santa Cruz: a construção registra a pior queda do país",
    "bajada_pt": "O emprego na construção caiu 40% em relação ao ano anterior no primeiro semestre de 2026 — o pior desempenho do país — e marca a maior diferença em relação à média histórica. A UOCRA voltou a bloquear a Rota 3 esta semana por causa do congelamento dos fundos das represas do rio Santa Cruz.",
    "cuerpo_pt": cuerpo_pt,
    "titulo_zh": "圣克鲁斯省:建筑业遭遇全国最严重萎缩",
    "bajada_zh": "2026年上半年,圣克鲁斯省建筑业就业同比下降40%,为全国表现最差,创下与历史平均水平差距最大的纪录。本周,UOCRA工会因圣克鲁斯河大坝资金被冻结再次封锁3号公路。",
    "cuerpo_zh": cuerpo_zh
}

with open(PROPIOS, "r", encoding="utf-8") as f:
    propios = json.load(f)

with open(HISTORIAL, "r", encoding="utf-8") as f:
    historial = json.load(f)

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
