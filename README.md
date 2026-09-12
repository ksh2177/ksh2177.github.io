# portfolio — site CV de Stephen Casse

Site CV portfolio une page, **en ligne sur https://ksh2177.github.io/** (CS Consulting,
Ingénieur DevOps freelance). Bilingue **FR / EN**, thème **clair / sombre**.
Refondu le 08/09/2026 (fin du thème « CRT terminal » Superdesign).

## Ce que produit le repo

Une seule source de contenu, **cinq livrables** :

| Livrable | Fichier | Rôle |
| --- | --- | --- |
| Site | `index.html` | la vitrine publique, deux langues et deux thèmes dans un seul fichier |
| CV PDF | `cv-stephen-casse-{fr,en}.pdf` | 2 pages A4, **téléchargeables depuis le site** |
| CV Word | `cv-stephen-casse-{fr,en}.docx` | le même CV, **éditable** — envoi direct, plateformes de sourcing, ESN |

Le site ne propose **que les PDF** au téléchargement : le `.docx` existe pour être envoyé à
la main quand un interlocuteur réclame un Word, pas pour être exposé publiquement.

Tout sort de `build/content.py` : une mission corrigée là est corrigée dans les cinq. C'est
la règle du repo — il n'y a qu'un seul endroit où écrire, et il n'y en aura pas deux (le CV
Word a longtemps vécu à part, sur un template ESN hérité ; il divergeait déjà du reste).

## Structure

```
build/content.py     # LE contenu (FR + EN) + LES palettes (thèmes clair/sombre) — source unique
build/site.py        # génère index.html (deux langues + deux thèmes dans le même fichier)
build/cv.py          # génère cv-stephen-casse-<fr|en>.pdf  (2 pages A4, Chromium headless)
build/docx.py        # génère cv-stephen-casse-<fr|en>.docx (2 pages A4, OOXML à la main)
build/build.sh       # régénère tout
build/assets/        # logos sources (clair GTA VI, sombre Indigo — les CV réutilisent le clair)
index.html           # GÉNÉRÉ — ne pas éditer à la main
assets/              # GÉNÉRÉ — logos servis par le site
cv-stephen-casse-{fr,en}.{pdf,docx}   # GÉNÉRÉS
```

Aucun build côté GitHub Pages : tout est généré ici et commité. Dépendances locales :
`python3` et `chromium` (impression des PDF). Le site charge ses polices depuis Google Fonts
(Space Grotesk + JetBrains Mono).

## Modifier le contenu

1. Éditer `build/content.py` (une mission, une compétence, un projet — dans les deux langues).
2. `./build/build.sh`
3. Vérifier `index.html` dans un navigateur (sélecteurs FR/EN et clair/sombre en haut à droite,
   mémorisés en localStorage ; par défaut = langue du navigateur et `prefers-color-scheme`).
4. Vérifier les CV — voir ci-dessous, **les deux formats doivent tenir en 2 pages**.
5. Commit + push (§ Publication).

## Vérifier les CV

Le PDF est composé par Chromium sur des pages de **hauteur fixe** (`@page 794×1123`, `.pg` en
`overflow: hidden`) : un texte allongé ne repousse rien, il passe **par-dessus le pied de page**
ou disparaît sous la découpe — et le fichier fait toujours 2 pages. Le `.docx`, lui, est en flux
Word : il ne chevauche pas, il pousse le bloc formation / langues sur une troisième page.

> ⚠️ **`pdfinfo | grep Pages` ne peut pas détecter le débordement du PDF.** Il reste à 2 quoi
> qu'il arrive. Le seul contrôle valable est le **rendu image des deux pages**, relu — vécu le
> 12/09/2026 deux fois : une ligne de renvoi passée sous le pied de page, puis un bloc collé à
> lui. Le garde-fou `padding-bottom: 46px` sur `.body` réserve désormais la hauteur du pied de
> page, mais il ne dispense pas de regarder.

