# 0005 — Images : photo libre Unsplash / Pexels, pas de générateur IA

- **Date :** 2026-11-17
- **Statut :** Acceptée
- **Décideurs :** Romuald

## Contexte
L'équipe n'a aucun outil de génération d'images. Options étudiées le 2026-11-17 : Gemini via l'offre étudiants Google (plan exact AI Plus ou AI Pro non tranché par les sources 🔎), ChatGPT gratuit (quota limité), serveur MCP Pollinations (gratuit, sans clé, qualité moyenne, serveurs communautaires), Recraft gratuit (≈ 30 crédits/jour, usage non commercial, créations publiques), Figma Education (MCP limité 🔎).

## Décision
Photos libres **Unsplash** et **Pexels**, recherchées et sélectionnées par l'agent. Tout le reste (pictos, motifs, illustrations, graphiques) est construit en SVG/CSS. Niveau d'outillage « tier 0 — Claude seul ».

## Options écartées
- **Gemini / ChatGPT à la main** : meilleure qualité, mais un aller-retour manuel à chaque image.
- **Pollinations en MCP** : génération directe, mais qualité moyenne et code tiers à auditer.
- **Recraft** : utile pour des pictos SVG, mais créations publiques et non commerciales.

## Conséquences
- Pour chaque photo utilisée : noter la source, l'auteur et la licence (dans `.agents/brand-strategy.md` puis dans la bibliothèque d'images de la DA).
- Pas de photo réelle de foule aux Arcs depuis les webcams dans la DA : droits non vérifiés, et contraire au principe « aucune image stockée ».
- On pourra passer à Gemini plus tard si une image précise manque : nouvelle fiche dans ce cas.
