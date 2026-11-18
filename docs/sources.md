# Sources d'images — FlowView · Place Publique

*Tenu à jour à chaque source ajoutée. ✅ vérifié (avec la date) · 🔎 à vérifier. **Aucune image brute n'est versionnée** (`.gitignore` : `data/raw/`, `data/captures/`, `data/reference/images/`) ; seuls les manifestes (fichier, source, date, licence, empreinte) le sont.*

## 1. Caméras des Arcs (client de démonstration) : 6 webcams et 3 livecams

Page officielle : <https://www.lesarcs.com/fr/livecams-et-webcams>, avec une **vue carte**. Relevé du 18/11/2026 ✅ : **9 caméras, 6 webcams (images fixes) et 3 livecams (vidéo)**. Les positions viennent des marqueurs de la vue carte (`map_markers` de la page). Chaque marqueur a été rattaché à sa caméra par l'identifiant présent sur la page de la caméra.

### 1.1 Webcams (images fixes JPG, Trinum / webcam-hd)
| Caméra | Position (lat, lon) ✅ | Image en direct | Format (relevé le 17/11/2026) | Ce qu'elle montre | Archive |
|---|---|---|---|---|---|
| Arcabulle | 45.551178, 6.810725 | `trinum.com/ibox/ftpcam/les-arcs_arcabulle.jpg` | Panorama 2815 × 600, rafraîchi ~10 min ✅ | Panorama 360° : arrivée du télésiège, bâtiment et terrasse, zone où les skieurs débarquent ✅ (18/11) | **Quotidienne depuis le 01/10/2025** ✅ (lecteur `app.webcam-hd.com/lesarcs/arcabulle`) |
| Mont-Blanc (TSD) | 45.586964, 6.810735 | `trinum.com/ibox/FTPCam/les_arcs_tsd-mont-blanc.jpg` | 4063 × 600 ✅ | Panorama 360° : gare du télésiège (panneau « Mont-Blanc »), piste au centre, seconde gare à droite ✅ (18/11) | probablement la même 🔎 |
| Varet | 45.554963, 6.836849 | `trinum.com/ibox/FTPCam/les_arcs_catex.jpg` | 3561 × 600 ✅ | Gare d'arrivée et terrasse du Varet (2 600 m) ; objectif en partie givré le 18/11 ✅ | 🔎 |
| Arpette | 45.572518, 6.811082 | `trinum.com/ibox/ftpcam/les-arcs_arpette.jpg` | 2026 × 600 ✅ | **Objectif entièrement givré le 18/11** ✅ : cadrage inconnu, à revoir dans l'archive | 🔎 |
| Aiguille Rouge | 45.551646, 6.847782 | `trinum.com/ibox/ftpcam/les_arcs_aiguille.jpg` | 1915 × 600 ✅ | Sommet (3 226 m) ; **objectif givré le 18/11** ✅ ; peu de monde attendu | 🔎 |
| Grizzly (Peisey-Vallandry) | 45.548214, 6.792144 | `app.webcam-hd.com/tnm/ibox/FTPCam/peisey-vallandry_grizzly.jpg` | 3040 × 600 ✅ | Panorama : gare de télésiège au centre, pistes de part et d'autre, zone de départ devant la gare ✅ (18/11) | 🔎 |

### 1.2 Livecams (vidéo en direct, YouTube)
| Livecam | Position (lat, lon) ✅ | Page | Ce qu'elle montre | Usage possible |
|---|---|---|---|---|
| Vagère | 45.573521, 6.779448 | `lesarcs.com/fr/livecams/livecam-vagere` | Départ du télésiège de la Vagère (Arc 1800), 1280 × 720, horodaté ✅ (vu le 17/11) | **La meilleure vue de file** ; candidate n°1 pour le mode direct (fiche 0019) |
| Arc 2000 | 45.570226, 6.831508 | `lesarcs.com/fr/livecams/livecam-arc-2000` | Front de neige d'Arc 2000 au pied des résidences, panneaux de pistes, zone piétonne ✅ (18/11) | **Bonne pour compter des piétons** ; candidate pour le mode direct |
| Varet | 45.554962, 6.836826 | `lesarcs.com/fr/livecams/livecam-varet` | Même point que la webcam Varet (à 2 m près) ; dans le brouillard le 18/11 ✅ | À revoir par beau temps |

