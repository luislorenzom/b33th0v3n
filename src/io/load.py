import pandas as pd

from os import listdir
from os.path import isfile, join


def load_songs_from_csv(song_dataset: str) -> pd.DataFrame:
    """
    Loads a csv with songs names to analyze

    :param song_dataset: where is the csv file

    :return: Dataframe with songs names
    """
    return pd.read_csv(song_dataset, sep='\n', names=['songs']).applymap(lambda x: x.replace('.mp3', '')).applymap(lambda x: x.lower())


def load_songs_from_folder(songs_folder: str) -> pd.DataFrame:
    """
    Loads songs names from given folder to analyze

    :param songs_folder: where are the csv files

    :return: Dataframe with songs names
    """
    df = pd.DataFrame()
    df['songs'] = pd.Series([f for f in listdir(songs_folder) if isfile(join(songs_folder, f)) and f.endswith('.mp3')])
    return df.applymap(lambda x: x.replace('.mp3', '')).applymap(lambda x: x.lower())
