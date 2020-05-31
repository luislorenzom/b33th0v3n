import librosa.display

from matplotlib import pyplot as plt


audio_path = 'file.mp3'
x, sr = librosa.load(audio_path, sr=None)

# -------------------------------
# Display Spectrogram
# -------------------------------
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')

#If to pring log of frequencies
#librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()
plt.show()


# -------------------------------
# Feature extraction
# -------------------------------
zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
