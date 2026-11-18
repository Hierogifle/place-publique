# 0002 — Branches personnelles `Romuald` et `Olivier`

- **Date :** 2026-11-17
- **Statut :** Rétablie par [0028](0028-chacun-sa-branche-puis-branches-de-feature.md) (0017 l'avait remplacée par erreur)
- **Décideurs :** Romuald

## Contexte
Deux personnes travaillent sur le dépôt ; la note est ajustée individuellement d'après l'historique Git (sujet, grille d'évaluation ✅).

## Décision
Création de deux branches `Romuald` et `Olivier` à partir de `main` (commit `29fb93b`), poussées sur GitHub.

## Options écartées
Aucune discutée à ce moment-là : c'était une demande directe pour démarrer.

## Conséquences
- Une branche par personne vieillit mal : elles divergent, et les fusions deviennent pénibles.
- Proposition de Claude, en attente (jamais validée par Romuald ; voir 0028) : `main` protégée (déploiement), `dev` (intégration), branches `feature/*` courtes par tâche, fusion par pull request. L'auteur de chaque commit reste visible, donc la contribution individuelle reste prouvée.
