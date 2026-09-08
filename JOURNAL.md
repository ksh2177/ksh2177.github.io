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
- Tentative, sur cette passe, de repeindre aussi le dossier de compétences Word hors repo
  (`~/Business/CV/CS_CONSULTING_CV_2026`) : accent or `#CDA963` → `#6866A7`, logo et filigrane
  par rotation de teinte, surlignages jaunes retirés, tampon ISO 9001 supprimé. **Annulé** à la
  3e passe (voir plus bas) : les fichiers du poste ont été remis à l'identique, empreintes
  vérifiées. Mauvaise piste — on retapait un document qui n'était pas la source.

### Décisions prises (2e passe)
- Le CV imprimé suit le thème **clair** du site, pas une palette à lui : une seule identité.
- Bandeau du CV = dégradé du hero plutôt qu'aplat violet (choix de Stephen sur maquette) —
  fidélité maximale au site, et plus besoin d'un logo dédié au CV.
- `COMMON["palette"]` (bleu/vert/rouge) ne sert plus à rien ; retirée à la 4e passe.

### Fait (3e passe — le CV Word rentre dans le repo)

- Le CV Word vivait hors du repo (`~/Business/CV/CS_CONSULTING_CV_2026.doc[x]`), sur un vieux
  template ESN 5 pages hérité (or `#CDA963` sur marine, tampon ISO 9001 d'une autre société,
  surlignages jaunes de relecture). Repeindre ce document était une impasse : il ne partageait
  ni le contenu ni la palette du reste. Il est **abandonné** (laissé intact sur le poste).
- `build/docx.py` génère désormais `cv-stephen-casse-{fr,en}.docx` depuis `content.py` :
  même contenu, même modèle 2 pages, même palette que le PDF. Ajouté à `build.sh`.
- OOXML écrit à la main (zip + XML), **aucune dépendance** ajoutée — `python-docx` n'est pas
  installé et le repo tient à ne dépendre que de python3 + chromium.

### Décisions prises (3e passe)
- Une seule source pour **cinq** livrables : site, PDF FR/EN, Word FR/EN. Plus de CV « à part ».
- Polices du `.docx` : **Calibri + Consolas** au lieu de Space Grotesk / JetBrains Mono — un
  Word est relu et édité ailleurs ; Calibri est substituée par Carlito à métriques identiques
  sous LibreOffice, là où Segoe UI tombait sur une serif quelconque.
- Bandeau : la localisation se pose sur une tabulation droite de la ligne `whoami`. Une colonne
  dédiée (ce que le PDF fait en flex) coupait « Île-de-France · Remote » en deux lignes.
- Le tampon ISO 9001 disparaît de fait avec le vieux template : il n'a jamais appartenu à CS
  Consulting, il venait du dossier de compétences de l'ESN d'origine.
- Ce qui a coûté du temps : avoir cru que le `.doc` hérité *était* le CV à faire évoluer. Le
  bon réflexe était de regarder d'où venait le PDF (du repo) et de faire descendre le Word
  depuis la même source, pas de remonter le PDF vers le Word.

### Fait (4e passe — documentation)
- README refondu : tableau des cinq livrables, procédure de vérification des CV (`pdfinfo`,
  rendu LibreOffice, les deux langues), section dédiée à `docx.py` (OOXML sans dépendance,
  les deux écarts assumés avec le PDF, options nommées imposées par le hook qualité), et
  historique des palettes abandonnées pour ne pas les réintroduire.
- `COMMON["palette"]` retirée de `content.py` : plus aucun lecteur depuis la 2e passe. Les
  hex restent consignés dans le README, section Identité visuelle.

### Décisions prises (4e passe)
- Le site ne propose **que les PDF** au téléchargement. Le `.docx` est un livrable d'envoi
  direct (sourcing, ESN qui réclament un Word), pas une pièce exposée publiquement.
- Pas de `.doc` legacy : le générer imposerait LibreOffice comme dépendance du build pour un
  format que plus personne n'exige. À reconsidérer seulement si un client le demande.
