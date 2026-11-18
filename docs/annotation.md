# Annotation — outil et méthode

*Outil choisi : **CVAT** (fiche [0025](decisions/0025-pre-annotation-et-taille-du-jeu.md)). Il sert aux images maintenant (vérité terrain du palier 1) et à la vidéo plus tard (pistes de suivi).*

## 1. Installation locale (faite le 18/11/2026)
- **Version :** CVAT **v2.83.0** (sortie le 12/11/2026), licence MIT. Dépôt cloné **hors du projet**, dans `M2/cvat/` : il ne fait pas partie de notre code.
- **Lancement :** Docker Compose. Toutes les images sont officielles : `cvat/server`, `cvat/ui`, `postgres`, `redis`, `traefik`, `clickhouse`, `grafana`, `vector`, `opa`, `kvrocks`.
- **Adresse :** <http://localhost:8080>, en local seulement.

Commandes (depuis le dossier `M2/cvat`) :
```bash
docker compose up -d      # démarrer
docker compose stop       # arrêter (les annotations sont conservées)
docker compose down       # supprimer les conteneurs (les volumes de données restent)
```

**Compte :** Romuald a créé son compte depuis l'interface web le 18/11/2026. C'est un compte utilisateur, suffisant pour annoter. L'agent ne choisit jamais de mot de passe. Si un compte administrateur devient nécessaire, Romuald le crée avec cette commande, dans un terminal :
```bash
docker exec -it cvat_server bash -ic "python3 ~/manage.py createsuperuser"
```

**Docker Desktop, incident du 18/11 :** une erreur « Inference manager » est apparue au démarrage. Elle venait de deux instances de Docker Desktop lancées en même temps ; le moteur est resté actif. Si elle revient, désactiver « Docker Model Runner » dans les réglages de Docker Desktop. Ce module ne sert pas au projet.

## 2. Guide de comptage (étape 1.4) — à lire avant la première image

> Validé par Romuald le 18/11/2026. Ces règles s'appliquent **à l'identique** au comptage sans aide et à la correction après pré-annotation.

### 2.1 Les 8 classes et leurs attributs
*Mise à jour du 18/11/2026 (fiche [0027](decisions/0027-huit-classes-et-seuils-par-classe.md)) : 8 classes au lieu de `person` seule. Étiquettes à coller dans CVAT : `configs/cvat_labels.json`.*

**Personnes : la classe dit ce que fait la personne, pas ce qu'elle porte.**
| Classe | Quand | Exemples |
|---|---|---|
| `skieur` | Skis **aux pieds** | Skieur sur la piste, à l'arrêt skis aux pieds, assis sur un télésiège avec ses skis |
| `snowboardeur` | Snowboard **aux pieds** (ou attaché à un pied) | Snowboardeur sur la piste, sur le télésiège |
| `pieton` | **À pied**, sans matériel de glisse aux pieds | Marche en chaussures de ski, skis portés à la main, raquettes, tenue de ville en terrasse ou au village |

| Attribut (personnes) | Valeur | Quand le changer |
|---|---|---|
| `tenue` | `ski` par défaut / `ville` | Mettre `ville` pour une tenue de ville : manteau, jean, pas de combinaison |
| `sur_remontee` | coché / non | La personne est sur un siège, dans une cabine ou sur un téléski |
| `incertain` | coché / non | Doute sur la présence (poteau, ombre, silhouette très lointaine) **ou** sur la classe. Pour du matériel de glisse dont on ne sait pas si ce sont des skis ou un snowboard : `skieur` + `incertain` |

**Véhicules, engins et animaux**
| Classe | Quand | Attribut |
|---|---|---|
| `voiture` | Voiture de tourisme | `incertain` |
| `camion` | Utilitaire, camionnette, camion | `incertain` |
| `bus` | Navette, car, bus | `incertain` |
| `engin_neige` | Dameuse, motoneige, quad | `type` (dameuse, motoneige, quad, autre) et `incertain`. **Son conducteur visible est annoté en plus**, comme `pieton` |
| `animal` | Chien surtout | `incertain` |

