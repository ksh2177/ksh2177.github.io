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

## 🎯 12 SEPTEMBRE 2026 — le CV rejoint le positionnement LinkedIn

Séance ouverte par une comparaison CV ↔ profil LinkedIn, trois jours après la refonte
intégrale du profil (11/09). Verdict : pas une contradiction, une **omission asymétrique** —
chaque support disait vrai, aucun ne disait tout.

### Fait
- `df78dc0` — alignement complet du contenu (`build/content.py`) : CS Consulting devient la
  première expérience (arc Astre Solutions → Co&Sta → Norteo, puis le produit, puis les
  20 600 tests) ; BPCE IT renversé (le projet est le service de consultation des logs,
  ~1 200 serveurs et les quinze DSI de la branche ; la stack Apache portable est ce qui le
  rend déployable) ; Amundi gagne la migration SAS menée de bout en bout ; titre, pitch et
  tuiles portent la vérification ; familles de compétences « Vérification » et « IA & agents ».
- Exactitude : entrée chez Amundi ramenée à **nov. 2017** (le trou de douze mois affiché
  n'existait pas — enchaînement à une semaine d'Euler Hermes) ; chevauchement Amundi / BPCE IT
  supprimé ; « 11 ans » au lieu de « 10 ans » ; « 80 % de temps gagné » retiré faute de preuve ;
  citations sans auteur supprimées ; OpenShift retiré (pas en production) ; « AP2 » écrit en
  toutes lettres ; entité unifiée sur BPCE IT.
- Rendu : ligne de couverture ajoutée au PDF et au Word, colonne citations conditionnelle,
  projets sur trois colonnes, répartition 2 blocs page 1 / 1 page 2. `docx.py` : entités HTML
  décodées, saut de page forcé retiré, marges resserrées.
- `Perso/notes` `092ba29` — `docs/ksh-carriere/matiere.md`, l'inventaire de carrière privé qui
  alimente désormais les trois supports ; les cinq notes LinkedIn de juin 2025 marquées périmées.

### Décisions prises
- **Un inventaire unique précède les supports.** La divergence ne venait pas d'un défaut de
  mémoire mais de son absence : le CV ignorait le service de logs, la migration SAS et
  CS Consulting ; LinkedIn ignorait la bascule PSI et le Control-M as code. L'inventaire vit
  dans `Perso/notes`, pas ici — ce dépôt pousse sur GitHub Pages, donc en public.
