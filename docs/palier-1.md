# Palier 1 · Un comptage mesuré — protocole et carnet

*Méthode (fiche [0019](decisions/0019-socle-periodique-puis-temps-reel.md)) : une étape à la fois. Avant chaque étape, on écrit **l'hypothèse**, **la mesure** et **le critère de passage**. On ne passe à l'étape suivante que lorsque le critère est atteint, et le résultat est noté ici, daté. Les choix qui en découlent vont dans [decisions/](decisions/README.md).*

**Critère de validation du sujet :**
- un notebook reproductible produit le tableau d'erreurs par classe sur le jeu de référence ;
- un seuil d'acceptabilité par classe est écrit et justifié par l'usage (à titre indicatif : erreur relative médiane ≤ 20 % sur les classes principales).

| Étape | Hypothèse | Mesure | Critère de passage | État |
|---|---|---|---|---|
| **1.1 Sources** | Il existe des images de **notre contexte** (vues de webcams de station, avec et sans foule, jour, nuit, météo variée), utilisables légalement pour un projet d'école | Liste des sources avec licence ou autorisation vérifiée ; couverture caméra × moment × météo × affluence | Au moins une source utilisable dans le cadre pédagogique (fiche 0021) qui couvre 3 caméras et des scènes chargées | **en cours** |
| **1.2 Jeu de référence figé** | ≥ 100 images variées suffisent à mesurer l'erreur avec une précision utile | Nombre d'images par strate ; doublons quasi identiques écartés (empreinte perceptuelle) | `data/reference/manifest.csv` versionné (fichier, source, date, licence, SHA-256) ; chaque strate ≥ 10 images ; plus jamais modifié | à faire |
| **1.3 Seuil d'acceptabilité** | L'usage (niveaux d'affluence affichés, seuil d'alerte) fixe l'erreur tolérable | Écart entre deux niveaux d'affluence, par classe | Seuil écrit dans `docs/evaluation.md` et **commité avant le premier lancement de la baseline** : l'horodatage Git prouve qu'on ne l'a pas ajusté aux résultats | à faire |
| **1.4 Vérité terrain** | On peut compter à la main de façon fiable | Guide de comptage (qui compte : personne partielle, sur un siège, au loin…) ; **10 images comptées deux fois** pour mesurer l'écart entre deux comptages | ≥ 50 images comptées par classe ; écart entre deux comptages < seuil de 1.3 | à faire |
| **1.5 Baseline** | YOLO26n pré-entraîné (COCO), sans fine-tuning, atteint le seuil sur `person` | MAE, biais, erreur relative médiane, par classe et par tranche de densité ; en 640 puis 1280 px | Tableau produit par `notebooks/01_baseline.ipynb` ; comparaison avec le seuil | à faire |
| **1.6 Analyse des erreurs** | Les erreurs ont des causes nommables (petite taille, foule serrée, contre-jour…) | Les 10 pires images, classées par cause | Une cause dominante identifiée et une piste pour le palier suivant | à faire |
| **1.7 Reproductibilité** | Un clone vierge redonne le même tableau | Relance complète du notebook | Mêmes chiffres à la décimale près | à faire |

---

## Carnet

### 2026-11-17 · Étape 1.1, premier passage
Sources vérifiées : voir [sources.md](sources.md).

**Fait marquant :** les webcams des Arcs sont servies par webcam-hd / Trinum avec une **archive quotidienne depuis le 1er octobre 2025** ✅ (liste des dates relevée dans le lecteur officiel, caméra Arcabulle). Toute la saison 2025-2026 est donc consultable, vacances de février comprises. Ça pourrait lever le risque n°1 du projet (pas de foule avant le 12/12). On aurait des images de **notre** contexte exact, comme le demande le sujet, au lieu de jeux publics mal assortis (les jeux « skieurs » de Roboflow sont surtout des plans serrés de course 🔎).

**Mais :** les mentions légales de lesarcs.com interdisent toute reproduction sans autorisation écrite ✅. Il faut donc **demander l'autorisation** (brouillon dans [sources.md](sources.md)) avant de constituer le jeu de référence à partir de cette archive. Je n'ai rien téléchargé de l'archive.

**Décision à prendre (Romuald) :** demander l'autorisation aux Arcs et à webcam-hd, et en attendant soit patienter, soit avancer avec les jeux publics. Si la réponse est oui, la fiche 0016 (données en trois temps) sera à réviser.

### 2026-11-18 · Étape 1.1, droits tranchés
Romuald : pas de demande d'autorisation, le cadre pédagogique et la règle du sujet suffisent ; la question va dans les **limites réglementaires** (→ [0021](decisions/0021-webcams-usage-pedagogique-sans-autorisation.md)). Garde-fous : environ 150 images, accès normaux seulement, rien dans Git, rien de publié sans flou, source citée, suppression en fin de projet.

