# Journal de bord — portfolio

> Une entrée par jour travaillé (jamais deux le même jour), format
> `## <emoji> <JJ MOIS AAAA> — <résumé>` avec `### Fait` (hashs de commits) et,
> si pertinent, `### Décisions prises` — le POURQUOI et les mesures, pas
> seulement le quoi. Journal démarré le 01/09/2026 ; l'historique antérieur
> vit dans `git log`.

## 📓 01 SEPTEMBRE 2026 — journal de bord démarré

Journal ouvert à la demande de Stephen : Skynet s'en sert pour suivre les sujets
entre sessions. État du repo au démarrage :

- Portfolio scasse.com ; dernier chantier le 25/08/2026 : carte homelab,
  pills contact (notion/freelance), doc de structure et backlog.

## 🎨 08 SEPTEMBRE 2026 — refonte complète : bilingue, deux thèmes, CV PDF

### Fait
- Fin du thème « CRT terminal » Superdesign (dossier `.superdesign/` retiré, Tailwind CDN
  abandonné). Nouveau site généré depuis `build/content.py` par `build/site.py` : FR + EN dans
  le même `index.html`, thèmes clair (graine GTA VI) et sombre (identité Indigo) par variables
  CSS, sélecteurs mémorisés en localStorage, responsive, meta description et Open Graph.
- CV 2 pages A4 (modèle « Grille technique », validé sur canevas) généré par `build/cv.py`
  en FR et EN, téléchargeable depuis le site. Même contenu que le site : une seule source.
- Logos recolorés par thème (règle : lettres d'origine, accents thémés).

### Décisions prises
- Une seule source de contenu pour site et CV : plus de divergence « 8 ans / 10 ans ».
- Plus de barres de compétences en pourcentages ni de valeurs décoratives codées en dur.
- Page Notion supprimée par Stephen ; le site GitHub devient la porte d'entrée unique.
- Chromium sous firejail n'écrit que dans `/tmp` : les PDF passent par un dossier temporaire.
- AWS retiré partout (jamais pratiqué) ; Azure/Terraform datés « BPCE Lease 2021 ».

### Fait (2e passe — palette)
- Les CV PDF vivaient encore sur l'ancienne palette CS Consulting (bleu nuit `#373643`, vert
  `#18cb96`, rouge `#ff4b4b`) alors que le site refondu le matin tourne sur la graine GTA VI :
  qui ouvrait le site puis téléchargeait le CV voyait deux identités. Corrigé (`fca7336`).
- `THEMES` (clair + sombre) remonte dans `content.py` : source unique de palette. `site.py` en
  sort les deux thèmes, `cv.py` ne consomme que le clair. `index.html` inchangé au bit près.
- `cv.py` ne code plus aucune couleur en dur : bandeau = dégradé du hero du site, accents
  `#6866A7` / `#9775BA` (titres, icônes, `whoami`) et `#A86F9F` (dates, liserés), tags sur le
  fond chip `#f2ecf3`. Le CV réutilise `logo-light.png` : `logo-cv.png` supprimé.
- Hors repo, même passe sur le dossier de compétences Word `~/Business/CV/CS_CONSULTING_CV_2026`
  (`.docx` → `.doc` + `.pdf` régénérés, originaux dans `_backup-2026-09-08/`) : accent or
  `#CDA963` → `#6866A7`, bandeau logo et filigrane recolorés par rotation de teinte, 8
  surlignages jaunes de relecture retirés.

### Décisions prises (2e passe)
- Le CV imprimé suit le thème **clair** du site, pas une palette à lui : une seule identité.
- Bandeau du CV = dégradé du hero plutôt qu'aplat violet (choix de Stephen sur maquette) —
  fidélité maximale au site, et plus besoin d'un logo dédié au CV.
- `COMMON["palette"]` (bleu/vert/rouge) reste pour mémoire mais plus rien ne s'en sert.
- Reste à trancher : le tampon **ISO 9001 (Lloyd's Register)** en pied du dossier Word vient du
  template de l'ESN d'origine — il n'appartient pas à CS Consulting et devrait sauter.
