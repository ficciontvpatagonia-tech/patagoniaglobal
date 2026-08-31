#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Publica el informe "EEUU amenaza con soltarle la mano a Londres por Malvinas"
# en propios.json (modelo: publicar_kelper_reaccion_bandera.py)
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

def quote(txt):
    return ('<blockquote style="border-left:4px solid #7aadcc;margin:2rem 0;'
            'padding:.4rem 0 .4rem 1.4rem;font-size:1.25rem;line-height:1.5;'
            f'font-style:italic">{txt}</blockquote>')

IMG_PORTADA = "fotos/malvinas-milei-trump.webp"
IMG_PARLAMENTO = "fotos/malvinas-parlamento-britanico.webp"

# ============================== ESPAÑOL ==============================
cuerpo = "\n\n".join([
    DATELINE.format("Malvinas — Informe GLOBALpatagonia"),

    "<p>La administración Trump volvió a poner a Malvinas en el tablero de la geopolítica, esta vez como herramienta de presión dentro de la OTAN. Según reveló el diario británico <em>The Telegraph</em>, altos funcionarios del Pentágono evalúan retirar el respaldo político que Estados Unidos le da tradicionalmente al Reino Unido sobre la soberanía de las islas si el gobierno de Andy Burnham no eleva su inversión en Defensa hasta el 5% del Producto Bruto Interno, el número que exige la Alianza Atlántica a sus miembros.</p>",

    "<h3>Una ficha más en la mesa de la OTAN</h3>",

    "<p>La jugada encaja en la estrategia de Trump de forzar a los socios europeos de la OTAN a pagar más por su propia defensa —lo que en Washington ya llaman informalmente “OTAN 3.0”— y no implica, por ahora, un respaldo formal al reclamo argentino. El embajador estadounidense en Buenos Aires, Peter Lamelas, lo dejó claro semanas atrás:</p>",

    quote("“Los Estados Unidos tienen una posición de neutralidad sobre las islas. Eso no ha cambiado”."),

    img_block(IMG_PORTADA, "Javier Milei y Donald Trump",
              "El vínculo entre Washington y Buenos Aires atraviesa el trasfondo de una advertencia que, en los hechos, tensiona a Londres dentro de la propia OTAN."),

    "<h3>Londres se sacude</h3>",

    "<p>Pero la sola mención alcanzó para sacudir al Reino Unido. El presupuesto de Defensa que había presentado el Tesoro británico generó una catarata de críticas internas. La diputada conservadora Priti Patel escribió en X:</p>",

    quote("“El fracaso del Partido Laborista en comprometerse con el 3% del PBI en defensa nos ha dejado expuestos”."),

    "<p>Su compañero de bancada James Cartlidge fue más allá: “Las Malvinas son británicas. Punto final”. Y hasta el laborista Adam Jogee, del propio oficialismo, coincidió en el fondo: “Seamos muy claros: las Malvinas son británicas. Así de simple”.</p>",

    "<p>La ministra Bridget Phillipson evitó pronunciarse sobre la soberanía en una entrevista radial y se limitó a defender el nivel de gasto militar: “Estamos invirtiendo más que en cualquier otro momento desde la Guerra Fría”.</p>",

    img_block(IMG_PARLAMENTO, "Cámara de los Comunes del Parlamento británico",
              "El presupuesto de Defensa británico y la advertencia de Washington reabrieron, una vez más, el debate sobre Malvinas en el Parlamento."),

    "<h3>No es la primera vez</h3>",

    "<p>No es la primera vez que el tema aparece en Washington como ficha de negociación. En abril, un correo interno del Pentágono revelado por Reuters ya había expuesto que, ante la negativa de algunos socios europeos a respaldar operaciones militares en la guerra contra Irán, una de las opciones discutidas era revisar el apoyo diplomático a la administración británica de las islas. En su momento, el secretario de Estado Marco Rubio le bajó el tono al episodio: “un mail con algunas ideas”.</p>",

    "<h3>Cautela en la Cancillería argentina</h3>",

    "<p>Del lado argentino, la reacción oficial fue de cautela. Fuentes de Cancillería consultadas por Infobae señalaron que la posición debe leerse “en el marco de una estrategia de la administración Trump sobre los aliados de la OTAN, y no como un giro formal en la política exterior estadounidense”. Aun así, en el Gobierno no ocultan la expectativa: cualquier grieta en el respaldo histórico de Estados Unidos a Londres —por motivos ajenos a la causa Malvinas en sí— abre una ventana que Buenos Aires no tenía hace apenas una semana.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Fuentes: Página12, Infobae, <em>The Telegraph</em> (original), Canal26, BAE Negocios, Noticias Argentinas.</p>',
])

