# FlowView · Place Publique

**Un chiffre de fréquentation fiable, tiré des webcams déjà installées, pour décider quand ouvrir, renforcer ou fermer.**

[![CI](https://github.com/Hierogifle/place-publique/actions/workflows/ci.yml/badge.svg?branch=dev)](https://github.com/Hierogifle/place-publique/actions/workflows/ci.yml)

Projet de Master 2 Data / IA (La Plateforme_, 2026). FlowView compte les personnes visibles sur des webcams publiques à intervalle régulier, stocke les décomptes et les montre dans une application web avec la normale de l'heure, les alertes et une maquette 3D de la station. Client de démonstration : **le domaine skiable des Arcs** (Savoie).

> **Statut : lancement (J1).** La direction artistique, le plan et l'organisation du dépôt sont posés ; le code arrive avec le palier 1. Soutenance le 15 décembre 2026.

## Ce que FlowView promet (et ce qu'il ne promet pas)
- Une **occupation** à l'instant de la mesure, avec sa **fourchette** (« 55 ± 7 personnes »), comparée à **la normale de cette heure**.
- **« Pas de donnée »** quand une caméra ne répond pas, jamais un zéro trompeur.
- **Aucune image enregistrée** : seuls les décomptes sont stockés ; l'image affichée est floutée.
- Pas de « visiteurs de la journée » ni de flux d'entrées / sorties : une image toutes les 5 minutes ne le permet pas.

## Démarrer
*À venir avec le palier 2.* Objectif : depuis un clone vierge,

```bash
docker compose up
```

## Organisation du dépôt
```
.agents/          direction artistique (brand, stratégie, design.md validé, maquettes)
.github/          CI (tests, build Docker) et CD (image sur ghcr.io)
docs/             plan, décisions, journal, idées, fiche stations, récap du sujet
sujet/            énoncé et support du kick-off
veille.md         veille technique (8 questions)
CONTRIBUTING.md   comment on travaille à deux (branches, PR, commits, déploiement)
```
Prévu : `app/` (service d'inférence, planification, front Flask), `notebooks/`, `scripts/`, `tests/`, `conformite.md`, `architecture.md`.

## Documents clés
| Document | Pour quoi |
|---|---|
| [docs/sujet-recap.md](docs/sujet-recap.md) | Le sujet en une page : obligations, options, contradictions démêlées |
| [docs/plan.md](docs/plan.md) | Le plan d'attaque J1 → J15, la répartition, les risques |
| [docs/stations.md](docs/stations.md) | Tout savoir sur Les Arcs, Brides-les-Bains et la station de test |
| [docs/decisions/](docs/decisions/README.md) | Chaque choix et sa justification |
| [docs/journal.md](docs/journal.md) | Les points d'étape |
| [docs/idees.md](docs/idees.md) | Les idées produit, triées par faisabilité |
| [.agents/design.md](.agents/design.md) | Le système visuel validé (couleurs, polices, écran, états, vocabulaire) |
| [veille.md](veille.md) | La veille technique |

## Équipe
- **Romuald** : produit, front, planification, maquette 3D, Docker, CI.
- **Olivier** : données, jeu de référence, modèle, évaluation, inférence, tests.

## Données et crédits
- Remontées mécaniques et pistes : © contributeurs [OpenStreetMap](https://www.openstreetmap.org/copyright), licence ODbL.
- Relief : tuiles Terrarium (AWS Open Data).
- Photos d'illustration : Unsplash (auteurs crédités dans les maquettes).
- Aucune image brute de webcam n'est versionnée.

*Licence du code : à définir (voir `conformite.md` à venir, notamment la licence AGPL-3.0 d'Ultralytics YOLO).*
