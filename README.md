# TP POO EI3

## Forker le projet

Pour forker le projet, cliquez sur le bouton "Fork" en haut à droite
de la page en choississant le namespace correspondant à votre groupe
de TP.

## Cloner le projet

Pour cloner le projet, exécutez la commande suivante :

```bash
git clone https://<nom-utilisateur>@gitlabsu.sorbonne-universite.fr/...
```

Saisissez votre mot de passe Gitlab.


## Exécuter un `main.py`

Pour exécuter un fichier `main.py`, exécutez la commande suivante :

```bash
python tp1/main.py
# ou
python3 tp1/main.py
```

## Pytest

`pytest` est un framework de test pour Python. Pour l'installer, exécutez la commande suivante :

```bash
pip install pytest
```

Pour exécuter les tests, exécutez la commande suivante :

```bash
pytest
```

Pour rajouter un fichier de test, créez un fichier `test_<nom-du-fichier>.py` dans le dossier `tests/`.
Les fonctions de test doivent commencer par `test_`.


Plus d'informations sur `pytest` [ici](https://docs.pytest.org/en/stable/).

## Attendus sur les commits

Des commits réguliers nous permettent de suivre l'avancement de votre travail et de vous aider si besoin. Voici quelques règles à respecter :

- Les messages de commit doivent être courts et explicites.
- Les commits doivent être "atomiques" : un commit = une fonctionnalité ou une correction de bug.
- En une séance de TP, il est attendu un minimum de 3 commits.

## Workflow usuel avec Git

### Travail basique

1. Récupérer les dernières modifications du dépôt distant :

```bash
git pull
```

2. Ajouter les fichiers modifiés ou créés à l'index :

```bash
git add <fichier1> <fichier2> ...
```

3. Valider les modifications :

```bash
git commit -m "Message de commit"
```

4. Envoyer les modifications sur le dépôt distant :

```bash
git push
```

### Travailler avec des branches

Utiliser des branches permet de travailler sur des fonctionnalités ou des correctifs sans impacter le code principal. C'est une bonne pratique pour travailler en équipe, et obligatoire dans la plupart des projets professionnels.

1. Créer une branche :

```bash
git checkout -b <nom-de-branche>
```
ou
```bash
git switch -c <nom-de-branche>
```

On a créé et basculé sur la branche `<nom-de-branche>`.

2. Faire des modifications, ajouter, valider et pousser les modifications comme d'habitude.

3. Revenir sur la branche principale :

```bash
git checkout main
```
ou
```bash
git switch main
```

4. Fusionner la branche `<nom-de-branche>` avec la branche principale :

```bash
git merge <nom-de-branche>
```

5. Pousser les modifications sur le dépôt distant :

```bash
git push
```

Pour un exemple complet et complexe de workflow avec Git, voir [ce tutoriel](https://nvie.com/posts/a-successful-git-branching-model/).


## Liens utiles

- [Documentation Python](https://docs.python.org/3/)
- [Bonnes pratiques Python (codestyle)](https://www.python.org/dev/peps/pep-0008/)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Git](https://git-scm.com/doc)
- [Markdown](https://guides.github.com/features/mastering-markdown/)

## Contact

Téo Lohrer - teo.lohrer@sorbonne-universite.fr