**Reste pour fermer 1.1 :** regarder ce que montre chaque caméra des Arcs en journée de février (files, terrasses, front de neige ?) pour choisir les 3 caméras du jeu de référence.

### 2026-11-18 · Étape 1.1, revue des 9 caméras
Les 6 webcams vues ce matin en plein jour (images publiques du site), les 3 livecams sur leur page. Le cadrage d'une caméra fixe ne change pas entre novembre et février : on peut choisir sur la vue d'aujourd'hui.

| Caméra | Ce qu'elle montre | Pour le jeu de référence (archive) | Pour le mode direct |
|---|---|---|---|
| **Arcabulle** (webcam) | 360°, arrivée de télésiège, terrasse | **Oui** | — |
| **Mont-Blanc** (webcam) | 360°, gare de télésiège et piste | **Oui** | — |
| **Grizzly** (webcam) | Gare de télésiège, zone de départ | **Oui** | — |
| Varet (webcam) | Gare et terrasse à 2 600 m, objectif en partie givré | Réserve | — |
| Arpette (webcam) | Objectif givré, cadrage inconnu | À revoir dans l'archive | — |
| Aiguille Rouge (webcam) | Sommet, objectif givré, peu de monde | Non | — |
| **Vagère** (livecam) | Départ de télésiège, 720p, plus proche | Pas d'archive | **Oui, n°1** |
| **Arc 2000** (livecam) | Front de neige, piétons au pied des résidences | Pas d'archive | **Oui** |
| Varet (livecam) | Brouillard ce jour | — | À revoir |

**Proposition :** jeu de référence sur **Arcabulle, Mont-Blanc et Grizzly**, environ 50 images chacune, avec Varet en réserve. Ce sont des panoramas de 600 px de haut : les personnes y feront de 5 à 40 px. C'est le risque principal de la baseline, à mesurer dès l'étape 1.5 (640 px, 1280 px, tuiles).

**Pas encore vérifié :** la présence de foule dans l'archive de février. Le calendrier du lecteur officiel ne répond pas à mes clics : il faut regarder à la main un samedi des vacances (par exemple le 14/02/2026, vers 11 h).

### 2026-11-18 · Étape 1.1 close
- **Caméras retenues** (→ [0022](decisions/0022-jeu-de-reference-archive-des-arcs.md)) : Arcabulle, Mont-Blanc, Grizzly ; Varet en réserve. Image témoin choisie par Romuald : **14/02/2026 à 12 h 05**.
- **Critère de passage de 1.1 :** atteint. Il y a une source utilisable dans le cadre pédagogique (fiche 0021), sur 3 caméras, avec la saison 2025-2026 complète.
- **Vidéo :** après la baseline sur images (le suivi dépend du détecteur). Sources repérées dans [sources.md](sources.md) § 3 bis : MOT17 / MOT20 pour mesurer le suivi, extraits Pexels pour notre contexte.

**Étape suivante : 1.2, figer le jeu de référence.** Il faut d'abord écrire la grille des strates (caméra × moment × météo × affluence) et la règle anti-doublons, avant de choisir la moindre image.

---

## Étape 1.2 · Figer le jeu de référence : protocole (écrit le 18/11/2026, avant tout choix d'image)

**Hypothèse :** 150 images tirées au hasard dans des strates définies à l'avance représentent la saison. Elles permettent de mesurer l'erreur de comptage sans biais de sélection : personne ne choisit de « belles » images.

**Le tirage** (`configs/reference_lesarcs.json` → `data/reference/sampling_plan.csv`, graine 20261118, reproductible) :
- **Période :** saison 2025-2026, du 13/12/2025 au 25/04/2026 🔎 (clôture annoncée le 25 ou le 26/04 selon les sources).
- **3 caméras × 50 images**, plus 10 images de réserve par caméra :

| Strate | Par caméra | Définition (indicateur de calendrier, contrôlé ensuite par les comptages) |
|---|---|---|
| Affluence haute | 14 | Deux zones scolaires en vacances en même temps : 27/12 → 03/01 et 14/02 → 01/03 |
| Affluence moyenne | 13 | Autres jours de vacances (toutes zones) et week-ends hors vacances |
| Affluence basse | 13 | Jours de semaine hors vacances |
| Nuit (hors exploitation) | 5 | 22 h → 5 h : scène vide, pour mesurer les **fausses détections** |
| Crépuscule (hors exploitation) | 5 | 7 h 30 → 8 h 45 et 17 h → 18 h 30 : faible lumière |

