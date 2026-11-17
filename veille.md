# Veille technique — FlowView · Place Publique

*Compte rendu illustré et référencé des 8 questions du sujet. Chaque question a **un auteur qui la rédige et la défend** à la soutenance. Le sujet exige **au moins 2 questions par membre de l'équipe** : l'auteur de chaque question est à fixer au moment de la rédiger.*

> **État : version 1 (brouillon de travail du 17/11/2026).** Les chiffres marqués ✅ ont été relus dans la source primaire citée, à la date indiquée ; ceux marqués 🔎 restent à vérifier. Les cases « *à remplir* » attendent nos propres mesures (notebook du palier 1, CI, etc.). Avant la soutenance, chaque auteur **relit les sources, reformule avec ses mots** et doit pouvoir défendre chaque ligne.

**Règles de rédaction**
- Un **tableau comparatif** vaut mieux qu'un long paragraphe.
- Des **sources primaires et datées** (articles de recherche, documentation officielle, textes de loi, CNIL, CEPD) ; un blog seulement en complément.
- Distinguer ce qui est **mesuré** (chiffres, benchmarks avec leur source) de ce qui est **affirmé**.
- Finir chaque question par **« Ce qu'on en retient pour FlowView »** : la décision ou la conséquence concrète dans notre projet.
- Pas de copier-coller : on reformule et on cite.

