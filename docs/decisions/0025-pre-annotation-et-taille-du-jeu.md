# 0025 — Jeu de 3 × 80 images plus un contrôle ; vérité terrain pré-annotée puis corrigée dans CVAT

- **Date :** 2026-11-18
- **Statut :** Acceptée
- **Décideurs :** Romuald
- **Modifie :** [0023](0023-tirage-stratifie-du-jeu-de-reference.md) (quotas par caméra)

## Contexte
Romuald veut plus d'images, sans y passer ses journées : un modèle propose les cadres, lui vérifie et corrige. Il demande aussi de ne pas oublier les 3 autres webcams, et de ne pas installer « 30 trucs ».

## Décision
1. **Jeu de référence : 3 × 80 images** (Arcabulle, Mont-Blanc, Grizzly), toutes annotées.
   - Quotas par caméra : affluence haute 22, moyenne 21, basse 21, nuit 8, crépuscule 8 ; 15 images de réserve.
   - Le plan est régénéré avec la même graine, **avant toute collecte**.
2. **Jeu de contrôle : 3 × 10 images** sur Varet, Arpette et Aiguille Rouge, avec 5 de réserve chacune. Il sert à vérifier que le modèle tient sur des caméras non étudiées. Il ne sert pas à fixer le seuil.
3. **Pré-annotation** par un modèle **différent et plus fort** que celui qu'on évalue : un grand modèle, en haute résolution et par tuiles. Ce n'est **pas** le YOLO26n de la baseline. Romuald vérifie chaque image : il supprime les faux cadres, ajuste les autres, et **balaie tout le panorama** pour ajouter les personnes oubliées.
4. **Mesure du biais d'ancrage :** 24 images, soit 10 % tirées au sort, sont d'abord comptées **sans pré-annotation**, puis corrigées à partir des cadres du modèle, un autre jour. L'écart moyen entre les deux comptages dit à quel point la pré-annotation influence la vérité terrain.
   - Critère : écart ≤ 1 personne en moyenne. Sinon, on ne garde pas la pré-annotation telle quelle.
5. **Outil : CVAT** (licence MIT), lancé avec Docker. Docker est déjà installé et requis par le projet. CVAT sert aux images maintenant et **au suivi vidéo plus tard**, avec annotation de pistes et interpolation. Un seul outil pour tout le projet.

## Options écartées
- **6 × 50 :** Arpette et Aiguille Rouge sont souvent givrées ou vides, et noieraient l'erreur.
- **Pré-annoter avec le modèle évalué :** la vérité terrain hériterait de ses oublis, et l'erreur serait sous-estimée.
- **Label Studio :** plus léger, mais moins bon en vidéo, il faudrait un second outil au moment du suivi.
- **LabelImg :** archivé, il n'est plus maintenu.

## Conséquences
- Charge de vérification estimée : 270 images à 1 à 3 min chacune, soit **5 à 13 h**, plus 24 comptages à l'aveugle. À répartir sur plusieurs sessions.
- **Le GPU** (RTX 5060 portable, 8 Go) sert à la pré-annotation. Il ne sert ni à la baseline livrée ni à la CI (idée I-08).
- Le critère de l'étape 1.4 devient : 270 images annotées, et biais d'ancrage mesuré.

## Sources
- CVAT : <https://github.com/cvat-ai/cvat> (MIT)
- LabelImg, dépôt archivé : <https://github.com/HumanSignal/labelImg>
