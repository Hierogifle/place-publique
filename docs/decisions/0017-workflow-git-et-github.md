# 0017 — Workflow Git et GitHub : main, dev, branches de tâche, CI/CD

- **Date :** 2026-11-17
- **Statut :** Acceptée
- **Décideurs :** Romuald
- **Remplace :** [0002](0002-branches-personnelles.md)

## Contexte
Deux personnes, 15 jours, une note ajustée d'après l'historique Git. Romuald voulait une branche protégée reliée au déploiement Docker, une préproduction, une branche de développement. Le sujet exige une CI qui lance les tests et construit l'image, et accepte un déploiement simulé en local.

## Décision
- **`main`** : ce qui marche et qu'on peut montrer. Protégée : pas de push direct, merge par pull request seulement, CI verte obligatoire. Chaque push déclenche la **CD** : image Docker publiée sur `ghcr.io/hierogifle/place-publique` (`latest` + numéro court du commit).
- **`dev`** : l'intégration. Protégée de la même façon. Joue le rôle de **préproduction**.
- **Branches de tâche** courtes (`feature/`, `fix/`, `docs/`, `chore/`), une par tâche du plan, fusionnées dans `dev` par PR ; `dev` → `main` en fin de palier.
- **CI** (`.github/workflows/ci.yml`) : lint ruff + pytest à chaque PR et push sur `dev` / `main` ; construction Docker dès qu'un `Dockerfile` existe.
- Messages de commit : `type: description` en français (`feat`, `fix`, `docs`, `test`, `chore`, `refactor`).
- Règles détaillées : `CONTRIBUTING.md`.

## Options écartées
- **Branche `preprod` séparée** : à deux sur 15 jours, une branche de plus à synchroniser sans bénéfice ; `dev` en tient lieu.
- **Branches personnelles `Romuald` / `Olivier`** : elles divergent et se fusionnent mal ; l'auteur de chaque commit reste visible avec des branches de tâche.
- **Déploiement automatique sur un serveur** : pas de serveur ni de cloud ; le sujet ne l'exige pas. La machine de démo fait `docker compose pull && docker compose up -d`.

## Conséquences
- Relecture obligatoire par l'autre membre **dès qu'Olivier est ajouté comme collaborateur** (nom d'utilisateur GitHub à fournir) ; en attendant, la règle demande la PR et la CI, sans approbation.
- Les branches `Romuald` et `Olivier` seront supprimées une fois leur contenu fusionné (accord des deux).