- **Règle d'exposition.** Ne jamais publier la topologie de ce qui tourne : adresses, noms
  d'hôtes, versions en exploitation, réseau. Se publient sans coût les décisions, les principes,
  les méthodes, les effets. Conséquences immédiates : la fiche « Hub » est retirée (elle
  décrivait l'infra vivante) et le homelab est daté « état 2025 » — un montage démantelé
  enseigne sans rien ouvrir, c'est ce qui en fait une bonne pièce publique.
- **Le CV n'est pas cumulatif : une fenêtre glissante plus une ligne d'horizon.** Trois blocs
  détaillés (CS Consulting, BPCE IT, Amundi), le reste en une ligne de couverture qui garde les
  dates et les noms. Le coût d'une ligne est constant, celui d'un bloc croît avec la carrière :
  ce qui vieillit passe du bloc à la ligne, jamais du bloc au néant. e-Crea retirée du CV, gardée
  sur LinkedIn où la place est gratuite.
- **Un chiffre affiché engage la chronologie.** Annoncer onze ans et ne montrer que 2020 → 2026
  recrée l'incohérence « 8 ans / 10 ans » corrigée le 08/09. Soit la couverture suit le compteur,
  soit le compteur descend.

### Reste à faire
- Corriger LinkedIn : l'entrée Amundi y affiche encore nov. 2018.
- Trancher les questions ouvertes de `matiere.md` : la migration Oracle Financials / OBIEE
  Solaris → SUSE (réalisation ou accompagnement ?) et les chiffres du service de logs
  (~1 200 / 15 DSI contre 800-900 / 10 au deck CODIR de février).
- L'écrit public sur la vérification — la pièce qui manque pour que le positionnement tienne
  par lui-même, et la première entrée de la section Sélection le jour où elle existe.

### Suite de séance — la matière continue de remonter

Quatre échanges après la livraison, quatre faits que ni le CV ni LinkedIn ne portaient. Le
biais d'omission a donc frappé une quatrième fois dans la même journée.

- `565f55e` / `6ab15e0` — le service de logs affiche son **usage** : ~200 personnes, DSI métier
  et exploitation confondues. Un compte de serveurs prouve un déploiement, un compte
  d'utilisateurs prouve un usage ; et une adoption *des deux côtés* de la frontière de sécurité
  — ceux à qui la production est interdite et ceux qui l'exploitent — dit ce que « 200
  utilisateurs » seul ne dit pas.
- `081dac5` — **le pilote groupe Ansible Automation Platform**, que Stephen désigne lui-même
  comme le sujet dont il est le plus fier, et qui tenait jusque-là en six mots (« inventaire
  dynamique »). Premier périmètre du groupe à recevoir la plateforme, livrée nue : modèle
  d'habilitation instruit, nomenclatures et granularité de déploiement définies, inventaire
  dérivé de la CMDB *et enrichi* des variables des playbooks, standards présentés en CODIR puis
  répliqués sur une seconde production applicative par une formation qu'il a menée. C'est le
  seul endroit du dossier où le travail a été **repris par d'autres équipes sur décision de la
  hiérarchie**.
- `528579e` — AAP2 remonte en tête du bloc et les deux sections du service de logs sont
  réunies. Elles forment une paire causale (le service, puis pourquoi il fallait tout embarquer
  dans un binaire autonome) : une section intercalée oblige le lecteur à revenir en arrière.
  L'ordre suit la **cible de mission** — Ansible avant Apache — pas la chronologie.
- `de49322` — le corps du CV réserve la hauteur du pied de page.

### Décisions prises (suite)

- **Quatre questions contre l'omission**, écrites dans `matiere.md` et à rejouer avant chaque
  candidature : qu'ai-je reçu nu ou cassé et rendu utilisable ? qu'ai-je normé que d'autres
  appliquent ? qu'ai-je présenté ou fait arbitrer au-dessus de mon niveau ? qu'est-ce qui tourne
  encore sans moi ? Elles ont débusqué les quatre morceaux manquants.
- **`pdfinfo` ne vérifie pas la mise en page du PDF.** Les pages sont à hauteur fixe et `.pg` est
  en `overflow: hidden` : un contenu trop long chevauche le pied de page ou disparaît, et le
  compteur reste à 2. Deux occurrences dans la journée, dont une vue par Stephen et non par le
  contrôle automatique. Correctifs : `padding-bottom: 46px` sur `.body`, et la procédure du
  README exige désormais la **relecture du rendu image**.
- **Où récupérer de la hauteur**, selon le format : dans le `.docx` (flux) on resserre marges,
  interligne et espacements ; dans le PDF (pages fixes) la hauteur ne se récupère pas, elle se
  **redistribue** — une expérience bascule en page 2, ou une grille passe de deux à trois
  colonnes.

### Suite — la page LinkedIn CS Consulting et les deux bannières

Le chantier CV a débordé sur la présence LinkedIn : page entreprise CS Consulting refaite de bout
en bout (slogan, descriptif, 18 spécialisations, services, localisation) et deux bannières
générées depuis l'identité du site.

- `build/bannieres.py` — page entreprise 1128 × 191 et profil personnel 1584 × 396, rendues en 2×,
  palette et logo lus dans `content.py`. Les PNG ne sont pas commités : ils se régénèrent.
  Documenté dans le README.

### Décisions prises (bannières)

- **Ne pas redire ce que la page affiche déjà.** L'avatar LinkedIn porte le logo : le répéter dans
  la bannière faisait doublon, il n'en reste que les couleurs. Même raisonnement sur le profil, où
  LinkedIn affiche nom et titre juste en dessous — la bannière n'y garde que les preuves chiffrées.
- **La palette vient du logo, mesurée sur le fichier** (`#30303c` 79 %, `#60609c` 18 %, `#906cb4`
  4 %), pas reproduite à l'œil. Le pourcentage de pixels donne aussi la hiérarchie : l'anthracite
  est la dominante, le violet un accent.
- **Réserver la zone de l'avatar.** Il déborde sur la bannière en bas à gauche ; tout ce qui s'y
  trouve est masqué. C'est ce qui coupait « Automatisation » sur l'ancienne bannière de profil.
- **Juger l'image à la taille où elle est affichée.** LinkedIn rend la bannière à environ la moitié
  de sa taille source : un texte de 12 px y devient 6 px. Contrôle désormais systématique — réduire
  le PNG au quart avant de le regarder. Même famille d'erreur que `pdfinfo` sur le CV : un contrôle
  qui ne reproduit pas les conditions réelles ne contrôle rien.
- **Un indicateur doit répondre à « et alors ? ».** « 1 standard » ne disait rien ; « 1 200
  serveurs » pouvait décrire un exécutant. Chaque légende porte maintenant le verbe qui distingue —
  conçu, défini, adopté. « Pilote groupe » a remplacé « 1 standard » : c'est la réalisation la plus
  forte du dossier, et elle n'apparaissait sur aucun support.
