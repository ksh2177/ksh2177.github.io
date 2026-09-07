# -*- coding: utf-8 -*-
"""Génère index.html (FR + EN, clair + sombre) depuis content.py. Aucune dépendance."""
from pathlib import Path
from content import COMMON, LANGS

ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    # clair = graine GTA VI (matugen sur le fond du thème 6), sombre = identité Indigo #8b93f8
    "light": dict(bg="#fdf7ff", low="#f7f2f9", card="#ffffff", text="#1c1b20", muted="#484550",
                  primary="#6866A7", on_primary="#ffffff", outline="#cac4d2", chip="#f2ecf3", chip_fg="#484550",
                  mono="#7a68b4", hero="linear-gradient(135deg, #f7f2f9 0%, #ece0f2 55%, #f9e3ee 100%)",
                  k=["#6866A7", "#9775BA", "#A86F9F", "#655164"], kb=["#6866A7", "#9775BA", "#C898C2", "#655164"]),
    "dark": dict(bg="#131319", low="#1b1b21", card="#1f1f25", text="#e4e1ea", muted="#c1c3f0",
                 primary="#8b93f8", on_primary="#000141", outline="#464652", chip="#292930", chip_fg="#e4e1ea",
                 mono="#8b93f8", hero="linear-gradient(135deg, #131319 0%, #1b1b2b 60%, #1f1f25 100%)",
                 k=["#8b93f8", "#6fd3a6", "#e2b25f", "#C793E0"], kb=["#8b93f8", "#6fd3a6", "#e2b25f", "#C793E0"]),
}
ICONS = dict(
    mail='<path d="M3 5h18v14H3z"/><path d="M3 6l9 7 9-7"/>',
    link='<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1.5 1.5"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1.5-1.5"/>',
    git='<circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="8" r="2.5"/><path d="M6 8.5v7M18 10.5a6 6 0 0 1-6 6H8.5"/>',
    globe='<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    sun='<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    moon='<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>',
)


def icon(name, cls="", size=15):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def theme_vars(t):
    base = "\n".join(f"  --{k}: {v};" for k, v in t.items() if k not in ("k", "kb"))
    ks = "\n".join(f"  --k{i}: {c};\n  --kb{i}: {t['kb'][i]};" for i, c in enumerate(t["k"]))
    return base + "\n" + ks


