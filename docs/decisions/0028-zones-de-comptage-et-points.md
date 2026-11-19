# 0028 — On compte dans des zones dessinées par caméra ; la séance A se fait par points

- **Date :** 2026-11-19
- **Statut :** Acceptée (avant tout lancement de modèle)
- **Décideurs :** Romuald
- **Modifie :** [0026](0026-seuil-d-acceptabilite.md) et [0027](0027-huit-classes-et-seuils-par-classe.md) (ce qu'on compte), [0025](0025-pre-annotation-et-taille-du-jeu.md) (forme de la séance A)

## Contexte
La première image de la séance A (ARC-03) a demandé **69 cadres**. Au même rythme, les 24 images prendraient 8 à 12 heures, puis 270 de plus. Ce n'est pas tenable.

L'exploitant ne décide pas sur tout le panorama 360°. Il décide sur des lieux : une gare, une file, une terrasse, un départ. Ce sont aussi les pastilles de la maquette 3D.

## Décision
1. **Zones de comptage par caméra,** des polygones **dessinés par Romuald** dans CVAT le 19/11/2026. Ils sont dans `configs/zones_lesarcs.json`, en pixels du panorama d'archive. Noms choisis par l'agent, à la demande de Romuald :
   - **Arcabulle :** ARC-Z1 Plateau du sommet (gare et terrasse), ARC-Z2 Piste centrale et chalet, ARC-Z3 Télésiège Arcabulle et arrivée.
   - **Grizzly :** GRZ-Z1 Front de neige et espace luge, GRZ-Z2 Télésiège Grizzly et gare.
   - **Mont-Blanc :** MTB-Z1 Gare du TSD Mont-Blanc, télésiège et piste.
2. **Arrivée et télésiège sont regroupés** (choix de Romuald). Ce sont des photos : un instantané peut montrer des sièges vides alors que les suivants, hors champ, sont pleins. Séparer les deux donnerait une mesure instable.
3. **Les panoramas sont alignés d'un jour à l'autre :** mesuré sur Arcabulle (64 images, décalage nul), vérifié à l'œil sur 4 dates pour Mont-Blanc et Grizzly. Les zones fixes valent donc toute la saison.
4. **Ce qu'on compte** (règle technique proposée par l'agent, pas encore confirmée par Romuald) : les objets dont le **point au sol** (bas du cadre, ou le point lui-même) tombe dans une zone. Un objet dans deux zones appartient à la première listée (un recouvrement minime existe entre ARC-Z2 et ARC-Z3). Les seuils S1 à S7 s'appliquent au **total des zones d'une image**, et le détail par zone est publié.
5. **Séance A par points :** un clic par objet, sur des **découpes par zone** où l'extérieur de la zone est grisé. Les labels du projet CVAT acceptent maintenant les points et les cadres (`type: any`).
6. **La première image n'est pas perdue :** les 69 cadres d'ARC-03 donnent 58 objets dans ARC-Z1, 9 dans ARC-Z3 et 2 hors zone.

## Options écartées
- **Rectangles :** trop grossiers. Romuald a demandé des zones articulées qu'il puisse modifier lui-même.
- **Compter tout le panorama :** trop long, et les silhouettes lointaines ne servent à aucune décision.
- **Réduire la séance A à 12 images :** la mesure du biais d'ancrage deviendrait fragile.

## Conséquences
- Moins de surface à parcourir (de 39 à 58 % de l'image selon la caméra), et un clic au lieu d'un cadre par objet.
- **On ne mesure plus le panorama entier.** Ce qui est hors zone n'est pas compté, et l'écran FlowView le dira (« dans les zones suivies »).
- Pour une nouvelle caméra, il faudra dessiner ses zones. C'est une étape de mise en service, générique, qui ne dépend pas du client.
- **Pré-enregistrement préservé :** ce changement intervient **avant** tout lancement de modèle.
