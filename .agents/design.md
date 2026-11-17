# Creative Direction — FlowView
<!-- This file is .agents/design.md: the visual-system spec every application skill (web-design, motion-design, collateral-design) builds against. Living record: downstream skills append below the line, with a date and a one-sentence why. -->

*Last updated: 2026-11-17 (v3 « maquette » ajoutée, voir §9) · Status: **VALIDÉ par Romuald le 2026-11-17** · écran principal = la maquette 3D (§9), système visuel = §3. Le front peut être codé, au palier 2, après le service d'inférence et la base.*
*Depth: Revolution · Source: `.agents/brand-strategy.md` (Q1 → Q11), `.agents/brand.md`, `.agents/competitors.md`*
*Chosen direction: **04 · Les Crêtes, vues du refuge**, écran en **maquette 3D (v3)** · Proof: `.agents/stylescapes/maquette.html` (v3, référence) et `piste-04.html` (v2, système) · Published copy: none*
*Decisions: `docs/decisions/0008` → `0014`*

---

## 1. Emotional Target (carried from brand-strategy)

| Émotion | Ce qu'elle interdit | Ce qu'elle impose |
|---|---|---|
| **Serein** — en trois couches : refuge (matière), guide (données), pilote (alerte) | Tout ce qui retient l'œil sans raison ; le rouge ailleurs que sur une alerte | Silence visuel tant que tout va bien |
| **Respecté dans son métier** — « c'est toi le pro, je suis ton second regard » | Mascotte, emojis, étincelles « IA », gamification, ton pédagogue | Vocabulaire du métier, allure d'outil professionnel |
| **En confiance** — le chiffre est cru parce que l'outil avoue ce qu'il ne sait pas | Fausse précision (« 98,7 % »), KPI triomphants, zéro à la place d'une absence | Fourchette, heure de mesure, normale de l'heure, « pas de donnée » visible |

**Antagoniste :** l'écran qui dévore le métier → la surprise → le chiffre menteur.
**Promesse produit :** le tableau de bord qu'on n'a pas besoin de regarder, sauf quand il faut.

---

## 2. Concepts Explored

Rendus : `.agents/stylescapes/stylescapes.html` (01 à 03) et `piste-04.html` (04).

### 01 · La Vigie — *non retenue*
- **Muses → abstractions :** guetteur à l'instrument (B6) → anneau gradué où chaque site a son cap ; structure de la tour (B1) → triangulation ; archive noir et blanc → traitement « bromure ».
- **Signature :** la visée qu'on fait tourner pour lire un site.
- **Pourquoi non :** la plus littérale (effet « cadran »), et un cercle se prête mal à un vrai tableau de bord.

### 02 · Le Refuge — *non retenue seule, sa matière est reprise en 04*
- **Muses → abstractions :** bois qui a vécu (A3) → fond noyer ; mains du sage (E2) + berceuse → voix du carnet ; comptage à la main → bâtons de comptage.
- **Pourquoi non seule :** proche du cliché « serif + crème + accent chaud », fond sombre peu lisible au bureau. Romuald en a gardé la chaleur.

### 03 · Les Crêtes — *non retenue seule, son langage de données est repris en 04*
- **Muses → abstractions :** crêtes dans la brume (C) → affluence dessinée en relief ; la normale en crête pâle derrière, aujourd'hui devant ; le doute en nappe de brume.
- **Pourquoi non seule :** la plus « graphique classique » ; froide sans la matière du refuge.

### 04 v1 · Les Crêtes, vues du refuge — *remplacée par la v2*
Synthèse 02 + 03 avec la station en 3D au centre. Retour de Romuald (Q11) : mal ordonnée, peu belle, l'image analysée doit passer devant.

