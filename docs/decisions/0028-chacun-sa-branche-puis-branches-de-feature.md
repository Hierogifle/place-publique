# 0028 — Chacun sa branche pendant le développement, branches de feature ensuite

- **Date :** 2026-11-18
- **Statut :** Acceptée
- **Décideurs :** Romuald
- **Rétablit :** [0002](0002-branches-personnelles.md)
- **Remplace en partie :** [0017](0017-workflow-git-et-github.md) (la partie sur les branches de travail ; `main`, `dev`, protections, CI et CD restent valables)

## Contexte
La fiche 0017 rangeait les branches personnelles `Romuald` et `Olivier` dans les options écartées et prévoyait de les supprimer. **Romuald ne l'avait jamais décidé** : c'était une proposition de Claude (déjà écrite comme « proposition en attente » dans 0002), notée par erreur comme une décision. `CONTRIBUTING.md` reprenait cette erreur. Le 18/11, la session Claude d'Olivier a lu ces deux fichiers et lui a conseillé de ne plus utiliser sa branche.

## Décision
Deux temps.

1. **Pendant le développement de l'application (maintenant) : chacun sa branche.**
   - Romuald travaille sur `Romuald`, Olivier sur `Olivier`, chacun à son rythme, sans contrainte de taille ni de durée.
   - Quand un travail est prêt, son auteur ouvre une PR de sa branche vers `dev`. L'application se construit ainsi dans `dev`.
2. **Une fois l'application développée : branches de feature.**
   - Une branche courte par fonctionnalité ou correction (`feature/`, `fix/`, `docs/`, `chore/`), créée depuis `dev` et fusionnée dans `dev` par PR.
   - Le moment de la bascule est décidé par Romuald et Olivier ; il n'est pas encore fixé.

Inchangé (0017) : `main` et `dev` protégées, pas de push direct, PR obligatoire, CI verte, `dev` → `main` en fin de palier, CD Docker à chaque push sur `main`, messages de commit `type: description`.

## Options écartées
- **Branches de tâche dès maintenant** (ce qu'écrivait 0017) : Romuald veut que chacun développe tranquillement de son côté tant que l'application n'existe pas.

## Conséquences
- Les branches `Romuald` et `Olivier` sont gardées. **Elles sont en retard sur `dev`** (`Romuald` s'arrête au commit `3ff9435`, `Olivier` au commit `29fb93b` du 17/11). Chacun doit d'abord mettre la sienne à jour depuis `dev` avant de s'en servir (voir `CONTRIBUTING.md`).
- Les branches courtes déjà fusionnées (PR #1 à #8) restent dans l'historique ; rien à défaire.
- Olivier a poussé un premier travail sur `docs/veille-olivier`, en suivant l'ancienne règle. Il choisit s'il le passe sur sa branche `Olivier` ou s'il ouvre la PR vers `dev` telle quelle.
- Risque connu : deux branches longues divergent de `dev`. On le limite en ouvrant des PR vers `dev` régulièrement et en récupérant `dev` sur sa branche après chaque fusion.
