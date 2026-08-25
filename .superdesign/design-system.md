# CRT Terminal Portfolio — Design System

## Color Palette (CSS Variables)

```css
--phosphor: #39ff7a          /* Primary accent, text-shadow glow */
--phosphor-dim: #2bbf5c      /* Dimmer green for bars/supporting elements */
--phosphor-faint: #1c7a3c    /* Faint green for body text accents */
--sage: #5f8d68              /* Muted sage for body text */
--near-white: #eafff1        /* Headings and strong text */
--amber: #ffd24a             /* Status dot and highlighted tags only */
--cyan: #5cf6ff              /* Prompt glyphs only (user@host) */
--bg-black: #000000          /* Canvas background */
--panel-black: #050805       /* Panel backgrounds */
--border-dim: #143614        /* Panel borders (brighter #1f4d1f on hover) */
```

## Typography

**Primary Font:** JetBrains Mono (400-800)
**Secondary Font:** IBM Plex Mono (300-600)
**Fallback:** monospace

- Name banner: 60px / weight 800 / glow-text
- Section headings: ~24px / weight 700
- Role/accent lines: 17-18px / weight 600
- Body text: 14-16px / weight 400
- Meta/labels: 12px / weight 500
- UI labels: 10-12px / weight 600 / uppercase tracking-wider

## Core Effects

- Phosphor glow: `text-shadow: 0 0 8px rgba(57,255,122,.45), 0 0 24px rgba(57,255,122,.18)` (name, role, buttons)
- Glow soft: `text-shadow: 0 0 12px rgba(57,255,122,.25)` (ASCII avatar, labels)
- Amber glow: `text-shadow: 0 0 10px rgba(255,210,74,.4)` (status dot, stars, tags)
- CRT scanlines: fixed repeating-linear-gradient overlay, mix-blend-mode multiply, opacity .5, z-index 100
- Radial glows: top-right rgba(57,255,122,.08), bottom-left rgba(57,255,122,.05)
- Blinking cursor: `steps(2, start)` 1.1s, 3 emplacements stratégiques (hero, command box, footer)
- Text selection: rgba(57,255,122,.3) sur blanc

## Layout

- Container max-width: 1120px
- Terminal window: rounded 8px, border dim-green, title bar 44px, footer strip
- Section spacing: py-24 ; panel padding p-5 à p-12 ; radii 3-8px max

## Composants réutilisables

1. Terminal window frame (title bar traffic lights + nav ~/work ~/stack ~/contact + badge amber « available »)
2. Section prompt header (`user` cyan / `~/dev $` phosphor / commande near-white)
3. Name banner + cursor-blink
4. ASCII avatar (pre, glow-soft)
5. Neofetch identity list (clés phosphor / valeurs sage, Status amber)
6. Project card (dossier/, ★ count amber, permissions unix, tags, liens → Live Demo / → Source)
7. Skill bar meter (gradient phosphor-dim→phosphor + glow)
8. Command box CTA (`$ mail …` + cursor)
9. Social pills (bordure dim → phosphor au hover, flèche translate)
10. Footer strip (echo copyright + fake git status)

## Principes clés

1. Monospace partout — hiérarchie par taille/graisse/glow uniquement
2. Le glow phosphore est l'accent principal
3. L'ambre est réservé au statut/tags — jamais pour le corps ou les titres
4. Effet CRT non négociable (scanlines + radial glows)
5. Brackets ASCII `[x]` au lieu de checkmarks
6. Pas de photos stock, pas d'emoji, pas d'effets glossy
