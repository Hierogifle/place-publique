# 0001 — Sujet rangé dans `sujet/`, guide formateur hors du dépôt public

- **Date :** 2026-11-17
- **Statut :** Acceptée
- **Décideurs :** Romuald

## Contexte
Les fichiers du sujet étaient en vrac à la racine : énoncé PDF + DOCX, un doublon `Place_Publique_V2(1).docx` (même texte, autre export), le PowerPoint du kick-off, et deux exemplaires du *Guide formateur* (même texte). Le dépôt GitHub `Hierogifle/place-publique` est **public** ✅. Le guide formateur contient les questions de soutenance, les réponses attendues à la veille et les signaux d'alerte de l'évaluateur.

## Décision
- Énoncé (PDF, DOCX) et PowerPoint du kick-off versionnés dans `sujet/`.
- Guide formateur (2 exemplaires) et doublon de l'énoncé déplacés dans `sujet/non_versionne/`, **ignoré par Git** : ils restent sur le poste de Romuald.

## Options écartées
- **Tout pousser** : publierait un document destiné au formateur sur un dépôt public.
- **Passer le dépôt en privé** : possible, mais le rendu se fait sur un dépôt GitHub d'équipe et la visibilité n'a pas été décidée.
- **Supprimer les doublons** : rien ne garantissait lequel était le plus récent ; on garde tout, localement.

## Conséquences
- Olivier n'a pas le guide formateur via Git : à lui transmettre autrement.
- Le guide reste une source de travail précieuse (attentes par palier) : on s'en sert, on ne le publie pas.
