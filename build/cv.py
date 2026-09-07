# -*- coding: utf-8 -*-
"""Génère le CV (2 pages A4, modèle « Grille technique ») en HTML puis PDF via Chromium headless.
Usage : python3 build/cv.py fr|en  → cv-stephen-casse-<lang>.pdf à la racine du repo."""
import base64, shutil, subprocess, sys, tempfile
from pathlib import Path
from content import COMMON, LANGS

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "build" / "assets"
BLUE, GREEN, RED = COMMON["palette"]["blue"], COMMON["palette"]["green"], COMMON["palette"]["red"]
MONO = "font-family: 'JetBrains Mono', ui-monospace, monospace;"
ICONS = dict(
    mail='<path d="M3 5h18v14H3z"/><path d="M3 6l9 7 9-7"/>',
    phone='<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
    pin='<path d="M12 21s-7-6.5-7-11a7 7 0 0 1 14 0c0 4.5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    link='<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1.5 1.5"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1.5-1.5"/>',
    git='<circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="8" r="2.5"/><path d="M6 8.5v7M18 10.5a6 6 0 0 1-6 6H8.5"/>',
    globe='<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
)


def svg(name, color=GREEN, size=11):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" style="flex: none;">{ICONS[name]}</svg>')


def data_uri(path):
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode()


def li(items):
    return '<ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def card(inner, extra=""):
    return f'<div class="card" style="{extra}">{inner}</div>'


def xp_block(x):
    ctx = f'<div class="ctx">{x["ctx"]}</div>' if x["ctx"] else ""
    return card(f'<div class="row"><div class="co">{x["co"]}</div><div class="when">{x["when"]}</div></div>'
                f'<div class="role">{x["role"]} <span>· {x["where"]}</span></div>{ctx}{li(x["items"])}')


def header(L, logo):
    contact = " ".join(f'<span class="ct">{svg(k)}{v}</span>' for k, v in
                       [("mail", COMMON["mail"]), ("phone", COMMON["phone"]), ("link", COMMON["linkedin"]), ("git", COMMON["github"]), ("globe", COMMON["site"])])
    return f"""<div class="band">
  <img src="{logo}" style="width: 84px; height: auto; flex: none;">
  <div class="id"><div class="whoami">~/cs-consulting $ whoami</div>
    <div class="name">{COMMON['name']} <span>· {COMMON['alias']}</span></div>
    <div class="title">{L['title']} <span>— {L['subtitle']}</span></div></div>
  <div class="loc">{svg('pin', GREEN, 12)}{L['location']}</div>
</div><div class="strip">{contact}</div>"""


def page1(L, logo):
    u = L["ui"]
    facts = "".join(f'<div class="card fact" style="border-top: 3px solid {GREEN if i % 2 == 0 else RED};"><div class="n">{k}</div><div class="l">{v}</div></div>' for i, (k, v) in enumerate(L["facts"]))
    return f"""<div class="pg">{header(L, logo)}
<div class="body">
  <div class="pitch">{L['pitch']}</div>
  <div class="facts">{facts}</div>
  <div><div class="h2">// {u['sec']['xp']}</div><div class="stack">{''.join(xp_block(x) for x in L['xp'][:3])}</div></div>
</div>
<div class="foot"><span>stephen-casse.cv — {u['page']} 1/2</span><span style="color: {GREEN};">● {L['available']}</span></div></div>"""


def page2(L, logo):
    u = L["ui"]
    skills = "".join(f'<div class="sk"><div class="k">{k}</div><div class="tags">{"".join(f"<span class=\"tag\">{t.strip()}</span>" for t in v.split(","))}</div></div>' for k, v in L["skills"])
    projects = "".join(card(f'<div class="pt">{t}</div><div class="ps">{s}</div><div class="pd">{d}</div>', f"border-left: 3px solid {GREEN if i % 2 == 0 else RED};")
                       for i, (t, s, d, _u) in enumerate(L["projects"]))
    edu = "".join(f'<div class="ed"><span>{y}</span>{t}</div>' for y, t in L["edu"])
    langs = "".join(f'<div><b>{l}</b> — {n}</div>' for l, n in L["langs"])
    quotes = "".join(f'<div class="q">« {q} »</div>' for q in L["quotes"])
    return f"""<div class="pg"><div class="band small"><img src="{logo}" style="width: 44px; height: auto;"><span class="name2">{COMMON['name']}</span>
  <span class="pg2">{L['title'].lower().replace(' ', '-')} · {u['page']} 2/2</span></div>
<div class="body">
  <div class="stack">{''.join(xp_block(x) for x in L['xp'][3:])}</div>
  <div><div class="h2">// {u['sec']['skills']}</div><div class="grid2">{skills}</div></div>
  <div><div class="h2">// {u['sec']['projects']}</div><div class="grid2 tight">{projects}</div></div>
  <div class="grid3">
    <div><div class="h2">// {u['sec']['edu']}</div><div class="col">{edu}</div></div>
    <div><div class="h2">// {u['sec']['langs']}</div><div class="col">{langs}</div></div>
    <div><div class="h2">// {u['sec']['quotes']}</div><div class="col">{quotes}</div></div>
  </div>
</div></div>"""


