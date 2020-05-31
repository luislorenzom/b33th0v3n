from pandas import DataFrame

from src.constants import DEFAULT_MANOF
from .artist import ArtistRefactor
from .track import TrackRefactor


def refactor(df: DataFrame) -> dict:
    """
    Recommends a refactor for several music files names

    :param df: DataFrame where are all the music file names

    :return: refactor recommendation for artists and track name
    """
    # -----------------------------------------------------------------
    def __refactor(filename: str, manof: int = DEFAULT_MANOF) -> dict:
        """
        Recommends a refactor for a music file name

        :param filename: raw music file name
        :param manof: (MASK ARTIST NAME OFFSET FILTER) distance offset for datasets track and artists name in
        comparison with input's name

        :return: refactor recommendation for artists and track name
        """
        recommendations = dict()

        recommendations['artists'] = ArtistRefactor(manof).process_filename(filename)
        recommendations['tracks'] = TrackRefactor(manof).process_filename(filename)

        return recommendations
    # -----------------------------------------------------------------
    r = dict()
    for song in list(df.songs):
        r = {**r, **__refactor(song)}
    return r
