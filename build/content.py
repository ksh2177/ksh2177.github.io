# -*- coding: utf-8 -*-
"""Contenu unique du site et des CV — FR et EN. Modifier ICI, puis `./build/build.sh`."""

COMMON = dict(
    name="Stephen Casse", alias="ksh", company="CS Consulting",
    phone="06 58 44 35 79", mail="contact@scasse.com",
    linkedin="linkedin.com/in/stephen-casse", github="github.com/ksh2177", site="ksh2177.github.io",
)

# Palettes du site — source unique, consommées par site.py (les deux thèmes) et par cv.py
# (le thème clair uniquement : le CV imprimé suit l'identité du site en mode clair).
# clair = graine GTA VI (matugen sur le fond du thème 6), sombre = identité Indigo #8b93f8.
THEMES = {
    "light": dict(bg="#fdf7ff", low="#f7f2f9", card="#ffffff", text="#1c1b20", muted="#484550",
                  primary="#6866A7", on_primary="#ffffff", outline="#cac4d2", chip="#f2ecf3", chip_fg="#484550",
                  mono="#7a68b4", hero="linear-gradient(135deg, #f7f2f9 0%, #ece0f2 55%, #f9e3ee 100%)",
                  k=["#6866A7", "#9775BA", "#A86F9F", "#655164"], kb=["#6866A7", "#9775BA", "#C898C2", "#655164"]),
    "dark": dict(bg="#131319", low="#1b1b21", card="#1f1f25", text="#e4e1ea", muted="#c1c3f0",
                 primary="#8b93f8", on_primary="#000141", outline="#464652", chip="#292930", chip_fg="#e4e1ea",
                 mono="#8b93f8", hero="linear-gradient(135deg, #131319 0%, #1b1b2b 60%, #1f1f25 100%)",
                 k=["#8b93f8", "#6fd3a6", "#e2b25f", "#C793E0"], kb=["#8b93f8", "#6fd3a6", "#e2b25f", "#C793E0"]),
}