Les livecams sont diffusées sur YouTube. Lire un live YouTube avec un outil tiers est probablement contraire aux conditions de YouTube 🔎 : la question est à trancher avant le mode direct.

**Archive (relevé du 18/11/2026) ✅ :**
- Les 6 webcams ont une archive quotidienne dans le lecteur officiel webcam-hd, avec environ une image toutes les 30 à 35 minutes.
- Chaque image existe en trois tailles. **En `mega`, c'est le panorama 360° complet en 18 543 × 3 953 px**, environ 3 à 5 Mo.
- Les skieurs y sont nettement visibles, ce qui réduit fortement le risque des petites silhouettes.
- Collecte : fiche [0024](decisions/0024-collecte-scriptee-adresses-du-lecteur.md).

**Remarques techniques :**
- **En direct**, ce sont des panoramas de 600 px de haut. **Dans l'archive**, ils font 18 543 × 3 953 px. Le jeu de référence utilise l'archive. En production, il faudra soit la haute résolution, soit accepter des silhouettes minuscules : à mesurer (étape 1.5 et palier 2).
- Une image toutes les ~10 min suffit au socle périodique (fiche 0019).

**Droits :**
- Mentions légales de lesarcs.com (relues le 17/11/2026) ✅ : « Toute reproduction ou réutilisation est interdite sans accord préalable des titulaires des droits ».
- Le sujet prévoit ce cas : « À défaut d'accord des propriétaires des webcams publiques, l'exploitation des flux bruts peut être soumise à des restrictions légales : ne versionnez pas d'images brutes ».
- **Décision (fiche [0021](decisions/0021-webcams-usage-pedagogique-sans-autorisation.md)) :** pas de demande d'autorisation. Usage dans le seul cadre pédagogique, écrit comme une **limite réglementaire**, avec garde-fous : peu d'images, accès normaux seulement, rien dans Git, rien de publié sans flou, source citée, suppression en fin de projet.

## 2. Station déjà ouverte (deuxième temps, fiche 0016)
- **Val Thorens :** ouverture annoncée le 21/11/2026 🔎. Au moins une caméra Roundshot (Roc de 3 Marches), avec des archives de 14 et 180 jours selon bergfex 🔎. Conditions d'utilisation de Roundshot non trouvées 🔎.
- Détails dans [stations.md](stations.md).

## 3. Jeux de données publics (premier temps, fiche 0016)

