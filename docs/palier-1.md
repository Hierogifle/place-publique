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