FR = dict(
    lang="fr", title="Ingénieur DevOps / SRE Freelance", subtitle="Vérification · Automatisation",
    location="Île-de-France · Remote", available="disponible pour mission",
    pitch=("Onze ans en production bancaire critique (Amundi, BPCE, Euler Hermes), et l'exploitation "
           "de mes propres produits — paiement Stripe, agrégation bancaire DSP2. J'applique l'ingénierie "
           "de production aux systèmes IA : pas les prompts, ce qu'il y a autour — preuve exécutable, "
           "coût mesuré, sécurité auditée, plan de sortie testé."),
    facts=[("11 ans", "production bancaire critique"),
           ("20 600 tests", "sur un SaaS que j'exploite : paiement, agrégation bancaire"),
           ("~1 200 serveurs", "service de consultation des logs, grand compte"),
           ("1 standard", "stack Apache portable RHEL 6 → 9.5, adoptée en production")],
    skills=[
        ("Automatisation & CI/CD", "Ansible, Ansible Automation Platform 2, AWX, Jenkins, GitLab CI, Bitbucket, Artifactory, XL Deploy / XL Release, ArgoCD, Helm, Kustomize"),
        ("Conteneurs & orchestration", "Docker, Kubernetes, K3s, Longhorn, MetalLB, ingress-nginx, cert-manager, Sealed Secrets"),
        ("Cloud & IaC", "Azure et Terraform (migration BPCE Lease 2021), XCP-ng, vSphere, Docker Compose"),
        ("Systèmes", "Red Hat (RHEL 6 → 9.5), SUSE, Debian/Arch, AIX, Solaris, Windows Server, Apache HTTPD, JBoss, Nginx"),
        ("Vérification", "Tests unitaires, tests de bout en bout, Vitest, Playwright, SonarQube, analyse statique de sécurité, détection de secrets, scan de vulnérabilités"),
        ("IA & agents", "LLMOps, Model Context Protocol (MCP), agents IA, sécurité des LLM, suivi de coût par modèle, Anthropic Claude"),
        ("Observabilité", "Prometheus, Grafana, Loki, OpenTelemetry, VictoriaMetrics, Centreon, Zabbix, AppDynamics, Splunk"),
        ("Sécurité", "SSL/TLS, OpenSSL, keystores JKS, Venafi, LDAP, Infisical, Authentik, durcissement Linux"),
        ("Langages", "Bash, Python, jq, YAML, Jinja2, JSON, Rust (notions)"),
    ],
    xp=[
        dict(co="CS Consulting", role="Ingénieur DevOps & Plateforme — Fondateur", when="févr. 2020 → aujourd'hui", where="Paris · hybride · indépendant",
             ctx="Ma structure : je conçois et j'exploite des produits de bout en bout — architecture, spécification, mise en production, exploitation, support. Auto-entrepreneur en 2020, EURL en 2023.",
             items=["<b>Du papier carbone au SaaS multi-tenant</b> : Astre Solutions gérait ses bons de commande et de livraison sur papier carbone, en double exemplaire. Je leur ai livré un outil de génération documentaire macOS, synchronisé et sauvegardé hors site. Le même client m'a ensuite confié l'automatisation des CERFA fluides frigorigènes pour Co&amp;Sta, puis le CRM, le planning, les techniciens — c'est devenu <b>Norteo</b>, aujourd'hui proposé à d'autres frigoristes avec son accord.",
                    "<b>Norteo</b>, SaaS de gestion multi-métier que je conçois et exploite : 15 métiers, 70 modèles de données, architecture multi-instance en marque blanche, isolation multi-tenant par JWT, MFA TOTP. Abonnements Stripe, agrégation bancaire via Bridge API v3 (agrégateur agréé DSP2) avec rapprochement automatique des paiements. Documents réglementaires générés : CERFA 15497, export SYDEREP.",
                    "Ce qui tient l'ensemble : <b>20 600 tests automatisés</b> — 19 000 unitaires (Vitest), 1 300 de bout en bout (Playwright) — porte qualité SonarQube bloquante avant le build, analyse statique de sécurité, détection de secrets et de vulnérabilités en intégration continue. Ces produits portent des chemins où circule de l'argent : je ne conçois pas mon métier comme écrire du code, mais comme <b>spécifier ce qui doit être vrai et construire la preuve que ça l'est</b>."]),
        dict(co="BPCE IT", role="Ingénieur DevOps Build & Intégration", when="nov. 2024 → aujourd'hui", where="Paris · hybride · freelance",
             ctx="Transformer un outil interne abandonné en service généralisé, sur un parc réparti sur quatre générations de RHEL.",
             items=["<b>Les logs aux développeurs, sans leur donner la production</b> : l'accès SSH est interdit en production aux équipes de développement — donc aucune consultation autonome d'un log applicatif, et des délais de résolution allongés à chaque incident. J'ai repris un outil périmé, non maintenu et non sécurisé pour en faire un service de consultation en libre-service : une instance par serveur, une URL dédiée, authentification LDAP/Kerberos, consultation et téléchargement par navigateur. La friction disparaît, la frontière de sécurité reste intacte. <b>Déployé sur ~1 200 serveurs</b>, adopté par l'ensemble des quinze DSI métier de la branche et utilisé par environ 200 personnes, DSI métier et exploitation confondues ; présenté en CODIR, à l'étude comme produit groupe.",
                    "<b>Ce qui rend le déploiement possible</b> : stack Apache compilée de bout en bout — Apache, APR, OpenSSL, OpenLDAP, Expat — sans aucune dépendance système, exécutable sans privilège root, de RHEL 6 à RHEL 9.5. Elle s'installe sur un Red Hat nu, cohabite avec un Apache ou un JBoss existant et survit à une montée de version d'OS — <b>adoptée comme standard de production</b>. Chaîne de livraison Bitbucket → Jenkins → Artifactory → XL Deploy.",
                    "<b>Inventaire dérivé de la CMDB</b> : l'inventaire Ansible Automation Platform était tenu à la main ; il est désormais construit dynamiquement depuis la CMDB, environnements normalisés — il découle de la source de vérité au lieu d'être déclaré deux fois. Même principe pour les keystores et truststores JKS.",
                    "Run quotidien, astreintes 24/7, référent d'un pôle applicatif auprès des DSIM ; formation de l'équipe (Ansible, Jenkins, Artifactory, Bitbucket) et présentation groupe d'Ansible Automation Platform."]),
        dict(co="Amundi", role="Ingénieur DevOps — référent applicatif, lead technique adjoint", when="janv. 2022 → oct. 2024", where="Paris · hybride · freelance",
             ctx="Périmètre applicatif d'une direction financière : quatre à cinq progiciels, interlocuteurs métier côté demande, appui direct du team leader.",
             items=["<b>Migration SAS de bout en bout</b> : outil d'analyse stratégique en fin de support — sans montée de version, la direction financière le perdait. Six mois, du cadrage à la mise en production, avec un consultant de l'éditeur : étude des cibles possibles et dimensionnement avec les équipes infra, cadrage du périmètre métier avec les utilisateurs, provisionnement, installation, raccordements réseau, LDAP et Active Directory, documentation, passation.",
                    "Bascule des clusters applicatifs et des bases automatisée lors des PSI : une procédure manuelle devenue <b>rejouable à l'identique</b>, sans saisie humaine. Déploiements Git → AWX → Ansible et Control-M « as code » (JSON/Jinja2 déployés par playbook). Météo applicative collectée et publiée par la chaîne, au lieu d'être relevée à la main chaque matin.",
                    "Migration Oracle Financials & OBIEE de Solaris vers SUSE ; applications portées par une plateforme Rancher Kubernetes pilotée par ArgoCD. Diagnostic des incidents sur l'ensemble du périmètre, en particulier ceux remontés sans élément technique exploitable ; réunions d'équipe animées en anglais ; formation des arrivants et documentation interne."]),
    ],
    xp_more=("Avant : BPCE Lease (2020 → 2021) — migration vers Azure reprise et livrée seul après le départ du chef de "
             "projet · Amundi (2017 → 2020) — analyste d'exploitation · Euler Hermes (2015 → 2017) — technicien "
             "d'exploitation & datacenter."),
    projects=[
        ("Homelab K3s 100 % GitOps", "homelab.scasse.com", "3 Raspberry Pi 4, K3s, MetalLB, Longhorn, cert-manager, Sealed Secrets, Argo CD App-of-Apps (9 apps), 3 playbooks Ansible, doc Hugo déployée par GitLab CI. État 2025 : l'infrastructure a depuis migré vers un socle XCP-ng.", "https://homelab.scasse.com"),
        ("Skynet — cockpit IA local-first", "Claude · MCP", "Assistant personnel piloté par Claude, tenu comme une application de production : CI à tolérance zéro, déploiement conditionné au vert, observabilité OpenTelemetry, suivi du coût par modèle, audits de sécurité rejoués à chaque évolution, exercice de reprise trimestriel.", None),
        ("nalarch — open source", "Rust · MIT", "Gestionnaire de paquets TUI pour Arch Linux ; rien ne s'exécute sans écran d'approbation.", "https://github.com/ksh2177/nalarch"),
    ],
    private="// code privé",
    edu=[("2018", "Certification ITIL (niv. 1)"), ("2017", "Piscine École 42 Paris — programmation C, notation par les pairs, aucun enseignant"),
         ("2016", "Certification administration AIX (niv. 1)")],
    langs=[("Français", "natif"), ("Anglais", "opérationnel — réunions d'équipe animées en anglais")],
    quotes=[],
    ui=dict(nav=["Expériences", "Projets", "Compétences", "Contact"], whoami="$ whoami",
            cv_btn="Télécharger le CV (PDF)", contact_btn="Me contacter",
            sec=dict(xp="expériences", projects="projets", skills="compétences", contact="contact",
                     edu="formation", langs="langues", quotes="on dit de moi"),
            tagline="Automatisons votre delivery.", cv_fr="CV français (PDF)", cv_en="CV anglais (PDF)",
            footer_right="construit en HTML statique · GitHub Pages", theme="Basculer clair / sombre",
            cv_file="cv-stephen-casse-fr.pdf", page="page"),
)

