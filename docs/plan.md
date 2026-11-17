# Plan d'attaque — FlowView · Place Publique

*Version 1 · 2026-11-17 · à mettre à jour à chaque fin de palier (et noter les écarts dans [journal.md](journal.md)).*
*Légende : ✅ vérifié · 🔎 supposé / à vérifier · **R** = Romuald · **O** = Olivier · **R+O** = ensemble.*

## 1. Le cadre

| Repère | Date |
|---|---|
| Lancement | mardi 17 novembre 2026 |
| Ouverture du domaine des Arcs | samedi 12 décembre 2026 ✅ (lesarcs.com) |
| Soutenance | mardi 15 décembre 2026 |
| Temps de projet | **15 jours** répartis sur 4 semaines, avec une période en entreprise au milieu (dates exactes à compléter, §6) |

**Règles du sujet qui pilotent tout :**
- Trois paliers, chacun avec un critère de validation ; **on n'attaque pas le suivant avant d'avoir validé le précédent**.
- Le formateur regarde le tableau d'erreurs avant le code, fait ajouter une webcam en direct, fait cloner le dépôt par une autre équipe.
- Note collective **ajustée par l'historique Git et les réponses individuelles** : chacun commite son travail et peut expliquer le module de l'autre.
- Veille : chacun **rédige et défend au moins 2 questions**.

## 2. Le risque n°1 : les données, avant l'ouverture des pistes

Le domaine est fermé jusqu'au 12 décembre : en novembre, les places et les départs de remontées des Arcs sont presque vides. Un jeu de référence de 100 images rempli de zéros ne permet de mesurer aucune erreur de comptage.

| Option | Principe | Pour | Contre |
|---|---|---|---|
| **A. Une webcam « relais » dès aujourd'hui** | Une place publique animée (ville ou station déjà ouverte) avec les mêmes classes (personnes) sert au palier 1 et au rejeu ; Les Arcs entrent en jeu le 12/12 | Données réelles tout de suite ; **prouve la généricité exigée par le sujet** (« sans enfermer le code dans ce seul client ») | Le client de démo change de caméra en cours de route : à expliquer |
| **B. Une station déjà ouverte** | Station d'altitude ou de glacier ouverte fin novembre 🔎 (à vérifier : Val Thorens, Tignes…) | Même type d'images que Les Arcs | Ouverture et webcams exploitables à vérifier ; peu de monde en semaine de novembre |
| **C. Un jeu de données public en complément** | Images annotées de stations / foules (Roboflow Universe, COCO) 🔎 licences à vérifier | Variété (nuit, neige, foule) | Pas « nos » caméras ; le sujet veut un jeu de référence de **notre** contexte |

**Décision de Romuald (2026-11-17, fiche [0016](decisions/0016-sources-de-donnees-en-trois-temps.md)) : trois temps.**
1. **Jeux de données d'images** (option C) pour construire et **figer le jeu de référence** et mesurer la baseline. Images choisies pour ressembler à une vue de webcam de station (personnes sur la neige, files, places), licences vérifiées une par une.
2. **« Production » dans une station déjà ouverte** (option B) : Val Thorens et Tignes annoncent une ouverture le 21 novembre 2026, Val d'Isère et Les 2 Alpes le 28 🔎 (dates prévisionnelles, selon l'enneigement). On branche le service sur 2 ou 3 de leurs webcams pour vérifier que ça marche en conditions réelles. Les images capturées forment un **jeu de validation terrain séparé** : le jeu de référence, lui, ne bouge plus.
3. **Les Arcs à la fin**, à l'ouverture du 12 décembre, pour la démo de soutenance (même code, nouvelles caméras ajoutées depuis l'interface : c'est la preuve de généricité).

À faire valider par le formateur : un jeu de référence issu de jeux de données publics, alors que le sujet parle d'images « de votre contexte ».

**Dans tous les cas, dès le J1 :** un script de capture tourne en continu (une image toutes les 5 min, stockée **hors du dépôt**, `.gitignore`), y compris pendant la période en entreprise. Il accumule jour, nuit, météo et affluence pour le rejeu du palier 2.

