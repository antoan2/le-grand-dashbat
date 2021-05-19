from dataclasses import dataclass, field
import pandas as pd

from data_types import DatasetName
from datasets import Dataset


def get_num_contribution_per_theme() -> pd.DataFrame:
    rows = []
    for dataset_name in Dataset.get_dataset_names():
        dataset = Dataset(dataset_name)
        rows.append([dataset.name, dataset.num_contribution])
    return pd.DataFrame(data=rows, columns=["Thème", "Nombre contribution"])
