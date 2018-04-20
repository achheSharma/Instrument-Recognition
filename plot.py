import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.core.load("C:\\Users\\aksha\\Desktop\\Music_Information_Retrieval\\DataBase\\Instruments\\Saxophone\\SopSax.vib.ff.stereo\\SopSax.vib.ff.A3.stereo.aif")
# print (librosa.core.get_duration(y = y, sr=sr))
plt.figure()
librosa.display.waveplot(y,sr=sr)
plt.show()
# print (sr)