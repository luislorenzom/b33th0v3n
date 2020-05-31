import requests

from src.constants import ARTIST_DATASET_ZIP, TRACKS_DOWNLOAD_URL, TRACKS_DATASET_ZIP, ARTIST_DOWNLOAD_URL


def __download(url: str, path: str) -> None:
    r = requests.get(url)

    with open(path, 'wb') as f:
        f.write(r.content)


def download_artist_dataset() -> None:
    """
    Download artist dataset
    """
    __download(ARTIST_DOWNLOAD_URL, ARTIST_DATASET_ZIP)


def download_tracks_dataset() -> None:
    """
    Download tracks dataset
    """
    __download(TRACKS_DOWNLOAD_URL, TRACKS_DATASET_ZIP)
