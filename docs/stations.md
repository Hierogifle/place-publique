# Fiche stations — tout savoir pour adapter FlowView

*Version 1 · 2026-11-17 · ✅ vérifié (source citée) · 🔎 supposé ou sources divergentes, à confirmer auprès de l'exploitant.*
*Sert à : choisir les zones à surveiller, régler la normale de l'heure, répondre aux questions du jury sur le terrain.*

---

## 1. Les Arcs (client de démonstration)

### L'essentiel
| Élément | Valeur | Fiabilité |
|---|---|---|
| Commune | Bourg-Saint-Maurice (Savoie, Tarentaise) | ✅ |
| Villages-stations | Arc 1600, Arc 1800, Arc 1950, Arc 2000 (+ Peisey-Vallandry, Villaroger sur le même domaine) | ✅ (OpenStreetMap) |
| Point culminant | Aiguille Rouge, 3 226 m | ✅ (guide-ski, Skiinfo) |
| Domaine Les Arcs / Peisey-Vallandry | ≈ 200 km de pistes | ✅ (Compagnie des Alpes, guide-ski) |
| Pistes | 123 (Skiinfo) ; d'autres sources comptent autrement | 🔎 |
| Remontées mécaniques | 52 ou 53 (Skiinfo, guides) ; 85 si l'on compte plusieurs domaines (Alti-Mag) ; **65 tracés** dans notre zone de maquette (OpenStreetMap, 17/11/2026) | 🔎 |
| Surface skiable | 518 ha | 🔎 (Skiinfo) |
| Domaine relié | **Paradiski** (Les Arcs + La Plagne) : ≈ 425 km, reliés par le téléphérique Vanoise Express | ✅ |
| Exploitant | **ADS** (Arcs Domaine Skiable), filiale de la **Compagnie des Alpes** | ✅ (compagniedesalpes.com) |
| Accès depuis la vallée | Funiculaire Bourg-Saint-Maurice → Arc 1600 (gare SNCF à Bourg-Saint-Maurice) | ✅ (guide-ski) |
| Lits touristiques | ≈ 32 900 | 🔎 (Alti-Mag, seule source) |
| Hébergement | Surtout de grandes résidences (architecture des années 1970-80), plus chalets et hôtels | ✅ (mon-sejour-en-montagne) |

### La saison 2026-2027
| Repère | Date | Fiabilité |
|---|---|---|
| Ouverture du domaine | **samedi 12 décembre 2026** | ✅ (lesarcs.com, Skiinfo) |
| Fermeture | 24 avril 2027 (Les Arcs) ; Vanoise Express jusqu'au 17 avril 2027 | ✅ (guide-ski) |
| Durée | ≈ 19 semaines | calcul |
| Horaires des remontées | Non publiés dans les sources trouvées ; varient selon les secteurs et la période | 🔎 à demander à l'exploitant (Skiinfo : +33 4 79 07 12 57) |

### Les webcams
| Caméra | Où | Format | Usage possible |
|---|---|---|---|
| Vagère (Arc 1800) | Départ de télésiège | Live YouTube, 1280 × 720, horodaté | **Départ de remontée, distance moyenne** : la meilleure candidate pour une file ✅ (vue le 17/11) |
| Arcabulle (Arc 1800 selon lesarcs.com) | Panoramique | JPG rafraîchi (trinum), 2815 × 600 | Personnes très petites : à tester ✅ |
| Arpette, Aiguille Rouge, Mont-Blanc, Varet (Arc 2000) | Sommets et panoramas | JPG rafraîchis (trinum) | Météo et neige plutôt que comptage |
| Grizzly (Peisey-Vallandry) | — | JPG (webcam-hd) | À regarder |
| Place Manoir, Horloge, Clocher (Arc 1950) | **Place du village** | Sur le site d'Arc 1950 (lecteur JS) | **Comptage piétons sur une place** : à tester 🔎 |
| Livecam Arc 2000, Livecam Varet | — | Live YouTube | À regarder |

**Conditions d'utilisation des webcams : non lues à ce jour** (lesarcs.com, trinum, webcam-hd, arc1950.com). À faire avant toute capture. Récupérer un live YouTube avec un outil tiers est probablement contraire aux conditions de YouTube 🔎. Ne jamais versionner d'image brute.

