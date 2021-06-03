import pandas as pd

from dashbat.data_types import DATASET_NAMES, DatasetName
from dashbat.datasets import Dataset

from dashbat.data_preparation import (
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
    return NUM_CONTRIBUTION_PER_THEME


def get_num_contribution_over_time() -> pd.DataFrame:
    return NUM_CONTRIBUTION_OVER_TIME


def get_num_contribution_per_type() -> pd.DataFrame:
    return NUM_CONTRIBUTION_PER_TYPE


def get_map_per_theme(dataset_name: DatasetName) -> pd.DataFrame:
    return MAP_PER_THEME[dataset_name]