| Q | Thème | Auteur | Palier | État |
|---|---|---|---|---|
| [Q1](#q1) | Modèles de détection : vitesse, précision, ressources | à fixer | 1 | v1 rédigée |
| [Q2](#q2) | Évaluer un détecteur sur caméras fixes ; mAP ≠ comptage | à fixer | 1 | v1 rédigée, chiffres à mesurer |
| [Q3](#q3) | Datasets, annotation, augmentation, adaptation de domaine | à fixer | 1 | v1 rédigée, licences Roboflow à vérifier |
| [Q4](#q4) | Architectures flux → inférence → base → front | à fixer | 2 | v1 rédigée, schéma à dessiner |
| [Q5](#q5) | MLOps : MLflow, CI/CD, versioning, tests | à fixer | 3 | v1 rédigée, à compléter au fil du projet |
| [Q6](#q6) | Dérive de données et de concept, ré-entraînement | à fixer | 3 | v1 rédigée, seuils à calibrer |
| [Q7](#q7) | RGPD et AI Act appliqués au comptage vidéo | à fixer | 3 | v1 rédigée, **un point ouvert** |
| [Q8](#q8) | Enjeux éthiques du comptage dans l'espace public | à fixer | 3 | v1 rédigée |

---

<a id="q1"></a>
## Q1 · Quels modèles de détection pour la vidéosurveillance, et quels compromis ?
*Auteur : · Dernière mise à jour : 2026-11-17*

> Quels sont aujourd'hui les principaux modèles de détection d'objets utilisés en vidéosurveillance (YOLO, Faster R-CNN, DETR…) et quels compromis font-ils entre vitesse, précision (mAP) et ressources sur du matériel limité ?

**Réponse courte.** Trois familles dominent. Les **détecteurs à deux étapes** (Faster R-CNN) proposent d'abord des régions puis les classent : solides mais lents et lourds. Les **détecteurs en une étape** (famille YOLO) prédisent tout en une passe : le meilleur rapport vitesse / précision sur CPU, d'où leur usage massif en vidéo. Les **transformers de détection** (DETR, puis RT-DETR, RF-DETR) suppriment l'étape de suppression des doublons (NMS) et dépassent désormais YOLO en précision à vitesse égale sur GPU. Sur du matériel limité, le vrai choix se fait entre **taille du modèle** (n, s, m…) et **résolution d'entrée**, et la **licence** pèse autant que le mAP.

| Modèle | Famille | mAP COCO val2017 (50-95) | Vitesse (matériel de la source) | Paramètres | Licence | Pour FlowView ? |
|---|---|---|---|---|---|---|
| Faster R-CNN R50-FPN 3x (Detectron2) | Deux étapes | 40,2 ✅ | 0,038 s / image (V100) ✅ | ~42 M 🔎 | Apache 2.0 | Non : lent sur CPU, dépassé |
| DETR R50 (Carion 2020) | Transformer | 42,0 ✅ | 0,036 s / image (V100) ✅ ; 500 époques d'entraînement | 41 M 🔎 | Apache 2.0 | Non : historique, lent à ré-entraîner |
| YOLO11n (Ultralytics) | Une étape | 39,5 ✅ | 56,1 ms CPU ONNX ✅ | 2,6 M ✅ | **AGPL-3.0** | Candidat baseline |
| YOLO11s | Une étape | 47,0 ✅ | 90,0 ms CPU ONNX ✅ | 9,4 M ✅ | **AGPL-3.0** | Candidat |
| YOLO26n (Ultralytics, dernière génération) | Une étape, sans NMS | 40,9 ✅ | 38,9 ms CPU ONNX ✅ | 2,4 M ✅ | **AGPL-3.0** | **Baseline proposée** |
| YOLO26s | Une étape, sans NMS | 48,6 ✅ | 87,2 ms CPU ONNX ✅ | 9,5 M ✅ | **AGPL-3.0** | Candidat si n trop faible |
| RT-DETR R18 (Zhao, CVPR 2024) | Transformer temps réel | 46,5 ✅ | 217 FPS (T4 TensorRT) ✅ | 20 M ✅ | Apache 2.0 | Comparaison possible |
| RF-DETR Nano (Roboflow, 2025) | Transformer temps réel | 48,4 ✅ | 2,3 ms (T4 TensorRT) ✅ | 30,5 M ✅ | Apache 2.0 | **Alternative si licence bloquante** |
| RF-DETR Small | Transformer temps réel | 53,0 ✅ | 3,5 ms (T4 TensorRT) ✅ | 32,1 M ✅ | Apache 2.0 | Alternative |

*Vitesses non comparables entre lignes : chaque source mesure sur son propre matériel (V100, Xeon en ONNX, T4 en TensorRT).*

**Trois pièges que la veille révèle**
1. **Qui mesure compte.** Ultralytics annonce 39,5 pour YOLO11n ; le README de RF-DETR, avec son propre protocole, lui donne 37,4 ✅. Un benchmark publié par un concurrent n'est pas neutre : on mesurera nous-mêmes, sur nos images.
2. **Le mAP COCO moyenne 80 classes et toutes les tailles d'objets.** Nous n'avons qu'une classe utile (`person`) et des skieurs souvent **petits et lointains** : c'est le sous-score *AP small* qui nous concerne, et il est bien plus bas que le mAP global sur tous ces modèles 🔎 (à relever dans nos mesures).
3. **La latence dépend du mode** (fiche [0019](docs/decisions/0019-socle-periodique-puis-temps-reel.md)). Dans le **socle périodique** (une image par caméra toutes les quelques secondes ou minutes), elle ne compte pas : même YOLO26s (~90 ms sur CPU) tient largement, et la contrainte est la **justesse du comptage sur de petites silhouettes**. La résolution d'entrée (640 contre 1280 px) pèsera probablement plus que le choix entre n et s 🔎. Dans le **mode direct avec suivi**, c'est l'inverse : il faut tenir 10 à 50 images par seconde *par caméra*. On passe donc sur GPU (TensorRT ou ONNX en fp16) et on arbitre entre cadence, résolution et nombre de caméras. 1280 px sur plusieurs flux à 30 images/s n'est pas acquis 🔎 (à mesurer sur la carte de Romuald).

**Ce qu'on en retient pour FlowView :**
- Baseline **YOLO26n pré-entraîné COCO**, classe `person`, en 640 puis 1280 px, comparé à YOLO26s : décision au vu de l'erreur de comptage, pas du mAP.
- **Licence AGPL-3.0** : compatible avec notre dépôt public (code source ouvert). Pour un FlowView commercial, il faudrait une licence Ultralytics ou passer à **RF-DETR (Apache 2.0)**. À écrire dans `conformite.md`.
- Pas d'entraînement de zéro (règle du sujet) ; fine-tuning éventuel sur GPU, inférence livrée sur CPU (idée I-08).
- Pour le mode direct : le suivi (ByteTrack ou BoT-SORT, intégrés à Ultralytics) s'ajoute **par-dessus** le même détecteur. Les détecteurs sans suppression des doublons (YOLO26, RF-DETR) ont une latence plus régulière, ce qui aide en flux continu 🔎.

**Sources** (consultées le 2026-11-17) :
- Ultralytics, README et tableau de performances YOLO26 / YOLO11 : <https://github.com/ultralytics/ultralytics>, <https://docs.ultralytics.com/models/yolo11/>
- Detectron2 Model Zoo (Faster R-CNN R50-FPN 3x) : <https://github.com/facebookresearch/detectron2/blob/main/MODEL_ZOO.md>
- Carion et al., *End-to-End Object Detection with Transformers* (DETR), ECCV 2020 ; dépôt <https://github.com/facebookresearch/detr>
- Zhao et al., *DETRs Beat YOLOs on Real-time Object Detection*, CVPR 2024 : <https://arxiv.org/abs/2304.08069> ; dépôt <https://github.com/lyuwenyu/RT-DETR>
- Roboflow, RF-DETR (README, tableau et licences) : <https://github.com/roboflow/rf-detr>
- Ren et al., *Faster R-CNN*, NeurIPS 2015 : <https://arxiv.org/abs/1506.01497>

---

<a id="q2"></a>
## Q2 · Évaluer rigoureusement un détecteur sur caméras fixes
*Auteur : · Dernière mise à jour : 2026-11-17*

> Comment évaluer rigoureusement un modèle de détection sur des caméras fixes (mAP, précision/rappel par classe, IoU, analyse d'erreurs), et pourquoi un bon mAP ne garantit-il pas un bon comptage ?

**Réponse courte.** Le mAP mesure si le modèle **classe et place bien** ses boîtes, en moyenne sur tous les seuils de confiance. Un comptage, lui, se fait à **un seul seuil** et ne demande qu'un nombre. Les deux divergent : un modèle peut avoir un bon mAP et compter faux (seuil mal choisi, foules où les boîtes fusionnent, doublons), ou compter juste par chance (faux positifs et oubliés qui s'annulent). On évalue donc **à deux niveaux** : la détection (précision, rappel par classe) pour comprendre, le **comptage** (erreur absolue moyenne, biais) pour décider. Sur caméra fixe, il faut en plus découper l'erreur **par caméra, par moment et par densité**, car la moyenne cache les cas qui comptent.

| Métrique | Ce qu'elle mesure | Ce qu'elle cache | Utile pour nous ? |
|---|---|---|---|
| IoU (intersection sur union) | Recouvrement entre boîte prédite et boîte vraie | Rien sur le nombre ; seuil arbitraire (0,5) | Indirect : sert à apparier les boîtes |
| mAP@0.5 / mAP@0.5:0.95 | Qualité de classement et de localisation, tous seuils de confiance confondus | Le seuil réellement utilisé ; les erreurs qui s'annulent | Pour comparer des modèles, pas pour décider |
| Précision / rappel par classe | Part des détections justes / part des personnes trouvées, à un seuil donné | La compensation entre les deux dans le total | Oui : explique *pourquoi* le compte est faux |
| Erreur absolue moyenne du comptage (MAE) | Écart moyen, en personnes, entre compté et vrai | Le sens de l'erreur ; les images rares mais graves | **Oui : métrique principale** |
| Biais (erreur signée moyenne) | Sur- ou sous-comptage systématique | La dispersion | **Oui : un sous-comptage dans les foules est le pire cas** |
| Erreur par tranche de densité | MAE pour 0-5, 6-20, plus de 20 personnes | — | **Oui : le seuil d'alerte se joue dans les fortes densités** |
| Erreur relative (MAPE) | Écart en % | Explose quand le vrai compte vaut 0 ou 1 | Non, ou seulement au-dessus d'un minimum |

**Exemple (illustratif, construit pour l'explication, pas mesuré)** : une image contient 10 skieurs. Le modèle en trouve 8 et ajoute 2 fausses détections (un panneau, une ombre). Compte affiché : **10, exact**. Pourtant précision = 0,8 et rappel = 0,8. Sur l'image suivante, 25 skieurs serrés dans une file : les boîtes se recouvrent, la suppression des doublons en fusionne, le modèle en compte 17. Erreur de −8, **précisément là où une alerte devrait partir**. La moyenne des deux images (MAE = 4) masque ce biais.

**Exemple chiffré tiré de notre jeu de référence :** *à remplir* (lien vers `notebooks/01_baseline.ipynb` : MAE, biais par classe et par tranche de densité, 10 pires images commentées).

**Méthode retenue pour le palier 1**
1. Jeu de référence **figé** (≥ 100 images, plusieurs caméras, matin / midi / soir, beau temps / neige / brouillard), jamais modifié après coup.
2. Vérité terrain à la main sur ≥ 50 images, par classe (`person`, et `skis` / `snowboard` si utile).
3. Choix du seuil de confiance **sur une partie des images, évaluation sur le reste** (sinon on triche).
4. Tableau MAE / biais global, par caméra, par tranche de densité ; analyse des 10 pires images (oubli dans la foule ? petite taille ? contre-jour ? fausse détection ?).
5. **Seuil d'acceptabilité justifié par l'usage**, par exemple : « l'erreur doit rester inférieure à l'écart entre deux niveaux d'affluence affichés », à fixer une fois les niveaux définis 🔎.

**Ce qu'on en retient pour FlowView :** on choisit le modèle et le seuil sur la **MAE et le biais du comptage**, pas sur le mAP ; on affiche à l'exploitant une **fourchette honnête** (le « chiffre honnête » de la DA) plutôt qu'un nombre faussement précis.

**Sources** (consultées le 2026-11-17) :
- COCO, définition des métriques de détection : <https://cocodataset.org/#detection-eval>
- Padilla, Netto, da Silva, *A Survey on Performance Metrics for Object-Detection Algorithms*, IWSSIP 2020
- Hoiem, Chodpathumwan, Dai, *Diagnosing Error in Object Detectors*, ECCV 2012
- Bolya et al., *TIDE: A General Toolbox for Identifying Object Detection Errors*, ECCV 2020 : <https://arxiv.org/abs/2008.08115>
- Zhang et al., *Single-Image Crowd Counting via Multi-Column CNN* (MAE / MSE en comptage de foule), CVPR 2016

---

<a id="q3"></a>
## Q3 · Datasets, annotation, augmentation, adaptation de domaine
*Auteur : · Dernière mise à jour : 2026-11-17*

> Comment sélectionner, combiner et annoter des datasets pour couvrir la variété des contextes clients, et quelles augmentations ou adaptations de domaine (météo, saison, angle, résolution) améliorent la robustesse ?

**Réponse courte.** Les jeux publics généralistes (COCO) apprennent « une personne » mais presque jamais **une personne en combinaison de ski, minuscule, sur fond blanc, vue d'une webcam en hauteur**. L'écart entre ces images et les nôtres (le *décalage de domaine*) est le premier risque. On combine donc : un modèle pré-entraîné sur COCO, des jeux **proches du domaine** (foules, scènes de neige), puis **nos propres images annotées**. Les augmentations simulent ce que les jeux publics n'ont pas (neige, brouillard, contre-jour, basse résolution), mais elles ne remplacent pas de vraies images : on ne garde que celles qui **font baisser l'erreur mesurée** sur le jeu de référence.

| Dataset / outil | Contenu | Licence | Pertinence (station, neige, foule) |
|---|---|---|---|
| COCO 2017 (Lin et al., 2014) | 118 k images, 80 classes dont `person`, `skis`, `snowboard` | Annotations CC BY 4.0 ; images soumises aux conditions Flickr de chaque auteur ✅ | Base du pré-entraînement ; peu de petites silhouettes sur neige |
| CrowdHuman (Shao et al., 2018) | Foules denses, fortes occlusions | **Usage non commercial, recherche et enseignement, pas de redistribution des images** ✅ | Utile pour les files d'attente ; usage scolaire seulement |
| Jeux « skieurs » de Roboflow Universe | Skieurs, pistes, remontées (selon le jeu) | **Variable, jeu par jeu** 🔎 ; un ré-envoi peut afficher une licence différente de l'original (cas observé sur CrowdHuman ✅) | Très proche du domaine ; à vérifier un par un avant usage |
| Nos captures (station ouverte, puis Les Arcs) | Les vraies caméras, les vrais angles | Conditions d'utilisation des webcams à lire 🔎 ; images jamais versionnées (`.gitignore`) | **Indispensable** : seule source du vrai domaine |
| CVAT | Outil d'annotation (boîtes, export YOLO / COCO) | MIT 🔎 | Annotation de la vérité terrain |
| Label Studio | Outil d'annotation | Apache 2.0 🔎 | Alternative |

| Augmentation / adaptation | Ce qu'elle simule | Mesure concrète (au moins deux) |
|---|---|---|
| Neige, brouillard, pluie synthétiques (Albumentations `RandomSnow`, `RandomFog`, `RandomRain`) | Météo de montagne | MAE sur les images « neige / brouillard » du jeu de référence, avant / après |
| Luminosité, contraste, reflets (`RandomBrightnessContrast`, `RandomSunFlare`) | Soleil sur neige, contre-jour, fin de journée | MAE par tranche horaire |
| Basse résolution, compression JPEG, flou | Webcam de qualité moyenne, image compressée | MAE sur les caméras les moins nettes |
| Échelle et recadrage (*mosaic*, *random crop*) | Silhouettes plus ou moins lointaines | Rappel sur les petites boîtes (*AP small*) |
| Pseudo-étiquetage (le modèle annote, un humain corrige) | Adaptation au domaine à moindre coût d'annotation | Temps d'annotation par image ; MAE après fine-tuning |
| Adaptation de domaine adverse (DA Faster R-CNN, Chen 2018) | Aligner les caractéristiques source / cible sans annoter la cible | Hors périmètre : cité pour la culture, trop lourd pour 15 jours |

**Ce qu'on en retient pour FlowView :**
- **Aucune image dans le jeu d'entraînement ne doit venir du jeu de référence figé** (sinon l'évaluation ment). Séparation par caméra et par jour, pas image par image (deux images à une minute d'écart sont presque identiques).
- Chaque jeu tiers entre dans un **tableau de provenance** (source, licence vérifiée, date, nombre d'images) dans `conformite.md`.
- Une augmentation n'est gardée que si elle améliore la MAE mesurée sur le jeu de référence.

**Sources** (consultées le 2026-11-17) :
- Lin et al., *Microsoft COCO: Common Objects in Context*, ECCV 2014 ; conditions d'utilisation : <https://cocodataset.org/#termsofuse>
- Shao et al., *CrowdHuman: A Benchmark for Detecting Human in a Crowd*, 2018 : <https://arxiv.org/abs/1805.00123>
- Buslaev et al., *Albumentations: Fast and Flexible Image Augmentations*, Information 11(2), 2020 : <https://albumentations.ai/>
- Chen et al., *Domain Adaptive Faster R-CNN for Object Detection in the Wild*, CVPR 2018
- Sakaridis, Dai, Van Gool, *Semantic Foggy Scene Understanding with Synthetic Data*, IJCV 2018

---

<a id="q4"></a>
## Q4 · Relier flux vidéo, inférence, base temporelle et front
*Auteur : · Dernière mise à jour : 2026-11-17*

> Quelles architectures relient flux vidéo, service d'inférence, base temporelle et frontend (batch périodique ou quasi temps réel, microservices, file de messages), et avec quels effets sur la scalabilité et la tolérance aux pannes ?

**Réponse courte.** Le bon choix dépend de **ce qu'on veut mesurer**. L'**occupation** (combien de personnes à un instant) évolue à l'échelle de quelques minutes : un **batch périodique** (une capture par caméra toutes les N secondes ou minutes, analysée puis rangée en base) suffit, et reste simple, robuste et peu coûteux. C'est ce que demande le sujet. Le **flux** (combien de personnes passent par minute, à quel débit se vide une file) exige de **suivre les personnes d'une image à l'autre** : il faut alors une analyse **quasi temps réel** du flux vidéo, qui coûte un GPU par poignée de caméras. Les **microservices avec file de messages** (Kafka, RabbitMQ) découplent capture, inférence et stockage, et passent à l'échelle de centaines de caméras, au prix d'une complexité qu'un projet de 15 jours ne peut pas justifier. **FlowView fait les deux, dans l'ordre** (fiche [0019](docs/decisions/0019-socle-periodique-puis-temps-reel.md)) : le socle périodique, puis un mode direct avec suivi sur les caméras choisies.

**Schéma de notre architecture** *(à dessiner pour `architecture.md`)* :

```
Webcam publique ──(toutes les N min, APScheduler)──▶ capture
      capture ──▶ détection YOLO (CPU) ──▶ comptage + image floutée
                                   │                  │
                                   ▼                  ▼
                     SQLite : comptes agrégés   dernière image floutée
                     (horodatés, par caméra)    (écrasée à chaque cycle)
                                   │
                                   ▼
                     Flask (+ gunicorn en production) ──▶ écran FlowView
```
L'image brute n'est **jamais écrite sur disque** : seuls le compte et une image floutée (la dernière) sortent du traitement.

Mode direct (extension, après les paliers) :
```
Flux vidéo (RTSP / HLS autorisé, ou vidéo en rejeu) ──▶ lecture OpenCV
      ──▶ détection YOLO (GPU) ──▶ suivi ByteTrack (identifiants en mémoire seulement)
      ──▶ franchissement de ligne / zone ──▶ passages par minute, occupation moyenne
                 │                                        │
                 ▼                                        ▼
   images floutées diffusées à l'écran          SQLite : agrégats par minute
   (jamais enregistrées)                         (même base que le socle)
```

| Option | Principe | Scalabilité | Tolérance aux pannes | Coût / complexité |
|---|---|---|---|---|
| **Batch périodique (socle)** | Un planificateur déclenche capture → inférence → écriture | Linéaire et prévisible : à 39 ms par image (YOLO26n, Xeon, ONNX ✅), 20 caméras ≈ 1 s de calcul par cycle (ordre de grandeur, **à mesurer sur notre machine**) | Une caméra en panne n'en bloque pas d'autres ; un cycle raté devient une ligne « **pas de donnée** », jamais un zéro | Faible : un processus, une base fichier |
| **Quasi temps réel avec suivi (mode direct, extension)** | Lecture continue du flux, détection et suivi image par image | Coûteuse : un GPU pour quelques flux ; le décodage vidéo peut devenir le goulot avant le modèle 🔎 | Reconnexion au flux, mémoire tampon bornée (on jette les images en retard plutôt que d'accumuler du retard) ; un flux coupé devient « pas de donnée » | Élevée ; **seul moyen de mesurer le flux** (passages, débit) |
| Microservices + file de messages | Capture, inférence, stockage séparés, reliés par une file | Horizontale (ajouter des « workers » d'inférence) | Bonne : la file garde les messages si un service tombe | Très élevée pour 2 personnes et 15 jours |

**Points d'ingénierie qui découlent de ce choix**
- **SQLite** convient : un seul écrivain (le planificateur), quelques lecteurs (Flask). Le mode **WAL** permet de lire pendant qu'on écrit ✅. Au-delà de plusieurs écrivains concurrents, on passerait à PostgreSQL / TimescaleDB.
- **Flask** sert l'écran ; son serveur intégré est réservé au développement, la documentation Flask demande un serveur WSGI en production ✅. **gunicorn** ne tourne que sous Unix ✅ : il vit donc dans l'image Docker (Linux), et on développe avec `flask run` sous Windows.
- Le planificateur ne doit tourner **qu'une fois** : s'il est lancé dans chaque worker gunicorn, chaque capture serait faite N fois. Planificateur dans un processus séparé (ou un seul worker) 🔎 à trancher au palier 2.

- Mode direct : un **processus séparé par flux** (ou un seul processus qui regroupe les images de plusieurs caméras en lots sur le GPU 🔎), qui écrit des agrégats par minute dans la même base. L'affichage en direct passe par un flux MJPEG servi par Flask (méthode citée par le sujet, PyImageSearch) ou par WebSocket 🔎.

**Ce qu'on en retient pour FlowView :** socle en batch périodique, SQLite en WAL, Flask derrière gunicorn dans Docker. Le mode direct vient ensuite et réutilise le même détecteur et la même base. La file de messages est décrite dans `architecture.md` comme **chemin de passage à l'échelle**, pas construite.

**Sources** (consultées le 2026-11-17) :
- Flask, *Deploying to Production* : <https://flask.palletsprojects.com/en/stable/deploying/>
- Gunicorn, documentation (« WSGI HTTP Server for UNIX ») : <https://gunicorn.org/>
- APScheduler, documentation : <https://apscheduler.readthedocs.io/>
- SQLite, *Write-Ahead Logging* : <https://www.sqlite.org/wal.html> ; *Appropriate Uses For SQLite* : <https://www.sqlite.org/whentouse.html>
- Kleppmann, *Designing Data-Intensive Applications*, O'Reilly, 2017 (chapitres sur les files de messages et le traitement par lots)
- Zhang et al., *ByteTrack: Multi-Object Tracking by Associating Every Detection Box*, ECCV 2022 : <https://arxiv.org/abs/2110.06864>
- Ultralytics, mode *Track* (BoT-SORT, ByteTrack) : <https://docs.ultralytics.com/modes/track/>
- PyImageSearch, diffuser une vidéo OpenCV vers un navigateur avec Flask (ressource citée par le sujet)

---

<a id="q5"></a>
## Q5 · MLOps : un cycle de vie maîtrisé du modèle
*Auteur : · Dernière mise à jour : 2026-11-17*

> Quels outils et pratiques MLOps (MLflow, CI/CD, versioning de modèles, tests) assurent un cycle de vie maîtrisé du modèle, de l'expérimentation au déploiement reproductible ?

**Réponse courte.** Le code d'un système d'apprentissage automatique n'en est qu'une petite partie : données, configuration, modèle et surveillance pèsent plus lourd et vieillissent mal si on ne les trace pas (la « dette technique cachée » de Sculley et al.). Un cycle maîtrisé repose sur quatre briques : **tracer chaque expérience** (paramètres, métriques, artefacts), **versionner** le modèle *et* les données qui l'ont produit, **tester** au-delà du code (non-régression sur un jeu de référence), et **automatiser** construction et déploiement. Google décrit trois niveaux de maturité, du tout-manuel (niveau 0) à l'entraînement continu automatisé (niveau 2) ; pour un projet de 15 jours, viser un **niveau 1 partiel** est réaliste.

| Étape | Outil | Ce qu'on a vraiment fait dans le projet (lien) |
|---|---|---|
| Suivi d'expériences | MLflow (paramètres, métriques MAE / biais, artefacts) | *à faire au palier 1* : un run par modèle × résolution × seuil |
| Versioning du modèle | Registre de modèles MLflow ; poids jamais dans Git (`*.pt` dans `.gitignore` ✅) | *à faire* : modèle « en production » = une version du registre, avec son hash |
| Versioning des données | Manifeste du jeu de référence (liste des fichiers + empreinte SHA-256) | *à faire* : prouve que le jeu figé n'a pas bougé |
| Tests | pytest | *à faire* : comptage, calcul des erreurs, routes Flask, **test de non-régression** (MAE sur 5 images de référence sous un plafond) |
| CI | GitHub Actions : ruff + pytest, puis construction de l'image Docker | ✅ en place (`.github/workflows/ci.yml`) |
| CD | Image publiée sur ghcr.io à chaque push sur `main` | ✅ en place (`.github/workflows/cd.yml`) ; déploiement par `docker compose pull && docker compose up -d` |

**Ce qu'on en retient pour FlowView :**
- **Aucun modèle ne part en production sans un run MLflow** qui prouve sa MAE sur le jeu de référence figé.
- Le test de non-régression vit dans la CI : un changement de modèle ou de seuil qui dégrade le comptage casse la construction.
- Image Docker sur CPU (torch CPU) : reproductible sur n'importe quelle machine ; l'entraînement sur GPU reste hors CI (idée I-08).

**Sources** (consultées le 2026-11-17) :
- Sculley et al., *Hidden Technical Debt in Machine Learning Systems*, NeurIPS 2015 : <https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems>
- Google Cloud, *MLOps: Continuous delivery and automation pipelines in machine learning* : <https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning>
- Breck et al., *The ML Test Score: A Rubric for ML Production Readiness*, IEEE Big Data 2017
- MLflow, documentation (Tracking, Model Registry) : <https://mlflow.org/docs/latest/>
- GitHub Actions, documentation : <https://docs.github.com/actions>

---

<a id="q6"></a>
## Q6 · Détecter la dérive et déclencher un ré-entraînement
*Auteur : · Dernière mise à jour : 2026-11-17*

> Quels signaux détectent la dérive de données ou de concept dans un système de comptage, et comment déclencher un ré-entraînement pertinent ?

**Réponse courte.** Deux dérives à distinguer. La **dérive de données** : les images changent (neige fraîche, brouillard, caméra déplacée ou salie, nouvel éclairage) alors que le modèle reste le même. La **dérive de concept** : la relation entre image et bonne réponse change (par exemple, des files qui se forment autrement après des travaux, ou une nouvelle tenue qui trompe le modèle). En production, **on n'a pas la vérité terrain** : on surveille donc des signaux indirects (scores de confiance, nombre de détections comparé à l'historique, part d'échecs), et on **ré-annote un petit échantillon** régulièrement pour mesurer la vraie erreur. Le ré-entraînement se déclenche sur une erreur mesurée, jamais sur un simple signal indirect, et le nouveau modèle ne remplace l'ancien qu'après un test de non-régression.

| Signal | Comment le calculer | Seuil proposé (à calibrer 🔎) | Ce qu'il révèle |
|---|---|---|---|
| Distribution des scores de confiance | Médiane et histogramme des scores par caméra et par jour ; test de Kolmogorov-Smirnov contre une semaine de référence | Médiane en baisse de plus de 15 % sur 3 jours | Images moins « lisibles » : météo, caméra sale, nouvel angle |
| Taux de détection par heure vs historique | Compte moyen par créneau horaire, comparé au même créneau des semaines passées | Écart de plus de 3 écarts-types, hors événement connu | Panne silencieuse ou vrai changement d'affluence (à distinguer) |
| Part de « pas de donnée » | Cycles sans image exploitable / cycles prévus | Plus de 10 % sur une journée | Problème de capture, pas de modèle ; ne pas ré-entraîner |
| Statistiques de l'image | Luminosité moyenne, netteté (variance du laplacien), histogramme | Rupture brutale sur une caméra | Caméra déplacée, objectif couvert de neige |
| Retour utilisateur | Bouton « ce chiffre me paraît faux » sur l'écran ; image floutée jointe | Plus de N signalements par semaine sur une caméra | Le signal le plus direct, à ne pas négliger |
| **Erreur mesurée** | MAE sur un échantillon ré-annoté (20 images / caméra / mois) | Au-dessus du seuil d'acceptabilité du palier 1 | **Seul déclencheur de ré-entraînement** |

**Déclencheurs de ré-entraînement :**
1. La MAE ré-annotée dépasse le seuil d'acceptabilité sur une caméra ou une condition (ex. brouillard).
2. Une nouvelle caméra ou un nouveau client (nouveau domaine) : annotation d'un lot, fine-tuning.
3. Le nouveau modèle doit **faire au moins aussi bien sur le jeu de référence figé** que l'actuel (non-régression) **et** mieux sur les images qui ont posé problème. Validation humaine avant déploiement.

**Ce qu'on en retient pour FlowView :** dans le projet, on **calcule et affiche** les signaux indirects (scores, « pas de donnée ») et on décrit la boucle complète dans `architecture.md` ; le ré-entraînement automatique reste sur le papier, conformément au sujet.

**Sources** (consultées le 2026-11-17) :
- Gama et al., *A Survey on Concept Drift Adaptation*, ACM Computing Surveys 46(4), 2014 : <https://doi.org/10.1145/2523813>
- Lu et al., *Learning under Concept Drift: A Review*, IEEE TKDE 31(12), 2019
- Rabanser, Günnemann, Lipton, *Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift*, NeurIPS 2019 : <https://arxiv.org/abs/1810.11953>
- Evidently AI, documentation sur la dérive de données : <https://docs.evidentlyai.com/>

---

<a id="q7"></a>
## Q7 · RGPD et AI Act appliqués au comptage par vidéo
*Auteur : · Dernière mise à jour : 2026-11-17*

> Comment le RGPD et l'AI Act qualifient-ils un système de comptage par vidéo, quelles obligations en découlent (base légale, AIPD, transparence) et quelles pratiques techniques (agrégation, absence de stockage vidéo) aident à rester conforme ?

**Réponse courte.** Même si FlowView ne garde qu'un nombre, **analyser une image où des personnes sont reconnaissables est un traitement de données personnelles** au sens du RGPD, et le fait que la webcam soit déjà publique n'y change rien : l'analyse par IA est un **traitement distinct** de la simple diffusion (avis du Conseil d'État cité par la CNIL ✅). Il faut donc une base légale, une information des personnes, probablement une AIPD, et une conception qui minimise tout. Côté **AI Act**, un comptage sans identification ni catégorisation des personnes n'est **ni interdit ni à haut risque** : c'est un système à risque minimal, soumis surtout à l'obligation de maîtrise de l'IA (article 4).

| Texte (date) | Ce qu'il dit pour un comptage agrégé | Obligation pour nous |
|---|---|---|
| RGPD, art. 4 et 6 (règlement 2016/679) | Une image de personne identifiable est une donnée personnelle ; il faut une base légale | Base légale : **intérêt légitime** de la station (gestion des flux, art. 6.1.f), avec mise en balance écrite |
| RGPD, art. 25 | Protection des données dès la conception et par défaut | Image brute jamais stockée, floutage, agrégats seuls |
| RGPD, art. 35.3.c | AIPD obligatoire pour une **surveillance systématique à grande échelle d'une zone accessible au public** | **AIPD à rédiger** (au moins une version simplifiée dans `conformite.md`) |
| RGPD, art. 13 / 21 | Information des personnes ; droit d'opposition | Panneau d'information près des caméras ; question de l'opposition (voir point ouvert) |
| CNIL, position sur les caméras « augmentées » (19/07/2022) ✅ | Un comptage **à finalité statistique** (agrégats anonymes, images effacées au plus vite) bénéficie d'un régime dérogatoire qui peut **exclure le droit d'opposition** (art. 89 RGPD, art. 116 du décret du 29/05/2019). Mais un traitement qui **déclenche lui-même une décision immédiate, comme une alerte**, n'est « généralement pas » purement statistique ✅ | **Point ouvert ci-dessous** |
| CNIL, même position | Garanties citées : baisse de définition, floutage, traitement local, suppression quasi immédiate des images sources ✅ | Toutes reprises dans notre conception |
| CEPD, lignes directrices 3/2019 sur les dispositifs vidéo (v2.0, adoptées le 29/01/2020) ✅ | Cadre général de la vidéo au regard du RGPD ; l'analyse « intelligente » peut être plus ou moins intrusive, le simple comptage étant en bas de l'échelle 🔎 (formulation à relire dans la version finale) | Justifier la proportionnalité |
| AI Act, règlement (UE) 2024/1689, art. 5 | Interdictions : identification biométrique à distance en temps réel pour les forces de l'ordre, reconnaissance des émotions au travail, catégorisation biométrique sensible… | **Non concerné** : aucune donnée biométrique, aucune identification |
| AI Act, annexe III | Haut risque : biométrie, infrastructures critiques listées, emploi, etc. | **Non concerné** : pas de biométrie, les remontées mécaniques ne figurent pas dans les infrastructures critiques listées 🔎 |
| AI Act, annexe I, section A, point 8 : règlement 2016/424 sur les **installations à câbles** ✅ | Une IA qui serait un **composant de sécurité** d'une remontée relèverait du haut risque | **Non concerné tant que FlowView ne commande pas la remontée** : il informe un humain, il n'agit pas sur l'installation. À écrire noir sur blanc |
| AI Act, art. 4 et art. 50 | Maîtrise de l'IA (depuis le 02/02/2025) ; transparence pour les IA qui dialoguent ou génèrent du contenu | Art. 4 : former les utilisateurs (ce que le chiffre veut dire, sa marge d'erreur). Art. 50 : non concerné |
| Omnibus numérique sur l'IA, règlement (UE) 2026/1744 (JO du 24/07/2026) 🔎 | Reporte les obligations à haut risque de l'annexe III au 02/12/2027 | Ne change pas notre qualification |

**Notre qualification (démontrée, pas affirmée) :**
1. **Donnée personnelle ?** Oui, pendant les quelques secondes où l'image est analysée : des personnes peuvent y être reconnaissables. Après : non, il ne reste qu'un compte agrégé et une image floutée.
2. **Biométrie ?** Non : nous ne faisons aucun traitement technique destiné à identifier une personne de manière unique (pas de visage, pas d'attribut genre / âge, pas de réidentification d'une caméra à l'autre).
3. **AI Act ?** Système à risque minimal, à condition de rester un **outil d'aide à la décision humaine**, sans action sur l'installation.
4. **Et le mode direct avec suivi ?** Le suivi attribue un identifiant temporaire à chaque silhouette pour la suivre quelques secondes dans le champ d'une caméra. Ce n'est pas de la biométrie : l'identifiant repose sur la position et l'apparence de la boîte, pas sur une caractéristique physique unique 🔎. Mais il crée une **trajectoire individuelle**, ce qui est plus intrusif qu'un comptage sur image fixe, et l'analyse vidéo devient continue. Garde-fous : identifiants **en mémoire seulement**, effacés à la sortie du champ, jamais stockés ni affichés ; aucune réidentification entre caméras ; seuls des agrégats par minute vont en base ; flou appliqué avant tout affichage. Le mode direct a sa **propre section dans l'AIPD**.

**Point ouvert à présenter au jury (et à faire trancher par le formateur)** : la CNIL considère qu'un comptage qui **déclenche une alerte** n'est généralement plus purement statistique. Or FlowView alerte. Conséquences possibles :
- soit on sépare nettement deux traitements : (a) le comptage statistique, qui produit des agrégats anonymes et efface l'image ; (b) l'alerte, qui ne lit **que les agrégats en base** et jamais l'image. L'argument : la décision est prise « sur le fondement des données anonymes », ce que la CNIL admet pour le statistique ✅. Mais la proximité temporelle (alerte quasi immédiate) fragilise l'argument 🔎 ;
- soit on accepte que le traitement n'est pas purement statistique : le droit d'opposition ne peut alors pas être écarté par ce régime, il faut l'organiser (information, mise en balance de l'intérêt légitime) et l'AIPD devient centrale.
Nous recommandons d'**exposer cette tension honnêtement** plutôt que de la cacher : c'est exactement ce qu'un client exploitant devra traiter avec son délégué à la protection des données.

**Ce qu'on en retient pour FlowView :** pas de stockage d'image brute, floutage avant toute sortie, suivi limité au mode direct avec identifiants éphémères jamais stockés, pas d'attribut démographique, agrégats seuls en base, image floutée unique écrasée à chaque cycle, panneau d'information, AIPD dans `conformite.md`, et la frontière « informe, ne commande pas » écrite dans l'architecture.

**Sources** (consultées le 2026-11-17) :
- Règlement (UE) 2016/679 (RGPD), art. 4, 6, 13, 21, 25, 35, 89 : <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- CNIL, *Caméras dites « augmentées » dans les espaces publics : la position de la CNIL*, juillet 2022, §4.4 « dispositifs à des fins statistiques » : <https://www.cnil.fr/fr/cameras-dites-augmentees-dans-les-espaces-publics-la-position-de-la-cnil> (PDF : <https://www.cnil.fr/sites/cnil/files/atoms/files/cameras-intelligentes-augmentees_position_cnil.pdf>)
- CEPD, *Lignes directrices 3/2019 sur le traitement des données à caractère personnel par des dispositifs vidéo*, v2.0, 29/01/2020 : <https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_fr>
- Règlement (UE) 2024/1689 (AI Act), art. 3, 4, 5, 50, annexes I et III : <https://eur-lex.europa.eu/eli/reg/2024/1689/oj> ; annexe I sur le service d'assistance de la Commission : <https://ai-act-service-desk.ec.europa.eu/fr/ai-act/annex-1>
- Omnibus numérique sur l'IA (règlement (UE) 2026/1744) : synthèse <https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/> 🔎 texte officiel à relire sur EUR-Lex

---

<a id="q8"></a>
## Q8 · Les enjeux éthiques du comptage automatisé dans l'espace public
*Auteur : · Dernière mise à jour : 2026-11-17*

> Quels sont les enjeux éthiques du comptage automatisé dans l'espace public (surveillance de masse, biais, réutilisation des données) et quelles mesures de conception les limitent ?

**Réponse courte.** Le comptage paraît anodin, mais il installe **des caméras qui regardent et un logiciel qui interprète** dans un lieu où les gens viennent se détendre. Trois risques : le **glissement d'usage** (un outil de comptage devient un outil de surveillance parce que la capacité technique existe déjà), les **biais** (le modèle se trompe plus sur certains groupes ou certaines situations, et l'erreur n'est pas répartie au hasard), et la **réutilisation des données** (des images ou des séries conservées pour une autre finalité). La CNIL le résume : même pour produire une statistique, construire cet indicateur à partir d'images filmées dans l'espace public « n'est pas anodin ».

| Risque | Exemple concret | Mesure de conception dans FlowView |
|---|---|---|
| Glissement vers la surveillance | L'expérimentation de vidéosurveillance algorithmique prévue pour les JO 2024 a été prolongée : une première prolongation a été censurée en avril 2025, une seconde validée en 2026 🔎 (dates exactes à relire sur le site du Conseil constitutionnel) | **Impossibilité technique** plutôt que promesse : pas de stockage d'image brute, pas de visage, pas de zoom ; en mode direct, suivi limité à une caméra, identifiants effacés à la sortie du champ, aucune réidentification entre caméras ; le code est public |
| Biais de détection | Wilson et al. (2019) mesurent des détecteurs de piétons **moins performants sur les peaux foncées** ✅. Chez nous, le biais attendu porte surtout sur la **distance, l'occlusion et la densité** : le modèle sous-compte les foules serrées 🔎 (à mesurer) | Biais mesuré **par tranche de densité et par caméra** (Q2) ; marge d'erreur affichée ; « pas de donnée » jamais confondu avec zéro |
| Réutilisation des données | Une série horodatée par caméra pourrait servir à surveiller un employé (un perchman, un pisteur) ou à vendre de la donnée de fréquentation | Agrégats seulement, pas de donnée par individu ; finalité écrite (gestion des flux) ; durée de conservation définie ; pas d'accès tiers prévu |
| Confiance aveugle dans le chiffre | « Les données et l'IA, ça ment beaucoup » (notre persona d'exploitant) | Le « chiffre honnête » de la DA : fourchette, date de la dernière image, image floutée consultable pour **vérifier de ses yeux** |
| Décision automatisée | Fermer une file ou un accès sur la seule foi du modèle | FlowView **informe, l'humain décide** ; aucune action automatique sur les installations (lien avec l'annexe I de l'AI Act, Q7) |

**Notre position argumentée.** Nous pensons que le comptage d'affluence est **légitime** quand il sert directement les personnes comptées (moins d'attente, moins de foule dangereuse) et qu'il est **techniquement incapable** de faire autre chose. La protection la plus solide n'est pas une charte mais une architecture : ce que le système ne stocke pas, il ne peut pas le divulguer ni le réutiliser. C'est pourquoi nous refusons des fonctions pourtant faciles et vendeuses, comme la segmentation par genre ou âge (que la CNIL cite comme possible en statistique ✅) ou le suivi d'une personne à travers la station. Le suivi que nous gardons (mode direct) reste à l'intérieur d'une seule caméra et ne dure que le temps de compter un passage. Le risque qui reste, c'est l'**erreur** : un sous-comptage dans les foules est un biais qui joue contre la sécurité. Nous le mesurons et l'affichons plutôt que de le cacher derrière un nombre rond.

**Sources** (consultées le 2026-11-17) :
- CNIL, position sur les caméras « augmentées », juillet 2022 (voir Q7)
- Wilson, Hoffman, Morgenstern, *Predictive Inequity in Object Detection*, arXiv 2019 (non relu par les pairs) : <https://arxiv.org/abs/1902.11097>
- Koops, *The concept of function creep*, Law, Innovation and Technology 13(1), 2021 🔎
- Conseil constitutionnel, décision d'avril 2025 sur la loi relative à la sûreté dans les transports (censure de la prolongation) ; commentaire de la décision de 2026 🔎 : <https://www.conseil-constitutionnel.fr/>
- CEPD, lignes directrices 3/2019 (voir Q7)
