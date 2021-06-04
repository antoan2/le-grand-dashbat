from collections import Counter
from typing import cast

import pandas as pd

from dashbat.data.data_types import DatasetName
from dashbat.data.datasets import Dataset
from dashbat.data.data_fetch import _DATA_FOLDER

P_NUM_CONTRIBUTION_OVER_TIME = _DATA_FOLDER.joinpath("num_contribution_over_time.pkl")
P_NUM_CONTRIBUTION_PER_TYPE = _DATA_FOLDER.joinpath("num_contribution_per_type.pkl")
P_NUM_CONTRIBUTION_PER_THEME = _DATA_FOLDER.joinpath("num_contribution_per_time.pkl")
P_MAP_PER_THEME = _DATA_FOLDER.joinpath("map_per_theme_{dataset_name}.pkl")


def load_population_per_departement() -> pd.DataFrame:
    population_per_departement = pd.read_csv(
        _DATA_FOLDER.joinpath("population_per_departement.csv")
    )
    population_per_departement["CODDEP"] = population_per_departement["CODDEP"].apply(
        lambda x: x.zfill(2)
    )
    return population_per_departement


def prepare_num_contribution_per_theme() -> pd.DataFrame:
    rows = []
    for dataset_name in Dataset.get_dataset_names():
        dataset = Dataset(dataset_name)
        rows.append([dataset.name, dataset.num_contribution])
    return pd.DataFrame(
        data=rows,
        columns=[
            "Thème",
            "Nombre contributions",
        ],  # , dtype={"Thème": str, "Nombre de contributions": str}
    )


def _get_merged_dataset() -> pd.DataFrame:
    keys = ["publishedAt", "authorId", "authorType", "authorZipCode"]
    dataframes = []
    for dataset_name in Dataset.get_dataset_names():
        local_df = Dataset(dataset_name).data[keys]
        local_df["Thème"] = dataset_name
        dataframes.append(local_df)
    return cast(pd.DataFrame, pd.concat(dataframes))


def prepare_num_contribution_over_time() -> pd.DataFrame:
    merged = _get_merged_dataset()
    merged["Date"] = merged.publishedAt.apply(lambda x: x.date())
    res = merged.groupby(["Date", "Thème"]).count().reset_index()
    return res.rename(columns={"authorId": "Nombre contributions"})


def prepare_num_contribution_per_type() -> pd.DataFrame:
    merged = _get_merged_dataset()
    res = merged.groupby(["authorType"]).count().reset_index()
    return res.rename(
        columns={
            "authorId": "Nombre contributions",
            "authorType": "Type de contributeur",
        }
    )


def prepare_map_per_theme(dataset_name: DatasetName) -> pd.DataFrame:
    dataset = Dataset(dataset_name)
    population_per_departement = load_population_per_departement()
    zipcode_contributions = Counter(
        dataset.data.authorZipCode.apply(lambda x: str(x)[:2])
    )

    map = pd.DataFrame(
        data=list(zipcode_contributions.items()),
        columns=["Departement", "Nombre contributions"],
    )
    map = (
        map.set_index("Departement")
        .join(population_per_departement.set_index("CODDEP"), how="left")
        .reset_index()
    )
    map["Contributions 1 000 habitants"] = map["Nombre contributions"] / (
        map["PTOT"] / 1_000
    )
    return map


if __name__ == "__main__":
    # Will load the data
    for dataset_name in Dataset.get_dataset_names():
        dataset = Dataset(name=dataset_name)

    num_contribution_over_time = prepare_num_contribution_over_time()
    num_contribution_over_time.to_pickle(P_NUM_CONTRIBUTION_OVER_TIME)

    num_contribution_per_type = prepare_num_contribution_per_type()
    num_contribution_per_type.to_pickle(P_NUM_CONTRIBUTION_PER_TYPE)

    num_contribution_per_theme = prepare_num_contribution_per_theme()
    num_contribution_per_theme.to_pickle(P_NUM_CONTRIBUTION_PER_THEME)

    for dataset_name in Dataset.get_dataset_names():
        map_per_theme = prepare_map_per_theme(dataset_name)
        map_per_theme.to_pickle(str(P_MAP_PER_THEME).format(dataset_name=dataset_name))
