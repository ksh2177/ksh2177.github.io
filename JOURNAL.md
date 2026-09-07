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
