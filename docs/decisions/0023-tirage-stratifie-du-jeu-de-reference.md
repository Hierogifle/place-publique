# 0023 — Jeu de référence tiré au sort, par strates, avant de voir les images

- **Date :** 2026-11-18
- **Statut :** Acceptée
- **Décideurs :** Romuald

## Contexte
Le sujet demande « au moins 100 images de votre contexte (jour/nuit, météo, affluence variable) », figées dès le départ. Si on choisit les images à la main, on risque de prendre celles où le comptage est facile : l'erreur mesurée serait alors trop optimiste.

## Décision
- **Tirage au sort reproductible :** graine 20261118, avec 150 créneaux et 30 de réserve sur Arcabulle, Mont-Blanc et Grizzly (saison 2025-2026). Il est écrit et commité **avant** la collecte. Configuration : `configs/reference_lesarcs.json` ; plan : `data/reference/sampling_plan.csv`.
- **Strates par caméra :**
  - affluence haute 14, moyenne 13, basse 13 ;
  - hors exploitation : nuit 5 et crépuscule 5, pour mesurer les fausses détections ;
  - les moments de la journée sont répartis à parts égales ;
  - une seule image par jour et par caméra.
- **L'affluence est estimée par le calendrier :** vacances scolaires officielles, chevauchement de deux zones, week-ends. On la vérifiera ensuite avec les comptages à la main.
- **La météo est notée après coup.** On ne la connaît pas d'avance, mais on vérifie qu'il y a au moins 10 images par classe.
- **Anti-doublons :** une empreinte de ressemblance de 128 bits ; on remplace une image si elle diffère d'une autre de 10 bits ou moins (seuil à calibrer).
- **Le code est générique :** il ne dépend que d'un fichier de configuration par client, comme le demande le sujet (« sans enfermer le code dans ce seul client »).

## Options écartées
- **Choix à la main de 150 « bonnes » images :** biais de sélection.
- **Tirage simple sans strates :** la nuit et l'affluence haute auraient pu manquer.

## Conséquences
- La collecte se fait à la main dans le lecteur officiel (fiche 0021), en suivant le plan. Pour une image absente, on prend la réserve suivante de la même caméra.
- L'image témoin du 14/02/2026 à 12 h 05, choisie à la main, n'entre pas dans le jeu.

## Sources
- Calendrier scolaire 2025-2026, jeu de données officiel : <https://data.education.gouv.fr/explore/dataset/fr-en-calendrier-scolaire/> (consulté le 18/11/2026).
- Dates de saison des Arcs 2025-2026 : 13/12/2025 → 25 ou 26/04/2026 selon les sources 🔎 (skiinfo, annecy-ville.fr).
