import pandas as pd

from src.constants import TRACKS_DATASET_PATH
from src.refactor.abstract import AbstractRefactor


class TrackRefactor(AbstractRefactor):

    def load_dataset(self) -> pd.DataFrame:
        """
        Load tracks dataset

        :return: DataFrame with tracks name
        """
        return pd.read_csv(TRACKS_DATASET_PATH, dtype={'names': str}).dropna().applymap(lambda x: x.lower())