| Jeu | Contenu (relevé le 17/11/2026) | Licence affichée | Pertinence |
|---|---|---|---|
| Roboflow · SkiTB « Skier detection » | 1 200 images, classes Ski / Skier ✅ | CC BY 4.0 (déclarée par l'auteur du dépôt) ✅ | Faible 🔎 : SkiTB est un jeu de suivi d'athlètes en course (plans télé serrés), pas des vues de webcam |
| Roboflow · « Skiers and Snowboarders » | 100 images, skier / snowboarder ✅ | CC BY 4.0 ✅ | À regarder ; très petit |
| Roboflow · « Ski detection » | 156 images, flag / skier ✅ | CC BY 4.0 ✅ | Probablement des portes de slalom, donc faible 🔎 |
| JHU-CROWD++ | 4 372 images de foule, dont pluie, neige, brouillard ; annotations par points ✅ | Non trouvée 🔎 (site crowd-counting.com) | Bonne pour la météo et la densité ; pas des stations |
| CrowdHuman | Foules denses, boîtes ✅ | Non commercial, recherche et enseignement, pas de redistribution ✅ | Files serrées ; usage scolaire seulement |
| COCO 2017 | 80 classes dont person, skis, snowboard | Annotations CC BY 4.0, images Flickr ✅ | Base du pré-entraînement : ne peut pas servir de jeu de référence (le modèle l'a déjà vu) |

**Attention :** une licence CC BY 4.0 affichée sur Roboflow est **déclarée par celui qui a déposé le jeu**. Si les images viennent de la télévision ou d'un autre site, il n'en détient peut-être pas les droits 🔎. On le note pour chaque jeu retenu.

## 3 bis. Vidéo (pour le suivi, après la baseline sur images)
Recherche du 18/11/2026 : **aucune archive vidéo publique de webcam de station trouvée.** Les « archives » des sites de webcams (skiresort.info, bergfex, snow-online) sont des **images** espacées, pas de la vidéo 🔎.

| Source | Ce que c'est | Licence | Usage prévu |
|---|---|---|---|
| **MOT17 / MOT20** (MOTChallenge) | Vidéos de piétons, scènes très chargées (gares, places), avec **pistes annotées** (identifiants d'une image à l'autre) ✅ | CC BY-NC-SA 3.0 selon un miroir 🔎 (à relire sur motchallenge.net) | Mesurer le suivi avec des métriques reconnues (HOTA, IDF1, MOTA) **sans annoter nous-mêmes** |
| **Vidéos Pexels « ski lift queue », « ski resort »** | Plusieurs milliers d'extraits, dont des vues hautes et fixes de domaines skiables ✅ (vu le 18/11) | Licence Pexels : usage gratuit, pas de vente en l'état 🔎 (à relire) | **Notre contexte en vidéo, légalement** : on compte à la main les passages sur quelques extraits de 1 à 2 min |
| SkiTB (Univ. Udine, WACV 2024) | 300 vidéos, un athlète suivi par vidéo ✅ | 🔎 | Peu utile : courses, pas des files |
| Livecams Vagère et Arc 2000 (YouTube) | Direct, 720p ✅ | Conditions YouTube 🔎 | Mode direct à partir du 12/12, si la lecture est permise |
| Station ouverte avec un flux vidéo hors YouTube | À chercher 🔎 | 🔎 | Mode direct avant le 12/12 |

## 4. Brouillon de demande d'autorisation (non envoyé, gardé pour un usage hors école)
À : service communication des Arcs (ADS / office de tourisme) et webcam-hd (Trinum)
Objet : Demande d'autorisation, usage pédagogique d'images de vos webcams

> Bonjour,
>
> Étudiant en Master Data et IA à La Plateforme_ (Marseille), je réalise avec un camarade un projet d'école (soutenance le 15 décembre 2026) : estimer automatiquement la fréquentation d'un domaine skiable à partir de webcams existantes, en ne gardant que des **comptages agrégés** (aucune identification de personne, aucune image publiée ni redistribuée).
>
> Nous aimerions utiliser, **pour ce seul projet pédagogique**, environ 150 images de vos webcams (dont l'archive de la saison 2025-2026), afin de constituer un jeu de test : compter les personnes à la main, puis mesurer l'erreur d'un modèle de détection. Les images resteraient sur notre poste, ne seraient jamais versionnées dans notre dépôt public et seraient supprimées à la fin du projet. Les personnes visibles seraient floutées dans toute illustration.
>
> Pourriez-vous nous indiquer si cet usage est possible, et à quelles conditions (mention de la source, nombre d'images, durée) ?
>
> Merci d'avance, et bonne ouverture de saison !
>
> [Prénom Nom], La Plateforme_, [adresse e-mail]

## 5. Ce qui reste à vérifier
- [ ] Ce que montre chaque caméra des Arcs en journée de février (y a-t-il des files, des terrasses chargées ?). À regarder dans le lecteur officiel, sans rien télécharger.
- [ ] Conditions d'utilisation de Roundshot (Val Thorens).
- [ ] Licence de JHU-CROWD++ ; contenu réel des jeux Roboflow (vues larges ou plans serrés ?).
- [ ] Faire valider par le formateur la source du jeu de référence.

## Sources consultées (17/11/2026)
- Les Arcs, webcams : <https://www.lesarcs.com/fr/livecams-et-webcams> ; mentions légales : <https://www.lesarcs.com/fr/mentions-legales>
- Lecteur webcam-hd (archive) : <https://app.webcam-hd.com/lesarcs/arcabulle>
- Roboflow Universe : <https://universe.roboflow.com/skitb/skier-detection>, <https://universe.roboflow.com/object-detection-rrer5/skiers-and-snowboarders>, <https://universe.roboflow.com/timondb01-gmail-com/ski-detection>
- JHU-CROWD++ : <https://arxiv.org/abs/2004.03597>
- Bergfex, archive Roundshot Val Thorens : <https://www.bergfex.com/snow-parks/snowpark-val-thorens/webcams/c8853/?archive=1>
