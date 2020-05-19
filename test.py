import pandas as pd
from src.name.file_name_sorter import process_song_name

# Load songs names and do some transformations
songs = pd.read_csv('dataset/song_dataset.csv', sep='\n', names=['songs']).applymap(lambda x: x.replace('.mp3', '')).applymap(lambda x: x.lower())
file_name = songs.iloc[11].songs

result = process_song_name(file_name)