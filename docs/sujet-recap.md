# Le sujet en une page — Place Publique

*Source : `sujet/Place_Publique_V2.pdf` (énoncé officiel) et le support du kick-off. Version 1 · 2026-11-17.*

## Le besoin, en une phrase
Compter automatiquement, à intervalle régulier, les personnes (ou véhicules, bateaux) visibles sur 2 à 3 webcams publiques d'un même type, stocker ces décomptes, et les montrer dans une application web avec graphiques et alertes, **de façon générique** (pas enfermée dans un seul client).

## Les obligations (ce qui est noté)
| Domaine | Ce qui est exigé |
|---|---|
| **Palier 1 · comptage mesuré** | Jeu de référence figé (≥ 100 images variées, jamais modifié) ; vérité terrain à la main (≥ 50 images, par classe) ; baseline avec un modèle pré-entraîné (ex. YOLO COCO) **sans entraîner de zéro** ; erreur absolue moyenne et biais par classe ; analyse des 10 pires images ; **seuil d'acceptabilité écrit et justifié par l'usage** ; notebook reproductible ; veille Q1 à Q3 |
| **Palier 2 · service de bout en bout** | Service d'inférence via une API (image → décompte par classe + image annotée), stockage **SQLite** ; planification à intervalle configurable (cron, APScheduler…) ; caméra indisponible = réessai et **« pas de donnée »** (un zéro trompeur est une erreur) ; **front Flask** (Jinja + Chart.js) : ajouter une webcam (URL, nom, localisation), choisir les classes, graphiques temporels, dernière image annotée ; une règle d'**alerte** visible ; fine-tuning **seulement si une classe manque**, comparé dans MLflow ; script de **rejeu** ; veille Q4 |
| **Palier 3 · fiabiliser et cadrer** | Tests unitaires (comptage, erreurs, routes) ; **Dockerfile / docker compose** ; **GitHub Actions** (tests + build de l'image) ; `conformite.md` (RGPD, AI Act, privacy by design, licence du modèle) ; `architecture.md` (production, dérive, ré-entraînement, sur le papier) ; veille Q5 à Q8 |
| **Rendu** | Dépôt GitHub avec code, notebooks, `README.md` (lancer depuis un clone vierge), `veille.md`, `conformite.md`, `architecture.md`, tableau d'erreurs et seuils, tests, CI |
| **Soutenance** | 20 min de présentation (panel « clients et investisseurs ») + 10 min de démo + questions ; **chacun doit pouvoir expliquer n'importe quelle partie** |
| **Veille** | 8 questions, sources fiables ; **chacun rédige et défend au moins 2 questions** ; tableaux comparatifs plutôt que longs paragraphes |
| **Contraintes** | Python ; Git avec structure standard dès le début ; entraînement possible sur laptop ou Colab ; MLflow dès qu'on compare des modèles ; datasets libres de droits ; **aucune image brute de webcam dans le dépôt** |

**Grille (sur 20) :** comptage et évaluation /5 · application /5 · ingénierie /3 · veille, conformité, architecture /4 · soutenance /3. Note collective **ajustée individuellement** (historique Git + réponses). Les extensions ne comptent que si les trois paliers sont validés.

## Les options (« pour aller plus loin », seulement après les trois paliers)
1. Détection à classes ouvertes : signaler un objet inconnu, boucle de ré-annotation.
2. Passer de Flask seul à **gunicorn** (avec éventuellement Nginx) + test de charge.
3. Calcul réel des indicateurs de dérive et suivi dans MLflow, avec alerte.

Nos propres extensions (voir `docs/idees.md`) : maquette 3D de la station, point du matin, files anormales.

## Les « contradictions » apparentes, démêlées
| On lit | Et ailleurs | En réalité |
|---|---|---|
| « Frontend en **Flask** » | « Passage de Flask à **gUnicorn** » | **Pas de contradiction.** Flask est le *framework* (le code de l'application). Son serveur intégré (`flask run`) est fait pour développer, pas pour la production. **gunicorn** est un *serveur* qui fait tourner cette même application Flask avec plusieurs processus ; Nginx se place devant. L'application reste en Flask. ⚠️ gunicorn ne tourne pas sous Windows : en développement on garde `flask run` (ou waitress), et gunicorn tourne dans le conteneur Docker (Linux). |
| « Compter » les objets | Clients qui veulent des « entrants et sortants » (marina) | Une image toutes les 5 min = une **occupation** à un instant, jamais un flux. Un flux demande du suivi d'objets (tracking). On écrit ce que notre chiffre dit et ne dit pas. |
| Fine-tuning « c'est votre palier 2 » (kick-off) | Fine-tuning « seulement si une classe manque » (énoncé) | **L'énoncé fait foi** : on fine-tune uniquement pour une classe absente de COCO, et on le justifie. |
| Annoter « 50-100 images » (kick-off) | ≥ 100 images, ≥ 50 annotées (énoncé) | **L'énoncé fait foi** : 100 images dans le jeu, au moins 50 comptées à la main. |
| « Aucune image stockée » (privacy by design) | « La dernière image annotée » dans le front | On montre la dernière image **floutée**, gardée en mémoire le temps de l'affichage, jamais archivée ; on ne stocke que les décomptes. |
| Ultralytics YOLO recommandé | FlowView veut un **produit** commercial | YOLO d'Ultralytics est sous **AGPL-3.0** (licence commerciale payante sinon) : on peut l'utiliser pour le projet, mais on le signale dans `conformite.md` et on propose une alternative sous licence permissive. |
| « Déploiement automatisé non exigé » | Notre CD publie une image à chaque push sur `main` | Compatible : la CD prépare l'image, le « déploiement » reste un `docker compose pull && up -d` en local. |
| « SQLite » | Séries temporelles à analyser | SQLite suffit (une table de mesures horodatées en UTC) ; une base temporelle se discute dans `architecture.md`. |
| Chart.js « par exemple » | Notre maquette 3D (three.js) | Chart.js pour les graphiques ; la 3D est une extension en plus, pas un remplacement. |

## Les pièges annoncés par le sujet
- Ne pas mélanger des webcams trop différentes (pistes de ski et port dans le même modèle).
- Les liens de webcams changent ou disparaissent : d'où le jeu de référence figé.
- La nuit ou la pluie font chuter la détection : c'est un **résultat à documenter**, pas un échec.
- Le bon niveau d'exigence dépend de l'usage : « compter 40 au lieu de 50 suffit pour dimensionner un accueil, pas pour déclencher une alerte sécurité ».
