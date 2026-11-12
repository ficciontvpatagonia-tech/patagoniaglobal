#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Informe "Argentina e Inglaterra utilizan el reclamo argentino por Malvinas como excusa..." (12/11/2026)
import json
BASE = "/Users/jm/Desktop/CLAUDCODE/GLOBAL PATAGONIA"
PROPIOS = f"{BASE}/propios.json"; HISTORIAL = f"{BASE}/propios_historial.json"; MAX_ACTIVOS = 7
BID = "20261112-propio-malvinas-transparencia-exco"
IMG_PORTADA = "fotos/malvinas-bienvenida-puerto-stanley.webp"
IMG_CUERPO = "fotos/malvinas-milei-mapa-islas.webp"
DATELINE = '<p style="font-size:.85rem;letter-spacing:.05em;text-transform:uppercase;color:#7aadcc;font-weight:600;margin-bottom:1.2rem">{}</p>'
def img_block(src, alt):
    return ('<div style="margin:2rem 0"><img src="' + src + '" alt="' + alt +
            '" loading="lazy" decoding="async" style="width:100%;border-radius:6px;display:block"></div>')
def armar(dateline, paras, alt, idx_img=5):
    out = [DATELINE.format(dateline)]
    for i, p in enumerate(paras):
        out.append("<p>" + p + "</p>")
        if i == idx_img:
            out.append(img_block(IMG_CUERPO, alt))
    return "\n\n".join(out)