# ============================== ENGLISH ==============================
cuerpo_en = "\n\n".join([
    DATELINE.format("Malvinas — GLOBALpatagonia Report"),

    "<p>The Trump administration has put Malvinas (the Falkland Islands) back on the geopolitical chessboard, this time as a pressure tool inside NATO. According to the British newspaper <em>The Telegraph</em>, senior Pentagon officials are weighing whether to withdraw the political backing the United States traditionally gives the United Kingdom over sovereignty of the islands, unless Prime Minister Andy Burnham's government raises defence spending to the 5% of GDP the Atlantic Alliance demands of its members.</p>",

    "<h3>One more bargaining chip at the NATO table</h3>",

    "<p>The move fits Trump's broader strategy of forcing NATO's European partners to pay more for their own defence — informally dubbed “NATO 3.0” in Washington — and does not, for now, amount to formal support for Argentina's claim. The US ambassador in Buenos Aires, Peter Lamelas, made that clear weeks ago:</p>",

    quote("“The United States holds a position of neutrality on the islands. That has not changed.”"),

    img_block(IMG_PORTADA, "Javier Milei and Donald Trump",
              "The Washington–Buenos Aires relationship sits in the background of a warning that, in practice, puts pressure on London within NATO itself."),

    "<h3>London rattled</h3>",

    "<p>But the mere mention was enough to rattle Britain. The defence budget presented by the UK Treasury drew a wave of internal criticism. Conservative MP Priti Patel wrote on X:</p>",

    quote("“Labour's failure to commit to 3% of GDP on defence has left us exposed.”"),

    "<p>Fellow Conservative James Cartlidge went further: “The Falklands are British. Full stop.” Even Labour's own Adam Jogee agreed on the substance: “Let's be very clear: the Falklands are British. It's as simple as that.”</p>",

    "<p>Minister Bridget Phillipson avoided the sovereignty question in a radio interview and instead defended the spending level: “We are investing more than at any point since the Cold War.”</p>",

    img_block(IMG_PARLAMENTO, "The House of Commons at the British Parliament",
              "Britain's defence budget and Washington's warning reopened, once again, the debate over Malvinas (the Falklands) in Parliament."),

    "<h3>Not the first time</h3>",

    "<p>This is not the first time the issue has surfaced in Washington as a bargaining chip. In April, an internal Pentagon email revealed by Reuters had already shown that, faced with some European allies' refusal to back military operations in the war against Iran, one of the options discussed was reviewing diplomatic support for Britain's administration of the islands. At the time, Secretary of State Marco Rubio played the episode down: “an email with some ideas.”</p>",

    "<h3>Caution at Argentina's Foreign Ministry</h3>",

    "<p>On the Argentine side, the official reaction was cautious. Foreign Ministry sources consulted by Infobae said the position should be read “within the framework of a Trump administration strategy toward NATO allies, not as a formal shift in US foreign policy.” Even so, the government does not hide its expectations: any crack in Washington's historical backing of London — for reasons unrelated to the Malvinas cause itself — opens a window Buenos Aires didn't have just a week ago.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Sources: Página12, Infobae, <em>The Telegraph</em> (original), Canal26, BAE Negocios, Noticias Argentinas.</p>',
])

