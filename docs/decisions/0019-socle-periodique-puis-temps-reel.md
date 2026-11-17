# 0019 — Socle périodique d'abord, mode « direct » avec suivi ensuite

- **Date :** 2026-11-17
- **Statut :** Acceptée
- **Décideurs :** Romuald

## Contexte
Romuald avait compris le projet comme une analyse en temps réel, avec suivi des personnes d'une image à l'autre (tracking), sur toutes les caméras, à 10, 30 ou 50 images par seconde selon le modèle et la carte graphique. Il préfère cette approche.

Ce que dit le sujet (`sujet/Place_Publique_V2.docx`, relu le 17/11) ✅ :
- « Le système analyse les flux à périodicité régulière (par exemple toutes les 5 minutes) ».
- « l'objectif est un dénombrement à gros grain à des fins statistiques, pas une détection parfaite ».
- Palier 2 : le service « lit périodiquement une image », à « intervalle configurable (cron, APScheduler…) » ; validation par une série d'au moins 48 points produite par un script de rejeu.
- Le tracking n'apparaît nulle part, pas même dans « Pour aller plus loin ». Les extensions ne comptent que si les trois paliers sont validés.

Ce que le temps réel apporte : le **flux** (passages par minute, débit d'un départ de remontée), qu'une image toutes les 5 minutes ne peut pas mesurer (occupation ≠ flux, voir [sujet-recap.md](../sujet-recap.md)).

## Décision
1. **D'abord le socle demandé par le sujet** : capture périodique à intervalle configurable (jusqu'à quelques secondes), comptage, SQLite, « pas de donnée », rejeu. C'est lui qui valide les paliers.
2. **Ensuite, en extension**, un **mode « direct »** sur les caméras choisies : détection et suivi image par image sur le GPU de Romuald, affichage en direct avec les personnes floutées sous leurs cadres. **C'est l'objectif final, pas une option** : Romuald vise la version la plus ambitieuse du projet comme point d'arrivée (« on part sur le plus ambitieux… je veux bien dire la fin »), avec autant de caméras que la carte le permet, à la cadence la plus haute possible (10, 30 ou 50 images par seconde selon le modèle).
3. **Le chemin pour y arriver est granulaire, méthodique et scientifique** : une étape à la fois, chacune avec une hypothèse, une mesure et un critère de passage écrits avant de commencer. Pas d'étape suivante tant que la précédente n'est pas mesurée. L'ordre : les trois paliers du sujet ; puis 1 caméra en direct ; puis 2 ; puis la montée en charge.
4. Le mode direct **n'enregistre que des agrégats** (passages par minute, occupation moyenne) ; les identifiants de suivi restent en mémoire et ne sont jamais stockés ni affichés.
5. Le même service de détection sert les deux modes : rien n'est jeté.

## Options écartées
- **Temps réel et suivi au cœur du projet** : hors de ce que le sujet note ; risque de ne pas valider le palier 2 dans les temps ; démo dépendante d'une carte graphique.
- **Périodique seulement** : conforme au sujet, mais renonce à mesurer le flux, qui intéresse le plus un exploitant de remontées.

## Conséquences
- **Source vidéo** : la meilleure caméra des Arcs pour une file (Vagère) est un live YouTube ; le lire avec un outil tiers est probablement contraire aux conditions de YouTube 🔎. Il faut trouver un flux lisible par OpenCV (RTSP / HLS) autorisé, ou faire le mode direct sur une vidéo libre de droits en rejeu.
- **RGPD** : le suivi crée des trajectoires individuelles, même anonymes et brèves. C'est plus intrusif qu'un comptage : à traiter à part dans l'AIPD de `conformite.md` (veille Q7).
- **Docker** : l'image livrée reste sur CPU (idée I-08) ; le mode direct tourne sur CPU à cadence réduite, ou en GPU si la machine en a une (profil Docker séparé 🔎).
- **Démo** : toujours sur le rejeu ; le mode direct se montre en bonus, avec une vidéo de secours.

## Sources
- Sujet `Place_Publique_V2.docx` : contexte, « À retenir », palier 2, « Pour aller plus loin ».
- Suivi d'objets intégré à Ultralytics (BoT-SORT, ByteTrack) : <https://docs.ultralytics.com/modes/track/>
- Zhang et al., *ByteTrack: Multi-Object Tracking by Associating Every Detection Box*, ECCV 2022 : <https://arxiv.org/abs/2110.06864>
