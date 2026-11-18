# 0022 — Jeu de référence tiré de l'archive des Arcs ; la vidéo vient après

- **Date :** 2026-11-18
- **Statut :** Acceptée
- **Décideurs :** Romuald
- **Remplace :** [0016](0016-sources-de-donnees-en-trois-temps.md) (le premier temps, « jeux de données publics », n'est plus la source du jeu de référence)

## Contexte
La fiche 0016 prévoyait de bâtir le jeu de référence à partir de jeux publics, faute de foule aux Arcs avant le 12/12. Deux faits nouveaux :
- Les webcams des Arcs ont une **archive quotidienne depuis le 01/10/2025** ✅, donc toute la saison dernière.
- Les jeux « skieurs » publics sont surtout des plans serrés de course 🔎, loin d'une vue de webcam.

Romuald a ouvert l'archive au **14/02/2026 à 12 h 05** (samedi des vacances d'hiver) comme image témoin.

Romuald demande aussi des tests sur de la **vidéo**, pour le suivi des personnes (fiche [0019](0019-socle-periodique-puis-temps-reel.md)).

## Décision
1. **Jeu de référence (images fixes) :** environ 150 images de l'archive 2025-2026 des webcams **Arcabulle, Mont-Blanc et Grizzly** (environ 50 chacune), avec Varet en réserve. Elles sont réparties par moment de la journée, météo et affluence (étape 1.2 du [palier 1](../palier-1.md)). L'usage est pédagogique, avec garde-fous (fiche [0021](0021-webcams-usage-pedagogique-sans-autorisation.md)).
2. **Validation terrain :** une station déjà ouverte (Val Thorens, à partir du 21/11) reste le deuxième temps, en jeu séparé. Le jeu de référence, lui, ne bouge plus.
3. **Vidéo et suivi :** **après** la baseline sur images, pas en parallèle. Le suivi s'appuie sur le détecteur, il ne peut pas être meilleur que lui. Seule la recherche de sources vidéo se prépare en parallèle (voir [sources.md](../sources.md) § Vidéo).
4. Les jeux publics ne servent plus qu'en complément : fine-tuning éventuel, météo rare.

## Options écartées
- **Jeux publics comme jeu de référence :** pas « notre contexte », alors que le sujet l'exige.
- **Images et vidéo en parallèle :** deux évaluations à construire en même temps, alors que la seconde dépend de la première.

## Conséquences
- Le risque n° 1 (pas de foule avant le 12/12) est levé pour le palier 1.
- **Nouveau risque :** les panoramas font 600 px de haut, donc les personnes y font de 5 à 40 px. C'est à mesurer dès la baseline (640 px, 1280 px, tuiles).
- Il faudra une vérité terrain spécifique à la vidéo (passages comptés à la main sur des extraits) et des mesures de suivi (HOTA, IDF1, erreur sur les passages).

## Sources
- Lecteur officiel webcam-hd : <https://app.webcam-hd.com/lesarcs/arcabulle> (liste des dates d'archive relevée le 17/11/2026).
- Zhang et al., *ByteTrack*, ECCV 2022 : <https://arxiv.org/abs/2110.06864>