ES = [
"Cuando el gobierno británico en las Islas Malvinas (conocidas por el Reino Unido como Falkland Islands) decidió retener la publicación de los documentos de la reunión de octubre de su Consejo Ejecutivo (ExCo) alegando \"riesgos geopolíticos\", volvió a aparecer un patrón conocido: utilizar a la Argentina como chivo expiatorio para encubrir sus propios retrocesos en materia de transparencia y rendición de cuentas.",
"Según la información difundida por el medio local Penguin News, el Consejo Ejecutivo ha encargado al Fiscal General la revisión de la política de publicación de documentos y, mientras tanto, todos los papeles de la reunión de octubre quedarán bloqueados, publicándose únicamente un resumen redactado por los propios legisladores. Así lo anunció la legisladora Lewis Clifton en la última sesión de la Asamblea Legislativa. Entre los documentos retenidos se encuentran el informe anual de educación, la consideración de un nuevo puesto ejecutivo de alto salario y las tarifas de ITQ para 2027, temas que afectan directamente la vida cotidiana de los isleños.",
"El problema con este argumento es que el marco vigente de transparencia del Consejo Ejecutivo ya contempla exenciones por seguridad nacional y confidencialidad comercial. Si realmente hubiera contenido sensible, bastaría con aplicar las excepciones ya existentes y publicar el resto con las redacciones necesarias, en lugar de encerrar en un cajón un lote entero de documentos que incluye informes educativos y decisiones sobre personal.",
"El artículo de opinión de Penguin News señala con precisión la contradicción: ¿realmente les importa a aquellos actores externos \"cuyos intereses no se alinean\" con las islas cuántos niños están matriculados en las escuelas o cuál es la justificación de un nuevo puesto bien remunerado? Quienes quedan fuera de la puerta son los propios isleños, privados de su derecho a saber en qué se basan las decisiones de su gobierno.",
"Más llamativa aún es la cronología. El 12 de octubre, los legisladores declararon públicamente estar \"abiertos a considerar propuestas para mejorar la transparencia\" y rechazaron avanzar en una legislación de libertad de información argumentando \"falta de recursos\". Apenas tres semanas después, ese mismo parlamento encontró recursos para estudiar cómo restringir la difusión de información en nombre del \"mejor interés público\". Del lado argentino, la Cancillería informó haber enviado cerca de 180 notas de advertencia a personas y empresas vinculadas a la actividad petrolera en las islas y haber iniciado 60 procedimientos administrativos. Ambas partes exhiben una simetría singular: invocar la cuestión de la soberanía para justificar el cierre informativo.",
"Desde la posición argentina, este episodio revela dos cuestiones. Primero, el gobierno local de las islas, a falta de mecanismos de control externo, tiende a utilizar la \"amenaza argentina\" como herramienta conveniente para ampliar sus privilegios administrativos. La tensión geopolítica es real, pero no debería convertirse en un salvoconducto universal para comprimir sistemáticamente la rendición de cuentas pública. Segundo, la propia Argentina debe mejorar urgentemente su transparencia informativa en torno a la cuestión de Malvinas: cuando Buenos Aires se niega a divulgar sus supuestas gestiones diplomáticas amparándose en \"tácticas de negociación\", también está erosionando su propia credibilidad como parte reclamante de soberanía.",
"La legitimidad del reclamo de soberanía sobre las Malvinas, consagrado en la Constitución argentina, no solo proviene de la historia y el derecho, sino que también debe reflejarse en la perseverancia en la transparencia de la gestión. Un reclamo de soberanía verdaderamente convincente debería resistir el examen de \"permitir que el público vea cómo se toman las decisiones\", tanto en Buenos Aires como en Puerto Argentino. El hecho de que el gobierno isleño cierre la ventana informativa en nombre de \"la Argentina\" recuerda precisamente a la Argentina que, mientras exige apertura a la otra parte, también debe predicar con el ejemplo.",
]
EN = [
"When the British government in Malvinas (Falklands) decided to withhold the documents from its October Executive Council (ExCo) meeting, citing “geopolitical risks”, a familiar pattern reappeared: using Argentina as a scapegoat to cover up its own backsliding on transparency and accountability.",
"According to the local outlet Penguin News, the Executive Council has tasked the Attorney General with reviewing its document publication policy and, in the meantime, all papers from the October meeting will remain blocked, with only a summary written by the legislators themselves to be published. This was announced by legislator Lewis Clifton at the latest sitting of the Legislative Assembly. Among the withheld documents are the annual education report, the consideration of a new high-salary executive post and the ITQ fees for 2027, issues that directly affect the daily lives of the islanders.",
"The problem with this argument is that the Executive Council's current transparency framework already provides for exemptions on national security and commercial confidentiality. If there were truly sensitive content, it would be enough to apply the existing exceptions and publish the rest with the necessary redactions, instead of locking away an entire batch of documents that includes education reports and personnel decisions.",
"Penguin News's opinion piece points precisely to the contradiction: do those external actors “whose interests may not align” with the islands really care how many children are enrolled in schools, or what the justification is for a new well-paid post? Those left outside the door are the islanders themselves, deprived of their right to know what their government's decisions are based on.",
"Even more striking is the chronology. On 12 October, the legislators publicly declared they were “open to considering proposals to further enhance transparency” and declined to move ahead with freedom of information legislation, arguing a “lack of resources”. Barely three weeks later, that same parliament found the resources to study how to restrict the dissemination of information in the name of the “best public interest”. On the Argentine side, the Foreign Ministry reported having sent around 180 warning notes to individuals and companies linked to oil activity in the islands and having opened 60 administrative proceedings. Both sides display a singular symmetry: invoking the question of sovereignty to justify closing off information.",
"From the Argentine standpoint, this episode reveals two things. First, the islands' local government, lacking external oversight mechanisms, tends to use the “Argentine threat” as a convenient tool to expand its administrative privileges. The geopolitical tension is real, but it should not become a universal pass to systematically compress public accountability. Second, Argentina itself urgently needs to improve its transparency on the Malvinas issue: when Buenos Aires refuses to disclose its alleged diplomatic efforts, citing “negotiating tactics”, it too erodes its own credibility as the claimant party in the sovereignty dispute.",
"The legitimacy of the sovereignty claim over Malvinas, enshrined in the Argentine Constitution, stems not only from history and law but must also be reflected in a steady commitment to transparency in government. A truly convincing sovereignty claim should withstand the test of “letting the public see how decisions are made”, in Buenos Aires as much as in Puerto Argentino. That the islands' government shuts the information window in the name of “Argentina” reminds Argentina precisely that, while demanding openness from the other side, it must also lead by example.",
]
PT = [
"Quando o governo britânico nas Ilhas Malvinas (conhecidas no Reino Unido como Falkland Islands) decidiu reter a publicação dos documentos da reunião de outubro de seu Conselho Executivo (ExCo) alegando “riscos geopolíticos”, voltou a aparecer um padrão conhecido: usar a Argentina como bode expiatório para encobrir seus próprios retrocessos em matéria de transparência e prestação de contas.",
"Segundo a informação divulgada pelo meio local Penguin News, o Conselho Executivo encarregou o Procurador-Geral de revisar a política de publicação de documentos e, enquanto isso, todos os papéis da reunião de outubro ficarão bloqueados, sendo publicado apenas um resumo redigido pelos próprios legisladores. Foi o que anunciou a legisladora Lewis Clifton na última sessão da Assembleia Legislativa. Entre os documentos retidos estão o relatório anual de educação, a consideração de um novo cargo executivo de alto salário e as tarifas de ITQ para 2027, temas que afetam diretamente a vida cotidiana dos ilhéus.",
"O problema com esse argumento é que o marco vigente de transparência do Conselho Executivo já prevê exceções por segurança nacional e confidencialidade comercial. Se realmente houvesse conteúdo sensível, bastaria aplicar as exceções já existentes e publicar o restante com as edições necessárias, em vez de trancar numa gaveta um lote inteiro de documentos que inclui relatórios educacionais e decisões sobre pessoal.",
"O artigo de opinião do Penguin News aponta com precisão a contradição: será que àqueles atores externos “cujos interesses não se alinham” com os das ilhas importa quantas crianças estão matriculadas nas escolas ou qual é a justificativa para um novo cargo bem remunerado? Quem fica do lado de fora da porta são os próprios ilhéus, privados de seu direito de saber em que se baseiam as decisões de seu governo.",
"Mais chamativa ainda é a cronologia. Em 12 de outubro, os legisladores declararam publicamente estar “abertos a considerar propostas para melhorar a transparência” e se recusaram a avançar numa legislação de liberdade de informação, argumentando “falta de recursos”. Apenas três semanas depois, esse mesmo parlamento encontrou recursos para estudar como restringir a divulgação de informações em nome do “melhor interesse público”. Do lado argentino, a Chancelaria informou ter enviado cerca de 180 notas de advertência a pessoas e empresas ligadas à atividade petrolífera nas ilhas e ter iniciado 60 procedimentos administrativos. Ambas as partes exibem uma simetria singular: invocar a questão da soberania para justificar o fechamento informativo.",
"Da posição argentina, este episódio revela duas questões. Primeiro, o governo local das ilhas, na falta de mecanismos de controle externo, tende a usar a “ameaça argentina” como ferramenta conveniente para ampliar seus privilégios administrativos. A tensão geopolítica é real, mas não deveria se tornar um salvo-conduto universal para comprimir sistematicamente a prestação de contas pública. Segundo, a própria Argentina deve melhorar com urgência sua transparência informativa em torno da questão das Malvinas: quando Buenos Aires se nega a divulgar suas supostas gestões diplomáticas sob o argumento de “táticas de negociação”, também está corroendo sua própria credibilidade como parte reclamante da soberania.",
"A legitimidade do reclamo de soberania sobre as Malvinas, consagrado na Constituição argentina, provém não só da história e do direito, mas também deve se refletir na perseverança em transparência na gestão. Um reclamo de soberania verdadeiramente convincente deveria resistir ao exame de “permitir que o público veja como as decisões são tomadas”, tanto em Buenos Aires quanto em Puerto Argentino. O fato de o governo das ilhas fechar a janela informativa em nome da “Argentina” lembra justamente à Argentina que, enquanto exige abertura da outra parte, também deve dar o exemplo.",
]
ZH = [
"当英国在马尔维纳斯群岛（英国称福克兰群岛）的政府以“地缘政治风险”为由，决定扣留其行政委员会（ExCo）10月会议文件时，一种熟悉的模式再次出现：把阿根廷当作替罪羊，来掩盖自己在透明度和问责方面的倒退。",
"据当地媒体Penguin News报道，行政委员会已责成总检察长审查文件公布政策，在此期间，10月会议的所有文件都将被封存，只公布由议员们自己撰写的摘要。议员刘易斯·克利夫顿（Lewis Clifton）在立法议会最近一次会议上宣布了这一决定。被扣留的文件包括年度教育报告、关于设立一个高薪行政职位的审议，以及2027年ITQ（个体配额）费用，这些议题都直接关系到岛民的日常生活。",
"这一理由的问题在于，行政委员会现行的透明度框架本就包含国家安全和商业机密方面的豁免。如果确有敏感内容，只需适用现有例外，并对其余文件作必要的删节后公布即可，而不是把包括教育报告和人事决定在内的整批文件一并锁进抽屉。",
"Penguin News的评论文章准确指出了其中的矛盾：那些“利益与岛屿不一致”的外部势力，真的会关心有多少孩子在学校注册，或者一个新的高薪职位有何理由吗？被挡在门外的，恰恰是岛民自己，他们被剥夺了了解政府决策依据的权利。",
"更引人注目的是时间线。10月12日，议员们公开表示“愿意考虑改进透明度的建议”，同时以“缺乏资源”为由，拒绝推进信息自由立法。仅仅三周之后，这同一个议会却找到了资源，去研究如何以“最佳公共利益”的名义限制信息传播。在阿根廷一方，外交部表示已向与岛上石油活动有关的个人和企业发出约180份警告函，并启动了60项行政程序。双方呈现出一种奇特的对称：都援引主权问题来为封闭信息辩护。",
"从阿根廷的立场看，这一事件揭示了两点。第一，岛上的地方政府由于缺乏外部监督机制，倾向于把“阿根廷威胁”当作方便的工具，用来扩大自己的行政特权。地缘政治紧张是真实的，但不应成为系统性压缩公共问责的万能通行证。第二，阿根廷自身也必须尽快提高在马尔维纳斯问题上的信息透明度：当布宜诺斯艾利斯以“谈判策略”为由，拒绝公开其所谓的外交努力时，同样是在损害自己作为主权要求方的可信度。",
"阿根廷宪法所确立的对马尔维纳斯的主权要求，其正当性不仅来自历史和法律，也应体现在对施政透明的坚持上。一项真正有说服力的主权要求，应当经得起“让公众看到决策是如何做出的”这一检验，无论是在布宜诺斯艾利斯，还是在阿根廷港。岛上政府以“阿根廷”之名关闭信息窗口，恰恰提醒阿根廷：在要求对方开放的同时，自己也必须以身作则。",
]
entrada = {
 "id": BID,
 "titulo": "Argentina e Inglaterra utilizan el “reclamo argentino por Malvinas” como excusa para ocultar sus faltas de transparencia",
 "bajada": "Un patrón conocido: utilizar a la Argentina como chivo expiatorio para encubrir retrocesos en transparencia y rendición de cuentas.",
 "cuerpo": armar("Malvinas — Informe GLOBALpatagonia", ES, "Javier Milei frente a un mapa de las islas Malvinas"),
 "titulo_en": "Argentina and England use the “Argentine claim over Malvinas (Falklands)” as an excuse to hide their lack of transparency",
 "bajada_en": "A familiar pattern: using Argentina as a scapegoat to cover up backsliding on transparency and accountability.",
 "cuerpo_en": armar("Malvinas — GLOBALpatagonia Report", EN, "Javier Milei in front of a map of the Malvinas Islands"),
 "titulo_pt": "Argentina e Inglaterra usam a “reivindicação argentina sobre as Malvinas” como desculpa para ocultar suas falhas de transparência",
 "bajada_pt": "Um padrão conhecido: usar a Argentina como bode expiatório para encobrir retrocessos em transparência e prestação de contas.",
 "cuerpo_pt": armar("Malvinas — Informe GLOBALpatagonia", PT, "Javier Milei diante de um mapa das ilhas Malvinas"),
 "titulo_zh": "阿根廷与英国以“阿根廷对马尔维纳斯的主权要求”为借口，掩盖各自在透明度上的缺失",
 "bajada_zh": "一种熟悉的模式：把阿根廷当作替罪羊，掩盖自己在透明度和问责方面的倒退。",
 "cuerpo_zh": armar("马尔维纳斯 — GLOBALpatagonia 报道", ZH, "哈维尔·米莱站在马尔维纳斯群岛地图前"),
 "tag": "🇦🇷 Malvinas", "categoria": "malvinas|politica|internacional",
 "fuente": "GLOBALpatagonia", "autor": "J. Martineau", "propio": True, "url_original": "",
 "pais": "malvinas", "imagen": IMG_PORTADA,
 "imagen_keywords": "malvinas falkland islands cartel bienvenida puerto stanley transparencia consejo ejecutivo penguin news",
 "hashtags_en": "#Malvinas #Falklands #Transparency #Argentina #UK",
 "meta": "Informe · GLOBALpatagonia", "excluir_feed": True, "galeria": []
}
if __name__ == "__main__":
    propios = json.load(open(PROPIOS, encoding="utf-8")); historial = json.load(open(HISTORIAL, encoding="utf-8"))
    if any(p["id"] == BID for p in propios): raise SystemExit("Ya existe — abortando")
    if len(propios) >= MAX_ACTIVOS:
        m = propios.pop(); historial.insert(0, m); print("Movido al historial:", m["id"])
    propios.insert(0, entrada)
    json.dump(propios, open(PROPIOS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    json.dump(historial, open(HISTORIAL, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("OK propios[0] =", BID, "| activos:", len(propios))
