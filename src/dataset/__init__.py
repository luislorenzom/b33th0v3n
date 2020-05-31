from os import path

from src.constants import ARTIST_DATASET_PATH, TRACKS_DATASET_PATH
from .download import download_tracks_dataset, download_artist_dataset
from .uncompress import uncompress_artist_dataset, uncompress_tracks_dataset


def get_datasets():
    """
    Prepare dataset's folder to first program's execution
    """
    if not path.exists(ARTIST_DATASET_PATH):
        download_artist_dataset()
        uncompress_artist_dataset()

    if not path.exists(TRACKS_DATASET_PATH):
        download_tracks_dataset()
        uncompress_tracks_dataset()