**Ce qu'on n'annote jamais :** reflets dans une vitre, affiches, statues, mannequins, ombres. Pas d'âge, pas de genre, aucune caractéristique de la personne au-delà de son activité et de sa tenue.

**Étiquettes d'image (une par image) :**
- `meteo` : beau, couvert, neige-brouillard ou nuit ;
- `lieu` : piste, gare-remontee, front-de-neige-terrasse ou route-village. Si plusieurs lieux sont visibles, on prend celui qui occupe le plus l'image ;
- `inexploitable` : objectif givré ou couvert, image noire ou corrompue. Dans ce cas, aucun cadre.

### 2.2 Comment parcourir une image
1. **Zoom à 100 %** ; les panoramas font environ 18 500 × 4 000 px.
2. **Balayer de gauche à droite, par bandes**, sans sauter de zone : terrasses, files, gares, pistes, et le ciel (télésièges).
3. **Bords du panorama 360° :** le bord gauche et le bord droit montrent le même endroit. Une personne coupée en deux n'est comptée **qu'une fois, sur le bord gauche**.
4. **Image inexploitable** : étiquette `inexploitable`, aucun cadre. Elle sera comptée comme « pas de donnée », jamais comme zéro.
5. **Étiquettes d'image :** `meteo` et `lieu` sur chaque image. La météo est reportée ensuite dans la colonne `weather` du manifeste.

### 2.3 Ordre des séances (pour mesurer le biais d'ancrage, fiche 0025)
1. **Séance A, sans aide :** les **24 images tirées au sort** (8 par caméra, `data/reference/blind_set.csv`), dans une tâche CVAT **sans aucun cadre pré-calculé**.
2. **Au moins un jour plus tard :** les 240 images de référence et les 30 de contrôle, avec la pré-annotation d'un modèle **plus fort que la baseline**, dans une autre tâche. On supprime les faux cadres, on ajuste, puis on balaie pour ajouter les oubliés.
3. **Comparaison automatique** des 24 images : comptage sans aide contre comptage corrigé. Critère : écart moyen ≤ 1 personne (voir [evaluation.md](evaluation.md) § 4).

### 2.4 Exports
- **CVAT :** export au format COCO, dans `data/reference/annotations/` (hors de Git, comme les images).
- **Versionné :** `data/reference/ground_truth.csv`. Par image : le nombre d'objets certains et incertains **par classe**, les personnes sur une remontée, la répartition des tenues, la météo, le lieu et l'étiquette inexploitable.

### 2.5 Exemple
L'image témoin du 14/02/2026 à 12 h 05 (hors jeu de référence, fiche 0023) sert d'exemple pour se faire la main avant la séance A. Elle n'entre dans aucune mesure.

## 3. Séance A, sans aide : mode d'emploi
**Images :** les 24 de `data/reference/blind_set.csv` (graine 20261119, 8 par caméra, hors nuit), copiées dans `data/reference/sessions/A_aveugle/` (hors de Git).

**Dans CVAT** (<http://localhost:8080>) :
1. **Projets → +** : nom `FlowView — référence`. Dans « Constructeur », onglet **Raw**, coller le contenu de `configs/cvat_labels.json`, puis valider. On obtient les 8 classes (§ 2.1) avec leurs attributs, et les étiquettes d'image `meteo`, `lieu` et `inexploitable`. **Si le projet existe déjà avec l'ancien label `person` et sans annotation, remplacer le contenu Raw par le nouveau.**
2. **Tâches → +** : nom `A — sans aide (24)`, projet `FlowView — référence`. Ajouter les 24 fichiers du dossier `A_aveugle`.
3. **Configuration avancée :** **Qualité d'image : 100**, pour voir les silhouettes lointaines sans compression. Laisser les autres réglages par défaut.
4. **Annoter** en suivant le guide (§ 2) : zoom à 100 %, bandes de gauche à droite, une étiquette `meteo` par image.
5. **Aucune pré-annotation** dans cette tâche. Ne pas ouvrir la tâche pré-annotée sur ces images avant le lendemain.
6. **Noter le temps passé** par image (approximatif). Il servira à estimer la durée des séances suivantes.
7. **À la fin :** Actions → Exporter les annotations → **COCO 1.0**, dans `data/reference/annotations/A_aveugle/`.
