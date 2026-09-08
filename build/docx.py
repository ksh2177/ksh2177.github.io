# -*- coding: utf-8 -*-
"""Génère le CV Word (2 pages A4, modèle « Grille technique ») depuis content.py.
Usage : python3 build/docx.py fr|en  → cv-stephen-casse-<lang>.docx à la racine du repo.

OOXML écrit à la main : aucune dépendance (même parti pris que site.py pour le HTML).
Même contenu et même palette que le PDF — le .docx est la version ÉDITABLE, pour les
plateformes de sourcing et les ESN qui réclament un Word.
"""
import re, sys, zipfile
from pathlib import Path
from content import COMMON, LANGS, THEMES

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "build" / "assets"
T = THEMES["light"]
INK, MUTED, PRIMARY = T["text"][1:], T["muted"][1:], T["primary"][1:]
ACC1, ACC2 = T["k"][1][1:], T["k"][2][1:]
LOW, OUTLINE, CHIP, MONOC = T["low"][1:], T["outline"][1:], T["chip"][1:], T["mono"][1:]
BAND = "F3EAF6"          # aplat du dégradé hero : Word ne fait pas de dégradé de fond simplement
SOFT, FAINT = "5B5866", "7C7889"
# Le PDF compose en Space Grotesk / JetBrains Mono ; un .docx est relu et édité ailleurs,
# donc polices présentes des deux côtés : Calibri (→ Carlito sous Linux, mêmes métriques)
# et Consolas pour le monospace.
SANS, MONO = "Calibri", "Consolas"

PAGE_W, MARGIN = 11906, 680          # A4 en twips, marges 1,2 cm
BODY_W = PAGE_W - 2 * MARGIN         # 10546
IDENT_W = BODY_W - 1400 - 460        # largeur utile de la cellule identité du bandeau


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def rpr(**o):
    """<w:rPr> depuis des options nommées (b, i, color, sz, font, spacing) ;
    l'ordre des éléments produits suit le schéma OOXML, qui l'impose."""
    font, sz = o.get("font", SANS), o.get("sz", 19)
    x = f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>'
    if o.get("b"): x += "<w:b/><w:bCs/>"
    if o.get("i"): x += "<w:i/>"
    if o.get("color"): x += f'<w:color w:val="{o["color"]}"/>'
    if o.get("spacing"): x += f'<w:spacing w:val="{o["spacing"]}"/>'
    return f'<w:rPr>{x}<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/></w:rPr>'


def run(text, **k):
    return f'<w:r>{rpr(**k)}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'


def rich(text, **k):
    """Texte du contenu où <b>…</b> marque le gras : un run par segment."""
    out = ""
    for part in re.split(r"(<b>.*?</b>)", text):
        if not part:
            continue
        if part.startswith("<b>"):
            out += run(part[3:-4], **{**k, "b": True})
        else:
            out += run(part, **k)
    return out


def tab(**k):
    return f"<w:r>{rpr(**k)}<w:tab/></w:r>"


def para(inner="", **o):
    """<w:p> depuis des options nommées (before, after, line, ind, hang, tabs, keep)."""
    p = "<w:pPr>"
    if o.get("keep"): p += "<w:keepNext/><w:keepLines/>"
    if o.get("tabs"):
        p += "<w:tabs>" + "".join(f'<w:tab w:val="{v}" w:pos="{pos}"/>' for v, pos in o["tabs"]) + "</w:tabs>"
    p += (f'<w:spacing w:before="{o.get("before", 0)}" w:after="{o.get("after", 60)}"'
          f' w:line="{o.get("line", 252)}" w:lineRule="auto"/>')
    if o.get("ind") or o.get("hang"):
        p += f'<w:ind w:left="{o.get("ind", 0)}" w:hanging="{o.get("hang", 0)}"/>'
    return f"<w:p>{p}</w:pPr>{inner}</w:p>"


def bullet(text, **k):
    return para(run("• ", color=PRIMARY, **k) + rich(text, color=MUTED, sz=18),
                ind=227, hang=142, after=40, line=240)


def cell(paras, w, **o):
    """<w:tc> de largeur w. Options : fill, mar (haut, gauche, bas, droite),
    borders = dict côté → (couleur, épaisseur en 1/8 pt)."""
    tc = f'<w:tcW w:w="{w}" w:type="dxa"/>'
    if o.get("borders"):
        b = "".join(f'<w:{s} w:val="single" w:sz="{sz}" w:space="0" w:color="{c}"/>'
                    for s in ("top", "left", "bottom", "right")
                    for c, sz in [o["borders"].get(s, (OUTLINE, 4))])
        tc += f"<w:tcBorders>{b}</w:tcBorders>"
    if o.get("fill"):
        tc += f'<w:shd w:val="clear" w:color="auto" w:fill="{o["fill"]}"/>'
    t, l, bo, r = o.get("mar", (80, 120, 80, 120))
    tc += (f'<w:tcMar><w:top w:w="{t}" w:type="dxa"/><w:left w:w="{l}" w:type="dxa"/>'
           f'<w:bottom w:w="{bo}" w:type="dxa"/><w:right w:w="{r}" w:type="dxa"/></w:tcMar>')
    return f"<w:tc><w:tcPr>{tc}</w:tcPr>{paras or para()}</w:tc>"


