# Dossier tests partagé entre Holberton pour le test du projet : 0x0C. Python - Almost a circle

Merci de prendre connaissance des bonnes pratiques ici

</br>

## soumis à évolution

Création 04/02/2022

</br>

## Participer aux tests

Se déplacer dans sur home :

<code>cd</code>

</br>
cloner le repo :

<code>git clone git@github.com:tlenormand/holberton_tests.git</code>

</br>
créer sa branche à son nom :

<code>git branch Thomas</code>

</br>
Faire les tests nécessaires en local.

Ne pas oublier, la branche main peut évoluer entre temps.

Une fois le fichier mis à jour, le push sur sa branche :

<code>git push -u origin Thomas</code>

</br>
sur github, créer un merge entre notre branche et la branche main

</br>
sur sa machine, ne pas oublier de mettre à jour la branche main puis la sienne :)

</br>

## Arborescence :

0x0C. Python - Almost a circle
```
.
├── models
│   ├── __init__.py__
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
|   
└── tests
    └── test_models
        ├── __init__.py
        ├── test_base.py
        ├── test_rectangle.py
        └── test_square.py
```

</br>

Important : créer un fichier \_\_init\_\_.py dans le dossier _models_ et _test_models_ afin de pouvoir lancer les tests.

</br>

## Commandes :

Se déplacer dans 0x0C-python-almost_a_circle :

<code>cd 0x0C-python-almost_a_circle</code>

</br>
Pour lancer un test unitaire, utiliser :

<code>python3 -m unittest tests/test_models/\<nom du fichier></code>

</br>
Pour tester tous les fichiers, utiliser :

<code>python3 -m unittest discover tests</code>

