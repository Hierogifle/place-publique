# Évaluation du comptage — seuil d'acceptabilité

*Étape 1.3 du [palier 1](palier-1.md). **Ce document doit être validé et commité avant le premier lancement d'un modèle sur le jeu de référence.** L'horodatage Git prouve que le seuil n'a pas été ajusté aux résultats.*

> **Statut : VALIDÉ par Romuald le 18/11/2026**, avant tout lancement de modèle sur le jeu de référence (fiche [0026](decisions/0026-seuil-d-acceptabilite.md)). **Complété le 18/11/2026**, toujours avant tout modèle, par les 8 classes et les seuils par classe S6 et S7 (fiche [0027](decisions/0027-huit-classes-et-seuils-par-classe.md)).

## 1. L'usage, d'où vient le seuil
FlowView sert à l'exploitant à **décider** : ouvrir ou renforcer une remontée, envoyer du personnel, prévenir les pisteurs. Il ne sert pas à facturer à la personne près. L'écran montre :
- un **niveau d'affluence** par zone (calme, habituel, chargé, très chargé), comparé à « d'habitude à cette heure » ;
- une **alerte** quand une zone dépasse nettement sa normale.

Ce qui compte donc :
1. **Que l'erreur ne fasse pas sauter un niveau.** Une zone « chargée » ne doit pas apparaître « calme ».
2. **Qu'il n'y ait pas de sous-comptage systématique dans les foules.** C'est là que l'alerte doit partir, et un biais vers le bas la ferait manquer (veille Q2).
3. **Qu'une scène vide reste vide.** Une fausse foule la nuit détruirait la confiance, et le « chiffre honnête » est un engagement de la marque.

Le sujet le dit lui-même : « compter 40 piétons au lieu de 50 suffit pour dimensionner un accueil, pas pour déclencher une alerte sécurité ». FlowView n'est **pas** un outil de sécurité : l'alerte informe un humain, elle ne commande rien (fiche [0019](decisions/0019-socle-periodique-puis-temps-reel.md), veille Q7).

## 2. Classes
Le sujet demande de compter **2 à 10 classes** selon le contexte du client. On en compte **8** (fiche [0027](decisions/0027-huit-classes-et-seuils-par-classe.md)).

| Classe | Ce qu'elle couvre | Comment le modèle de départ (COCO) la produit |
|---|---|---|
| `skieur` | Personne avec des skis aux pieds, y compris assise sur une remontée | `person` dont le cadre recouvre un cadre `skis` |
| `snowboardeur` | Personne avec un snowboard aux pieds | `person` dont le cadre recouvre un cadre `snowboard` |
| `pieton` | Personne à pied (chaussures de ski, skis portés, raquettes, tenue de ville) | `person` sans skis ni snowboard associés |
| `voiture` | Voiture de tourisme | `car` |
| `camion` | Utilitaire, camion | `truck` |
| `bus` | Navette, car, bus | `bus` |
| `engin_neige` | Dameuse, motoneige, quad | **Aucune classe COCO** : fine-tuning nécessaire, autorisé par le sujet pour une classe manquante |
| `animal` | Chien surtout | `dog` (et `cat`, `horse` si présents) |

- **Total des personnes** = skieur + snowboardeur + piéton. C'est le chiffre qui décide, jugé par S1 à S5.
- **La classe dit ce que fait la personne, pas ce qu'elle porte.** L'attribut `tenue` (ski / ville) sert à l'analyse d'erreurs et au biais de détection (veille Q8), pas au comptage.
- **Pas de classe d'âge ni de genre.** C'est de la segmentation démographique, refusée dans la veille (Q8) et dans la conformité. Elle rapprocherait aussi le système de la catégorisation biométrique de l'AI Act.
- `skis` et `snowboard` (COCO) ne sont pas comptés pour eux-mêmes : ils servent à classer les personnes.

## 3. Le seuil sur le total des personnes (skieur + snowboardeur + piéton, jeu de référence, 240 images)