### Ce que ça change pour FlowView (hypothèses à valider avec un exploitant)
- **Le samedi est le jour des arrivées et des départs** des locations à la semaine 🔎 : affluence au funiculaire et aux départs le matin, pistes plus calmes. La normale doit être calculée **par jour de la semaine**, pas seulement par heure.
- **Vacances scolaires** (zones A, B, C, open data ✅) : facteur n°1 de l'affluence ; à afficher dans le point du matin.
- **Pics horaires probables** 🔎 : ouverture des remontées (première montée), fin de matinée aux départs des secteurs hauts, retour en fin d'après-midi vers les villages.
- **Météo** : vent ou mauvaise visibilité = remontées d'altitude fermées et report sur les secteurs bas ; à noter dans l'historique, pas à prédire.
- **Les places de village** (Arc 1950) se remplissent surtout le midi et en fin de journée 🔎.

---

## 2. Brides-les-Bains (plan B, non retenu)

| Élément | Valeur | Fiabilité |
|---|---|---|
| Type | Station thermale à ≈ 600 m, Tarentaise | ✅ (les3vallees.com) |
| Domaine | Accès au domaine des **3 Vallées** (Méribel) par la télécabine de l'Olympe | ✅ |
| Webcams | 7 sur le site des 3 Vallées, dont 1 seule au village (« Centre village », vue plongeante lointaine) | ✅ (vue le 17/11) |
| Pourquoi pas retenue | Aucune caméra trouvée sur la file de l'Olympe ; contexte différent des Arcs (station thermale) | fiche [0003](decisions/0003-station-les-arcs.md) |

---

## 3. La station « production » pour les tests (avant le 12/12)

Rappel de la décision [0016](decisions/0016-sources-de-donnees-en-trois-temps.md) : tester le service sur une station déjà ouverte, puis brancher Les Arcs.

| Station | Ouverture annoncée 2026-2027 | Webcams repérées | Fiabilité |
|---|---|---|---|
| **Val Thorens** (3 Vallées) | 21 novembre 2026 | Page officielle des 3 Vallées ; une caméra « Rond-point des pistes » montre le **front de neige animé** et les départs (Portette, Funitel de Thorens) | ouverture 🔎 (dépend de la neige) ; webcams ✅ à vérifier une par une |
| **Tignes** | 21 ou 23 novembre 2026 selon les sources | À chercher | 🔎 |
| Val d'Isère, Les 2 Alpes | 28 novembre 2026 | À chercher | 🔎 |

**Recommandation :** Val Thorens en premier (ouverture la plus tôt, caméra de front de neige identifiée, même massif que Les Arcs).

---

## 4. Sources
- Les Arcs, chiffres et saison : https://guide-ski.fr/stations-de-ski-france/les-arcs-hiver-guide-ski-pistes-forfaits/ · https://www.skiinfo.fr/alpes-du-nord/les-arcs-bourg-st-maurice/forfaits-de-ski · https://www.alti-mag.com/stations/les-arcs · https://www.alti-mag.com/domaines-skiables/paradiski
- Exploitant : https://compagniedesalpes.com/en/les-marques/les-arcs · https://www.lesarcs-peiseyvallandry.com/en/le-domaine-de-montagne
- Accès, funiculaire, piétons : https://guide-ski.fr/?p=10776
- Hébergement : https://www.mon-sejour-en-montagne.com/station/arc2000/
- Webcams Les Arcs : https://www.lesarcs.com/fr/livecams-et-webcams · https://arc1950.com/en/les-webcams-arc-1950-1445
- Brides-les-Bains : https://www.les3vallees.com/en/live/webcams-brides-les-bains
- Val Thorens : https://www.les3vallees.com/en/live/webcams-val-thorens · https://www.alti-mag.com/guide-stations-de-ski-alpes/webcam-alpes-du-nord/webcam-val-thorens
- Ouvertures 2026-2027 : https://guide-ski.fr/?p=4038
- Vacances scolaires (open data) : https://data.gouv.fr/en/datasets/le-calendrier-scolaire
- Remontées et pistes : © contributeurs OpenStreetMap (ODbL), extraction Overpass du 17/11/2026
