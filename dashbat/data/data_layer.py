import pandas as pd

from dashbat.data.data_types import DATASET_NAMES, DatasetName
from dashbat.data.datasets import Dataset

from dashbat.data.data_preparation import (
    P_NUM_CONTRIBUTION_PER_THEME,
    P_NUM_CONTRIBUTION_OVER_TIME,
    P_NUM_CONTRIBUTION_PER_TYPE,
    P_MAP_PER_THEME,
)

NUM_CONTRIBUTION_PER_THEME = pd.read_pickle(P_NUM_CONTRIBUTION_PER_THEME)
NUM_CONTRIBUTION_OVER_TIME = pd.read_pickle(P_NUM_CONTRIBUTION_OVER_TIME)
NUM_CONTRIBUTION_PER_TYPE = pd.read_pickle(P_NUM_CONTRIBUTION_PER_TYPE)
MAP_PER_THEME = dict()
for dataset_name in Dataset.get_dataset_names():
    MAP_PER_THEME[dataset_name] = pd.read_pickle(
        str(P_MAP_PER_THEME).format(dataset_name=dataset_name)
    )


def get_num_contribution_per_theme() -> pd.DataFrame:
    """
    Return a dataframe with the number of contributions per theme
    - Thème
    - Nombre contributions
    """
    return NUM_CONTRIBUTION_PER_THEME


def get_num_contribution_over_time() -> pd.DataFrame:
    """
    Return a dataframe with the number of contributions per theme and over time
    - Date
    - Thème
    - publishedAt
    - Nombre contributions
    - authorType
    - authorZipCode
    """
    return NUM_CONTRIBUTION_OVER_TIME


def get_num_contribution_per_type() -> pd.DataFrame:
    """
    Return a dataframe with the number of contributions per type of contributor
    - Type de contributeur
    - publishedAt
    - Nombre contributions
    - authorZipCode
    - Thème
    """
    return NUM_CONTRIBUTION_PER_TYPE


def get_map_per_theme(dataset_name: DatasetName) -> pd.DataFrame:
    """
    Return a dataframe with the number of contributions per departement.
    An aggregate allows to get the number of contributions per 1 000 inhabitants.
    - Departement
    - Nombre contributions
    - DEP
    - NBARR
    - NBCAN
    - NBCOM
    - PMUN
    - PTOT
    - Contributions 1 000 habitants
    """
    return MAP_PER_THEME[dataset_name]
