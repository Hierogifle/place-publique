# Travailler à deux sur FlowView · Place Publique

Ce guide explique comment on avance sur le dépôt sans se marcher dessus, et comment une modification arrive jusqu'à l'application qui tourne.

## Le vocabulaire en 30 secondes
| Mot | Ce que ça veut dire |
|---|---|
| **commit** | Une photo de ton travail, enregistrée sur ton PC avec un message |
| **push** | Envoyer tes commits sur GitHub |
| **pull** | Récupérer sur ton PC ce que l'autre a envoyé sur GitHub |
| **branche** | Une ligne de travail séparée ; on peut en avoir plusieurs en parallèle |
| **pull request (PR)** | Une demande pour fusionner une branche dans une autre ; l'autre relit, la CI vérifie |
| **merge** | La fusion, une fois la PR acceptée |
| **CI** (intégration continue) | GitHub lance les tests et la construction Docker à chaque PR et à chaque push sur `dev` / `main` |
| **CD** (déploiement continu) | À chaque push sur `main`, GitHub publie une nouvelle image Docker de l'application |

## Les branches
```
main      ← ce qui marche et qu'on peut montrer (protégée, déployée)
  └─ dev  ← l'intégration : on y rassemble le travail des deux (protégée)
      ├─ feature/capture-webcams   ← une branche courte par tâche
      ├─ feature/baseline-yolo
      ├─ fix/pas-de-donnee
      └─ docs/veille-q1
```
- **On ne pousse jamais directement sur `main` ni sur `dev`** : tout passe par une pull request.
- **Une branche = une tâche du plan** (`docs/plan.md`), de quelques heures à deux jours. Préfixes : `feature/`, `fix/`, `docs/`, `chore/` (configuration, outillage).
- Les branches personnelles `Romuald` et `Olivier` ne servent plus (voir `docs/decisions/0017`).

## Le cycle d'une tâche
```bash
git switch dev
git pull                                   # récupérer le travail de l'autre
git switch -c feature/ma-tache             # créer sa branche
# ... travailler, puis :
git add <fichiers>
git commit -m "feat: compter les personnes par classe"
git push -u origin feature/ma-tache        # GitHub affiche le lien pour ouvrir la PR
```
1. Ouvrir la PR **vers `dev`** (le modèle de PR s'affiche tout seul).
2. La CI tourne ; l'autre relit et commente.
3. Quand c'est vert et relu : **Merge**, puis supprimer la branche.
4. En fin de palier : une PR **`dev` → `main`**. Elle déclenche le déploiement.

## Les messages de commit
`type: ce que fait le commit`, au présent, en français :
- `feat:` nouvelle fonctionnalité · `fix:` correction · `docs:` documentation · `test:` tests · `chore:` configuration, outillage · `refactor:` réorganisation sans changement de comportement.

Chacun commite **son** travail : la note est ajustée d'après l'historique Git.

## Ce qui ne va jamais dans Git
- Images brutes de webcams, captures, jeux de données téléchargés (`data/raw/`, `data/captures/`, `data/reference/images/`).
- Le guide formateur (`sujet/non_versionne/`).
- Secrets, mots de passe, clés (`.env`).
- Les sorties d'expériences MLflow (`mlruns/`).

## Le déploiement
- **CI** (`.github/workflows/ci.yml`) : tests et lint à chaque PR ; construction de l'image Docker dès qu'un `Dockerfile` existe.
- **CD** (`.github/workflows/cd.yml`) : à chaque push sur `main`, l'image est publiée sur `ghcr.io/hierogifle/place-publique` (étiquettes `latest` et le numéro court du commit).
- **Sur la machine qui fait tourner l'application** (un de nos PC pour la démo) :
  ```bash
  docker compose pull && docker compose up -d
  ```
  récupère la dernière image et redémarre l'application. Le sujet n'exige pas de déploiement automatique sur un serveur : on s'arrête là, et `architecture.md` décrira la version production.