| # | Mesure | Sur quelles images | Seuil | Pourquoi ce chiffre |
|---|---|---|---|---|
| S1 | **Erreur relative médiane** \|compté − vrai\| / vrai | Images en exploitation avec **au moins 5 personnes** | **≤ 20 %** | Valeur indicative du sujet. 20 % fait passer 50 personnes à 40 ou 60, ce qui reste dans le même niveau d'affluence si les niveaux sont espacés d'environ ×1,5 (à vérifier sur les comptages) |
| S2 | **Erreur absolue moyenne (MAE)** | Images en exploitation avec **moins de 5 personnes** | **≤ 1,5 personne** | Pour peu de monde, l'erreur relative n'a pas de sens (1 au lieu de 2 = 50 %). À ces niveaux, une ou deux personnes d'écart ne changent aucune décision |
| S3 | **Biais relatif moyen** (compté − vrai) / vrai, avec son signe | Images avec au moins 5 personnes | **entre −10 % et +10 %** | Un sous-comptage systématique ferait manquer les alertes ; un sur-comptage en créerait de fausses |
| S4 | **Erreur relative médiane, affluence haute seule** | Strate « haute », au moins 5 personnes | **≤ 25 %** | C'est la strate où l'alerte se joue. On tolère un peu plus, car les foules serrées sont plus dures, mais on la mesure à part pour ne pas la noyer dans la moyenne |
| S5 | **Fausses détections de personnes hors exploitation** | Images de nuit et de crépuscule (48) | **≤ 0,5 détection par image en moyenne** | Une scène vide doit rester presque vide. La vérité terrain compte le personnel réel (dameurs, pisteurs à pied) |

**Règles d'application :**
- Chaque mesure est donnée avec son **intervalle de confiance à 95 %** (bootstrap, 2 000 tirages). Le seuil est jugé sur la valeur mesurée ; l'intervalle est publié à côté pour qu'on sache s'il est serré ou non.
- **Les images marquées « inexploitables »** (objectif givré, image noire) sont exclues des mesures S1 à S4. Elles sont comptées à part comme « pas de donnée », jamais comme zéro.
- **Les personnes marquées « incertaines »** dans la vérité terrain donnent une fourchette. La mesure principale utilise les personnes certaines, et la fourchette est publiée.
- **La baseline passe si S1, S2, S3 et S5 sont tenus.** S4 est **bloquant pour l'alerte** : si S4 échoue, l'alerte reste affichée comme « indicative » jusqu'à amélioration.
- **Le jeu de contrôle** (Varet, Arpette, Aiguille Rouge) est mesuré avec les mêmes règles. Il **ne compte pas** dans la décision : il dit si le modèle tient sur des caméras non étudiées.

### 3 bis. Seuils par classe (ajoutés le 18/11/2026, avant tout modèle)
| # | Mesure | Sur quelles images | Seuil | Pourquoi |
|---|---|---|---|---|
| S6 | **Skieur, snowboardeur, piéton, chacun à part :** erreur relative médiane | Images où la classe compte au moins 5 objets | **≤ 30 %** | Le partage pistes / à pied éclaire la décision, mais c'est le total qui décide. On tolère plus, et la confusion ski / snowboard sur des silhouettes lointaines est attendue |
| S6 bis | Même chose : erreur moyenne (MAE) | Images où la classe compte moins de 5 objets | **≤ 2** | L'erreur relative n'a pas de sens à faible nombre |
| S7 | **Voiture, camion, bus, engin de neige, animal :** MAE | Toutes les images exploitables | **≤ 1 par image** | Objets rares sur ces caméras ; un écart d'un objet ne change aucune décision |
| S7 bis | Même chose : **détection de présence** (rappel par image) | Images où la classe est présente | **≥ 80 %** | Un engin ou une navette présents doivent être vus. C'est utile pour le suivi de nuit des dameuses |

- **Une classe présente sur moins de 10 images** du jeu est déclarée **« non mesurable »**, sans chiffre inventé.
- **`engin_neige`** : la baseline COCO échoue par construction (aucune classe). L'écart avant / après fine-tuning est mesuré dans MLflow, sur ce même jeu.
- **S6 et S7 ne bloquent pas le comptage des personnes.** Une classe qui échoue est affichée comme « indicative » dans l'écran, jusqu'à amélioration.

## 4. Ce que la vérité terrain doit garantir pour que le seuil ait un sens
La précision de la vérité terrain doit être **meilleure que le seuil**. L'étape 1.4 mesure deux écarts :
- **Biais d'ancrage :** l'écart entre le comptage sans aide et le comptage corrigé après pré-annotation, sur 24 images. Critère : **≤ 1 personne en moyenne**.
- **Si l'écart dépasse 10 % sur les images à 5 personnes ou plus,** S1 (20 %) n'est plus mesurable proprement : on revoit le protocole avant de conclure.

## 5. Ce qui n'est pas jugé ici
- **Le mAP et la précision / le rappel par cadre :** calculés et publiés pour la veille Q2, mais ce n'est pas le critère d'usage.
- **Le flux (passages par minute) :** il viendra avec le mode direct et le suivi, avec son propre seuil (fiche 0019).