### 04 v2 · Les Crêtes, vues du refuge — **CHOISIE (2026-11-17)**
- **Une seule histoire :** on lit la montagne depuis la fenêtre du refuge. Dedans (papier, encre brune, la voix) ; dehors (relief, ardoise, les chiffres) ; une balise rouge pour l'alerte. C'est exactement l'empilement validé en Q4 (fiche 0010).
- **Muses → abstractions :**
  - Refuge au petit matin (D3) + bois qui a vécu (A3) → neutres papier chauds, encre brune, grain fin ; mode sombre = le refuge le soir (noyer).
  - Crêtes dans la brume (C) → la journée vue de côté (normale pâle, aujourd'hui net, brume = pas de donnée) et le relief 3D réel des Arcs.
  - Guetteur à l'instrument (B6) → l'image analysée au premier plan : on montre ce que la machine a vu.
  - Lumière dans les bois (G2) → une seule source qui attire l'œil : la balise.
  - Vieux sage + berceuse → la phrase du gardien (« D'habitude, à cette heure… »), lente, calme.
- **Signature (deux éléments, un seul langage) :**
  1. **La journée vue de côté** : la crête du jour devant la crête de la normale, la brume pour le doute, « à venir » après l'heure courante.
  2. **L'image honnête** : cadres du modèle sur des personnes floutées ; on peut masquer les cadres, jamais le flou.
- **Pourquoi elle répond au trio :** serein (calme, une seule alerte), respecté (outil sobre, vocabulaire du métier, le gardien conseille sans commander), en confiance (fourchette, normale, brume, aveu du doute, transparence de l'image).

---

## 3. The System (04 v2)

### 3.1 Color — par rôle

**Clair : le refuge de jour (par défaut)**

| Rôle | Nom | Hex | Contraste vérifié |
|---|---|---|---|
| Fond de page | Papier | `#F2EFE9` | — |
| Surface (cartes) | Page | `#FBFAF7` | — |
| Surface 2 (contrôles, survol) | Page usée | `#F5F2EC` | — |
| Texte principal | Encre brune | `#2A2420` | 14,7:1 sur Page ✅ |
| Texte secondaire | Écorce | `#6B625A` | 5,7:1 sur Page, 5,2:1 sur Papier ✅ |
| Filets | Trait | `#E3DED5` | décoratif |
| Donnée (chiffres, crête du jour) | Ardoise | `#1F3140` | 12,8:1 ✅ |
| Donnée secondaire (± , normale) | Crête | `#4B6273` | 6,1:1 ✅ |
| Normale (aire) | Crête pâle | `#B9C6CF` | graphique |
| Pas de donnée | Brume | `#C9D3DA` | graphique |
| **Alerte** | **Balise** | **`#C8342A`** | 5,05:1 sur Page ✅ ; texte clair sur balise 4,95:1 ✅ |
| Fond d'alerte (pastille) | Balise douce | `#F7E4E1` | texte en `#A52A21` : 5,8:1 ✅ |

**Sombre : le refuge le soir (suit le réglage du système)**

| Rôle | Hex | Contraste vérifié |
|---|---|---|
| Fond / surface / surface 2 | `#1A1512` / `#231D18` / `#2B241E` | — |
| Texte principal / secondaire | `#EFE8DC` / `#B3A796` | 13,7:1 / 7,1:1 ✅ |
| Donnée / donnée secondaire | `#E1E9EE` / `#9FB1BD` | 13,6:1 / 7,5:1 ✅ |
| Normale / brume | `#5A6B78` / `#3B4852` | graphique |
| Alerte / fond d'alerte | `#FF6A58` / `#3A211D` | 5,9:1 / 5,3:1 ✅ |

**Règles :**
- **La balise est sacrée** : elle n'apparaît que pour une alerte (chiffre au-dessus de la normale, marqueur, crête rouge, statut). Jamais sur un bouton, un lien, une décoration ou un état actif.
- **Dedans / dehors :** ce qui vient du refuge (phrases, interface) est en encre brune ; ce qui vient de la montagne (chiffres, courbes) est en ardoise.
- **La carte et l'image restent en lumière de jour** dans les deux modes : ce sont des fenêtres sur l'extérieur.
- **Variation autorisée (marge de liberté) :** la lumière du relief 3D se réchauffe en mode « Préparer » (`#ECE5D9`) et se refroidit en « Alerter » (`#D6DEE3`).
- **Rampes** (deux ombres, base, deux clartés ; calculées par mélange avec `#121212` à 45 / 22 % et `#F7F6F2` à 35 / 65 %) : Ardoise `#19232B · #1C2A36 · #1F3140 · #6B767E · #ABB1B4` ; Balise `#76251F · #A02D25 · #C8342A · #D87870 · #E7B2AC`. Pour du texte d'alerte sur fond clair teinté, utiliser `#A52A21` (token `--alert-strong`).
- **Propriété face aux concurrents :** personne n'occupe papier chaud + ardoise + balise rouge. Safari = blanc + vert néon ; Wintics = nuit + violet + mono ; Viziosense = noir et blanc. ✅

### 3.2 Typography

| Rôle | Police | Licence | Graisses | Règles |
|---|---|---|---|---|
| Interface + chiffres | **Inter** | SIL OFL 1.1 (Google Fonts) | 300 (grands chiffres), 400, 500, 600 | Chiffres tabulaires partout (`font-variant-numeric: tabular-nums`) |
| La voix du gardien | **Alegreya** | SIL OFL 1.1 (Google Fonts) | 500 | Uniquement pour la phrase du gardien (une par écran au plus). **Jamais** pour un libellé, un bouton ou un chiffre |

- **Pourquoi Inter :** choix neutre *assumé* (mode Operate : une famille porte l'outil) ; la marque est portée par la couleur, le relief et la voix, pas par la police. Aucun concurrent direct ne l'utilise.
- **Pourquoi Alegreya :** née de la calligraphie, elle donne la main du carnet sans police manuscrite ; contraste net avec Inter (serif humaniste vs sans).
- **Échelle (rem fixes, ratio ≈ 1,2) :** 12,5 / 13 / 15 (texte) / 18 (voix) / 24 (titre de zone) / 34 (normale) / 52 (chiffre principal).
- **Interdits :** police mono décorative, italique en titre, gras par défaut, majuscules sur du texte courant, tirets cadratins.
- **Caractères :** Inter et Alegreya couvrent le français complet (accents, guillemets « », espaces insécables). ✅

### 3.3 Motif, pattern & texture
- **Motif possédé : la crête.** Deux plans : la normale (pâle) derrière, aujourd'hui (net) devant. Utilisable sans logo : graphiques, fonds de slides, README, favicon possible.
- **La brume** = absence de donnée (aplat brume, jamais un creux à zéro).
- **Texture :** grain fin généré en canvas (opacité 0,25, `multiply`), jamais de `feTurbulence`.
- **À ne pas utiliser :** cadre de détection comme motif décoratif (signature de Wintics), grilles de points, dégradés violets, flou décoratif (le flou est réservé à l'anonymisation).

### 3.4 Iconography
- **Source unique : Phosphor, style Regular** (licence MIT), 18 px dans l'interface.
- Icônes utilisées : `warning` (alerte), `cloud-fog` (pas de donnée), `clock` (heure), `eye` / `eye-slash` (cadres), `mountains`, `chart-line-up`, `bell-ringing`, `notebook`.
- Une icône = un concept ; pas d'icône décorative ; pas d'emoji.

### 3.5 Illustration / product abstraction
- **Pas d'illustration.** Les abstractions du produit sont : la journée vue de côté, le relief 3D, la jauge avec le trait de la normale.

### 3.6 Photography
- **Dans l'application :** uniquement l'image de la caméra, personnes floutées sous leurs cadres, gardée en mémoire le temps du comptage, **jamais enregistrée**.
- **Hors application (slides, README) :** paysages de montagne libres (Unsplash / Pexels), grands plans avec plans successifs et brume (muse C) ; traitement : légère désaturation (`saturate(.85)`), contraste naturel. Toujours créditer l'auteur.
- **Interdit :** photo stock de skieurs souriants (couloir Safari), visages identifiables.

### 3.7 Motion (note de direction)
- Calme et utile : 150-250 ms, `cubic-bezier(.23, 1, .32, 1)`, transitions de `transform` / `opacity` / couleurs.
- **Une seule boucle autorisée :** le halo lent (3,2 s) autour d'un marqueur en alerte.
- Déplacement de la carte vers une zone : 900 ms.
- Boutons : `:active { transform: scale(.97) }`.
- `prefers-reduced-motion` : plus de halo, transitions instantanées.
- Interdits : apparitions au défilement, compteurs animés, chargements orchestrés.

### 3.8 Design tokens

```css
:root {
  /* Color: the refuge by day */
  --bg: #f2efe9; --surface: #fbfaf7; --surface-2: #f5f2ec;
  --ink: #2a2420; --muted: #6b625a; --line: #e3ded5;
  --data: #1f3140; --data-2: #4b6273; --normal: #b9c6cf; --mist: #c9d3da;
  --alert: #c8342a; --alert-soft: #f7e4e1; --alert-strong: #a52a21;
  /* Type */
  --font-ui: "Inter", system-ui, sans-serif;
  --font-voice: "Alegreya", Georgia, serif;
  --text-xs: .78rem; --text-sm: .8125rem; --text-base: .9375rem; --text-voice: 1.125rem;
  --text-lg: 1.5rem; --text-xl: 2.125rem; --text-2xl: 3.25rem;
  /* Space (4 px base) */
  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px; --space-5: 20px; --space-6: 24px; --space-8: 32px;
  /* Radius + shadow */
  --radius-chip: 6px; --radius-ctl: 8px; --radius-card: 12px;
  --shadow: 0 1px 2px rgba(42, 36, 32, .06), 0 8px 24px rgba(42, 36, 32, .06);
  /* Motion */
  --duration-fast: 150ms; --duration-base: 200ms; --duration-move: 900ms;
  --ease-out: cubic-bezier(.23, 1, .32, 1);
  /* Layers */
  --z-map-ui: 2; --z-sticky: 10; --z-grain: 20;
}
@media (prefers-color-scheme: dark) {
  :root {
    /* the refuge at night */
    --bg: #1a1512; --surface: #231d18; --surface-2: #2b241e;
    --ink: #efe8dc; --muted: #b3a796; --line: #3a3029;
    --data: #e1e9ee; --data-2: #9fb1bd; --normal: #5a6b78; --mist: #3b4852;
    --alert: #ff6a58; --alert-soft: #3a211d; --alert-strong: #ff6a58;
  }
}
```

---

## 4. Écran principal et composants (pour `web-design`)

### 4.1 Ordre de l'écran (validé en Q11)
1. **Barre du haut** : FlowView · station · date · heure · fréquence de mesure ; sélecteur **Préparer / Suivre / Alerter** ; résumé (« 1 site au-dessus de la normale · 1 caméra muette »).
2. **Colonne principale**
   - **L'image analysée** de la zone choisie (16:10), cadres + flou, heure de l'image et de la prochaine, bouton « Cadres du modèle ».
   - **Les faits** : chiffre ± fourchette, normale de l'heure, phrase du gardien, pastille « Au-dessus de la normale » si alerte.
   - **La bande des caméras** : une vignette floutée par zone, chiffre ou « pas de donnée ».
   - **La journée vue de côté** de la zone choisie.
3. **Colonne outils**
   - **La station en 3D** pour choisir une zone (marqueurs : normal, alerte avec halo, pas de donnée en pointillé).
   - **Le carnet** trié : alertes, puis caméras muettes, puis le reste ; jauge avec trait de normale.

### 4.2 États obligatoires
| État | Rendu |
|---|---|
| Normal | Chiffre en ardoise, « Rien à signaler, tout suit son cours. » |
| Alerte | Chiffre et marqueur en balise, pastille, crête rouge, phrase du gardien qui conseille une action |
| Pas de donnée | « ? », aplat brume, « Nous réessayons toutes les 5 minutes », dernière image connue datée ; jamais zéro |
| Chargement | Squelettes à la forme finale (image, faits, vignettes), pas de spinner au milieu |
| Aucune caméra (premier lancement) | État vide qui explique : « Ajoutez votre première caméra : URL de l'image, nom, emplacement » (exigence du sujet) |
| Erreur de la carte | Message de secours ; les zones restent accessibles dans le carnet |

### 4.3 Implémentation (contraintes du sujet)
- **Flask + Jinja** : `app/templates/` (base + partials par composant), `app/static/css/tokens.css` (tokens ci-dessus), `app/static/js/`.
- **Graphique « journée vue de côté » :** Chart.js (imposé « par exemple » par le sujet), courbes remplies : normale (aire pâle), aujourd'hui (aire ardoise), segments au-dessus en balise ; la brume en annotation (plugin d'annotation de Chart.js) ou en SVG si Chart.js résiste.
- **Relief 3D :** MapLibre GL JS 4.7.1 (licence BSD-3) + tuiles Terrarium (AWS Open Data) ; remontées et pistes depuis OpenStreetMap (`.agents/stylescapes/data/arcs-osm.geojson`, ODbL, attribution obligatoire). Palier 2, **après** le service et la base.
- **Image analysée :** le flou est appliqué **côté serveur** sur l'image avant tout affichage (le flou CSS de la maquette n'est qu'une illustration).
- **Sous-ressources externes :** versions figées + `integrity` (SRI) comme dans la maquette.

### 4.4 Voix et vocabulaire
- **On dit :** « occupation », « personnes dans la zone », « d'habitude à cette heure », « à quelques personnes près », « pas de donnée », « à venir », « au-dessus de la normale ».
- **On ne dit jamais :** « visiteurs de la journée », « flux » (sans suivi d'objets), « précision de 95 % », « risque de blessure », « intelligence artificielle » en argument.
- La phrase du gardien : courte, au présent, une recommandation au conditionnel (« Je préviendrais l'accueil »), jamais un ordre.
- Pas de tiret cadratin, pas d'emoji, pas de point d'exclamation.

---

## 5. Documented Styles & Asset Sources

| Élément | Source | Licence | Où |
|---|---|---|---|
| Polices Inter, Alegreya | Google Fonts | SIL OFL 1.1 | toutes les surfaces |
| Icônes | Phosphor Icons (web 2.1.1) | MIT | interface |
| Relief 3D | Tuiles Terrarium, AWS Open Data | Ouvert (attribution conseillée) | carte |
| Remontées, pistes | OpenStreetMap, extraction Overpass du 17/11/2026 | ODbL (attribution obligatoire) | `data/arcs-osm.geojson` |
| Photo d'illustration caméra | Unsplash, @joanoger | Licence Unsplash | maquette seulement |
| Photos des muses | Unsplash, Wikimedia Commons (NARA) | Unsplash ; Wikimedia à vérifier | `muse-board.html` |
| Moteur de carte | MapLibre GL JS 4.7.1 | BSD-3-Clause | carte |

---

## 6. Application Proof
- **Écran principal :** `.agents/stylescapes/piste-04.html` (v2), vérifié sur ordinateur et mobile, sans erreur console, sans défilement horizontal, design-taste 0 erreur.
- **Notification d'alerte :** présente dans la v1 (`piste-04` v1, téléphone) ; à reprendre dans la v2 au moment de `collateral-design` / slides.
- **À produire plus tard :** une slide de soutenance et l'en-tête du README dans ce système.

---

## 7. Challenges & Differentiation

**Ce qui sera difficile à coder :**
- La 3D (MapLibre, tuiles en ligne, marqueurs) dans un front Flask/Jinja : faisable, mais c'est du palier 2 et ça ne doit pas passer avant le service.
- La journée vue de côté avec la brume et le « à venir » dans Chart.js (annotations, segments colorés).
- Le flou des personnes côté serveur à chaque analyse, sans rien enregistrer.
- Les états « pas de donnée » et « chargement » partout, pas seulement sur l'écran principal.

**Différence avec les concurrents directs :**
| Concurrent | Eux | FlowView |
|---|---|---|
| Safari AI | Blanc, photo stock, vert néon, « 95 %+ » | Papier chaud, image réelle floutée, fourchette et normale |
| Wintics | Nuit, violet, mono, cadre de détection en motif | Clair, ardoise, cadres seulement sur l'image analysée |
| Viziosense | Flou décoratif, peu de produit montré | Flou d'anonymisation, produit au premier plan |

---

## 8. Self-Audit (sur la v2 rendue)
- **Tropes repérés :** beaucoup de cartes (bordure + ombre) pour structurer l'écran ; pastilles et puces arrondies ; contrôles de carte MapLibre par défaut ; Inter peut être perçue comme le choix par défaut (ici assumé et documenté) ; une seule photo d'illustration pour toutes les zones ; cadres placés à la main.
- **Corrigés depuis la v1 :** mélange de polices, fond bois chargé, hiérarchie confuse, étiquettes de carte décalées, débordement horizontal sur mobile, contraste de la pastille d'alerte (passée à `#A52A21`).
- **Logo caché :** la v2 reste reconnaissable par la crête, le papier chaud, l'ardoise et la balise, plus que par la police.
- **Encore ouvert :** références d'interfaces de Romuald (goût) ; passe `art-direction` (photos des slides) ; `logo-design`.

---

## 9. Évolution v3 · la maquette 3D (2026-11-17)

**Pourquoi :** Romuald a montré ses références d'interface (CRM 3D d'un garage, d'une agence immobilière, d'une entreprise du bâtiment : maquette 3D douce, pastilles flottantes, chiffres clés, panneau de détail, frise du jour, colonnes de suivi). On reprend ce **patron d'écran**, pas le style d'un tiers ; la palette, les polices et les règles d'honnêteté de ce document restent inchangées. Détail : `brand-strategy.md` Q12, fiche `docs/decisions/0015`.

**Ce qui change par rapport à §4 :**
| Élément | v2 | v3 |
|---|---|---|
| La station | Relief cartographique MapLibre (ombrage), petit, à droite | **Maquette 3D stylisée au centre** : relief réel des Arcs en facettes, neige / roche selon la pente, sapins et chalets simplifiés, remontées (câbles, pylônes, gares), socle en bois comme une maquette posée sur une table |
| Les zones | Marqueurs ronds | Empreinte au sol (couleur d'état), **petite foule proportionnelle au comptage** (en file vers la remontée si alerte), pastille flottante « nom · chiffre ± » reliée par une tige |
| L'image analysée | Grande, colonne principale | **Panneau de détail à droite** (code de zone, statut, image floutée avec cadres, 4 faits, phrase du gardien, historique) |
| La journée vue de côté | Carte à part | **Frise du jour** : la crête (normale / aujourd'hui / brume) sert de fond à la frise, avec les événements en pastilles (passé foncé, alerte en balise, à venir en contour) |
| En haut | Barre + statut | Rangée de **4 chiffres clés** (personnes suivies ±, zones au-dessus, caméras qui répondent, prochaine mesure) + secteur + Préparer / Suivre / Alerter |
| En bas | Carnet trié | **Suivi des zones** en 3 colonnes (dans la normale / au-dessus / pas de donnée) ; les zones changent de colonne d'elles-mêmes à chaque mesure (pas de glisser-déposer : l'état est calculé, pas décidé) |

**Couleurs ajoutées (maquette uniquement) :** neige `#F3F5F4` / `#E4EAEE`, roche `#AAB3B9` / `#8F9AA2`, prairie d'hiver `#DCDCCD`, sapins `#5C7A66` (± variation), chalets `#EFE9DF` et toits `#6B5442`, socle bois `#9C7F66`, plateau `#E9E3D8`. Manteaux de la foule en tons sourds (`#3F5566`, `#6B625A`, `#8A7A68`…) : **jamais de rouge**, réservé à la balise.

**Technique :** three.js 0.160.0 (licence MIT) + OrbitControls + CSS2DRenderer, versions figées avec `integrity` dans l'import map. Relief : tuiles Terrarium z13 rééchantillonnées en grille 220 × 186 (`.agents/stylescapes/data/arcs-dem.json`, ≈ 39 m par maille, exagération verticale × 1,4). Remontées et pistes : `data/arcs-osm-maquette.json` (ODbL). Vue par défaut depuis la vallée (nord-ouest), vol de caméra de 900 ms vers une zone, zoom, retour à la vue d'ensemble, halo lent sur l'alerte (désactivé si mouvement réduit).

**Preuve :** `.agents/stylescapes/maquette.html` : vérifiée en grand écran et en mobile, sans erreur console ni débordement, design-taste 0 erreur (2 avertissements : polices Google).

**Points ouverts :** pastilles proches qui se chevauchent en vue d'ensemble (Arcabulle, Place Manoir, Varet) ; coût de rendu sur un PC faible (≈ 3 200 sapins avec ombres) à mesurer ; coder la maquette en palier 2 seulement, après le service et la base.

---
<!-- ============ LIVING RECORD — appended by downstream skills ============ -->

## Logo *(à ajouter par logo-design)*
Pas encore de marque graphique : « FlowView » est composé en Inter 600 dans la maquette, en attendant `logo-design`.

## Art Direction *(à ajouter par art-direction)*

## Icon Library — as adopted *(à ajouter)*
Phosphor Regular prévu (voir 3.4).

## Motion System — as built *(à ajouter par motion-design)*

## Application Notes *(à ajouter par web-design)*
