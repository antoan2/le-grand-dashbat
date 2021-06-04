# Le Grand Dashbat

## Introduction

Cette application démo a été réalisée dans le cadre des ateliers [BlueHats](https://github.com/blue-hats/ateliers)
le [04/06/2021](https://github.com/blue-hats/ateliers/blob/main/ateliers.org#4-juin--pr%C3%A9sentation-du-framework-dash-plotlyjs-react-et-flask)
afin de présenter le framework [Dash](https://plotly.com/dash/).

Contributeurs :
    - [Jordan Munoz](https://github.com/jmunozz)
    - [Line Rahal](https://github.com/lrahal)
    - [Rémi Delbouys](https://github.com/remidbs)
    - [Antoine Biard](https://github.com/antoan2)

Le code est disponible sur github : [le-grand-dashbat](https://github.com/antoan2/le-grand-dashbat/)

### Live code

Dans le cadre de l'atelier BlueHats, un live code a été réalisé qu'il est possible de retracer en comparant la branche `master`
et la branche `live-code-final-state` : [déroulé du live code](https://github.com/antoan2/le-grand-dashbat/compare/live-code-final-state)

## Installation

Création d'un env virtuel, et installation des requirements :

    mkvirtualenv -a . --python=3.8 grand-dashbat
    pip install -r requirements.txt
    pre-commit install

Il faut lancer la préparation de la données utilisée par l'application :

    PYTHONPATH='.:$PYTHONPATH' python dashbat/data/data_preparation.py

On peut maintenant lancer l'application :

    PYTHONPATH='.:$PYTHONPATH' python dashbat/main.py

Le lancement de l'application permet de choisir le port et l'hôte :

    PYTHONPATH='.:$PYTHONPATH' python dashbat/main.py --host 0.0.0.0 --port 8888

## Dataset du grand débat

```python
from app.datasets import Dataset

transition_dataset = Dataset('transition')
print(f'Nombre de contributions : {transition_dataset.data.shape[0]}') # 351313
```

## Ressources

- Whimsical : https://whimsical.com/le-grand-dashbat-DLFcRcfHaZCoKrHWhgG47x
- Data le grand débat : https://www.data.gouv.fr/en/datasets/donnees-ouvertes-du-grand-debat-national/
