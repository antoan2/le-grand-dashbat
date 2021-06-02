from collections import Counter
from typing import cast

import pandas as pd

from dashbat.datasets import Dataset


def get_num_contribution_per_theme() -> pd.DataFrame:
    rows = []
    for dataset_name in Dataset.get_dataset_names():
        dataset = Dataset(dataset_name)
        rows.append([dataset.name, dataset.num_contribution])
    return pd.DataFrame(data=rows, columns=["Thème", "Nombre contribution"])


def _get_merged_dataset() -> pd.DataFrame:
    keys = ["publishedAt", "authorId", "authorType", "authorZipCode"]
    dataframes = []
    for dataset_name in Dataset.get_dataset_names():
        local_df = Dataset(dataset_name).data[keys]
        local_df["Catégorie"] = dataset_name
        dataframes.append(local_df)
    return cast(pd.DataFrame, pd.concat(dataframes))


def get_num_contribution_over_time() -> pd.DataFrame:
    merged = _get_merged_dataset()
    merged["Date"] = merged.publishedAt.apply(lambda x: x.date())
    res = merged.groupby(["Date", "Catégorie"]).count().reset_index()
    return res.rename(columns={"authorId": "Nombre contributions"})


def get_num_contribution_per_type() -> pd.DataFrame:
    merged = _get_merged_dataset()
    res = merged.groupby(["authorType"]).count().reset_index()
    return res.rename(
        columns={
            "authorId": "Nombre contributions",
            "authorType": "Type de contributeur",
        }
    )


def get_map_per_theme(dataset_name: str) -> pd.DataFrame:
    dataset = Dataset(dataset_name)
    zipcode_contributions = Counter(dataset.data.authorZipCode.apply(lambda x: str(x)[:2]))

    return pd.DataFrame(
        data=list(zipcode_contributions.items()),
        columns=["Departement", "Nombre contributions"],
    )
