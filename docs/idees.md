# Idées produit — à trier

Les idées qui ne sont pas encore des décisions. On ne les perd pas, on ne les code pas tant que les trois paliers ne sont pas validés. Quand une idée est retenue ou rejetée, on crée une fiche dans [decisions/](decisions/README.md) et on met à jour son statut ici.

*Légende : ✅ vérifié · 🔎 supposé / à vérifier.*

| # | Date | Idée (Romuald) | Faisabilité | Statut |
|---|---|---|---|---|
| I-01 | 2026-11-17 | **Point du matin** : une estimation de la fréquentation de la journée au démarrage, à partir de données externes. | Réaliste sous la forme « normale de l'heure » (historique propre) enrichie de facteurs connus à l'avance : vacances scolaires par zone ✅ (open data, data.gouv.fr), météo 🔎, jour de la semaine. Pas de chiffre public par station : les journées-skieurs ne sont publiées qu'au niveau national (DSF) ✅. | À discuter, palier 2 ou « pour aller plus loin » |
| I-02 | 2026-11-17 | **Détecter les problèmes de fluidité** sur la journée. | C'est déjà l'alerte du sujet (« affluence supérieure à la normale pour cette heure »). Faisable au palier 2. | Dans le périmètre |
| I-03 | 2026-11-17 | **Panne de remontée** : la file grossit parce que la remontée est arrêtée ; afficher le nombre de personnes bloquées. | Le nombre de personnes dans la zone de file : faisable (comptage dans une zone de l'image). La *cause* (panne) n'est pas visible sur une image toutes les 5 min ; on peut seulement signaler « file anormale qui ne se résorbe pas ». Détecter des sièges immobiles demanderait deux images rapprochées 🔎. | Extension, après les paliers |
| I-04 | 2026-11-17 | **Report de la foule sur les pistes** quand une remontée bloque. | Pas mesurable sans caméra sur les pistes ni suivi des personnes (occupation ≠ flux). | À écarter ou à reformuler |
| I-05 | 2026-11-17 | **Plus de monde d'un coup = plus de risque d'accidents.** | Aucune donnée d'accidents pour le prouver ; afficher un risque de blessure serait une promesse qu'on ne peut pas tenir (contraire au « chiffre honnête ») et un sujet sensible (responsabilité). Reformulation possible : « forte affluence sur ce secteur, à signaler aux pisteurs », sans parler de blessés. | Freins acceptés par Romuald (2026-11-17) : I-04 écartée, I-05 reformulée |
| I-06 | 2026-11-17 | **La station en 3D** comme écran principal, qu'on tourne et qu'on explore : alertes, zones plus ou moins chargées, caméras cliquables ; puis une vue de côté pour la journée ou une zone. | Faisable sans modélisation à la main : MapLibre GL JS (open source) avec relief 3D ✅ ; relief gratuit sans clé (tuiles AWS Terrarium) ✅ ou IGN RGE ALTI (Licence Ouverte ✅, clé d'accès à vérifier 🔎) ; remontées et pistes depuis OpenStreetMap (`aerialway=*`, `piste:type=downhill`) ✅, attribution ODbL obligatoire. « Trait pour trait » (bâtiments modélisés) : hors de portée en 15 jours. La « vue de côté » = le relief des Crêtes. | Proposée pour le palier 2, après le service et la base |
| I-07 | 2026-11-17 | **Flux en direct avec les détections du modèle**, pour la transparence. | Le sujet demande déjà « la dernière image annotée » (une image toutes les X minutes), pas une vidéo : la plupart des webcams des Arcs sont des JPG rafraîchis ✅. Vidéo + inférence continue = coût CPU élevé dans Docker. Montrer des personnes identifiables en direct = logique de vidéosurveillance (RGPD, CNIL, couloir de Wintics). Alternative proposée : dernière image annotée, **personnes floutées sous leurs cadres**, gardée en mémoire et non stockée. | Accepté sur le principe (2026-11-17) : Romuald gère la qualité vidéo et l'anonymisation (flou après détection) plus tard |
| I-08 | 2026-11-17 | **Utiliser le GPU du PC de Romuald.** | Utile pour le fine-tuning et pour tester l'inférence sur vidéo en local. Mais l'image Docker et la CI doivent rester en **CPU** (le jury clone le dépôt sur une machine quelconque ; le guide formateur insiste sur torch CPU pour éviter une image de plusieurs Go). | À cadrer : GPU pour l'entraînement, CPU pour la livraison |

## Sources
- Journées-skieurs nationales (DSF), saison 2024-2025 : https://www.lechotouristique.com/article/hiver-2024-2025-la-france-tutoie-les-55-millions-de-journees-skieurs
- Saison 2025-2026 : https://www.tourmag.com/Stations-de-ski-la-France-retrouve-la-premiere-place-mondiale_a133360.html
- Données par station fournies sur demande par DSF (étude 2013) : https://balise.documentation.developpement-durable.gouv.fr/docs/Balise/0066/Balise-0066061/CT69_DMOB_2013_rapport_trafic_rm_STRMTG_V3_cle74ed3b.pdf
- Calendrier scolaire (open data) : https://data.gouv.fr/en/datasets/le-calendrier-scolaire
- Vacances scolaires par zones : https://www.data.gouv.fr/datasets/vacances-scolaires-par-zones
- Les Arcs dans le groupe Compagnie des Alpes : https://www.lesarcs-peiseyvallandry.com/en/le-domaine-de-montagne
- MapLibre, relief 3D : https://maplibre.org/maplibre-gl-js/docs/examples/3d-terrain/
- Tuiles de relief AWS Terrarium : https://geodataviewer.pages.dev/datasets/dem/aws-elevation-tiles
- IGN RGE (Licence Ouverte, services WMS/WMTS) : https://www.data.gouv.fr/datasets/referentiel-a-grande-echelle-rge/
- OSM, remontées : https://wiki.openstreetmap.org/wiki/Tag:aerialway%3Dchair_lift · pistes : https://wiki.openstreetmap.org/wiki/Zh-hans:Key:piste:type
- Requête Overpass pour une carte de ski : https://docs.mapbox.com/help/tutorials/overpass-turbo