def table(rows, widths, borders=False):
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    none = "".join(f'<w:{s} w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
                   for s in ("top", "left", "bottom", "right", "insideH", "insideV"))
    pr = (f'<w:tblPr><w:tblW w:w="{sum(widths)}" w:type="dxa"/>'
          + ("" if borders else f"<w:tblBorders>{none}</w:tblBorders>")
          + '<w:tblLayout w:type="fixed"/><w:tblCellMar><w:left w:w="0" w:type="dxa"/>'
            '<w:right w:w="0" w:type="dxa"/></w:tblCellMar></w:tblPr>')
    trs = "".join(f"<w:tr>{r}</w:tr>" for r in rows)
    return f"<w:tbl>{pr}<w:tblGrid>{grid}</w:tblGrid>{trs}</w:tbl>"


def spacer(h=120):
    return f'<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="{h}" w:lineRule="exact"/></w:pPr></w:p>'


def image(px_w, px_h, rid="rId4"):
    cx, cy = px_w * 9525, px_h * 9525
    return (f'<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
            f'<wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="1" name="Logo CS Consulting"/>'
            f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:pic><pic:nvPicPr><pic:cNvPr id="1" name="logo.png"/><pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
            f"</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>")


def h2(label, before=130):
    return para(run("// ", color=ACC1, font=MONO, sz=18, b=True)
                + run(label.upper(), color=MONOC, font=MONO, sz=18, b=True, spacing=16),
                before=before, after=80, keep=True)


# ---------------------------------------------------------------- blocs du CV

def header_block(L):
    # La localisation se pose au bout de la ligne `whoami`, sur une tabulation droite :
    # une colonne dédiée (comme en flex dans le PDF) coupait « Île-de-France · Remote » en deux.
    ident = (para(run(f"~/cs-consulting {L['ui']['whoami']}", color=PRIMARY, font=MONO, sz=17)
                  + tab() + run(L["location"], color=SOFT, font=MONO, sz=17),
                  tabs=[("right", IDENT_W)], after=40)
             + para(run(COMMON["name"], b=True, sz=44, color=INK)
                    + run(f" · {COMMON['alias']}", sz=44, color=SOFT), after=40)
             + para(run(L["title"], b=True, sz=19, color=PRIMARY)
                    + run(f" — {L['subtitle']}", sz=19, color=SOFT), after=0))
    row = (cell(para(image(62, 64), after=0), 1400, fill=BAND, mar=(240, 260, 240, 0))
           + cell(ident, BODY_W - 1400, fill=BAND, mar=(240, 220, 240, 240)))
    contact = " · ".join([COMMON["mail"], COMMON["phone"], COMMON["linkedin"],
                          COMMON["github"], COMMON["site"]])
    strip = [cell(para(run(contact, color=MUTED, sz=17), after=0), BODY_W, fill=LOW,
                  borders={s: (LOW if s != "bottom" else OUTLINE, 4) for s in ("top", "left", "bottom", "right")},
                  mar=(110, 220, 110, 220))]
    return table([row], [1400, BODY_W - 1400]) + table([strip], [BODY_W], borders=True)


def facts_block(L):
    w = BODY_W // 4
    cells = []
    for i, (n, l) in enumerate(L["facts"]):
        top = (PRIMARY if i % 2 == 0 else ACC2, 24)
        inner = (para(run(n, b=True, font=MONO, sz=26, color=INK), after=20)
                 + para(run(l, color=SOFT, sz=15), after=0))
        cells.append(cell(inner, w - 60, borders={"top": top}, mar=(140, 160, 140, 160)))
        cells.append(cell("", 60) if i < 3 else "")
    return table([("".join(cells))], [w - 60, 60] * 3 + [w - 60], borders=True)


def xp_block(x):
    out = para(run(x["co"], b=True, sz=22, color=INK)
               + tab() + run(x["when"], color=ACC2, font=MONO, sz=16),
               tabs=[("right", BODY_W)], before=140, after=30, keep=True)
    out += para(run(x["role"], b=True, sz=18, color=PRIMARY)
                + run(f" · {x['where']}", sz=18, color=FAINT), after=30, keep=True)
    if x["ctx"]:
        out += para(run(x["ctx"], sz=17, color=SOFT), after=50)
    return out + "".join(bullet(i) for i in x["items"])


