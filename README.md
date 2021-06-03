# Le Grand Dashbat

## Installation

Création d'un env virtuel, et installation des requirements :

    mkvirtualenv -a . --python=3.8 grand-dashbat
    pip install -r requirements.txt
    pre-commit install

Il faut lancer la préparation de la données utilisée par l'application :

    PYTHONPATH='.:$PYTHONPATH' python dashbat/data_preparation.py

On peut maintenant lancer l'application :

    PYTHONPATH='.:$PYTHONPATH' python dashbat/main.py

Le lancement de l'application permet de choisir le port et l'hôte :

    PYTHONPATH='.:$PYTHONPATH' python dashbat/main.py --host 0.0.0.0 --port 8888


## Load dataset

```python
from app.datasets import Dataset

transition_dataset = Dataset('transition')
print(f'Nombre de contributions : {transition_dataset.data.shape[0]}') # 351313
```

## Ressources

- Whimsical : https://whimsical.com/le-grand-dashbat-DLFcRcfHaZCoKrHWhgG47x
- Data le grand débat : https://www.data.gouv.fr/en/datasets/donnees-ouvertes-du-grand-debat-national/