```bash
pdfinfo cv-stephen-casse-fr.pdf | grep Pages        # attendu : 2 — nécessaire, pas suffisant
pdftoppm -png -r 85 cv-stephen-casse-fr.pdf /tmp/cv # puis RELIRE les deux images

# le .docx, rendu via LibreOffice (outil de contrôle seulement, pas une dépendance du build)
soffice --headless --convert-to pdf --outdir /tmp cv-stephen-casse-fr.docx
pdfinfo /tmp/cv-stephen-casse-fr.pdf | grep Pages   # attendu : 2
pdftoppm -png -r 110 /tmp/cv-stephen-casse-fr.pdf /tmp/apercu   # relecture visuelle
```

Faire les deux langues : l'anglais est plus court en moyenne, mais certains libellés (dates,
localisation) y sont plus longs.

Si une page 3 réapparaît dans le `.docx`, la hauteur se récupère dans `docx.py` sur les marges
de page (`MARGIN`), l'interligne des puces (`line`) et leur `after`, le `before` des titres de
section et des blocs d'expérience — pas en réduisant le corps de texte. Si c'est le **PDF** qui
déborde, la hauteur ne se récupère pas : elle se redistribue, en déplaçant une expérience de la
page 1 vers la page 2 (`L['xp'][:2]` / `[2:]` dans `cv.py`) ou en passant une grille de deux à
trois colonnes.

## Le CV Word (`build/docx.py`)

OOXML écrit à la main : un `.docx` est un zip de fichiers XML, le script les assemble
(`document.xml`, `styles.xml`, le logo, les relations). **Aucune dépendance ajoutée** —
`python-docx` n'est pas installé et le repo tient à ne dépendre que de `python3` + `chromium` ;
c'est le même parti pris que `site.py`, qui écrit son HTML directement.

Deux écarts assumés avec le PDF, parce qu'un Word est relu et **édité chez quelqu'un d'autre** :

- **polices Calibri + Consolas** au lieu de Space Grotesk / JetBrains Mono, que le destinataire
  n'aurait pas. Calibri est substituée par Carlito sous Linux, aux métriques identiques, donc
  la mise en page ne bouge pas ; Segoe UI, essayée d'abord, tombait sur une serif quelconque ;
- **la localisation se pose sur une tabulation droite** de la ligne `whoami`. En colonne dédiée
  — ce que le PDF se permet en flex — « Île-de-France · Remote » se coupait en deux lignes.

Les constructeurs XML (`rpr`, `para`, `cell`) prennent leurs réglages en **options nommées**
plutôt qu'en paramètres positionnels : c'est ce qu'impose le hook qualité (max 5 paramètres),
et ça évite des appels illisibles à sept arguments.

## Identité visuelle

- Site clair = graine **GTA VI** (palette matugen du thème 6 du bureau Skynet) ; site sombre =
  identité **Indigo** `#8b93f8`. Quatre couleurs dominantes de la graine en rotation sur les accents.
- Les deux palettes vivent dans `build/content.py` (`THEMES`) : `site.py` en sort les deux thèmes,
  `cv.py` et `docx.py` ne consomment que le **clair**. Le CV imprimé et le site en mode clair
  sont donc la même identité : bandeau = dégradé du hero, accents `#6866A7` / `#9775BA` (titres,
  icônes, `whoami`) et `#A86F9F` (dates, liserés). Aucune couleur n'est codée en dur ailleurs.
- Logo : les lettres gardent leur couleur d'origine, seuls le carré et le trait prennent les
  accents du thème (`build/assets/logo-light.png`, `logo-dark.png`). Les CV réutilisent le logo
  clair — il n'y a pas d'asset dédié au CV à maintenir en double.
- Conventions conservées : pas d'emoji, pas de photo, un projet privé affiche `// code privé`
  au lieu d'un lien mort, pas de valeur décorative codée en dur (uptime, commit…).
- Historique, pour ne pas les remettre par erreur : la palette CS Consulting bleu nuit `#373643`
  / vert `#18cb96` / rouge `#ff4b4b` (les CV d'avant le 08/09) et l'or `#CDA963` sur marine
  `#233142` du template ESN sont **abandonnées**.

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
