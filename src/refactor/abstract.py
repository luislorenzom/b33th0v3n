import re
import logging

from abc import ABC, abstractmethod
from src.refactor.utils import permute_chunks
from src.refactor.parallel import add_distance_column, parallelize_dataframe


class AbstractRefactor(ABC):

    def __init__(self, manof):
        self.manof = manof
        self.dataset = self.load_dataset()

    @abstractmethod
    def load_dataset(self):
        pass

    def process_filename(self, file_name: str) -> dict:
        """
        Process a file name and recommend

        :param file_name: str to analyze

        :return: the most probably "canonical" names
        """
        # ------------------------------------------------------
        def compute_distances(word):
            # Filter artists to avoid huge delay in below operations
            mask = (self.dataset['names'].str.len() > len(word) - self.manof) & (self.dataset['names'].str.len() < len(word) + self.manof)
            df_masked = self.dataset.loc[mask]
            df_masked = parallelize_dataframe(df_masked, add_distance_column, word)
            candidate = df_masked.sort_values(by=['distances']).iloc[0]
            return {
                'refactor': candidate.names,
                'distance': candidate.distances
            }
        # ------------------------------------------------------

        # Remove from file refactor the "noise symbols"
        file_name = re.sub(r"(-|_|#|@|\||\*|\.|;|:|\?|¿|=|\/|\+|,|\s|\(|\)|\[|])", '_', file_name)

        # Split the file refactor using "_"
        chunks = list(filter(''.__ne__, file_name.split('_')))

        # Permute all the possible combination using last list
        permuted_chunks = permute_chunks(chunks)

        distances = dict()
        for chunk in permuted_chunks:
            distances[chunk] = compute_distances(chunk)
            logging.info('{}\t{}'.format(chunk, distances[chunk]))
        return distances

        # Sort by distances
        min_distance = min(list(map(lambda x: x.get('distance'), list(distances.values()))))
        return dict(filter(lambda x: x[1].get('distance') == min_distance, list(distances.items())))
