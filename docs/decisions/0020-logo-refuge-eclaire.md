# 0020 — Logo : « le refuge éclairé »

- **Date :** 2026-11-17
- **Statut :** Acceptée
- **Décideurs :** Romuald

## Contexte
Jusqu'ici, FlowView n'avait pas de logo : le nom était écrit en Inter demi-gras dans les maquettes. Romuald a demandé « un truc mieux ».

Contraintes posées par le rayon des concurrents, logos vus le 17/11/2026 ✅ :
- **Wintics :** un « W » en dents de scie, qui évoque des sommets.
- **Viziosense :** un œil dans le « o ».
- **Safari AI :** un glyphe vert dans un cadre.

Notre outillage est de niveau 0 : pas de générateur d'images, donc les esquisses sont dessinées en code.

## Décision
**Piste B1 « le refuge éclairé »** : la masse d'une montagne à un seul sommet, et une seule fenêtre carrée découpée en creux. Quelqu'un veille.
- La montagne est en ardoise, le nom « FlowView » en encre brune. Le nom est composé en Inter Display SemiBold puis vectorisé.
- Le point du « i » est un carré, l'écho de la fenêtre.
- Les fichiers sont verrouillés dans `.agents/assets/logo/` (SVG, PNG, JPEG, ICO, toutes les variantes). On les place, on ne les redessine jamais.

## Options écartées
- **A2, la crête et sa marge** (ma première recommandation) : une fois dessinée, elle se lit comme une icône de graphique, presque celle de notre propre interface (Phosphor ChartLine).
- **X3, la crête en zigzag :** trop proche du logo de Wintics.
- **X1, la tour de guet :** on y voit un pylône, donc l'univers de la surveillance.
- **X2, l'anneau gradué :** on y voit une boussole ou une icône de réglages.
- **C1, le nom seul :** faible en icône d'onglet. On en garde le point carré.

## Conséquences
- Le logo porte l'émotion n°1 (serein) et la règle « une seule lumière ». La fenêtre n'est jamais rouge : le rouge reste réservé à l'alerte.
- **Contrôle SAD :**
  - simple ✅ ;
  - approprié ✅ ;
  - distinct face aux concurrents ✅ ;
  - **distinct hors secteur : non évalué.** La recherche par image (Google Lens, Pinterest, base de marques de l'OMPI) n'a pas été lancée. La montagne avec chalet est un motif courant. À faire avant tout usage public hors école.
- Une passe d'un graphiste reste souhaitable. Ce n'est pas une recherche d'antériorité de marque.
- Au palier 2, le front utilisera `logo-lockup.svg` et `favicon.ico`.

## Sources
- Logos concurrents : <https://www.wintics.com>, <https://www.viziosense.com>, <https://www.getsafari.ai/ski-resorts> (consultés le 17/11/2026)
- Inter 4.1 (SIL OFL 1.1) : <https://github.com/rsms/inter/releases/tag/v4.1>
- Planche : `.agents/stylescapes/logo.html` ; esquisses : `.agents/stylescapes/logo-sketches.html`