def skills_block(L):
    def one(k, v):
        return (para(run(k, b=True, sz=18, color=INK), after=30, keep=True)
                + para(run(" · ".join(t.strip() for t in v.split(",")), font=MONO, sz=15, color=MUTED),
                       after=50))
    w = (BODY_W - 300) // 2
    rows, items = [], L["skills"]
    for a in range(0, len(items), 2):
        pair = items[a:a + 2]
        rows.append(cell(one(*pair[0]), w) + cell("", 300)
                    + cell(one(*pair[1]) if len(pair) > 1 else "", w))
    return table(rows, [w, 300, w])


def projects_block(L):
    def one(i, t, s, d):
        return (para(run(t, b=True, sz=19, color=INK), after=20, keep=True)
                + para(run(s, font=MONO, sz=15, color=MONOC), after=20)
                + para(run(d, sz=16, color=MUTED), after=0))
    w = (BODY_W - 240) // 2
    rows, items = [], L["projects"]
    for a in range(0, len(items), 2):
        pair = items[a:a + 2]
        cells = ""
        for j, (t, s, d, _u) in enumerate(pair):
            i = a + j
            cells += cell(one(i, t, s, d), w, borders={"left": (PRIMARY if i % 2 == 0 else ACC2, 24),
                                                       "top": (OUTLINE, 4)}, mar=(120, 160, 120, 140))
            if j == 0:
                cells += cell("", 240)
        if len(pair) == 1:
            cells += cell("", w)
        rows.append(cells)
        gap = spacer(90)
        rows.append(cell(gap, w, mar=(0, 0, 0, 0)) + cell(gap, 240) + cell(gap, w, mar=(0, 0, 0, 0)))
    return table(rows[:-1], [w, 240, w], borders=True)


def bottom_block(L):
    u = L["ui"]["sec"]
    edu = "".join(para(run(y + "  ", b=True, font=MONO, sz=16, color=ACC2) + run(t, sz=16, color=MUTED),
                       ind=340, hang=340, after=40) for y, t in L["edu"])
    langs = "".join(para(run(l, b=True, sz=16, color=INK) + run(f" — {n}", sz=16, color=MUTED), after=50)
                    for l, n in L["langs"])
    quotes = "".join(para(run(f"« {q} »", i=True, sz=16, color=INK), after=60) for q in L["quotes"])
    w = (BODY_W - 600) // 3
    head = lambda k: h2(u[k], before=0)
    col = lambda k, body: cell(head(k) + body, w)
    return table([col("edu", edu) + cell("", 300) + col("langs", langs) + cell("", 300) + col("quotes", quotes)],
                 [w, 300, w, 300, w])


def document(L):
    u = L["ui"]
    body = (header_block(L)
            + spacer(200)
            + para(rich(L["pitch"], sz=21, color=INK), after=180, line=276)
            + facts_block(L)
            + h2(u["sec"]["xp"])
            + "".join(xp_block(x) for x in L["xp"][:3])
            + '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
            + "".join(xp_block(x) for x in L["xp"][3:])
            + h2(u["sec"]["skills"]) + skills_block(L)
            + h2(u["sec"]["projects"]) + projects_block(L)
            + spacer(220) + bottom_block(L))
    sect = (f'<w:sectPr><w:pgSz w:w="{PAGE_W}" w:h="16838"/>'
            f'<w:pgMar w:top="{MARGIN}" w:right="{MARGIN}" w:bottom="{MARGIN}" w:left="{MARGIN}"'
            f' w:header="0" w:footer="0" w:gutter="0"/></w:sectPr>')
    ns = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
          'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
          'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
          'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
          'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"')
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f"<w:document {ns}><w:body>{body}{sect}</w:body></w:document>")


STYLES = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          f'<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
          f'<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="{SANS}" w:hAnsi="{SANS}"/>'
          f'<w:color w:val="{INK}"/><w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr></w:rPrDefault>'
          f'<w:pPrDefault><w:pPr><w:spacing w:after="60" w:line="252" w:lineRule="auto"/></w:pPr>'
          f"</w:pPrDefault></w:docDefaults>"
          f'<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>'
          f"</w:styles>")

CONTENT_TYPES = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                 '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                 '<Default Extension="xml" ContentType="application/xml"/>'
                 '<Default Extension="png" ContentType="image/png"/>'
                 '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-'
                 'officedocument.wordprocessingml.document.main+xml"/>'
                 '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-'
                 'officedocument.wordprocessingml.styles+xml"/></Types>')

RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
        'relationships/officeDocument" Target="word/document.xml"/></Relationships>')

DOC_RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
            'relationships/styles" Target="styles.xml"/>'
            '<Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
            'relationships/image" Target="media/logo.png"/></Relationships>')


def build(lang, out):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/document.xml", document(LANGS[lang]))
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/media/logo.png", (ASSETS / "logo-light.png").read_bytes())


if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) > 1 else "fr"
    out = ROOT / f"cv-stephen-casse-{lang}.docx"
    build(lang, out)
    print(out.name, ":", out.stat().st_size, "octets")