EN = dict(
    lang="en", title="Freelance DevOps / SRE Engineer", subtitle="Verification · Automation",
    location="Paris area, France · Remote", available="available for assignments",
    pitch=("Eleven years in critical banking production (Amundi, BPCE, Euler Hermes), plus the products "
           "I build and run myself — Stripe payments, PSD2 bank aggregation. I apply production engineering "
           "to AI systems: not the prompts, everything around them — executable proof, measured cost, "
           "audited security, a tested exit plan."),
    facts=[("11 years", "critical banking production"),
           ("20,600 tests", "on a SaaS I run myself: payments, bank aggregation"),
           ("~1,200 servers", "self-service log consultation, large account"),
           ("1 standard", "portable Apache stack, RHEL 6 → 9.5, adopted in production")],
    skills=[
        ("Automation & CI/CD", "Ansible, Ansible Automation Platform 2, AWX, Jenkins, GitLab CI, Bitbucket, Artifactory, XL Deploy / XL Release, ArgoCD, Helm, Kustomize"),
        ("Containers & orchestration", "Docker, Kubernetes, K3s, Longhorn, MetalLB, ingress-nginx, cert-manager, Sealed Secrets"),
        ("Cloud & IaC", "Azure and Terraform (BPCE Lease migration 2021), XCP-ng, vSphere, Docker Compose"),
        ("Systems", "Red Hat (RHEL 6 → 9.5), SUSE, Debian/Arch, AIX, Solaris, Windows Server, Apache HTTPD, JBoss, Nginx"),
        ("Verification", "Unit testing, end-to-end testing, Vitest, Playwright, SonarQube, static security analysis, secret detection, vulnerability scanning"),
        ("AI & agents", "LLMOps, Model Context Protocol (MCP), AI agents, LLM security, per-model cost tracking, Anthropic Claude"),
        ("Observability", "Prometheus, Grafana, Loki, OpenTelemetry, VictoriaMetrics, Centreon, Zabbix, AppDynamics, Splunk"),
        ("Security", "SSL/TLS, OpenSSL, JKS keystores, Venafi, LDAP, Infisical, Authentik, Linux hardening"),
        ("Languages", "Bash, Python, jq, YAML, Jinja2, JSON, Rust (basics)"),
    ],
    xp=[
        dict(co="CS Consulting", role="DevOps & Platform Engineer — Founder", when="Feb 2020 → present", where="Paris · hybrid · independent",
             ctx="My own company: I design and run products end to end — architecture, specification, go-live, operations, support. Sole trader in 2020, incorporated in 2023.",
             items=["<b>From carbon paper to a multi-tenant SaaS</b>: Astre Solutions ran its purchase and delivery notes on carbon paper, in duplicate. I delivered a macOS document generation tool, synchronised and backed up off site. The same client then asked me to automate refrigerant-gas regulatory forms for Co&amp;Sta, then the CRM, the scheduling, the field technicians — it became <b>Norteo</b>, now offered to other refrigeration companies with their agreement.",
                    "<b>Norteo</b>, a multi-trade management SaaS I design and operate: 15 trades, 70 data models, white-label multi-instance architecture, JWT tenant isolation, TOTP MFA. Stripe subscriptions, bank aggregation through Bridge API v3 (PSD2-licensed aggregator) with automatic payment reconciliation. Regulatory documents generated automatically.",
                    "What holds it together: <b>20,600 automated tests</b> — 19,000 unit (Vitest), 1,300 end-to-end (Playwright) — a blocking SonarQube quality gate before build, static security analysis, secret and dependency vulnerability scanning in CI. These products carry money paths: I do not see my job as writing code, but as <b>specifying what must be true and building the proof that it is</b>."]),
        dict(co="BPCE IT", role="DevOps Engineer, Build & Integration", when="Nov 2024 → present", where="Paris · hybrid · freelance",
             ctx="Turn an abandoned internal tool into a group-wide service, across an estate spanning four RHEL generations.",
             items=["<b>Logs for developers, without giving them production</b>: SSH access to production is denied to development teams — so no autonomous way to read an application log, and longer resolution times on every incident. I took over an outdated, unmaintained and insecure tool and turned it into a self-service log consultation service: one instance per server, a dedicated URL, LDAP/Kerberos authentication, browsing and download from the browser. The friction disappears, the security boundary stays intact. <b>Deployed on ~1,200 servers</b>, adopted by all fifteen business IT departments of the division and used by around 200 people across business IT and operations; presented to the executive committee, under review as a group product.",
                    "<b>What makes that deployment possible</b>: an Apache stack compiled end to end — Apache, APR, OpenSSL, OpenLDAP, Expat — with no system dependency, runnable without root privileges, from RHEL 6 to RHEL 9.5. It installs on a bare Red Hat, coexists with an existing Apache or JBoss and survives an OS upgrade — <b>adopted as the production standard</b>. Delivery pipeline Bitbucket → Jenkins → Artifactory → XL Deploy.",
                    "<b>Inventory derived from the CMDB</b>: the Ansible Automation Platform inventory was maintained by hand; it is now built dynamically from the CMDB with normalised environments — derived from the source of truth instead of being declared twice. Same principle for Java keystores and truststores.",
                    "Daily run, 24/7 on-call rotation, application-domain lead with the business IT departments; team training (Ansible, Jenkins, Artifactory, Bitbucket) and group-wide Ansible Automation Platform presentation."]),
        dict(co="Amundi", role="DevOps Engineer — application lead, deputy tech lead", when="Jan 2022 → Oct 2024", where="Paris · hybrid · freelance",
             ctx="Application scope of a finance division — finance, employee savings, private banking: four to five packaged products, business stakeholders on the demand side, direct support to the team leader.",
             items=["<b>End-to-end SAS migration</b>: a strategic analytics platform reaching end of support — without an upgrade, the finance division would lose it. Six months from scoping to go-live, alongside a vendor consultant: study of the possible targets and sizing with the infrastructure teams, scoping of the business perimeter with users, provisioning, installation, network, LDAP and Active Directory integration, documentation, handover.",
                    "Automated fail-over of application and database clusters during DR exercises: a manual procedure made <b>repeatable identically</b>, with no human input. Deployments Git → AWX → Ansible and Control-M “as code” (JSON/Jinja2 templates deployed by playbook). Daily application status collected and published by the pipeline instead of being checked by hand every morning.",
                    "Oracle Financials & OBIEE migration from Solaris to SUSE; applications running on a Rancher Kubernetes platform driven by ArgoCD. Diagnosis of incidents across the whole scope, in particular those reported with no usable technical evidence; team meetings run in English; onboarding of newcomers and internal documentation."]),
    ],
    xp_more=("Earlier: BPCE Lease (2020 → 2021) — migration of a critical reporting application to Azure, taken over and "
             "delivered single-handed after the project manager left · Amundi (2017 → 2020) — operations analyst, application "
             "production · Euler Hermes (2015 → 2017) — operations & datacenter technician."),
    projects=[
        ("Homelab K3s, 100 % GitOps", "homelab.scasse.com", "3 Raspberry Pi 4, K3s, MetalLB, Longhorn, cert-manager, Sealed Secrets, Argo CD App-of-Apps (9 apps), 3 Ansible playbooks, Hugo docs deployed by GitLab CI. As of 2025: the infrastructure has since moved to an XCP-ng platform.", "https://homelab.scasse.com"),
        ("Skynet — local-first AI cockpit", "Claude · MCP", "Personal assistant driven by Claude, run like a production application: zero-tolerance CI, deployment gated on green, OpenTelemetry observability, per-model cost tracking, security audits replayed on every change, quarterly recovery drill.", None),
        ("nalarch — open source", "Rust · MIT", "TUI package manager for Arch Linux; nothing runs without an approval screen.", "https://github.com/ksh2177/nalarch"),
    ],
    private="// private code",
    edu=[("2018", "ITIL certification (level 1)"), ("2017", "École 42 Paris “Piscine” — C programming, peer-graded, no teachers"),
         ("2016", "AIX administration certification (level 1)")],
    langs=[("French", "native"), ("English", "professional — team meetings run in English")],
    quotes=[],
    ui=dict(nav=["Experience", "Projects", "Skills", "Contact"], whoami="$ whoami",
            cv_btn="Download CV (PDF)", contact_btn="Get in touch",
            sec=dict(xp="experience", projects="projects", skills="skills", contact="contact",
                     edu="education", langs="languages", quotes="what they say"),
            tagline="Let's automate your delivery.", cv_fr="CV in French (PDF)", cv_en="CV in English (PDF)",
            footer_right="static HTML · GitHub Pages", theme="Toggle light / dark",
            cv_file="cv-stephen-casse-en.pdf", page="page"),
)

LANGS = {"fr": FR, "en": EN}