# ============================== PORTUGUÊS ==============================
cuerpo_pt = "\n\n".join([
    DATELINE.format("Malvinas — Relatório GLOBALpatagonia"),

    "<p>O governo Trump voltou a colocar as Malvinas no tabuleiro geopolítico, desta vez como ferramenta de pressão dentro da OTAN. Segundo revelou o jornal britânico <em>The Telegraph</em>, altos funcionários do Pentágono avaliam retirar o apoio político que os Estados Unidos tradicionalmente dão ao Reino Unido sobre a soberania das ilhas, caso o governo de Andy Burnham não eleve seu investimento em Defesa para 5% do PIB, o número exigido pela Aliança Atlântica a seus membros.</p>",

    "<h3>Mais uma ficha na mesa da OTAN</h3>",

    "<p>A jogada encaixa na estratégia de Trump de forçar os parceiros europeus da OTAN a pagar mais por sua própria defesa —o que em Washington já chamam informalmente de “OTAN 3.0”— e não implica, por ora, um apoio formal ao reclamo argentino. O embaixador americano em Buenos Aires, Peter Lamelas, deixou isso claro semanas atrás:</p>",

    quote("“Os Estados Unidos mantêm uma posição de neutralidade sobre as ilhas. Isso não mudou.”"),

    img_block(IMG_PORTADA, "Javier Milei e Donald Trump",
              "O vínculo entre Washington e Buenos Aires está no pano de fundo de um aviso que, na prática, pressiona Londres dentro da própria OTAN."),

    "<h3>Londres se abala</h3>",

    "<p>Mas a simples menção já bastou para abalar o Reino Unido. O orçamento de Defesa apresentado pelo Tesouro britânico gerou uma onda de críticas internas. A deputada conservadora Priti Patel escreveu no X:</p>",

    quote("“O fracasso do Partido Trabalhista em se comprometer com 3% do PIB em defesa nos deixou expostos.”"),

    "<p>Seu colega de bancada James Cartlidge foi além: “As Malvinas são britânicas. Ponto final.” E até o trabalhista Adam Jogee, do próprio governo, concordou no fundo: “Sejamos muito claros: as Malvinas são britânicas. É simples assim.”</p>",

    "<p>A ministra Bridget Phillipson evitou se pronunciar sobre a soberania em uma entrevista de rádio e se limitou a defender o nível de gasto militar: “Estamos investindo mais do que em qualquer outro momento desde a Guerra Fria.”</p>",

    img_block(IMG_PARLAMENTO, "Câmara dos Comuns do Parlamento britânico",
              "O orçamento de Defesa britânico e o aviso de Washington reabriram, mais uma vez, o debate sobre as Malvinas no Parlamento."),

    "<h3>Não é a primeira vez</h3>",

    "<p>Não é a primeira vez que o tema aparece em Washington como ficha de negociação. Em abril, um e-mail interno do Pentágono revelado pela Reuters já havia mostrado que, diante da recusa de alguns aliados europeus em apoiar operações militares na guerra contra o Irã, uma das opções discutidas era rever o apoio diplomático à administração britânica das ilhas. Na ocasião, o secretário de Estado Marco Rubio minimizou o episódio: “um e-mail com algumas ideias.”</p>",

    "<h3>Cautela na Chancelaria argentina</h3>",

    "<p>Do lado argentino, a reação oficial foi de cautela. Fontes do Ministério das Relações Exteriores consultadas pela Infobae afirmaram que a posição deve ser lida “no marco de uma estratégia do governo Trump em relação aos aliados da OTAN, e não como uma mudança formal na política externa americana”. Ainda assim, o governo não esconde a expectativa: qualquer rachadura no apoio histórico dos Estados Unidos a Londres —por motivos alheios à própria causa Malvinas— abre uma janela que Buenos Aires não tinha há apenas uma semana.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Fontes: Página12, Infobae, <em>The Telegraph</em> (original), Canal26, BAE Negocios, Noticias Argentinas.</p>',
])