CSS = """
:root {{
{light}
}}
:root[data-theme="dark"] {{
{dark}
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
{dark}
}} }}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{ margin: 0; background: var(--bg); color: var(--text); font-family: 'Space Grotesk', 'Segoe UI', system-ui, sans-serif; font-size: 16px; line-height: 1.55; }}
a {{ color: var(--primary); text-decoration: none; }} a:hover {{ color: var(--k1); }}
b {{ font-weight: 700; }}
.mono {{ font-family: 'JetBrains Mono', ui-monospace, monospace; }}
.wrap {{ max-width: 1200px; margin: 0 auto; padding: 0 32px; }}
[data-lang] {{ display: none; }} html[lang="fr"] [data-lang="fr"], html[lang="en"] [data-lang="en"] {{ display: revert; }}
.logo-light, .logo-dark {{ height: 46px; width: auto; display: none; }}
:root[data-theme="light"] .logo-light, :root:not([data-theme]) .logo-light {{ display: block; }}
:root[data-theme="dark"] .logo-dark {{ display: block; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme]) .logo-light {{ display: none; }} :root:not([data-theme]) .logo-dark {{ display: block; }} }}
nav {{ border-bottom: 1px solid var(--outline); position: sticky; top: 0; background: color-mix(in srgb, var(--bg) 88%, transparent); backdrop-filter: blur(10px); z-index: 5; }}
nav .wrap {{ display: flex; align-items: center; justify-content: space-between; gap: 16px; padding-top: 14px; padding-bottom: 14px; }}
nav .brand {{ display: flex; align-items: center; gap: 12px; }} nav .brand span {{ font-size: 13px; color: var(--muted); }}
nav .menu {{ display: flex; align-items: center; gap: 22px; font-weight: 600; font-size: 14px; flex-wrap: wrap; justify-content: flex-end; }}
nav .menu a {{ color: var(--text); }} nav .menu a:hover {{ color: var(--primary); }}
.pill {{ display: inline-flex; align-items: center; gap: 6px; padding: 5px 9px; border: 1px solid var(--outline); border-radius: 7px; background: transparent; color: var(--muted); cursor: pointer; font: inherit; font-size: 12px; }}
.pill svg {{ height: 14px; width: 14px; }}
.pill b {{ color: var(--primary); }} .pill:hover {{ border-color: var(--primary); }}
.hero {{ background: var(--hero); padding: 64px 0 52px 0; }}
.hero .wrap {{ display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); gap: 56px; align-items: center; }}
.hero h1 {{ font-size: clamp(34px, 5vw, 54px); font-weight: 700; line-height: 1.04; letter-spacing: -0.02em; margin: 14px 0 20px 0; }}
.hero h1 span {{ color: var(--primary); display: block; }}
.hero p {{ font-size: 18px; color: var(--muted); max-width: 620px; margin: 0 0 22px 0; }}
.cta {{ display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 20px; }}
.btn {{ display: inline-flex; align-items: center; gap: 8px; padding: 12px 20px; border-radius: 8px; font-weight: 600; font-size: 14px; border: 1px solid var(--primary); background: var(--primary); color: var(--on_primary); }}
.btn.ghost {{ background: transparent; color: var(--text); border-color: var(--outline); }} .btn:hover {{ filter: brightness(1.08); color: var(--on_primary); }} .btn.ghost:hover {{ color: var(--text); border-color: var(--primary); }}
.avail {{ display: flex; align-items: center; gap: 10px; font-size: 12px; color: var(--muted); }}
.avail i {{ width: 8px; height: 8px; border-radius: 50%; background: var(--k1); display: block; }}
.facts {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }}
.fact {{ padding: 18px 20px; border-radius: 12px; background: var(--card); border: 1px solid var(--outline); display: flex; flex-direction: column; gap: 4px; }}
.fact b {{ font-size: 26px; font-weight: 600; }} .fact span {{ font-size: 13px; color: var(--muted); }}
section {{ padding: 56px 0; }} section.alt {{ background: var(--low); }}
h2 {{ font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--mono); margin: 0 0 22px 0; }}
.xp {{ display: grid; grid-template-columns: 210px minmax(0, 1fr); gap: 24px; padding: 22px 0; border-top: 1px solid var(--outline); }}
.xp .when {{ font-size: 12px; line-height: 1.6; white-space: nowrap; }} .xp .when i {{ display: inline-block; width: 9px; height: 9px; border-radius: 50%; margin-right: 8px; }}
.xp .when small {{ display: block; color: var(--muted); }}
.xp h3 {{ font-size: 20px; margin: 0 0 4px 0; }} .xp .role {{ font-size: 14px; font-weight: 600; color: var(--primary); margin-bottom: 6px; }} .xp p {{ margin: 0; font-size: 14.5px; color: var(--muted); }}
.more {{ padding: 16px 0 0 234px; font-size: 13px; color: var(--muted); }}
.grid3 {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }}
.card {{ display: flex; flex-direction: column; gap: 8px; padding: 22px; border-radius: 12px; background: var(--card); border: 1px solid var(--outline); border-top-width: 3px; }}
.card h3 {{ font-size: 17px; margin: 0; }} .card .stack {{ font-size: 11px; color: var(--mono); }} .card p {{ margin: 0; font-size: 13.5px; color: var(--muted); flex: 1; }} .card .lnk {{ font-size: 11px; }} .card .priv {{ font-size: 11px; color: var(--muted); }}
.grid2 {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 26px 40px; }}
.sk h3 {{ font-size: 14px; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px; }} .sk h3 i {{ width: 10px; height: 10px; border-radius: 3px; display: block; }}
.tags {{ display: flex; flex-wrap: wrap; gap: 6px; }} .tag {{ font-size: 12px; padding: 5px 10px; border-radius: 6px; background: var(--chip); color: var(--chip_fg); }}
.contact {{ background: var(--card); border-top: 1px solid var(--outline); }}
.contact .wrap {{ display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 40px; align-items: center; }}
.contact .big {{ font-size: 28px; font-weight: 700; letter-spacing: -0.01em; margin-bottom: 14px; }}
.links {{ display: flex; flex-wrap: wrap; gap: 10px 22px; font-size: 14px; color: var(--muted); margin-bottom: 18px; }} .links span {{ display: inline-flex; align-items: center; gap: 6px; }}
.contact img {{ width: 120px; height: auto; }}
footer {{ border-top: 1px solid var(--outline); }} footer .wrap {{ display: flex; justify-content: space-between; gap: 12px; padding-top: 18px; padding-bottom: 18px; font-size: 11.5px; color: var(--muted); flex-wrap: wrap; }}
@media (max-width: 900px) {{
  .hero .wrap, .contact .wrap {{ grid-template-columns: 1fr; }} .grid3 {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
  .xp {{ grid-template-columns: 1fr; gap: 8px; }} .more {{ padding-left: 0; }}
}}
@media (max-width: 600px) {{
  .wrap {{ padding: 0 18px; }} .grid3, .grid2, .facts {{ grid-template-columns: 1fr; }} nav .brand span {{ display: none; }}
  nav .menu a {{ display: none; }} .hero {{ padding: 40px 0 36px 0; }} .contact img {{ display: none; }}
}}
"""