- **Moments :** matin (9 h → 11 h), midi (11 h → 14 h), après-midi (14 h → 16 h 30), répartis à parts égales dans chaque niveau d'affluence. L'heure est tirée au hasard dans la plage, au pas de 5 min.
- **Une seule image par jour et par caméra :** deux images d'une même journée se ressemblent trop.
- **Vacances scolaires 2025-2026 :** jeu de données officiel du ministère (data.education.gouv.fr), consulté le 18/11/2026 ✅. Noël : 20/12 → 04/01, toutes zones. Hiver : A 07/02 → 22/02, B 14/02 → 01/03, C 21/02 → 08/03. Printemps : A 04/04 → 19/04, B 11/04 → 26/04, C 18/04 → 03/05.

**La collecte (à la main, dans le lecteur officiel, fiche 0021) :**
1. Pour chaque ligne du plan : ouvrir la caméra à la date indiquée et prendre l'image **la plus proche de l'heure cible**.
2. L'enregistrer dans `data/reference/images/` sous le nom `<slot_id>_<AAAAMMJJ>-<HHMM>.jpg`, avec l'heure réelle de l'image. Exemple : `ARC-04_20251227-1230.jpg`.
3. **Image absente** (caméra en panne, givrée, archive vide) : noter le créneau comme absent et prendre la **réserve suivante de la même caméra**.
4. Renseigner la **météo** dans le manifeste : `beau`, `couvert`, `neige-brouillard` ou `nuit`.
5. Lancer `python -m flowview.reference.manifest data/reference/sampling_plan.csv data/reference/images data/reference/manifest.csv`. Le script calcule les empreintes (SHA-256, empreinte de ressemblance), signale les noms non conformes et les **quasi-doublons**, puis affiche la couverture par strate.

**Règle anti-doublons :** deux images d'une même caméra dont les empreintes de ressemblance diffèrent de 10 bits ou moins sur 128 sont des quasi-doublons. La seconde est remplacée par une réserve. Les images de nuit sont exemptées, puisqu'elles se ressemblent par nature. Le seuil de 10 bits est à calibrer sur les premières images 🔎.

**Critère de passage :**
- les 150 créneaux sont couverts (réserves comprises) ;
- au moins 10 images par strate (caméra × affluence, moment, météo) ;
- aucun quasi-doublon ;
- `manifest.csv` est commité.

**À partir de ce commit, le jeu ne bouge plus.**

**L'image témoin du 14/02/2026 à 12 h 05** (choisie par Romuald) **n'entre pas** dans le jeu, puisqu'elle a été choisie à la main. Elle peut servir d'exemple dans le guide de comptage (étape 1.4).

**Note :** les créneaux « crépuscule » ont une plage horaire fixe. Fin décembre, 18 h est déjà la nuit. La strate se lira donc comme « hors exploitation, lumière faible ou nulle », et la météo réelle sera notée à la main.

### 2026-11-18 · Étape 1.2, plan révisé avant collecte
Romuald veut plus d'images, pré-annotées par un modèle et corrigées par lui (→ [0025](decisions/0025-pre-annotation-et-taille-du-jeu.md)), avec une collecte scriptée (→ [0024](decisions/0024-collecte-scriptee-adresses-du-lecteur.md)). Le plan est régénéré, même graine, **aucune image encore collectée** :
- **Référence : 3 × 80**. Par caméra : haute 22, moyenne 21, basse 21, nuit 8, crépuscule 8, plus 15 de réserve.
- **Contrôle : 3 × 10** sur Varet, Arpette et Aiguille Rouge (haute 4, moyenne 3, basse 3), plus 5 de réserve chacune. Il est rapporté à part et n'entre pas dans le critère de passage.
- **Critère de passage de 1.2 mis à jour :** les 240 créneaux de référence sont couverts, avec au moins 10 images par strate et aucun quasi-doublon.
- **Étape 1.4 :** pré-annotation par un modèle plus fort que la baseline, correction dans CVAT, et 24 images comptées d'abord à l'aveugle pour mesurer le biais d'ancrage (critère : écart moyen ≤ 1 personne).

### 2026-11-18 · Étape 1.2, collecte
- **Adresses :** Romuald a ouvert le 14/02/2026 dans le lecteur. Le lecteur charge un index du jour qui liste des images à adresse publique simple (fiche 0024, vérification).
- **Script :** `flowview/reference/collect.py`, avec 10 tests ; il ne demande que les créneaux du plan et attend 5 s entre deux requêtes.
- **Résolution :** les images d'archive font **18 543 × 3 953 px**, contre 600 px de haut en direct. Sur ARC-02 (14/12/2025, 10 h 10), des dizaines de skieurs sont nettement visibles autour de la gare.
- **Hypothèse :** la difficulté du comptage viendra moins de la taille des silhouettes que de leur nombre et de leur densité près des gares. Elle sera mesurée en 1.5.
- **Collecte complète lancée :** 270 créneaux, soit 240 de référence et 30 de contrôle.
