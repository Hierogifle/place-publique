# 0021 — Images des webcams : usage pédagogique sans autorisation, avec garde-fous

- **Date :** 2026-11-18
- **Statut :** Acceptée
- **Décideurs :** Romuald

## Contexte
Les webcams des Arcs (Trinum / webcam-hd) gardent une archive quotidienne depuis le 01/10/2025 ✅. Elles sont la meilleure source pour le jeu de référence : notre contexte exact, avec de la foule. Mais les mentions légales de lesarcs.com interdisent « toute reproduction ou réutilisation […] sans accord préalable des titulaires des droits » ✅.

Ce que dit le sujet (`Place_Publique_V2.docx`) ✅ :
- « L'utilisation de webcams dont le client serait propriétaire n'est possible que dans un projet réel en entreprise. »
- « À défaut d'accord des propriétaires des webcams publiques, l'exploitation des flux bruts peut être soumise à des restrictions légales : ne versionnez pas d'images brutes de webcams dans votre dépôt (.gitignore). »

Le sujet prévoit donc l'usage de webcams publiques sans accord, dans le cadre de l'école, avec cette restriction.

## Décision
Pas de demande d'autorisation : on utilise les images des webcams publiques **dans le seul cadre pédagogique**, et on l'écrit dans les **limites réglementaires** du projet (`conformite.md`). Les garde-fous :
1. **Peu d'images :** le jeu de référence (environ 150) et les captures du socle. Pas d'aspiration massive de l'archive.
2. **Uniquement les accès normaux :** le lecteur officiel et les URL d'images publiques affichées par le site. Pas d'interface technique non documentée.
3. **Rien dans Git :** images brutes hors du dépôt (`.gitignore`). Seuls les manifestes sont versionnés (fichier, source, date, empreinte).
4. **Rien de publié :** aucune image brute dans les slides, le README ou une démo publique. Seulement des images floutées et des comptages agrégés.
5. **Source citée** partout où une image dérivée apparaît.
6. **Suppression des images à la fin du projet**, notée au journal.

## Options écartées
- **Demander l'autorisation aux Arcs et à webcam-hd :** plus propre juridiquement, mais Romuald juge que le cadre pédagogique et la règle du sujet suffisent. Le brouillon reste dans `docs/sources.md` si un usage hors école se présente.
- **Se limiter aux jeux publics :** ce ne sont pas des vues de webcam de station, et le sujet veut des images « de votre contexte ».

## Conséquences
- **Risque juridique faible mais réel :** c'est une reproduction d'œuvres protégées sans accord.
  - L'exception pédagogique du droit d'auteur (art. L122-5, 3°, e du Code de la propriété intellectuelle) est étroite et encadrée 🔎.
  - L'exception de fouille de textes et de données (art. L122-5-3) tombe si le titulaire s'y est opposé. Une mention générale « reproduction interdite » vaut-elle opposition ? Non tranché 🔎.
  - On ne prétend pas être couvert : on l'écrit comme une **limite**, avec les garde-fous ci-dessus.
- **Pour un vrai produit FlowView,** un accord écrit avec l'exploitant serait obligatoire : c'est lui le client et le propriétaire des caméras. À dire au jury.
- À reprendre dans `conformite.md`, section « Limites ».

## Sources
- Sujet, section « Ressources et contraintes ».
- Mentions légales des Arcs : <https://www.lesarcs.com/fr/mentions-legales> (relues le 17/11/2026).
- Code de la propriété intellectuelle, art. L122-5 et L122-5-3 : <https://www.legifrance.gouv.fr/codes/id/LEGITEXT000006069414/>