JS = """
(function () {
  var root = document.documentElement, store = window.localStorage;
  function get(k) { try { return store.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { store.setItem(k, v); } catch (e) {} }
  var lang = get('lang') || (navigator.language || 'fr').slice(0, 2);
  root.setAttribute('lang', lang === 'en' ? 'en' : 'fr');
  var theme = get('theme'); if (theme) root.setAttribute('data-theme', theme);
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-set-lang]'); if (b) { root.setAttribute('lang', b.dataset.setLang); set('lang', b.dataset.setLang); }
    var t = e.target.closest('[data-toggle-theme]');
    if (t) { var dark = root.getAttribute('data-theme') === 'dark' || (!root.getAttribute('data-theme') && matchMedia('(prefers-color-scheme: dark)').matches);
      var next = dark ? 'light' : 'dark'; root.setAttribute('data-theme', next); set('theme', next); }
  });
})();
"""


def render_lang(L, kcount=4):
    u, s = L["ui"], L["ui"]["sec"]
    facts = "".join(f'<div class="fact"><b style="color: var(--k{i % kcount});">{k}</b><span>{v}</span></div>' for i, (k, v) in enumerate(L["facts"]))
    xps = "".join(
        f'<div class="xp"><div class="when mono" style="color: var(--k{i % kcount});"><i style="background: var(--kb{i % kcount});"></i>{x["when"]}<small>{x["where"].replace(" · freelance", "")}</small></div>'
        f'<div><h3>{x["co"]}</h3><div class="role">{x["role"]}</div><p>{x["items"][0]}</p></div></div>' for i, x in enumerate(L["xp"][:3]))
    projs = "".join(
        f'<div class="card" style="border-top-color: var(--kb{i % kcount});"><h3>{t}</h3><div class="stack mono">{st}</div><p>{d}</p>'
        + (f'<a class="lnk mono" href="{url}" target="_blank" rel="noopener">→ {url.replace("https://", "")}</a>' if url else f'<span class="priv mono">{L["private"]}</span>')
        + '</div>' for i, (t, st, d, url) in enumerate(L["projects"]))
    skills = "".join(
        f'<div class="sk"><h3><i style="background: var(--kb{i % kcount});"></i>{k}</h3><div class="tags">{"".join(f"<span class=\"tag mono\">{t.strip()}</span>" for t in v.split(","))}</div></div>'
        for i, (k, v) in enumerate(L["skills"]))
    cv = u["cv_file"]
    return f"""
<div data-lang="{L['lang']}">
<header class="hero"><div class="wrap">
  <div>
    <div class="mono" style="font-size: 13px; color: var(--mono);">{u['whoami']}</div>
    <h1>{COMMON['name']}<span>{L['title']}</span></h1>
    <p>{L['pitch']}</p>
    <div class="cta"><a class="btn" href="{cv}" download>{u['cv_btn']}</a><a class="btn ghost" href="#contact">{u['contact_btn']}</a></div>
    <div class="avail mono"><i></i>{L['available']} · {L['location']}</div>
  </div>
  <div class="facts">{facts}</div>
</div></header>
<section id="xp"><div class="wrap"><h2 class="mono">// {s['xp']}</h2>{xps}<div class="more">{L['xp_more']}</div></div></section>
<section id="projects" class="alt"><div class="wrap"><h2 class="mono">// {s['projects']}</h2><div class="grid3">{projs}</div></div></section>
<section id="skills"><div class="wrap"><h2 class="mono">// {s['skills']}</h2><div class="grid2">{skills}</div></div></section>
<section id="contact" class="contact"><div class="wrap">
  <div><h2 class="mono">// {s['contact']}</h2><div class="big">{u['tagline']}</div>
    <div class="links"><span style="color: var(--k0);">{icon('mail')}<a href="mailto:{COMMON['mail']}">{COMMON['mail']}</a></span>
      <span style="color: var(--k1);">{icon('link')}<a href="https://{COMMON['linkedin']}" target="_blank" rel="noopener">{COMMON['linkedin']}</a></span>
      <span style="color: var(--k2);">{icon('git')}<a href="https://{COMMON['github']}" target="_blank" rel="noopener">{COMMON['github']}</a></span>
      <span style="color: var(--k3);">{icon('globe')}<a href="https://{COMMON['site']}" target="_blank" rel="noopener">{COMMON['site']}</a></span></div>
    <div class="cta"><a class="btn" href="cv-stephen-casse-fr.pdf" download>{u['cv_fr']}</a><a class="btn ghost" href="cv-stephen-casse-en.pdf" download>{u['cv_en']}</a></div>
  </div>
  <div><img class="logo-light" src="assets/logo-light.png" alt="CS Consulting" style="height: auto;"><img class="logo-dark" src="assets/logo-dark.png" alt="CS Consulting" style="height: auto;"></div>
</div></section>
<footer><div class="wrap mono"><span>© 2026 {COMMON['name']} — {COMMON['company']}</span><span>{u['footer_right']}</span></div></footer>
</div>"""