# ============================== 中文 ==============================
cuerpo_zh = "\n\n".join([
    DATELINE.format("马尔维纳斯 — GLOBALpatagonia 深度报道"),

    "<p>特朗普政府再次把马尔维纳斯群岛（福克兰群岛）摆上了地缘政治的棋盘，这一次是作为北约内部的施压筹码。据英国《每日电讯报》（<em>The Telegraph</em>）披露，五角大楼高层官员正在评估：如果安迪·伯纳姆领导的英国政府不将国防投入提高到北约要求成员国达到的GDP 5%，美国可能撤回其一贯给予英国、支持其对该群岛拥有主权的政治背书。</p>",

    "<h3>北约谈判桌上的又一枚筹码</h3>",

    "<p>这一举动符合特朗普一贯的策略：迫使北约的欧洲盟友为自身防务承担更多费用——华盛顿内部已非正式地称之为“北约3.0”——目前尚不意味着对阿根廷主权诉求的正式支持。美国驻布宜诺斯艾利斯大使彼得·拉梅拉斯几周前已明确表态：</p>",

    quote("“美国在群岛问题上保持中立立场，这一点没有改变。”"),

    img_block(IMG_PORTADA, "哈维尔·米莱与唐纳德·特朗普",
              "华盛顿与布宜诺斯艾利斯之间的关系，正是这场实际上对伦敦在北约内部构成压力的警告的背景。"),

    "<h3>伦敦为之震动</h3>",

    "<p>但仅仅是这一提法，就足以让英国感到震动。英国财政部提出的国防预算引发了国内一片批评声浪。保守党议员普里蒂·帕特尔在X平台上写道：</p>",

    quote("“工党未能承诺将GDP的3%用于国防，这让我们暴露在风险之中。”"),

    "<p>她的同党议员詹姆斯·卡特利奇则说得更直白：“福克兰群岛是英国的。就这么简单。”甚至连执政的工党议员亚当·约吉也在实质上表示认同：“我们要说清楚：福克兰群岛是英国的，就是这么简单。”</p>",

    "<p>大臣布里奇特·菲利普森在一次电台采访中回避了主权问题，只是为国防开支水平进行了辩护：“我们的投入是冷战结束以来任何时期都无法比拟的。”</p>",

    img_block(IMG_PARLAMENTO, "英国议会下议院",
              "英国的国防预算与华盛顿的警告，再次在议会内重新引发了关于马尔维纳斯群岛的辩论。"),

    "<h3>并非第一次</h3>",

    "<p>这并非华盛顿第一次把这一议题当作谈判筹码。今年4月，路透社披露的一封五角大楼内部邮件就曾显示：面对部分欧洲盟友拒绝支持对伊朗的军事行动，讨论中的选项之一，就是重新评估对英国管理该群岛的外交支持。当时，国务卿马尔科·鲁比奥淡化了这一事件：“只是一封提了一些想法的邮件。”</p>",

    "<h3>阿根廷外交部保持谨慎</h3>",

    "<p>在阿根廷一方，官方反应保持谨慎。Infobae援引外交部消息人士的话说，这一立场应被解读为“特朗普政府针对北约盟友的一项战略框架，而非美国对外政策的正式转向”。尽管如此，阿根廷政府也毫不掩饰自己的期待：美国对伦敦历来的支持出现任何裂痕——哪怕原因与马尔维纳斯议题本身无关——都为布宜诺斯艾利斯打开了一周前还不存在的一扇窗口。</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">资料来源：Página12、Infobae、《每日电讯报》（原文）、Canal26、BAE Negocios、Noticias Argentinas。</p>',
])

FECHA_META = "30 de agosto de 2026 · J. Martineau"

nueva_entrada = {
    "id": "20260830-propio-malvinas-eeuu-otan",
    "titulo": "EEUU amenaza con soltarle la mano a Londres por Malvinas",
    "bajada": "Washington le exige al Reino Unido subir su gasto militar en la OTAN al 5% del PBI — y usa el reclamo argentino como moneda de presión. El gobierno argentino, cauteloso: “no es un giro, es presión a la OTAN”.",
    "cuerpo": cuerpo,
    "titulo_en": "US threatens to let go of London's hand over Malvinas",
    "bajada_en": "Washington is demanding the UK raise its NATO defence spending to 5% of GDP — using Argentina's sovereignty claim as leverage. Argentina's government, cautious: “it's not a shift, it's pressure on NATO.”",
    "cuerpo_en": cuerpo_en,
    "titulo_pt": "EUA ameaçam soltar a mão de Londres nas Malvinas",
    "bajada_pt": "Washington exige que o Reino Unido eleve seu gasto militar na OTAN para 5% do PIB — e usa o reclamo argentino como moeda de pressão. O governo argentino, cauteloso: “não é uma mudança, é pressão sobre a OTAN”.",
    "cuerpo_pt": cuerpo_pt,
    "titulo_zh": "美国以放手英国相要挟,借马尔维纳斯向北约施压",
    "bajada_zh": "华盛顿要求英国将北约防务开支提高至GDP的5%——并利用阿根廷的主权诉求作为筹码。阿根廷政府态度谨慎:“这不是政策转向,而是对北约的施压”。",
    "cuerpo_zh": cuerpo_zh,
    "tag": "🇦🇷 Malvinas",
    "categoria": "malvinas|politica|internacional",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "malvinas",
    "imagen": IMG_PORTADA,
    "imagen_keywords": "malvinas eeuu trump otan reino unido presion soberania washington",
    "hashtags_en": "#Malvinas #Falklands #USA #NATO #UK",
    "meta": FECHA_META,
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
