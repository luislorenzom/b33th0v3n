from time import time

ts = lambda: str(int(time()))

# General
DATASET_FOLDER = 'dataset'
VERSION = '1.0'

# Dataset
ARTIST_DOWNLOAD_URL = 'https://drive.google.com/open?id=1v5b9MoJZtyDUTblFjp1c7dcE0oG8D5Nh'
TRACKS_DOWNLOAD_URL = 'https://drive.google.com/open?id=1XcbqOD0eVCwkT_2y_NLxen2-NrgTN7lL'
ARTIST_DATASET_ZIP = 'dataset/artist.zip'
TRACKS_DATASET_ZIP = 'dataset/tracks.zip'

# I/O
DEFAULT_OUTPUT = 'b33th0v3n_output_{}'.format(ts())

# Refactor Recommendation
ARTIST_DATASET_PATH = 'dataset/artist.csv'
TRACKS_DATASET_PATH = 'dataset/tracks.csv'
DEFAULT_MANOF = 5
