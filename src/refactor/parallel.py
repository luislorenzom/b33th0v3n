from types import FunctionType

import numpy as np
import pandas as pd

from functools import partial
from multiprocessing import Pool, cpu_count


def get_levenshtein_distance(str1: str, str2: str) -> float:
    """
    Computes the Levenshtein distance between two strings

    :param str1: first string
    :param str2: second string

    :return: the distance between the two params
    """
    size_x = len(str1) + 1
    size_y = len(str2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y
    for x in range(1, size_x):
        for y in range(1, size_y):
            if str1[x - 1] == str2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )
    return matrix[size_x - 1, size_y - 1]


def add_distance_column(filename: str, df: pd.DataFrame) -> pd.DataFrame:
    """
    Add new column to df which contains distance computed using filename

    :param filename: filename to compare to df
    :param df: df with artist or tracks names

    :return: df with new column
    """
    df['distances'] = df.applymap(lambda x: get_levenshtein_distance(filename, x))
    return df


def parallelize_dataframe(df: pd.DataFrame, func: FunctionType, word: str, n_cores: int = cpu_count() - 1) -> pd.DataFrame:
    """
    Apply certain func against dataframe parallelling the application

    :param df: DataFrame which contains the required by func
    :param func: func that will be parallelize through df
    :param word: to compute the distance using
    :param n_cores: thread to parallelize the function

    :return: DataFrame after func applied
    """
    df_split = np.array_split(df, n_cores)  # TODO: add df length check to get n_cores
    pool = Pool(n_cores)
    f = partial(func, word)
    df = pd.concat(pool.map(f, df_split))
    pool.close()
    pool.join()
    return df
