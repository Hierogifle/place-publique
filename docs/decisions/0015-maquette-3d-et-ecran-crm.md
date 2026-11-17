# 0015 — La station devient une maquette 3D, l'écran suit le patron « CRM 3D »

- **Date :** 2026-11-17
- **Statut :** Acceptée (validée par Romuald le 2026-11-17 : « Oui, je valide »)
- **Décideurs :** Romuald
- **Précise :** [0014](0014-direction-artistique-piste-04.md)

## Contexte
Après la piste 04 v2, Romuald a partagé trois références d'interface : des « CRM 3D » réalisés pour un garage, une agence immobilière et une entreprise du bâtiment (maquette 3D douce, pastilles flottantes, chiffres clés, panneau de détail, frise du jour, colonnes de suivi). Il voulait depuis le début une station « comme une maquette 3D qu'on peut explorer, tourner, manipuler ».

## Décision
- La station est montrée comme une **maquette 3D stylisée** construite sur le **vrai relief des Arcs** (tuiles Terrarium) avec les **vraies remontées** (OpenStreetMap), sapins et chalets simplifiés, socle en bois.
- Chaque zone a une empreinte au sol, une **petite foule proportionnelle au comptage** et une pastille flottante.
- Écran : chiffres clés en haut, maquette au centre, **panneau de détail à droite avec l'image analysée floutée**, **frise du jour sur fond de crête**, colonnes de suivi par état en bas.
- On garde toute la DA de la fiche 0014 : palette papier / ardoise / balise, Inter + voix Alegreya, chiffre honnête, une seule couleur d'alerte.

## Options écartées
- **Relief cartographique (MapLibre, v2)** : exact mais froid, ressemble à une carte et non à la maquette voulue.
- **Maquette modélisée à la main** (chaque bâtiment) : hors de portée en 15 jours.
- **Reprendre le style visuel des références** (bleu vif, rendu d'un tiers) : on reprend le patron d'écran, pas l'identité de quelqu'un d'autre.
- **Glisser-déposer des zones entre colonnes** (comme dans les références) : ici l'état est calculé par le modèle, pas décidé par l'utilisateur.

## Conséquences
- Code 3D en three.js (MIT) : plus de travail qu'une carte MapLibre ; à faire au palier 2, **après** le service d'inférence et la base.
- Données à embarquer dans l'app : `data/arcs-dem.json` (≈ 110 Ko) et `data/arcs-osm-maquette.json` (≈ 150 Ko, attribution ODbL obligatoire).
- Performance à mesurer sur un PC modeste (sapins avec ombres).
- Maquette de référence : `.agents/stylescapes/maquette.html` (source : `data/maquette.template.html`).