## 3. Le déroulé, jour par jour

### Palier 1 · Un comptage mesuré (J1 → J5)
| Jour | Quoi | Qui | Livrable |
|---|---|---|---|
| J1 | Choisir les jeux de données (licences), repérer 2 à 3 webcams d'une station ouverte et 2 à 3 des Arcs ; lire leurs conditions d'utilisation ; écrire le script de capture | R+O | `scripts/capture.py`, liste des sources dans `docs/sources.md` |
| J1 | Structure du dépôt, configuration GitHub (branches, protection, PR), `.gitignore` des images | R | dépôt prêt, `README.md` v0 |
| J2 | **Figer le jeu de référence** à partir des jeux de données : ≥ 100 images variées (jour, nuit, météo, affluence), pas de doublons quasi identiques | O | `data/reference/manifest.csv` (images hors Git, liste, source, licence et empreinte versionnées) |
| J3 | Vérité terrain : compter à la main ≥ 50 images, par classe | R+O (25 chacun) | `data/reference/ground_truth.csv` |
| J3 | Baseline : YOLO pré-entraîné COCO, sans fine-tuning, comptage par classe (`person`, et tester `skis` / `snowboard`) | O | `notebooks/01_baseline.ipynb` |
| J4 | Mesure : MAE et biais par classe, 10 pires images analysées, seuil de confiance réglé **sur le jeu de référence** | O | tableau d'erreurs par classe |
| J4 | Seuil d'acceptabilité **écrit et justifié par l'usage** (ex. erreur relative médiane ≤ 20 % sur `person`) | R+O | `docs/evaluation.md` |
| J5 | Veille v1 (Q1 à Q3) ; point de validation du palier 1 avec le formateur | O (Q1, Q2, Q3) | `veille.md` v1 |

**Critère de validation :** un notebook reproductible produit le tableau d'erreurs par classe, et le seuil d'acceptabilité est écrit avant d'avoir vu les résultats.

