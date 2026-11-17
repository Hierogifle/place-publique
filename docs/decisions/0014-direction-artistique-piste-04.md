# 0014 — Direction artistique : piste 04 « Les Crêtes, vues du refuge »

- **Date :** 2026-11-17
- **Statut :** Acceptée ; `.agents/design.md` validé le 2026-11-17 avec l'écran principal en maquette 3D (fiche [0015](0015-maquette-3d-et-ecran-crm.md))
- **Décideurs :** Romuald

## Contexte
Trois pistes visuelles ont été présentées (La Vigie, Le Refuge, Les Crêtes). Romuald a préféré Les Crêtes tout en regrettant la chaleur du Refuge, puis a demandé une station en 3D explorable. Une piste 04 de synthèse a été construite, critiquée (« mal ordonnée », « l'image avec les rectangles doit passer devant »), puis refaite en v2.

## Décision
La direction artistique de FlowView est la **piste 04 v2** :
- **Dedans (le refuge)** : neutres papier chauds, encre brune, voix du gardien en Alegreya ; mode sombre = le refuge le soir.
- **Dehors (les crêtes)** : chiffres et courbes en ardoise ; la journée vue de côté (normale pâle, aujourd'hui net, brume = pas de donnée) ; relief 3D réel des Arcs (MapLibre + OpenStreetMap).
- **Le pilote** : une seule couleur d'alerte, la balise `#C8342A`.
- **Écran principal** : l'image analysée (cadres + personnes floutées) au premier plan ; la 3D sert à choisir une zone ; le carnet trié par urgence.
- Interface en Inter (neutre assumé), icônes Phosphor.

## Options écartées
- **01 La Vigie** : trop littérale (cadran), difficile en tableau de bord.
- **02 Le Refuge seul** : proche du cliché « serif + crème + accent chaud », fond sombre peu lisible au bureau.
- **03 Les Crêtes seules** : froide, trop proche d'un graphique classique.
- **04 v1** : mal ordonnée (3D au centre), mélange de polices, fond bois chargé.

## Conséquences
- Spécification complète, tokens, états et règles de vocabulaire : `.agents/design.md` ; résumé dans `.agents/brand.md`.
- La 3D et le flou côté serveur sont du palier 2, après le service d'inférence et la base.
- Restent à faire : `logo-design`, passe `art-direction` (photos des slides), références d'interfaces de Romuald.
- Maquette de référence : `.agents/stylescapes/piste-04.html` (source : `.agents/stylescapes/data/piste-04.template.html` + `data/arcs-osm.geojson`).
