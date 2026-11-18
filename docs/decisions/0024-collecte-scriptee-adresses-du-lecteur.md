# 0024 — Collecte scriptée, limitée aux images que le lecteur officiel charge lui-même

- **Date :** 2026-11-18
- **Statut :** Acceptée
- **Décideurs :** Romuald
- **Modifie :** [0021](0021-webcams-usage-pedagogique-sans-autorisation.md), garde-fou n° 2 (« uniquement les accès normaux »)

## Contexte
Le jeu de référence compte environ 300 créneaux (fiche [0025](0025-pre-annotation-et-taille-du-jeu.md)). Les collecter à la main dans le lecteur prendrait plusieurs heures. Une première tentative pour deviner les adresses techniques de l'archive a été **bloquée par le contrôle automatique** de l'agent : c'était de la recherche d'interface non documentée, et ce blocage était justifié.

## Décision
- Romuald ouvre **lui-même** une image d'archive dans le lecteur officiel.
- On lit dans le navigateur l'adresse de l'image que le lecteur vient de charger.
- Si c'est une adresse d'image simple et datée, un script télécharge **uniquement les créneaux du plan tiré au sort**, réserves comprises, et rien d'autre.
- **Rythme lent :** une image toutes les 5 secondes au moins, sans requêtes parallèles.
- Si une image n'existe pas, elle est notée absente : pas d'exploration autour.
- Interdits : deviner d'autres adresses, énumérer l'archive, ou contourner une limite.

Les autres garde-fous de la fiche 0021 restent : rien dans Git, rien de publié sans flou, source citée, suppression en fin de projet.

## Options écartées
- **Collecte entièrement à la main :** des heures de clics pour 300 images, avec un risque d'erreur de nommage.
- **Explorer l'interface technique du lecteur :** refusé, c'est un accès non documenté.

## Conséquences
- Le script vit dans le dépôt (`flowview/reference/collect.py`). Il est lisible, journalisé, et on peut le relancer.
- Si l'adresse de l'image n'est pas simple (jeton, signature, protection), on revient à la collecte manuelle.

## Vérification (18/11/2026)
- **Ce que charge le lecteur :** quand on choisit une date, il charge un index du jour, `app.webcam-hd.com/api/webcam/<caméra>/day/<date>`. Cet index liste les images de la journée avec des **adresses publiques simples**, sans jeton ni signature.
- **Rythme de l'archive :** environ une image toutes les 30 à 35 minutes ✅.
- **Trois tailles :** `small`, `1080` et `mega`. En `mega`, le panorama fait **18 543 × 3 953 px** ✅, au lieu des 600 px de hauteur de l'image en direct.
- **Identifiants des 6 caméras :** relevés en ouvrant leur page dans le lecteur (navigation normale). Ils sont notés dans `configs/reference_lesarcs.json`.
- **Script :** `flowview/reference/collect.py`. Il récupère un index par créneau, puis l'image la plus proche de l'heure cible, à ± 45 min au plus ; au-delà, le créneau est noté absent. Il attend 5 s entre deux requêtes. Chaque essai est noté dans `data/reference/collect_log.csv`.