CSS = f"""
@page {{ size: 794px 1123px; margin: 0; }}
body {{ margin: 0; background: #fff; color: {BLUE}; font-family: 'Space Grotesk', 'Segoe UI', sans-serif; font-size: 10.5px; line-height: 1.45; }}
.pg {{ width: 794px; height: 1123px; position: relative; overflow: hidden; page-break-after: always; box-sizing: border-box; }} .pg:last-child {{ page-break-after: auto; }}
ul {{ margin: 0; padding-left: 16px; }} li {{ margin: 0 0 4px 0; }} b {{ font-weight: 700; }}
.band {{ background: {BLUE}; color: #fff; padding: 30px 40px 24px 40px; display: flex; align-items: center; gap: 22px; }}
.band.small {{ padding: 16px 40px; gap: 12px; }} .name2 {{ font-size: 15px; font-weight: 700; }} .pg2 {{ margin-left: auto; {MONO} font-size: 9.5px; color: {GREEN}; }}
.id {{ flex: 1; display: flex; flex-direction: column; gap: 4px; }} .whoami {{ {MONO} font-size: 9.5px; color: {GREEN}; }}
.name {{ font-size: 30px; font-weight: 700; line-height: 1; letter-spacing: -0.02em; }} .name span {{ color: #9c9ca8; font-weight: 500; }}
.title {{ font-size: 12.5px; font-weight: 600; color: {GREEN}; }} .title span {{ color: #b8b8c4; font-weight: 500; }}
.loc {{ display: flex; align-items: center; gap: 5px; {MONO} font-size: 9.5px; color: #b8b8c4; white-space: nowrap; align-self: flex-start; margin-top: 1px; }}
.strip {{ background: #f3f3f6; border-bottom: 1px solid #e1e1e6; padding: 8px 40px; display: flex; justify-content: space-between; gap: 8px; font-size: 9.5px; color: #4a4a58; }}
.ct {{ display: inline-flex; align-items: center; gap: 5px; white-space: nowrap; }}
.body {{ padding: 18px 40px 0 40px; display: flex; flex-direction: column; gap: 16px; }}
.pitch {{ font-size: 12.5px; line-height: 1.55; color: #2d2c38; }}
.facts {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; }}
.card {{ border: 1px solid #e1e1e6; border-radius: 8px; padding: 12px 14px; background: #fff; display: flex; flex-direction: column; gap: 2px; }}
.fact .n {{ {MONO} font-size: 18px; font-weight: 600; }} .fact .l {{ font-size: 9px; color: #5a5a68; }}
.h2 {{ {MONO} font-size: 10px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: {GREEN}; margin: 0 0 8px 0; }}
.stack {{ display: flex; flex-direction: column; gap: 10px; }}
.row {{ display: flex; justify-content: space-between; align-items: baseline; gap: 10px; }} .co {{ font-weight: 700; font-size: 12.5px; }} .when {{ {MONO} font-size: 9px; color: {RED}; white-space: nowrap; }}
.role {{ font-size: 10.5px; font-weight: 600; color: #4a4a58; }} .role span {{ font-weight: 400; color: #8a8a96; }} .ctx {{ font-size: 9.8px; color: #6b6b78; margin: 3px 0 5px 0; }}
.grid2 {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px 18px; }} .grid2.tight {{ gap: 8px; }}
.grid3 {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; }} .col {{ display: flex; flex-direction: column; gap: 4px; font-size: 9.8px; }}
.sk {{ display: flex; flex-direction: column; gap: 5px; }} .k {{ font-weight: 700; font-size: 10px; }} .tags {{ display: flex; flex-wrap: wrap; gap: 4px; }}
.tag {{ {MONO} font-size: 8.5px; padding: 2px 6px; border: 1px solid #d7d7dc; border-radius: 3px; color: #4a4a58; white-space: nowrap; }}
.pt {{ font-weight: 700; font-size: 10.5px; }} .ps {{ {MONO} font-size: 8.5px; color: #6b6b78; }} .pd {{ font-size: 9.6px; color: #4a4a58; }}
.ed {{ display: flex; gap: 8px; }} .ed span {{ {MONO} color: {RED}; flex: none; }} .q {{ font-style: italic; color: #2d2c38; font-size: 10.5px; }}
.foot {{ position: absolute; left: 40px; right: 40px; bottom: 22px; display: flex; justify-content: space-between; {MONO} font-size: 8.5px; color: #8a8a96; }}
"""


def render(lang):
    L = LANGS[lang]
    logo = data_uri(ASSETS / "logo-cv.png")
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>CV {COMMON['name']} — {L['title']}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">
<style>{CSS}</style></head><body>{page1(L, logo)}{page2(L, logo)}</body></html>"""


def to_pdf(html, out):
    """Chromium (sous firejail) n'écrit que dans /tmp : on exporte là, puis on copie."""
    tmp = Path(tempfile.mkdtemp(prefix="cv-"))
    src, pdf = tmp / "cv.html", tmp / "cv.pdf"
    src.write_text(html, encoding="utf-8")
    subprocess.run(["chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--run-all-compositor-stages-before-draw",
                    "--virtual-time-budget=8000", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f"file://{src}"],
                   check=True, capture_output=True)
    shutil.copy(pdf, out)
    shutil.rmtree(tmp)


if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) > 1 else "fr"
    out = ROOT / f"cv-stephen-casse-{lang}.pdf"
    to_pdf(render(lang), out)
    print(out.name, ":", out.stat().st_size, "octets")
