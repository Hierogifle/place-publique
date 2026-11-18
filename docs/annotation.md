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

### 2.1 Qui compte
| Cas | On annote ? | Comment |
|---|---|---|
| Personne visible (skieur, piéton, enfant, moniteur, perchman) | **Oui** | Un cadre par personne, ajusté au corps visible, skis exclus |
| Personne partiellement cachée (par une autre, un poteau, un bâtiment) | **Oui**, dès qu'on reconnaît une personne (tête ou buste visible) | Cadre sur la partie visible |
| Personne sur un siège de télésiège, dans une cabine, sur un téléski | **Oui** | Attribut `sur_remontee` coché |
| Conducteur visible d'une dameuse ou d'une motoneige | **Oui** | Le véhicule seul ne compte pas |
| Silhouette douteuse (poteau, ombre, sac, très lointaine) | **Oui, en incertaine** | Attribut `incertain` coché : elle compte dans la fourchette, pas dans le chiffre principal |
| Reflet dans une vitre, affiche, statue, mannequin | **Non** | — |
| Ombre d'une personne | **Non** | La personne seule |

### 2.2 Comment parcourir une image
1. **Zoom à 100 %** ; les panoramas font environ 18 500 × 4 000 px.
2. **Balayer de gauche à droite, par bandes**, sans sauter de zone : terrasses, files, gares, pistes, et le ciel (télésièges).
3. **Bords du panorama 360° :** le bord gauche et le bord droit montrent le même endroit. Une personne coupée en deux n'est comptée **qu'une fois, sur le bord gauche**.
4. **Image inexploitable** (objectif givré ou couvert, image noire, image corrompue) : on met l'étiquette d'image `inexploitable` et on n'annote rien. Elle sera comptée comme « pas de donnée », jamais comme zéro.
5. **Météo :** une étiquette d'image dans CVAT (`beau`, `couvert`, `neige-brouillard`, `nuit`), reportée ensuite dans la colonne `weather` du manifeste.

### 2.3 Ordre des séances (pour mesurer le biais d'ancrage, fiche 0025)
1. **Séance A, sans aide :** les **24 images tirées au sort** (8 par caméra, `data/reference/blind_set.csv`), dans une tâche CVAT **sans aucun cadre pré-calculé**.
2. **Au moins un jour plus tard :** les 240 images de référence et les 30 de contrôle, avec la pré-annotation d'un modèle **plus fort que la baseline**, dans une autre tâche. On supprime les faux cadres, on ajuste, puis on balaie pour ajouter les oubliés.
3. **Comparaison automatique** des 24 images : comptage sans aide contre comptage corrigé. Critère : écart moyen ≤ 1 personne (voir [evaluation.md](evaluation.md) § 4).

### 2.4 Exports
- **CVAT :** export au format COCO, dans `data/reference/annotations/` (hors de Git, comme les images).
- **Versionné :** `data/reference/ground_truth.csv`, avec par image le nombre de personnes certaines, d'incertaines et de personnes sur une remontée, et l'étiquette inexploitable.

### 2.5 Exemple
L'image témoin du 14/02/2026 à 12 h 05 (hors jeu de référence, fiche 0023) sert d'exemple pour se faire la main avant la séance A. Elle n'entre dans aucune mesure.
