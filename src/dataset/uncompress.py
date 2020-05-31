import zipfile

from os import remove
from src.constants import DATASET_FOLDER, ARTIST_DATASET_ZIP, TRACKS_DATASET_ZIP


def __uncompress(in_path: str, out_folder: str) -> None:
    with zipfile.ZipFile(in_path, 'r') as zip_ref:
        zip_ref.extractall(out_folder)


def uncompress_artist_dataset() -> None:
    """
    Unzip artist dataset
    """
    __uncompress(ARTIST_DATASET_ZIP, DATASET_FOLDER)
    remove(ARTIST_DATASET_ZIP)


def uncompress_tracks_dataset() -> None:
    """
    Unzip tracks dataset
    """
    __uncompress(TRACKS_DATASET_ZIP, DATASET_FOLDER)
    remove(TRACKS_DATASET_ZIP)
