# Veille technique — FlowView · Place Publique

*Compte rendu illustré et référencé des 8 questions du sujet. Chaque question a **un auteur qui la rédige et la défend** à la soutenance (au moins 2 par personne). Répartition proposée dans `docs/plan.md` (§4).*

**Règles de rédaction**
- Un **tableau comparatif** vaut mieux qu'un long paragraphe.
- Des **sources primaires et datées** (articles de recherche, documentation officielle, textes de loi, CNIL, CEPD) ; un blog seulement en complément.
- Distinguer ce qui est **mesuré** (chiffres, benchmarks avec leur source) de ce qui est **affirmé**.
- Finir chaque question par **« Ce qu'on en retient pour FlowView »** : la décision ou la conséquence concrète dans notre projet.
- Pas de copier-coller : on reformule et on cite.

| Q | Thème | Auteur | Palier | État |
|---|---|---|---|---|
| [Q1](#q1) | Modèles de détection : vitesse, précision, ressources | Olivier | 1 | à faire |
| [Q2](#q2) | Évaluer un détecteur sur caméras fixes ; mAP ≠ comptage | Olivier | 1 | à faire |
| [Q3](#q3) | Datasets, annotation, augmentation, adaptation de domaine | Olivier | 1 | à faire |
| [Q4](#q4) | Architectures flux → inférence → base → front | Romuald | 2 | à faire |
| [Q5](#q5) | MLOps : MLflow, CI/CD, versioning, tests | Olivier | 3 | à faire |
| [Q6](#q6) | Dérive de données et de concept, ré-entraînement | Olivier | 3 | à faire |
| [Q7](#q7) | RGPD et AI Act appliqués au comptage vidéo | Romuald | 3 | à faire |
| [Q8](#q8) | Enjeux éthiques du comptage dans l'espace public | Romuald | 3 | à faire |

---

<a id="q1"></a>
## Q1 · Quels modèles de détection pour la vidéosurveillance, et quels compromis ?
*Auteur : · Dernière mise à jour :*

> Quels sont aujourd'hui les principaux modèles de détection d'objets utilisés en vidéosurveillance (YOLO, Faster R-CNN, DETR…) et quels compromis font-ils entre vitesse, précision (mAP) et ressources sur du matériel limité ?

**Réponse courte** (3 à 5 lignes) :

| Modèle | Famille | mAP COCO (source, date) | Vitesse (matériel) | Taille | Licence | Pour FlowView ? |
|---|---|---|---|---|---|---|
| | | | | | | |

**Ce qu'on en retient pour FlowView :**

**Sources :**

---

<a id="q2"></a>
## Q2 · Évaluer rigoureusement un détecteur sur caméras fixes
*Auteur : · Dernière mise à jour :*

> Comment évaluer rigoureusement un modèle de détection sur des caméras fixes (mAP, précision/rappel par classe, IoU, analyse d'erreurs), et pourquoi un bon mAP ne garantit-il pas un bon comptage ?

**Réponse courte :**

| Métrique | Ce qu'elle mesure | Ce qu'elle cache | Utile pour nous ? |
|---|---|---|---|
| mAP@0.5 / mAP@0.5:0.95 | | | |
| Précision / rappel par classe | | | |
| Erreur absolue moyenne du comptage (MAE) | | | |
| Biais (sur / sous-comptage) | | | |

**Exemple chiffré tiré de notre jeu de référence :** *(lien vers `notebooks/01_baseline.ipynb`)*

**Ce qu'on en retient pour FlowView :**

**Sources :**

---

<a id="q3"></a>
## Q3 · Datasets, annotation, augmentation, adaptation de domaine
*Auteur : · Dernière mise à jour :*

> Comment sélectionner, combiner et annoter des datasets pour couvrir la variété des contextes clients, et quelles augmentations ou adaptations de domaine (météo, saison, angle, résolution) améliorent la robustesse ?

**Réponse courte :**

| Dataset / outil | Contenu | Licence | Pertinence (station, neige, foule) |
|---|---|---|---|
| | | | |

| Augmentation / adaptation | Ce qu'elle simule | Mesure concrète (au moins deux) |
|---|---|---|
| | | |

**Ce qu'on en retient pour FlowView :**

**Sources :**

---

<a id="q4"></a>
## Q4 · Relier flux vidéo, inférence, base temporelle et front
*Auteur : · Dernière mise à jour :*

> Quelles architectures relient flux vidéo, service d'inférence, base temporelle et frontend (batch périodique ou quasi temps réel, microservices, file de messages), et avec quels effets sur la scalabilité et la tolérance aux pannes ?

**Réponse courte :**

**Schéma de notre architecture** *(image ou diagramme, avec ses limites)* :

| Option | Principe | Scalabilité | Tolérance aux pannes | Coût / complexité |
|---|---|---|---|---|
| Batch périodique (notre choix) | | | | |
| Quasi temps réel (flux) | | | | |
| Microservices + file de messages | | | | |

**Ce qu'on en retient pour FlowView :**

**Sources :**

---

<a id="q5"></a>
## Q5 · MLOps : un cycle de vie maîtrisé du modèle
*Auteur : · Dernière mise à jour :*

> Quels outils et pratiques MLOps (MLflow, CI/CD, versioning de modèles, tests) assurent un cycle de vie maîtrisé du modèle, de l'expérimentation au déploiement reproductible ?

**Réponse courte :**

| Étape | Outil | Ce qu'on a vraiment fait dans le projet (lien) |
|---|---|---|
| Suivi d'expériences | MLflow | |
| Versioning du modèle | | |
| Tests | pytest | |
| CI / CD | GitHub Actions, ghcr.io | |

**Ce qu'on en retient pour FlowView :**

**Sources :**

---

<a id="q6"></a>
## Q6 · Détecter la dérive et déclencher un ré-entraînement
*Auteur : · Dernière mise à jour :*

> Quels signaux détectent la dérive de données ou de concept dans un système de comptage, et comment déclencher un ré-entraînement pertinent ?

**Réponse courte :**

| Signal | Comment le calculer | Seuil proposé | Ce qu'il révèle |
|---|---|---|---|
| Distribution des scores de confiance | | | |
| Taux de détection par heure vs historique | | | |
| Part de « pas de donnée » | | | |
| Retour utilisateur | | | |

**Déclencheurs de ré-entraînement :**

**Ce qu'on en retient pour FlowView :**

**Sources :**

---

<a id="q7"></a>
## Q7 · RGPD et AI Act appliqués au comptage par vidéo
*Auteur : · Dernière mise à jour :*

> Comment le RGPD et l'AI Act qualifient-ils un système de comptage par vidéo, quelles obligations en découlent (base légale, AIPD, transparence) et quelles pratiques techniques (agrégation, absence de stockage vidéo) aident à rester conforme ?

**Réponse courte :**

| Texte (date) | Ce qu'il dit pour un comptage agrégé | Obligation pour nous |
|---|---|---|
| RGPD | | |
| Position CNIL sur les caméras « augmentées » | | |
| CEPD, lignes directrices 3/2019 | | |
| Règlement (UE) 2024/1689 (AI Act) | | |

**Notre qualification (démontrée, pas affirmée) :**

**Ce qu'on en retient pour FlowView :**

**Sources :**

---

<a id="q8"></a>
## Q8 · Les enjeux éthiques du comptage automatisé dans l'espace public
*Auteur : · Dernière mise à jour :*

> Quels sont les enjeux éthiques du comptage automatisé dans l'espace public (surveillance de masse, biais, réutilisation des données) et quelles mesures de conception les limitent ?

**Réponse courte :**

| Risque | Exemple concret | Mesure de conception dans FlowView |
|---|---|---|
| Glissement vers la surveillance | | |
| Biais de détection | | |
| Réutilisation des données | | |

**Notre position argumentée** (pas un catalogue de risques) :

**Sources :**
