# 0026 — Seuil d'acceptabilité du comptage, fixé avant toute mesure

- **Date :** 2026-11-18
- **Statut :** Proposée (à valider par Romuald, puis commitée **avant** le premier lancement d'un modèle)
- **Décideurs :** Romuald

## Contexte
Le sujet exige un seuil d'acceptabilité par classe, écrit et justifié par l'usage du client, avec une valeur indicative : erreur relative médiane ≤ 20 % sur les classes principales. Le protocole du [palier 1](../palier-1.md) impose de l'écrire **avant** de voir les résultats.

## Décision (proposée)
Détail et justification dans [evaluation.md](../evaluation.md). Une seule classe principale, `person` ; `skis` et `snowboard` sont mesurés pour information, hors seuil.

| # | Mesure | Seuil |
|---|---|---|
| S1 | Erreur relative médiane, images à 5 personnes ou plus | ≤ 20 % |
| S2 | MAE, images à moins de 5 personnes | ≤ 1,5 personne |
| S3 | Biais relatif moyen, images à 5 personnes ou plus | entre −10 % et +10 % |
| S4 | Erreur relative médiane, strate « affluence haute » | ≤ 25 % ; bloquant pour l'alerte seulement |
| S5 | Fausses détections hors exploitation | ≤ 0,5 par image |

Chaque mesure est publiée avec son intervalle de confiance à 95 % (bootstrap). Les images inexploitables sont exclues et comptées comme « pas de donnée ». Le jeu de contrôle est mesuré mais ne compte pas dans la décision.

## Options écartées
- **Une seule erreur relative sur toutes les images :** elle n'a pas de sens pour 0 à 4 personnes.
- **Le mAP comme critère :** il ne dit pas si le comptage est juste (veille Q2).
- **Un seuil unique sans le biais :** il cacherait un sous-comptage systématique dans les foules.

## Conséquences
- La vérité terrain doit être plus précise que le seuil : biais d'ancrage ≤ 1 personne en moyenne (fiche 0025).
- Les niveaux d'affluence de l'écran devront être espacés d'environ ×1,5 pour qu'une erreur de 20 % ne fasse pas sauter un niveau. C'est à vérifier sur les comptages réels.
