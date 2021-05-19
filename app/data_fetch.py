import typing
import logging
import os
from pathlib import Path
from typing import Dict
from urllib.request import HTTPError, urlretrieve

import pandas as pd

from app.types import DatasetName

_BUCKET_URL = (
    "http://opendata.auth-6f31f706db6f4a24b55f42a6a79c5086.storage.sbg.cloud.ovh.net"
)
_DATA_FOLDER = Path(__file__).parent.parent / "data"
URLS: Dict[DatasetName, str] = {
    "transition": f"{_BUCKET_URL}/2019-04-08/QUESTIONNAIRE_LA_TRANSITION_ECOLOGIQUE.csv",
    "fiscalite": f"{_BUCKET_URL}/2019-04-08/QUESTIONNAIRE_LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES.csv",
    "democratie": f"{_BUCKET_URL}/2019-04-08/QUESTIONNAIRE_DEMOCRATIE_ET_CITOYENNETE.csv",
    "organisation": f"{_BUCKET_URL}/2019-04-08/QUESTIONNAIRE_ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS.csv",
}


def _download_file_if_doesnt_exist(source: str, destination: str) -> None:
    if os.path.exists(destination):
        return
    logging.info(f"Downloading {source} -> {destination}")
    try:
        urlretrieve(source, destination)
    except HTTPError as exc:
        print(source, exc)


def _local_filename(dataset: DatasetName) -> str:
    return str(_DATA_FOLDER / f"{dataset}.csv")


def _remote_filename(dataset: DatasetName) -> str:
    return URLS[dataset]


def _download_dataset(dataset: DatasetName) -> None:
    source = _remote_filename(dataset)
    destination = _local_filename(dataset)
    _download_file_if_doesnt_exist(source, destination)


def fetch_dataset(dataset: DatasetName) -> pd.DataFrame:
    _download_dataset(dataset)
    return pd.read_csv(_local_filename(dataset))
