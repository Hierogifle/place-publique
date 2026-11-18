# 0027 — Huit classes comptées et un seuil par classe

- **Date :** 2026-11-18
- **Statut :** Acceptée (validée par Romuald le 2026-11-18, avant tout lancement de modèle)
- **Décideurs :** Romuald
- **Complète :** [0026](0026-seuil-d-acceptabilite.md) (seuils S1 à S5 sur le total des personnes, inchangés)

## Contexte
Les étiquettes CVAT ne prévoyaient qu'une classe, `person`. Or le sujet demande d'« identifier et compter automatiquement **2 à 10 classes** d'objets », avec un seuil d'acceptabilité **par classe**. Romuald note aussi que les images et les vidéos montrent des scènes variées : télésièges occupés, gares, terrasses, routes et villages, engins de damage, personnes avec ou sans combinaison selon le lieu.

## Décision
- **8 classes comptées :** `skieur`, `snowboardeur`, `pieton`, `voiture`, `camion`, `bus`, `engin_neige`, `animal`.
- **La classe dit l'activité, pas la tenue.** L'attribut `tenue` (ski / ville) sert à mesurer le biais de détection selon la tenue (veille Q8).
- **Attributs des personnes :** `sur_remontee` (couvre les télésièges occupés sans créer de classe) et `incertain`.
- **Attribut des engins :** `type` (dameuse, motoneige, quad, autre).
- **Étiquettes d'image :** `meteo`, `lieu` (piste, gare-remontee, front-de-neige-terrasse, route-village) et `inexploitable`.
- **Seuils par classe** ([evaluation.md](../evaluation.md) § 3 bis) :
  - **S6**, pour skieur, snowboardeur et piéton pris à part : erreur relative médiane ≤ 30 %, ou erreur moyenne ≤ 2 sous 5 objets ;
  - **S7**, pour véhicules, engins et animaux : erreur moyenne ≤ 1 par image, et présence détectée sur au moins 80 % des images où l'objet est présent ;
  - une classe présente sur moins de 10 images est déclarée « non mesurable ».
- **Avec le modèle de départ (COCO) :** une personne associée à des skis devient `skieur`, à un snowboard `snowboardeur`, sinon `pieton`. `car`, `truck`, `bus` et `dog` donnent leurs classes. `engin_neige` n'existe pas dans COCO : il faudra un fine-tuning, mesuré avant et après.

## Options écartées
- **`person` seule :** en dessous des 2 classes minimum du sujet, et sans distinction pistes / à pied, alors que les décisions diffèrent.
- **Classe `enfant` (ou toute classe d'âge ou de genre) :**
  - peu fiable sur un panorama, où la taille dépend surtout de la distance ;
  - c'est de la segmentation démographique, refusée dans la veille (Q8) ;
  - elle rapprocherait le système de la catégorisation biométrique de l'AI Act (l'âge y est cité en exemple) et fragiliserait la qualification « risque minimal » (veille Q7).
  - Si le besoin est de repérer les cours de ski, un attribut `en_groupe` reste possible.
- **Classe par tenue (combinaison / ville) :** la tenue ne décide de rien pour l'exploitant. Elle reste un attribut, pour l'analyse d'erreurs.

## Conséquences
- Environ 30 % de temps d'annotation en plus : une classe à choisir pour chaque cadre.
- Les mêmes 8 classes serviront au mode direct en vidéo (fiche 0019).
- Le projet CVAT doit utiliser le nouveau `configs/cvat_labels.json`. S'il a déjà été créé sans annotation, on remplace son contenu « Raw ».
