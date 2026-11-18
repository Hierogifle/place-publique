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
On travaille en **deux temps** (fiche [0028](docs/decisions/0028-chacun-sa-branche-puis-branches-de-feature.md)).

### Maintenant, pendant le développement de l'application : chacun sa branche
```
main          ← ce qui marche et qu'on peut montrer (protégée, déployée)
  └─ dev      ← l'application se construit ici (protégée)
      ├─ Romuald   ← la branche de Romuald
      └─ Olivier   ← la branche d'Olivier
```
- **Chacun travaille sur sa branche**, `Romuald` ou `Olivier`, tranquillement et à son rythme.
- Quand un travail est prêt, on ouvre une **PR de sa branche vers `dev`**.
- **On ne pousse jamais directement sur `main` ni sur `dev`** : tout passe par une pull request.

### Plus tard, une fois l'application développée : branches de feature
```
dev
  ├─ feature/capture-webcams   ← une branche courte par fonctionnalité
  ├─ fix/pas-de-donnee
  └─ docs/veille-q1
```
- Une branche courte par fonctionnalité ou correction, créée depuis `dev`. Préfixes : `feature/`, `fix/`, `docs/`, `chore/` (configuration, outillage).
- On bascule dans ce mode quand on le décide ensemble. Ce n'est pas encore le cas.

## Le cycle de travail (maintenant)
Une seule fois au départ, ou quand sa branche est en retard sur `dev` :
```bash
git fetch origin
git switch Olivier                         # ou Romuald
git merge origin/dev                       # récupérer ce qui est déjà dans dev
git push
```
Ensuite, au quotidien :
```bash
git switch Olivier                         # ou Romuald
# ... travailler, puis :
git add <fichiers>
git commit -m "feat: compter les personnes par classe"
git push
```
1. Quand un travail est prêt : ouvrir une PR **`Olivier` → `dev`** (ou `Romuald` → `dev`) ; le modèle de PR s'affiche tout seul.
2. La CI tourne ; l'autre relit et commente.
3. Quand c'est vert et relu : **Merge**. **On ne supprime pas** sa branche personnelle.
4. Après chaque fusion dans `dev`, chacun récupère `dev` sur sa branche (`git merge origin/dev`) pour ne pas trop s'en éloigner.
5. En fin de palier : une PR **`dev` → `main`**. Elle déclenche le déploiement.

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
