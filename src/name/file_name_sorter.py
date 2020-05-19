import re
import pandas as pd
import swifter
import numpy as np


# MASK_ARTIST_NAME_OFFSET_FILTER
MANOF = 5

# Load database artists name, filter and transform data
artists = pd.read_csv('dataset/artist.csv', dtype={'names': str}).dropna().applymap(lambda x: x.lower())


def process_song_name(file_name):
    # ------------------------------------------------------

    def permute_chunks(_chunks):
        if len(_chunks) == 0:
            raise Exception('_chunks must not be empty')
        if len(_chunks) == 1:
            return _chunks
        else:
            l = [_chunks.pop(0)]
            for c in _chunks:
                l.append(l[-1] + ' ' + c)
        return l + permute_chunks(_chunks)

    # ------------------------------------------------------

    def compute_distances(_chunk):
        # ------------------------------------------------------
        def get_levenshtein_distance(_chunk, artist_name):
            size_x = len(_chunk) + 1
            size_y = len(artist_name) + 1
            matrix = np.zeros((size_x, size_y))
            for x in range(size_x):
                matrix[x, 0] = x
            for y in range(size_y):
                matrix[0, y] = y
            for x in range(1, size_x):
                for y in range(1, size_y):
                    if _chunk[x - 1] == artist_name[y - 1]:
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
        # ------------------------------------------------------
        # Filter artists to avoid huge delay in below operations
        mask = (artists['names'].str.len() > len(_chunk) - MANOF) & (artists['names'].str.len() < len(_chunk) + MANOF)
        _artists = artists.loc[mask]
        _artists['distances'] = _artists.swifter.applymap(lambda x: get_levenshtein_distance(_chunk, x))
        candidate = _artists.sort_values(by=['distances']).iloc[0]
        return {
            'name': candidate.names,
            'distance': candidate.distances
        }

    # ------------------------------------------------------
    # Remove from file name the "noise symbols"
    file_name = re.sub(r"(-|_|#|@|\||\*|\.|;|:|\?|¿|=|\/|\+|,|\s|\(|\)|\[|])", '_', file_name)

    # Split the file name using "_"
    chunks = list(filter(''.__ne__, file_name.split('_')))

    # Permute all the possible combination using last list
    permuted_chunks = permute_chunks(chunks)

    distances = dict()
    for chunk in permuted_chunks:
        distances[chunk] = compute_distances(chunk)

    # Sort by distances
    distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1].distance)}

    # Return most probably most probably name band
    return list(distances.keys())[0]