def render():
    fr, en = LANGS["fr"], LANGS["en"]
    css = CSS.format(light=theme_vars(THEMES["light"]), dark=theme_vars(THEMES["dark"]))
    nav_links = "".join(f'<a href="#{a}" data-lang="fr">{fr["ui"]["nav"][i]}</a><a href="#{a}" data-lang="en">{en["ui"]["nav"][i]}</a>'
                        for i, a in enumerate(["xp", "projects", "skills", "contact"]))
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stephen Casse — Ingénieur DevOps freelance · CS Consulting</title>
<meta name="description" content="Stephen Casse, ingénieur DevOps freelance (CS Consulting) : CI/CD, Ansible, Kubernetes, GitOps. Dix ans en production bancaire. Freelance DevOps engineer, Paris / remote.">
<meta property="og:title" content="Stephen Casse — Ingénieur DevOps freelance">
<meta property="og:description" content="Automatisons votre delivery. CI/CD, Ansible, Kubernetes, GitOps — dix ans en production bancaire.">
<meta property="og:image" content="https://ksh2177.github.io/assets/logo-light.png">
<link rel="icon" href="assets/logo-light.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">
<style>{css}</style>
<script>(function(){{try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);var l=localStorage.getItem('lang')||(navigator.language||'fr').slice(0,2);document.documentElement.setAttribute('lang',l==='en'?'en':'fr');}}catch(e){{}}}})();</script>
</head>
<body>
<nav><div class="wrap">
  <a class="brand" href="#"><img class="logo-light" src="assets/logo-light.png" alt="CS Consulting"><img class="logo-dark" src="assets/logo-dark.png" alt="CS Consulting"><span class="mono">ksh2177@cs-consulting:~$</span></a>
  <div class="menu">{nav_links}
    <span class="pill mono" role="group" aria-label="Langue"><button class="pill" data-set-lang="fr" style="border: 0; padding: 0;"><b data-lang="fr">FR</b><span data-lang="en">FR</span></button>·<button class="pill" data-set-lang="en" style="border: 0; padding: 0;"><span data-lang="fr">EN</span><b data-lang="en">EN</b></button></span>
    <button class="pill" data-toggle-theme title="{fr['ui']['theme']} / {en['ui']['theme']}" aria-label="Thème">{icon('sun', 'logo-light', 14)}{icon('moon', 'logo-dark', 14)}</button>
  </div>
</div></nav>
{render_lang(fr)}
{render_lang(en)}
<script>{JS}</script>
</body>
</html>
"""


if __name__ == "__main__":
    out = ROOT / "index.html"
    out.write_text(render(), encoding="utf-8")
    print("index.html :", out.stat().st_size, "octets")
