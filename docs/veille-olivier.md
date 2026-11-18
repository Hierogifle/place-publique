# Veille : compléments et vérifications d'Olivier (Q4, Q6, Q7, Q8)

*Version 1 · 2026-11-18 · complète `veille.md` sans le remplacer. Chaque point est étiqueté : **[Fait]** (page ouverte et lue le 18/11/2026), **[Fait Romuald]** (relevé dans le dépôt, non revérifié), **[Hypothèse]** (à tester), **[À valider]** (à relire ou à trancher). Chapitre juridique : Olivier n'est pas juriste, relecture du formateur demandée.*

Questions défendues par Olivier : **Q4, Q6, Q7, Q8** (le sujet exige au moins 2 questions par membre). Chaque auteur reformule avec ses mots avant la soutenance.

---

## Q4 · Architecture : ce que j'ajoute

**Limites par maillon, avec parade**

| Maillon | Limite | Parade |
|---|---|---|
| Planificateur | Un job est « manqué » s'il ne part pas à l'heure ; `misfire_grace_time` fixe la tolérance, `coalesce` regroupe les exécutions en attente, `max_instances` vaut 1 par défaut. Avec un stockage persistant, il faut un identifiant explicite et `replace_existing=True`, sinon une copie du job est créée à chaque redémarrage. Un job store ne doit jamais être partagé entre plusieurs schedulers. [Fait, [guide APScheduler 3.x](https://apscheduler.readthedocs.io/en/3.x/userguide.html)] | Un seul planificateur, hors des workers gunicorn (déjà noté dans `veille.md`) |
| Affichage | Avec `spanGaps` à false, un point `null` coupe la ligne. [Fait, [Chart.js](https://www.chartjs.org/docs/latest/charts/line.html)] | Stocker « pas de donnée » en valeur absente, jamais 0 ; le rejeu de 48 points le prouve |
| Inférence | YOLO26n : 38,9 ms par image en CPU ONNX ; YOLO26x : 525,8 ms. [Fait, [Ultralytics](https://docs.ultralytics.com/tasks/detect/)] | Sur le socle, la latence ne compte pas ; la résolution et le découpage en tuiles pèsent plus |
| Comptage de flux | Les compteurs IN/OUT reposent sur un suivi image par image ; la page ne détaille pas la réattribution des identifiants, et des commentaires de la communauté signalent des identifiants réattribués après occultation. [Fait, [guide de comptage](https://docs.ultralytics.com/guides/object-counting/)] | Le flux du mode direct aura sa propre marge d'erreur et son propre seuil (fiche 0019) |
| Déploiement | Plus de 20 formats d'export ; la page recommande de mesurer sur le matériel cible. [Fait, [Ultralytics](https://docs.ultralytics.com/guides/model-deployment-options/)] | Image Docker CPU livrée ; GPU de Romuald pour l'entraînement et le mode direct (idée I-08) |

**Rappel important :** « une image toutes les 5 minutes ne permet pas de suivi » est vrai pour le socle seulement. Le mode direct avec suivi est un objectif ferme (fiche 0019).

---

## Q6 · Dérive : ce que j'ajoute

**Vocabulaire et méthodes [Fait, [Evidently](https://www.evidentlyai.com/ml-in-production/data-drift)]** : dérive des données (distribution des entrées) contre dérive de concept (relation entrée-cible) ; tests (Kolmogorov-Smirnov, Chi-deux, trop sensibles sur de gros volumes), distances (Wasserstein, Jensen-Shannon, PSI), règles simples. Evidently conseille de vérifier la qualité des données avant tout ré-entraînement. La revue de [Lu et al.](https://arxiv.org/abs/2004.05785) distingue détecter, comprendre, s'adapter. [Fait]

**Propositions pour FlowView [Hypothèse, seuils à calibrer]**

1. Comparer le compte moyen **au même jour de la semaine et à la même heure** (`docs/stations.md` : le samedi est le jour des arrivées et des départs, les vacances scolaires sont le facteur principal). Une « dérive » peut être simplement l'ouverture du 12 décembre.
2. Traiter les caméras givrées (Arpette, Aiguille Rouge le 18/11) comme « inexploitables », pas comme une dérive du modèle.
3. Mesurer la vraie erreur sur un échantillon ré-annoté (S1 à S7), seul déclencheur de ré-entraînement.
4. La saison 2026-2027 peut changer l'angle, l'équipement et les habitudes : le jeu figé vient de 2025-2026.

---

## Q7 · RGPD et AI Act : ce que j'ajoute

**Dates et textes vérifiés le 18/11/2026**

| Texte | Ce qu'il dit | Statut |
|---|---|---|
| [CNIL, position de juillet 2022](https://www.cnil.fr/cameras-dites-augmentees-dans-les-espaces-publics-la-position-de-la-cnil) | Le comptage de piétons est cité comme exemple de caméra augmentée ; base légale au cas par cas ; proportionnalité à démontrer ; suppression quasi immédiate des images sources recommandée ; droit d'opposition limitable seulement pour une finalité statistique (résultats agrégés et anonymes, sans vocation opérationnelle) | [Fait] |
| [CNIL, fiche du 18/11/2024](https://cnil.fr/fr/cameras-augmentees-espaces-publics) | Mesure de fréquentation possible si le traitement produit uniquement des statistiques agrégées et anonymes, **sans finalité opérationnelle (pas d'alerte, pas de blocage d'accès)** | [Fait] |
| [CEPD, lignes directrices 3/2019](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en) | La page officielle indique une adoption de la version finale le **30 janvier 2020** ; `veille.md` écrit 29/01/2020. Seules les métadonnées de la page ont été lues | [Fait] + [À valider] : trancher dans le PDF |
| [AI Act, article 5](https://artificialintelligenceact.eu/article/5/) | Applicable depuis le 2 février 2025 ; interdit la catégorisation biométrique déduisant race, opinions politiques, etc., et l'identification biométrique à distance en temps réel dans l'espace public à des fins répressives, sauf exceptions encadrées | [Fait] |
| [AI Act, annexe III](https://artificialintelligenceact.eu/annex/3/) | Point 1 : identification biométrique à distance, catégorisation biométrique, reconnaissance des émotions. Le simple comptage de personnes n'y figure pas | [Fait] |
| [Règlement (UE) 2026/1744](https://donneespersonnelles.fr/omnibus-numerique-ia) | Publié au JOUE le 24/07/2026, en vigueur le 27/07/2026 ; haut risque de l'annexe III reporté au 02/12/2027, annexe I au 02/08/2028 ; l'article 5 n'est pas touché. Source secondaire | [Fait] à recouper avec le JOUE |
| [Loi Ripost n° 2026-798](https://www.leto.legal/news/loi-ripost-videoprotection-algorithmique-2030-conseil-constitutionnel-2026) | Prolonge au 31/12/2030 l'expérimentation de vidéoprotection algorithmique (sécurité, événements) ; décision 2026-915 DC du 14/08/2026. Source secondaire | [Fait] à recouper |

**Point à ajouter au « point ouvert » de `veille.md` Q7 :** la fiche CNIL de 2024 formule la condition de la mesure de fréquentation par l'absence d'alerte. Cela renforce la tension déjà identifiée : FlowView alerte. L'option A (comptage statistique séparé d'une alerte qui ne lit que les agrégats) reste fragile si l'alerte est quasi immédiate [Hypothèse]. À faire trancher par le formateur.

**Piège de date :** la fiche CNIL de novembre 2024 donne le 31 mars 2025 comme fin de l'expérimentation JOP. C'est dépassé (prolongée jusqu'au 31/12/2030 par la loi Ripost, d'après la source secondaire). Le cadre JOP/Ripost concerne la sécurité, pas un tableau d'affluence : ne pas le citer comme base légale de FlowView.

---

## Q8 · Éthique : ce que j'ajoute

- **Wilson et al.** ([arXiv 1902.11097](https://arxiv.org/abs/1902.11097)) : le résumé lu ne donne aucun chiffre, utilise un seul jeu (BDD100K) et deux groupes de tons de peau, et écrit que ni l'heure ni l'occlusion n'expliquent l'écart. À citer comme alerte, pas comme preuve pour des skieurs. [Fait]
- **Biais propres à la montagne à mesurer [Hypothèse]** : enfants en cours de ski, snowboardeurs, tenues très sombres ou très claires, groupes serrés. L'attribut `tenue` de la fiche 0027 permet de les mesurer **sans classer les personnes**.
- **Objection et réponse :** « le résultat est agrégé, donc pas d'enjeu ». Réponse : le même pipeline avec un seuil et une alerte devient opérationnel (Q7). Le garde-fou est la finalité écrite et la limite de périmètre, pas la technique.
- **Limite à écrire dans `conformite.md`** : les images d'archive sont utilisées sans accord des titulaires, dans le cadre pédagogique (fiche 0021). C'est une limite, pas une couverture.

---

## Chiffres de `veille.md` Q1 que j'ai recoupés

| Modèle | mAP COCO | Vitesse | Source ouverte |
|---|---|---|---|
| YOLO26n / s / m / l / x | 40,9 / 48,6 / 53,1 / 55,0 / 57,5 | CPU ONNX : 38,9 / 87,2 / 220,0 / 286,2 / 525,8 ms | [Ultralytics](https://docs.ultralytics.com/tasks/detect/) |
| RF-DETR N / S / M / L | 48,4 / 53,0 / 54,7 / 56,5 | T4 TensorRT FP16 : 2,3 / 3,5 / 4,4 / 6,8 ms | [RF-DETR](https://rfdetr.roboflow.com/latest/) |
| RF-DETR XL / 2XL | 58,6 / 60,1 | 11,5 / 17,2 ms | licence PML 1.0 : [licences](https://roboflow.com/model-licenses/rf-detr) |
| RT-DETR R50 / R101 | 53,1 / 54,3 | 108 / 74 FPS (T4) | [arXiv 2304.08069](https://arxiv.org/abs/2304.08069) |

Non revérifiés : Faster R-CNN R50-FPN (40,2), DETR R50 (42,0), YOLO11n/s, RT-DETR R18.

**Point supplémentaire pour Q1 [Hypothèse forte]** : les images d'archive font 12 000 à 18 543 px de large. En 640 px, la réduction est d'un facteur 19 à 29 : le découpage en tuiles et la résolution sont à tester avant de comparer des modèles (étape 1.5).
