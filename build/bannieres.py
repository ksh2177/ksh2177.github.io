# -*- coding: utf-8 -*-
"""Bannières LinkedIn (page entreprise CS Consulting + profil personnel).

Usage : python3 build/bannieres.py [dossier de sortie]  → deux PNG rendus en 2x.
Palette et logo lus dans content.py : une bannière ne peut pas diverger du site.
Formats imposés par LinkedIn : page entreprise 1128x191, profil 1584x396. Le quart
inférieur gauche du profil reste vide, la photo le recouvre.
Ces fichiers ne sont pas commités : ils se régénèrent."""
import base64, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from content import THEMES

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
T = THEMES["light"]
LOGO = "data:image/png;base64," + base64.b64encode((ROOT / "build/assets/logo-light.png").read_bytes()).decode()
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">')
MONO = "'JetBrains Mono', ui-monospace, monospace"


def shell(w, h, body, extra=""):
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">{FONTS}<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; width: {w}px; height: {h}px; overflow: hidden;
  background: {T['hero']}; color: {T['text']};
  font-family: 'Space Grotesk', 'Segoe UI', sans-serif;
  display: flex; align-items: center; }}
{extra}</style></head><body>{body}</body></html>"""


# Palette du logo (mesurée sur logo-light.png) : l'avatar de la page porte déjà le logo,
# la bannière n'en reprend que les couleurs — le répéter ferait doublon à l'écran.
LOGO_INK, LOGO_BLUE, LOGO_VIOLET = "#30303c", "#60609c", "#906cb4"


def page_entreprise():
    """Sans logo : l'avatar de la page se superpose en bas à gauche et le porte déjà.
    Le texte démarre à 300 px pour ne pas passer dessous."""
    fond = f"linear-gradient(135deg, {LOGO_INK} 0%, #3b3b52 52%, #4a4470 100%)"
    body = f"""<div style="display:flex; flex-direction:column; justify-content:center; gap:11px;
            padding:0 60px 0 300px; width:100%; height:100%;">
    <div style="font-size:33px; font-weight:700; letter-spacing:-0.02em; line-height:1.12;
                color:#f5f3fa; white-space:nowrap;">L'IA qui vous fait gagner du temps — et qui le prouve.</div>
    <div style="font-family:{MONO}; font-size:15px; color:#b9a9e0; letter-spacing:0.04em;">
      TPE &amp; PME &nbsp;·&nbsp; documents, saisies, suivi &nbsp;·&nbsp; sur mesure</div>
</div>"""
    return shell(1128, 191, body, extra=f"body {{ background: {fond}; }}")


def profil():
    faits = [("11 ans", "production bancaire critique"), ("20 600", "tests automatisés"),
             ("~1 200", "serveurs, 15 DSI"), ("1 standard", "adopté en production")]
    cartes = "".join(
        f"""<div style="background:{T['card']}; border-top:3px solid {T['k'][i % 4]}; border-radius:14px;
             padding:20px 22px; display:flex; flex-direction:column; justify-content:center;">
          <div style="font-family:{MONO}; font-size:29px; font-weight:600; letter-spacing:-0.01em;">{n}</div>
          <div style="font-size:13px; color:{T['muted']}; margin-top:5px; line-height:1.3;">{l}</div>
        </div>""" for i, (n, l) in enumerate(faits))
    body = f"""<div style="display:flex; width:100%; padding:46px 60px 0 60px; gap:40px; align-items:flex-start;">
  <div style="display:flex; flex-direction:column; gap:8px; flex:none; width:520px;">
    <div style="font-family:{MONO}; font-size:14px; color:{T['mono']};">~/cs-consulting $ whoami</div>
    <div style="font-size:52px; font-weight:700; letter-spacing:-0.03em; line-height:1;">Stephen Casse</div>
    <div style="font-size:23px; font-weight:600; color:{T['primary']}; line-height:1.25;">
      Ingénieur DevOps / SRE Freelance</div>
    <div style="font-family:{MONO}; font-size:14px; color:{T['muted']}; letter-spacing:0.03em;">
      Vérification · Automatisation · Production</div>
  </div>
  <div style="display:grid; grid-template-columns:repeat(2, 1fr); grid-template-rows:repeat(2, 1fr);
              gap:16px; flex:1; height:304px;">{cartes}</div>
</div>"""
    return shell(1584, 396, body, extra="body { align-items: flex-start; }")


for nom, html, (w, h) in [("banniere-cs-page", page_entreprise(), (1128, 191)),
                          ("banniere-profil", profil(), (1584, 396))]:
    src = OUT / f"{nom}.html"
    src.write_text(html, encoding="utf-8")
    subprocess.run(["chromium", "--headless", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=2", "--virtual-time-budget=6000",
                    f"--window-size={w},{h}", f"--screenshot={OUT / (nom + '.png')}",
                    f"file://{src}"], capture_output=True, check=True)
    print(f"{nom}.png  ({w}×{h} rendu en 2×)")
