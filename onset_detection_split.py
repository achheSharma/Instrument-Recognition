import time
import progressbar
from progressbar import ProgressBar
import argparse
import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import os

# for i in progressbar.progressbar(range(100)):
#     time.sleep(0.02)

start_fileid = 1
end_fileid = 1
instrument = "guitar"

filename = []
name = ""
# for i in range(start_fileid,end_fileid+1):
#     name = instrument + " (" + str(i) + ").mp3"
#     filename.append(name)
#     print (filename)

def prepare(y, sr=22050):
    y = librosa.to_mono(y)
    y = librosa.util.fix_length(y, sr) # 1 second of audio
    y = librosa.util.normalize(y)
    return y

def get_fingerprint(y, sr=22050):
    y = prepare(y, sr)
    cqt = librosa.cqt(y, sr=sr, hop_length=2048)
    return cqt.flatten('F')

def normalize(x):
    x -= x.min(axis=0)
    x /= x.max(axis=0)
    return x

def basename(file):
    file = os.path.basename(file)
    return os.path.splitext(file)[0]

# Loading Files
count = 0
for i in range(start_fileid-1,end_fileid):
    y, sr = librosa.core.load("C:\\Users\\aksha\\Desktop\\Music_Information_Retrieval\\DataBase\\Instruments\\" + instrument.title() + "\\" + instrument + " (" + str(1) + ").mp3")
    # o_env = librosa.onset.onset_strength(y, sr=sr, feature=librosa.cqt)
    o_env = onset_env = librosa.onset.onset_strength(y=y, sr=sr, aggregate=np.median, fmax=8000, n_mels=256)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)

    # plt.figure()
    # librosa.display.waveplot(y,sr=sr)
    # plt.show()

    # vectors = []
    # words = []
    # filenames = []

    onset_samples = list(librosa.frames_to_samples(onset_frames))
    onset_samples = np.concatenate(onset_samples, len(y))
    starts = onset_samples[0:-1]
    stops = onset_samples[1:]
    samples_folder = "out"
    try:
	    os.makedirs(samples_folder)
    except:
	    pass
    pbar = ProgressBar()
    
    for i, (start, stop) in enumerate(pbar(zip(starts, stops))):
        count = count+1
        audio = y[start:stop]
        filename = os.path.join(samples_folder, str(count) + '.wav')
        librosa.output.write_wav(filename, audio, sr)
        vector = get_fingerprint(audio, sr=sr)
        # word = basename(filename)
        # vectors.append(vector)
        # words.append(word)
        # filenames.append(filename)