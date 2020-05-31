import pandas as pd

from src.constants import ARTIST_DATASET_PATH
from src.refactor.abstract import AbstractRefactor


class ArtistRefactor(AbstractRefactor):

    def load_dataset(self) -> pd.DataFrame:
        """
        Load artist dataset

        :return: DataFrame with artist (singers and bands) name
        """
        return pd.read_csv(ARTIST_DATASET_PATH, dtype={'names': str}).dropna().applymap(lambda x: x.lower())
