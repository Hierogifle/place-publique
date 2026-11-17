# 0007 — Outillage de la direction artistique

- **Date :** 2026-11-17
- **Statut :** Acceptée
- **Décideurs :** Romuald

## Contexte
L'équipe veut une DA construite méthodiquement, du positionnement jusqu'au front, avec un contrôle qualité avant livraison.

## Décision
- Plugin **designskills** (marketplace `zstvns/design-skills`, v1.5.0) installé au niveau utilisateur : brand, brand-strategy, creative-direction, art-direction, logo-design, web-design, motion-design, collateral-design, design-principles.
- Skill **design-taste** (`h3nryprod01/design-taste`, v2.2.0) cloné dans `~/.claude/skills/` : contrôle qualité (`scripts/preflight.mjs`, Node ≥ 20 ✅ v22.21.0).
- Déroulé : brand → brand-strategy → creative-direction (3 stylescapes HTML) → art-direction → validation de `.agents/design.md` → web-design → motion-design → design-taste en contrôle final.

## Audit avant installation (lecture seule)
- ✅ Aucun hook, aucune commande, aucun serveur MCP dans les deux paquets ; `preflight.mjs` ne fait que lire des fichiers.
- ⚠️ Les skills n'écrivent **pas uniquement** dans `.agents/` : web-design et motion-design écrivent du code front ; plusieurs fichiers HTML n'ont pas d'emplacement imposé. Règle fixée : stylescapes et moodboards dans `.agents/stylescapes/`, front dans `app/templates` et `app/static`.

## Conséquences
- Les documents de DA vivent dans `.agents/` (brand.md, competitors.md, brand-strategy.md, puis design.md) et sont versionnés.
- Aucun front n'est implémenté avant validation de `.agents/design.md`.
