import librosa
import librosa.display
import matplotlib.pyplot as plt
import seaborn
import numpy, scipy
import IPython.display as ipd
import librosa, librosa.display, librosa.core

y, sr = librosa.core.load("C:\\Users\\aksha\\Desktop\\Music_Information_Retrieval\\DataBase\\Instruments\\Trumpet\\trumpet.vib.ff.stereo\\1.wav")
x = y
duration = librosa.core.get_duration(y = y, sr=sr)
print (duration)
# plt.figure()
# librosa.display.waveplot(y,sr=sr)
# plt.show()
# ipd.Audio(y, rate = sr)
# print (sr)
# librosa.output.write_wav("loda.aif", y, sr=sr)

''' Spectrogram '''
# S = numpy.abs(librosa.stft(y))
# Xmag = librosa.core.power_to_db(S)
# plt.figure()
# librosa.display.specshow(Xmag, sr=sr, x_axis='time', y_axis='log')
# plt.show()

''' Onset Detection '''
onset_frames = librosa.onset.onset_detect(x, sr=sr)
# print (onset_frames)
onset_times = librosa.frames_to_time(onset_frames, sr=sr)
print (onset_times)
onset_samples = librosa.frames_to_samples(onset_frames)
print (onset_samples)

# print(y)
''' Segmentation '''
frame_sz = int(1*sr)
segments = [x[i:i+frame_sz] for i in range(0,int(22050*duration),22050)]
count = 0
for i in segments:
    new_duration = librosa.core.get_duration(i, sr = sr)
    # librosa.output.write_wav(str(count) + ".wav", i, sr = sr)
    print (new_duration)
    count = count+1