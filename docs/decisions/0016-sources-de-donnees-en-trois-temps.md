# 0016 — Sources de données en trois temps : jeux d'images, station ouverte, puis Les Arcs

- **Date :** 2026-11-17
- **Statut :** Acceptée (à faire valider par le formateur pour le jeu de référence)
- **Décideurs :** Romuald
- **Complète :** [0003](0003-station-les-arcs.md)

## Contexte
Le domaine des Arcs n'ouvre que le 12 décembre 2026 ✅ ; avant, ses places et départs de remontées sont presque vides. Un jeu de référence rempli de zéros ne permet pas de mesurer une erreur de comptage. La soutenance a lieu le 15 décembre.

## Décision
1. **Jeux de données d'images** pour le palier 1 : construire et figer le jeu de référence (≥ 100 images, ≥ 50 comptées à la main) et mesurer la baseline. Pistes repérées sur Roboflow Universe : « Skier detection » (SkiTB), « skidanalys », « Ski detection » (CC BY 4.0) 🔎 ; licence vérifiée image par image, vues larges seulement.
2. **Test en production dans une station déjà ouverte** : Val Thorens et Tignes annoncent le 21/11/2026, Val d'Isère et Les 2 Alpes le 28/11 🔎 (dates prévisionnelles). Les captures forment un **jeu de validation terrain séparé** ; le jeu de référence n'est jamais modifié.
3. **Branchement sur Les Arcs à la fin** (ouverture le 12/12) pour la démo, en ajoutant les caméras depuis l'interface.

## Options écartées
- **Les Arcs seulement** : jeu de référence quasi vide avant le 12/12.
- **Une webcam de place urbaine** comme relais : changerait de contexte (ville au lieu de station).

## Conséquences
- Le passage d'une source à l'autre sans changer le code prouve la **généricité** demandée par le sujet.
- Risque : le sujet demande un jeu de référence « de votre contexte » ; des images publiques de stations s'en approchent mais ne sont pas nos caméras. À présenter honnêtement au formateur.
- Peu de monde en semaine de novembre dans la station ouverte : capturer aussi les week-ends.
- Conditions d'utilisation des webcams de la station ouverte à lire avant toute capture ; aucune image brute dans Git.

## Sources
- Ouvertures 2026-2027 : https://guide-ski.fr/?p=4038 · https://www.parisselectbook.com/?p=258478 · https://www.tourmag.com/Ski-les-stations-francaises-devoilent-leurs-dates-d-ouverture-pour-l-hiver-2026-2027_a133773.html
- Jeux de données : https://universe.roboflow.com/skitb/skier-detection · https://universe.roboflow.com/arcada-mwj8x/skidanalys · https://universe.roboflow.com/timondb01-gmail-com/ski-detection