### Palier 2 · Un service de bout en bout (J6 → J10)
| Jour | Quoi | Qui | Livrable |
|---|---|---|---|
| J6 | Service d'inférence : lit l'image, applique le modèle, renvoie décompte + image annotée **floutée** ; base SQLite (mesures, caméras, « pas de donnée ») | O | `app/inference/`, `app/db/` |
| J6 | Planification (APScheduler), intervalle configurable, réessai, horodatage UTC ; **une caméra muette = « pas de donnée », jamais zéro** | R | `app/scheduler.py` |
| J7 | Front Flask v1 sur les tokens de `design.md` : ajouter une caméra (URL, nom, emplacement, classes), dernière image annotée, chiffre ± et normale | R | `app/templates/`, `app/static/css/tokens.css` |
| J8 | Graphiques Chart.js (journée vue de côté, normale de l'heure) + règle d'alerte (au-dessus de la normale pour cette heure) | R | tableau de bord |
| J8 | Script de rejeu du jeu de référence comme un flux (horodatages cohérents) | O | `scripts/replay.py` |
| J8 | Branchement sur 2 à 3 webcams de la station ouverte (test en conditions réelles) ; captures = jeu de validation terrain séparé | R+O | `data/terrain/manifest.csv`, mesure d'erreur terrain |
| J9 | Fine-tuning **seulement si une classe manque** (sinon on l'écrit et on passe) ; comparaison avant / après dans MLflow | O | runs MLflow |
| J9 | Maquette 3D (three.js) si tout le reste du palier tourne ; sinon après la soutenance | R | `app/static/js/maquette/` |
| J10 | Veille v2 (Q4) ; répétition de la démo : ajout d'une webcam depuis l'interface, série ≥ 48 points en rejeu, coupure de source visible | R (Q4) | démo palier 2 |

**Critère de validation :** ajout d'une webcam depuis l'interface, puis une série temporelle d'au moins 48 points ; on coupe la source, le système continue et le trou est visible.

### Palier 3 · Fiabiliser et cadrer (J11 → J13)
| Jour | Quoi | Qui | Livrable |
|---|---|---|---|
| J11 | Tests unitaires : comptage sur une image de test, gestion des erreurs, routes de l'API | O | `tests/` |
| J11 | Dockerfile + docker compose (**torch CPU**, petit modèle) ; démarrage depuis un clone vierge | R | `Dockerfile`, `docker-compose.yml` |
| J12 | GitHub Actions : tests + construction de l'image ; CI verte | R | `.github/workflows/ci.yml` |
| J12 | `conformite.md` : RGPD (base légale, minimisation, AIPD), AI Act, privacy by design (agrégats, aucune image stockée, flou), **licence du modèle (Ultralytics = AGPL-3.0) et alternative permissive** | R+O | `conformite.md` |
| J13 | `architecture.md` : architecture de production (cloud ou edge), signaux de dérive, déclencheurs de ré-entraînement | O | `architecture.md` |
| J13 | Veille v3 (Q5 à Q8) | R (Q7, Q8) · O (Q5, Q6) | `veille.md` complet |

**Critère de validation :** CI verte et `docker compose up` démarre l'application depuis un clone vierge.

### J14 → J15 · Finalisation et soutenance
- README final (lancer le projet depuis un clone vierge), documentation, captures.
- Slides dans la DA (20 min) + démo répétée (10 min) **sur le rejeu, pas sur la webcam en direct** (consigne du guide formateur).
- Chacun répète une question sur un module qu'il n'a pas écrit.
- **Pas de nouvelle fonctionnalité.**

## 4. Répartition proposée (à discuter)
| | Romuald | Olivier |
|---|---|---|
| Fil rouge | Produit : front Flask, planification, maquette 3D, Docker, CI | Données et modèle : jeu de référence, baseline, évaluation, inférence, fine-tuning, tests |
| Veille | Q4 architecture, Q7 RGPD / AI Act, Q8 éthique | Q1 modèles, Q2 évaluation, Q3 datasets, Q5 MLOps, Q6 dérive |
| Commun | Vérité terrain (25 images chacun), conformite.md, soutenance | idem |

Le sujet demande au moins 2 questions chacun : 3 et 5 respecte la règle ; on peut rééquilibrer (par exemple Q5 à Romuald).

## 5. Risques et parades
| Risque | Parade |
|---|---|
| Pas de foule aux Arcs avant le 12/12 | Jeux de données puis station ouverte (§2) ; Les Arcs à la fin |
| Station ouverte : peu de monde en semaine de novembre | Capturer aussi les week-ends ; plusieurs webcams (départs de remontées, front de neige) |
| Jeux de données trop « gros plan » (skieurs filmés de près, pas des vues de webcam) | Les trier à la main ; ne garder que des vues larges ; compléter par la station ouverte dans le jeu terrain |
| Webcam qui change d'URL ou disparaît | Jeu de référence figé + images archivées hors Git ; au moins 2 sources |
| Conditions d'utilisation des webcams | Les lire au J1 ; ne versionner aucune image brute |
| Image Docker énorme (CUDA) | torch CPU dans Docker ; le GPU de Romuald sert seulement à l'entraînement |
| Licence AGPL d'Ultralytics | La signaler dans conformite.md, proposer une alternative permissive (à vérifier) |
| Le front et la 3D mangent le temps | Règle des paliers ; la maquette 3D vient en dernier au palier 2 |
| Soutenance qui dépend du direct | Démo sur le rejeu, vidéo de secours |

## 6. Calendrier
Pas de dates fixées pour J2 à J15 (choix de Romuald, 2026-11-17) : on avance au rythme des jours de projet. Deux dates comptent : **l'ouverture des Arcs le 12/12** (branchement final) et **la soutenance le 15/12**. Les webcams de la station ouverte doivent être branchées avant, pour avoir des journées réelles à montrer.

Pendant la période en entreprise : la capture tourne seule ; lecture pour la veille ; pas de développement prévu sauf accord entre nous deux.
