# portfolio — site CV de Stephen Casse

Site CV portfolio une page, **en ligne sur https://ksh2177.github.io/** (CS Consulting,
Ingénieur DevOps freelance). Bilingue **FR / EN**, thème **clair / sombre**, CV PDF téléchargeables.
Refondu le 08/09/2026 (fin du thème « CRT terminal » Superdesign).

## Structure

```
build/content.py     # LE contenu (FR + EN) + LES palettes (thèmes clair/sombre) — source unique
build/site.py        # génère index.html (deux langues + deux thèmes dans le même fichier)
build/cv.py          # génère cv-stephen-casse-<fr|en>.pdf (2 pages A4, Chromium headless)
build/build.sh       # régénère tout
build/assets/        # logos sources (clair GTA VI, sombre Indigo — le CV réutilise le clair)
index.html           # GÉNÉRÉ — ne pas éditer à la main
assets/              # GÉNÉRÉ — logos servis par le site
cv-stephen-casse-fr.pdf, cv-stephen-casse-en.pdf   # GÉNÉRÉS
```

Aucun build côté GitHub Pages : le HTML généré est commité. Dépendances locales : `python3`,
`chromium` (pour les PDF). Polices Google Fonts (Space Grotesk + JetBrains Mono).

## Modifier le contenu

1. Éditer `build/content.py` (une mission, une compétence, un projet — dans les deux langues).
2. `./build/build.sh`
3. Vérifier `index.html` dans un navigateur (sélecteurs FR/EN et clair/sombre en haut à droite,
   mémorisés en localStorage ; par défaut = langue du navigateur et `prefers-color-scheme`).
4. Commit + push (ci-dessous).

## Identité visuelle

- Site clair = graine **GTA VI** (palette matugen du thème 6 du bureau Skynet) ; site sombre =
  identité **Indigo** `#8b93f8`. Quatre couleurs dominantes de la graine en rotation sur les accents.
- Les deux palettes vivent dans `build/content.py` (`THEMES`) : `site.py` en sort les deux thèmes,
  `cv.py` ne consomme que le **clair**, pour que le CV imprimé et le site en mode clair soient
  la même identité (bandeau = dégradé du hero, accents `#6866A7` / `#9775BA` / `#A86F9F`).
  L'ancienne palette CS Consulting (bleu nuit `#373643`, vert `#18cb96`, rouge `#ff4b4b`) reste
  dans `COMMON["palette"]` pour mémoire, plus rien ne s'en sert.
- Logo : les lettres gardent leur couleur d'origine, seuls le carré et le trait prennent les
  accents du thème (`build/assets/logo-light.png`, `logo-dark.png`).
- Conventions conservées : pas d'emoji, pas de photo, un projet privé affiche `// code privé`
  au lieu d'un lien mort, pas de valeur décorative codée en dur (uptime, commit…).

## Publication

Deux remotes :

- `origin` → Gitea privé (`ssh://git@norteo:2222/ksh/portfolio.git`) — source de vérité ;
- `github` → repo public [`ksh2177/ksh2177.github.io`](https://github.com/ksh2177/ksh2177.github.io),
  servi par **GitHub Pages** (branche `main`, racine, HTTPS forcé).

```bash
git push origin && git push github   # Pages redéploie en ~1 min
```

Vérifier : `curl -s https://ksh2177.github.io/ | grep '<title>'` (Ctrl+Shift+R côté navigateur).

## Backlog

- [ ] domaine perso pointé sur GitHub Pages (CNAME) ;
- [ ] remplacer la page Notion (supprimée) par un vrai formulaire de contact si besoin ;
- [ ] mettre à jour homelab.scasse.com (décrit l'infra 2025 Raspberry Pi, pas le NUC 2026).
