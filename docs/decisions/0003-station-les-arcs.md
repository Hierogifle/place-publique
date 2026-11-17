# 0003 — Client de démonstration : Les Arcs plutôt que Brides-les-Bains

- **Date :** 2026-11-17
- **Statut :** Acceptée
- **Décideurs :** Romuald (proposition de l'agent)

## Contexte
Le sujet propose « la station des Arcs (et Brides-les-Bains) : compter les piétons sur la place et les skieurs dans les files des remontées pour optimiser l'ouverture des télésièges ». Il impose 2 à 3 webcams **du même type** et met en garde contre l'association de webcams trop différentes.

Les deux lieux sont très différents : Les Arcs est un domaine skiable d'altitude (Paradiski) ; Brides-les-Bains est une station thermale à 600 m, reliée au domaine des 3 Vallées par la télécabine de l'Olympe.

## Ce qu'on a vérifié (2026-11-17)
| | Les Arcs | Brides-les-Bains |
|---|---|---|
| Caméras | ✅ 9 sur lesarcs.com : JPG rafraîchis (trinum / webcam-hd) + 3 lives YouTube | ✅ 7 sur les3vallees.com, dont 1 seule au village |
| Départ de remontée | ✅ Live « Vagère » (Arc 1800, 1280×720) : départ de télésiège à distance moyenne | Aucune caméra trouvée sur la file de l'Olympe |
| Place piétonne | 🔎 Place Manoir et Horloge (Arc 1950), pas encore vues | ✅ Vue plongeante et lointaine sur des rues |
| Format exploitable | ✅ URL JPG directes, ex. `trinum.com/ibox/ftpcam/les-arcs_arcabulle.jpg` (2815×600, panoramique) | Widget JS, URL d'image `app.webcam-hd.com/brides-les-bains/centre-village` |

## Décision
Les Arcs est le client de démonstration. Brides-les-Bains reste un **plan B**.

## Options écartées
- **Brides-les-Bains seul** : une seule caméra au village, aucune sur une file de remontée.
- **Les deux ensemble** : contexte et classes trop différents, contraire à la consigne du sujet.

## Conséquences et risques
- ⚠️ **Saison** : ouverture du domaine le **12 décembre 2026** ✅ (bannière lesarcs.com), soutenance le **15 décembre**. Pas de file de skieurs pendant le palier 1 : il faut un plan B pour le jeu de référence (archives, dataset public, ou place de village d'abord). En contrepartie, la démo peut montrer 3 jours de vraie saison.
- Les panoramiques trinum (2815×600, 3561×600) rendent les personnes très petites : à tester avant de s'engager.
- Conditions d'utilisation des webcams (lesarcs.com, trinum, webcam-hd) **non lues** : à faire avant d'archiver une image toutes les 5 minutes. Récupérer un live YouTube par un outil tiers est probablement contraire aux conditions de YouTube 🔎.
- COCO connaît `person`, `skis` et `snowboard` : la détection d'un skieur sans fine-tuning est peut-être possible 🔎 (à tester).

## Sources
- https://www.lesarcs.com/fr/livecams-et-webcams
- https://arc1950.com/en/les-webcams-arc-1950-1445
- https://www.les3vallees.com/en/live/webcams-brides-les-bains
- https://www.lesarcs.com/fr (bannière d'ouverture)
