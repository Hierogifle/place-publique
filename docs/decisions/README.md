# Journal des décisions — FlowView · Place Publique

Chaque choix structurant du projet est consigné ici **au moment où il est pris** : ce qu'on a décidé, pourquoi, ce qu'on a écarté et à quel prix. Objectif : ne perdre aucune justification d'ici la soutenance du 15 décembre 2026, et pouvoir répondre à « pourquoi ça et pas autre chose ? » sur n'importe quel module.

## Règles
- **Une décision = un fichier** `NNNN-titre-court.md`, numéroté dans l'ordre, jamais renuméroté.
- **On ne réécrit pas l'histoire** : si une décision change, on crée une nouvelle fiche qui *remplace* l'ancienne, et on passe l'ancienne au statut `Remplacée par NNNN`.
- **On distingue** ce qui a été **vérifié** (✅, avec la source) de ce qui est **supposé** (🔎).
- Les points d'étape (ce qui a été fait, quand) vont dans [journal.md](../journal.md) ; les fiches ici ne gardent que les *choix*.

## Index

| N° | Date | Décision | Statut |
|---|---|---|---|
| [0001](0001-sujet-et-guide-formateur.md) | 2026-11-17 | Sujet rangé dans `sujet/`, guide formateur gardé hors du dépôt public | Acceptée |
| [0002](0002-branches-personnelles.md) | 2026-11-17 | Branches `Romuald` et `Olivier` créées | Remplacée par 0017 |
| [0003](0003-station-les-arcs.md) | 2026-11-17 | Client de démonstration : Les Arcs plutôt que Brides-les-Bains | Acceptée |
| [0004](0004-nom-de-marque-flowview.md) | 2026-11-17 | La marque est FlowView ; « Place Publique » = nom du projet | Acceptée |
| [0005](0005-imagerie-unsplash-pexels.md) | 2026-11-17 | Images : photo libre Unsplash/Pexels, pas de générateur IA | Acceptée |
| [0006](0006-panel-concurrentiel.md) | 2026-11-17 | Panel de concurrents retenu pour la DA | Acceptée |
| [0007](0007-outillage-direction-artistique.md) | 2026-11-17 | Outillage DA : skills designskills + design-taste | Acceptée |
| [0008](0008-emotion-serein-ennemi-ecran.md) | 2026-11-17 | Émotion n°1 « serein » ; ennemi principal : l'écran | Acceptée |
| [0009](0009-trois-serenites-de-la-journee.md) | 2026-11-17 | Trois sérénités selon le moment : refuge (matin), guide (journée), pilote (incident) | Acceptée |
| [0010](0010-empiler-les-trois-serenites.md) | 2026-11-17 | Les trois sérénités sont empilées : refuge = matière, guide = données, pilote = alerte | Acceptée |
| [0011](0011-trio-emotionnel.md) | 2026-11-17 | Trio d'émotions : serein, respecté dans son métier, en confiance | Acceptée |
| [0012](0012-muses-retenues.md) | 2026-11-17 | Muses retenues : bois vécu, tour, guetteur, crêtes, matin, mains, porter, lumière, berceuse | Acceptée |
| [0013](0013-socle-fixe-et-marge.md) | 2026-11-17 | Socle fixe (patine, silence, une alerte, chiffre honnête, voix du sage) et marge de liberté | Acceptée |
| [0014](0014-direction-artistique-piste-04.md) | 2026-11-17 | Direction artistique : piste 04 v2 « Les Crêtes, vues du refuge » | Acceptée (design.md validé) |
| [0015](0015-maquette-3d-et-ecran-crm.md) | 2026-11-17 | La station devient une maquette 3D ; écran sur le patron « CRM 3D » | Acceptée |
| [0016](0016-sources-de-donnees-en-trois-temps.md) | 2026-11-17 | Données en trois temps : jeux d'images, station déjà ouverte, puis Les Arcs | Acceptée (à faire valider) |
| [0017](0017-workflow-git-et-github.md) | 2026-11-17 | Workflow Git : main et dev protégées, branches de tâche, PR, CI et CD Docker | Acceptée |

## Modèle

```markdown
# NNNN — Titre

- **Date :** AAAA-MM-JJ
- **Statut :** Proposée | Acceptée | À revoir | Remplacée par NNNN
- **Décideurs :** Romuald, Olivier

## Contexte
Le problème, les contraintes, ce qu'on savait à ce moment-là.

## Décision
Ce qu'on fait, en une ou deux phrases.

## Options écartées
- Option B — pourquoi non.

## Conséquences
Ce que ça implique, ce que ça coûte, ce qu'il faudra surveiller.

## Sources
```
