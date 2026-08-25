# portfolio — site CV de Stephen Casse

Site CV portfolio une page, **en ligne sur https://ksh2177.github.io/**.
Design « CRT terminal phosphore vert » créé sur [superdesign.dev](https://superdesign.dev), puis
personnalisé en français (CS Consulting, Ingénieur DevOps freelance).

## Structure

```
index.html                      # tout le site : une seule page autonome
.superdesign/design-system.md   # le design system CRT (palette, typo, effets, composants)
.superdesign/resume.json        # état de reprise Superdesign (projectId + draftId du canvas)
```

`index.html` n'a **aucun build** : Tailwind via CDN, polices Google Fonts (JetBrains Mono +
IBM Plex Mono). L'ouvrir directement dans un navigateur suffit pour prévisualiser.

## Contenu (repères pour éditer)

Une section = un bloc `<section id="…">` dans `index.html` :

| Section | id | Contenu |
|---|---|---|
| Hero | `#hero` | bannière STEPHEN CASSE, rôle, bio, CTA |
| Neofetch | `#identity` | avatar ASCII + fiche système (rôle, stack, statut) |
| Projets | `#work` | 6 cartes : norteo, hub, skynet, nalarch, aubevent, homelab (→ homelab.scasse.com) |
| Compétences | `#stack` | 8 barres (CI/CD, Ansible, OpenShift/K8s, Docker, ArgoCD, Linux, Observabilité, Python/Bash) |
| Contact | `#contact` | command box → LinkedIn, pills github + linkedin |

Conventions du design (détail dans `.superdesign/design-system.md`) :

- prompt du terminal : `ksh2177 ~/devops $` ;
- l'**ambre** (`#ffd24a`) est réservé au statut et aux tags — jamais pour les titres ;
- pas d'emoji, pas de photos, brackets ASCII `[x]` au lieu de checkmarks ;
- les liens morts sont interdits : un projet privé affiche `// code privé` au lieu d'un lien.

## Publication

Deux remotes :

- `origin` → Gitea privé (`ssh://git@norteo:2222/ksh/portfolio.git`) — source de vérité ;
- `github` → repo public [`ksh2177/ksh2177.github.io`](https://github.com/ksh2177/ksh2177.github.io),
  servi par **GitHub Pages** (branche `main`, racine, HTTPS forcé).

Déployer une modification :

```bash
git push origin && git push github   # Pages redéploie en ~1 min
```

Vérifier : `curl -s https://ksh2177.github.io/ | grep '<title>'` (penser au Ctrl+Shift+R côté navigateur).

## Itérer sur le design (Superdesign)

Le draft d'origine reste lié via `.superdesign/resume.json`. Pour une évolution **visuelle**
(pas un simple changement de texte), passer par le canvas :

```bash
npx --yes @superdesign/cli@latest                # preflight (vérifie l'auth)
npx --yes @superdesign/cli@latest iterate-design-draft \
  --draft-id 0d582d82-96a8-4767-bdb8-588a2dd04884 \
  -p "<direction souhaitée>" --mode replace      # branch = pour comparer des variantes
npx --yes @superdesign/cli@latest get-design \
  --draft-id 0d582d82-96a8-4767-bdb8-588a2dd04884 --output index.html
```

⚠️ `get-design --output` **écrase** `index.html`, y compris la personnalisation du contenu :
itérer sur le canvas d'abord, récupérer ensuite, puis re-personnaliser (ou porter les changements
à la main). Le skill agent est installé dans `~/.claude/skills/superdesign/`.

## Évolutions envisagées (backlog)

- [ ] `cv.pdf` téléchargeable (re-ajouter la pill « cv.pdf » du design d'origine) ;
- [ ] domaine perso (ex. `cs-consulting.fr`) pointé sur GitHub Pages (CNAME) ;
- [ ] responsive mobile à vérifier finement (nav du terminal sur petit écran) ;
- [ ] éventuelle version anglaise ;
- [ ] variantes visuelles via le canvas Superdesign (mode branch).
