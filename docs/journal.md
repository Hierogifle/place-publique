# Journal de bord — FlowView · Place Publique

Points d'étape, du plus récent au plus ancien. Les **choix** et leur justification sont dans [decisions/](decisions/README.md).

## 2026-11-17 — Lancement
- Kick-off du projet. Soutenance le **15 décembre 2026**, avec une période en entreprise au milieu.
- Dépôt : sujet rangé dans `sujet/` (→ [0001](decisions/0001-sujet-et-guide-formateur.md)), branches `Romuald` et `Olivier` créées (→ [0002](decisions/0002-branches-personnelles.md)).
- Analyse du sujet, du PowerPoint et du guide formateur.
- Choix du contexte : les Arcs (→ [0003](decisions/0003-station-les-arcs.md)). Constat : le domaine n'ouvre que le 12 décembre.
- DA : installation des skills (→ [0007](decisions/0007-outillage-direction-artistique.md)), marque FlowView (→ [0004](decisions/0004-nom-de-marque-flowview.md)), images Unsplash/Pexels (→ [0005](decisions/0005-imagerie-unsplash-pexels.md)), panel concurrentiel (→ [0006](decisions/0006-panel-concurrentiel.md)).
- Démarrage de la stratégie de marque (`.agents/brand-strategy.md`).
- Stratégie de marque : première émotion « serein », ennemi principal « l'écran » (→ [0008](decisions/0008-emotion-serein-ennemi-ecran.md)).
- Stratégie de marque : trois sérénités selon le moment de la journée (→ [0009](decisions/0009-trois-serenites-de-la-journee.md)), empilées en une seule identité (→ [0010](decisions/0010-empiler-les-trois-serenites.md)).
- Stratégie de marque : trio d'émotions validé — serein, respecté, en confiance (→ [0011](decisions/0011-trio-emotionnel.md)). Prochaine étape : les muses.
- Muses proposées par Romuald (bois, Firewatch, vieux sage, berceuse, silence) ; planche de 23 images construite (`.agents/stylescapes/muse-board.html`).
- Muses retenues sur la planche (→ [0012](decisions/0012-muses-retenues.md)) ; sélection v2 en tête de planche.
- Socle fixe et marge de liberté validés (→ [0013](decisions/0013-socle-fixe-et-marge.md)).
- Trois pistes visuelles construites (`.agents/stylescapes/stylescapes.html`) : La Vigie, Le Refuge, Les Crêtes. Contrôle design-taste : 0 erreur, 3 avertissements (polices Google, nombre de sur-titres). Choix en attente.
- Romuald penche pour Les Crêtes et regrette la chaleur du Refuge ; proposition d'une piste 04 « Les Crêtes, vues du refuge ». Idées produit notées dans [idees.md](idees.md) (point du matin, fluidité, panne, report sur les pistes, risque d'accident).
- Freins acceptés (report sur les pistes, risque d'accident). Nouvelles idées : station en 3D explorable (I-06), flux en direct avec détections (I-07).
- GPU disponible chez Romuald (I-08 : GPU pour l'entraînement, CPU pour la livraison). Anonymisation par flou après détection acceptée.
- Piste 04 « Les Crêtes, vues du refuge » construite (`.agents/stylescapes/piste-04.html`) : vrai relief des Arcs en 3D (MapLibre + tuiles Terrarium), remontées et pistes OpenStreetMap extraites le 17/11 (`.agents/stylescapes/data/arcs-osm.geojson`, ODbL), caméra floutée, vue de côté, modes Préparer / Suivre / Alerter. Contrôle design-taste : 0 erreur.
- Retour de Romuald : interface mal ordonnée et peu belle (pas la faute de Flask, qui ne fait que servir le HTML). Piste 04 refaite en v2 : l'image analysée avec cadres et flou devient l'élément principal, la 3D sert à choisir une zone, mode clair et sombre. Vérifiée sur ordinateur et mobile, sans erreur.
- Piste 04 v2 choisie (→ [0014](decisions/0014-direction-artistique-piste-04.md)). `.agents/design.md` rédigé (système, tokens, contrastes vérifiés, états, vocabulaire, sources) et résumé dans `.agents/brand.md`. Contraste de la pastille d'alerte corrigé (`#A52A21`). En attente de validation avant tout code front.
- Références d'interface de Romuald (CRM 3D garage / immobilier / bâtiment). Piste 04 v3 « maquette » construite (`.agents/stylescapes/maquette.html`) : relief réel des Arcs en maquette three.js, foules proportionnelles, pastilles, panneau de détail avec image floutée, frise du jour sur fond de crête, colonnes de suivi (→ [0015](decisions/0015-maquette-3d-et-ecran-crm.md)). design.md complété (§9).
- **DA validée par Romuald** : `.agents/design.md` et la maquette 3D comme écran principal. Fin de la phase DA (hors logo et photos de slides). Prochaines étapes : plan d'attaque, configuration GitHub, palier 1.
