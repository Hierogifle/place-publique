# Brand Context — FlowView · Place Publique
<!-- This file is .agents/brand.md. Every design skill reads it first. Keep it current; never leave decisions only in chat history. -->

*Last updated: 2026-11-17*
*Sources ingested: sujet `sujet/Place_Publique_V2.pdf`, support de kick-off `sujet/M2 Kick-off — Place Publique FlowView.pptx`. Aucun site, logo ou charte existants : marque fictive, à créer.*

> **Statut : STUB.** Rédigé par `brand` (cas « marque qui n'existe pas encore »). Les sections marquées *(TBD)* seront remplies par `brand-strategy`, `creative-direction`, `logo-design` et `art-direction`.

## Brand at a Glance
**Name:** **FlowView** — marque principale (décidé le 2026-11-17). « Place Publique » reste le nom du projet d'école et peut nommer le produit/module, sous FlowView.
**Name usability:** radio test OK en anglais, prononciation hésitante en français (« flo-vi-ou ») ; homonymes probables dans le logiciel (à vérifier). Ironie à assumer ou à corriger : le nom dit « flow » alors que le produit mesure une **occupation**, pas un flux.
**One-liner (draft):** Un chiffre de fréquentation fiable, tiré des webcams déjà installées, pour décider quand ouvrir, renforcer ou fermer.
**Category:** Analyse vidéo de fréquentation (comptage de personnes / occupation) pour exploitants d'espaces publics et domaines skiables. SaaS B2B / B2G.
**REO depth:** **Revolution** — rien n'existe encore, il n'y a aucun acquis à protéger. Ce n'est pas un jugement, c'est un point de départ.

**Client de démonstration :** domaine skiable des Arcs (Bourg-Saint-Maurice, Paradiski) — occupation des places de village et des départs de remontées. Brides-les-Bains en plan B.

**Calendrier :** projet lancé le 2026-11-17 · ouverture du domaine des Arcs le 2026-12-12 (vérifié sur lesarcs.com) · **soutenance le 2026-12-15**. Conséquence : pas de file de skieurs avant le 12/12 ; la démo peut montrer 3 jours de vraie saison.

## Competitor Set — CONFIRMÉ (2026-11-17)
Directs : **Safari AI**, **Wintics**, **Viziosense**, **Parkoview**. Indirects : Bumbee Labs / SkiStar, Vail EpicMix Time, Eco-Compteur.
Analyse complète (relevé de DA, forces, faiblesses, opportunités) : [competitors.md](competitors.md).

**Competitive visual landscape:** deux couloirs seulement — « IA nocturne » (fond nuit, mono entre crochets, accent néon, cadre de détection : Wintics) et « SaaS lumineux » (blanc, photo stock, CTA vert néon : Safari). Tous montrent la caméra et présentent le chiffre comme exact. **Le couloir libre : le chiffre honnête, dans un langage alpin plutôt que de vidéosurveillance.**

## Emotional Target (Big Three)
*Validé le 2026-11-17 — détail et verbatims dans [brand-strategy.md](brand-strategy.md).*
1. **Serein** — décliné en trois couches empilées : le **refuge au petit matin** (la matière de la marque, toujours présente), le **guide qui lit le ciel** (la façon de montrer les données), le **pilote en croisière** (le système d'alerte : une seule couleur vive, réservée aux problèmes).
2. **Respecté dans son métier** — « c'est toi le pro, je suis ton second regard ». Pas de mascotte, d'emojis, d'« IA magique », de gamification.
3. **En confiance** — le chiffre est cru parce que l'outil avoue ce qu'il ne sait pas : fourchette, heure de la mesure, « pas de donnée » visible. Jamais de fausse précision.

**Antagoniste :** l'écran qui dévore le métier → la surprise → le chiffre menteur.
**Promesse :** le tableau de bord qu'on n'a pas besoin de regarder.

## Muses
*Validées le 2026-11-17 — images et sources : [stylescapes/muse-board.html](stylescapes/muse-board.html) ; détail : [brand-strategy.md](brand-strategy.md).*
| Muse | What we steal (the visual cue) |
|------|-------------------------------|
| Le bois qui a vécu (A3) | Grain profond, marques, lumière rasante — l'usure qui prouve la solidité |
| La structure de la tour de guet (B1) | Charpente apparente, contreventements, triangulation — pas la couleur |
| Le guetteur à l'instrument (B6, archive) | Noir et blanc argentique, geste précis sur l'anneau gradué, tenue sérieuse |
| Les crêtes dans la brume (C) | Plans successifs qui pâlissent — majesté, échelle qui nous dépasse |
| Le matin à la campagne (D3) | Grain photo, couleurs douces et rabattues, brume basse |
| Les mains du sage (E2) | L'âge comme force, prise ferme |
| Porter l'enfant (F2) | Confiance, fusion — pour le ton et le mouvement |
| La lumière dans les bois (G2) | Une seule source de lumière qui apaise dans l'obscurité |
| La berceuse | Voix lente, mélodique, apaisante — ton et rythme |

## Audience
**Primary:** direction d'exploitation des remontées mécaniques et office de tourisme des Arcs ; décident d'ouvrir un télésiège, de renforcer le personnel, d'ajuster des horaires.
**Secondary:** le jury de soutenance (« panel de clients et d'investisseurs »).
**They already find [X] trustworthy:** *(TBD — see brand-strategy)*

## Visual System
*Direction choisie le 2026-11-17 : **04 · Les Crêtes, vues du refuge (v2)**. Spécification complète, tokens et règles d'écran : [design.md](design.md). En attente de validation finale de Romuald.*

### Color
| Role | Color | Value | Ramp |
|------|-------|-------|------|
| Background | Papier | `#F2EFE9` (sombre : `#1A1512`) | — |
| Surface | Page | `#FBFAF7` (sombre : `#231D18`) | — |
| Text — primary | Encre brune | `#2A2420` | — |
| Text — secondary | Écorce | `#6B625A` | — |
| Data | Ardoise | `#1F3140` | `#19232B · #1C2A36 · #1F3140 · #6B767E · #ABB1B4` |
| Accent / alert | Balise | `#C8342A` | `#76251F · #A02D25 · #C8342A · #D87870 · #E7B2AC` |
| Support | Crête pâle / Brume | `#B9C6CF` / `#C9D3DA` | — |
**Action-color protection:** la balise ne sert qu'aux alertes ; jamais sur un bouton, un lien, un état actif ou une décoration. Les actions sont en encre brune / surface.

### Typography
| Role | Typeface | Weights allowed | Style rules |
|------|----------|-----------------|-------------|
| Interface + chiffres | Inter (OFL) | 300 (grands chiffres), 400, 500, 600 | Chiffres tabulaires ; neutre assumé |
| Voix du gardien | Alegreya (OFL) | 500 | Une phrase par écran au plus ; jamais en libellé |
**Prohibited:** mono décorative, italique en titre, gras par défaut, tirets cadratins, emojis.

### Composition
**Grid / spacing logic:** base 4 px ; deux colonnes (principale 1,7 / outils 1) ; une colonne sous 1100 px.
**Density:** moyenne (outil d'exploitation) ; silence tant que tout va bien.
**How the eye is directed:** l'image analysée et le chiffre d'abord ; la balise seule attire l'œil en cas d'alerte.

### Pattern & Texture
**Motifs:** la crête (normale pâle derrière, aujourd'hui net devant) ; la brume pour « pas de donnée ».
**Textures:** grain fin en canvas. Pas de cadre de détection décoratif, pas de flou décoratif.

### Illustration
Aucune. Abstractions produit : journée vue de côté, relief 3D, jauge avec trait de normale.

### Iconography
Phosphor Regular, 18 px, une icône par concept.

### Photography
Dans l'app : image de caméra floutée, jamais enregistrée. Hors app : paysages de montagne libres, plans successifs et brume, légère désaturation, auteur crédité.

## Logo
*Logo v1 « le refuge éclairé » (piste B1), choisi par Romuald le 2026-11-17. Planche et règles : [stylescapes/logo.html](stylescapes/logo.html) ; pistes explorées : [stylescapes/logo-sketches.html](stylescapes/logo-sketches.html) ; détail : [design.md](design.md) § Logo.*

**Idée :** la masse de la montagne (un sommet, un épaulement) et une seule fenêtre carrée découpée en creux : le refuge où quelqu'un veille. Le point du « i » de View est un carré, l'écho de la fenêtre.
**Fichiers verrouillés (à placer, jamais à redessiner) :** `.agents/assets/logo/`
- `logo-lockup.svg` (principal) · `logo-lockup-inverse.svg` · `logo-lockup-black.svg` · `logo-lockup-white.svg` · `logo-lockup-gray.svg`
- `logo-icon.svg` · `logo-icon-inverse.svg` · `avatar.svg` · `app-icon.svg` · `favicon.svg` · `favicon.ico`
- `raster/` : PNG (fond transparent) et JPEG de chaque variante, favicons 16 / 32 / 48 / 180 px
**Couleurs :** montagne ardoise `#1F3140`, nom encre `#2A2420` ; inversé : `#E1E9EE` / `#EFE8DC`. Une couleur : encre, clair `#FBFAF7`, gris `#6B625A`.
**Zone de protection :** une fenêtre (8 unités sur la grille de 64), incluse dans les fichiers. **Taille minimale :** bloc complet 96 px / 25 mm ; symbole seul 16 px.
**Interdits :** recolorer (jamais en rouge d'alerte), remplir la fenêtre, encadrer ou mettre en pastille, rogner, déformer, ajouter effet ou slogan, recomposer le nom.

**Contrôle SAD (2026-11-17) :**
- **Simple :** ✅ un seul dessin de 16 px à 1 600 px ; tient en une couleur et en inversé ; en 16 px la fenêtre devient un point, la montagne reste lisible.
- **Approprié :** ✅ serein (le refuge veille), respecté (aucune mascotte ni « IA »), une seule lumière.
- **Distinct, rayon :** ✅ aucun concurrent direct n'utilise de montagne, de forme pleine ni de couleur chaude (Wintics : W en zigzag ; Viziosense : œil ; Safari AI : glyphe vert encadré).
- **Distinct, ressemblances hors secteur :** **non évalué.** Google Lens, Pinterest et la base de marques de l'OMPI n'ont pas été lancés (il faut téléverser l'image). Une recherche par mots-clés n'a rien trouvé d'identique ; la montagne avec chalet reste un motif courant (location de chalets). À faire avant tout usage public hors école.

## Voice
**Tone:** la voix du vieux gardien de refuge : calme, lente, précise ; elle conseille au conditionnel, ne commande jamais.
**Personality:** expérimenté · honnête · discret · bienveillant.
**On dit :** « d'habitude à cette heure », « à quelques personnes près », « pas de donnée », « au-dessus de la normale ». **On ne dit jamais :** « visiteurs de la journée », « flux », « précision de 95 % », « risque de blessure ».
Contrainte posée par le sujet : le produit dit ce que son chiffre signifie **et ce qu'il ne dit pas** (occupation instantanée, pas un flux ; « pas de donnée » n'est pas zéro).

## Fixed Core vs. Flexible Range
*Validé le 2026-11-17.*

**Fixed core — must ALWAYS hold:**
- La patine (grain, matière qui a vécu)
- Le silence (espace, peu d'éléments)
- Une seule lumière d'alerte, jamais utilisée ailleurs
- Le chiffre honnête (fourchette, heure de mesure, « pas de donnée »)
- La voix du sage (calme, l'anecdote utile)

**Flexible range — free to flex:**
- Température de la lumière selon l'heure et la saison (même univers)
- Plus de spectacle pour la soutenance et le README
- Plus de densité sur l'écran d'alerte

**A flex is legitimate when:** la pièce reste silencieuse, patinée et honnête — même sans notre police ni nos couleurs.

## In Use
- Dashboard Flask (Jinja + Chart.js) — `app/templates`, `app/static` *(à venir)*
- Slides de soutenance (20 min + 10 min de démo)
- README et documents du dépôt

## Toolkit
**Tier:** 0 — Claude only (choix confirmé le 2026-11-17)
**Generators the operator runs by hand:** aucun.
**Imagery source:** photo libre **Unsplash / Pexels** — l'agent cherche, sélectionne et documente source + auteur + licence de chaque image. Le reste (pictos, motifs, illustrations, graphiques) est construit en SVG/CSS par l'agent.
**Connected to the agent:** aucun générateur ; `QUIVER_API_KEY` absent ; Figma présent mais non authentifié
**Design canvas:** aucun
**Last confirmed:** 2026-11-17
