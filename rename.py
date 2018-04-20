import librosa.display, librosa.util, librosa.core
import os

start_fileid = 1
end_fileid = 32
instrument = "saxophone"
folder = "SopSax.vib.ff.stereo"
path = "C:\\Users\\aksha\\Desktop\\Music_Information_Retrieval\\DataBase\\Instruments\\" + instrument.title() + "\\" + folder + "\\"
file_info = []
# duration = {}
name = ""
for i in range(start_fileid,end_fileid+1):
    name = instrument + " (" + str(i) + ").aif"
    file_info.append([name,0])
    # duration[name] = 0

# Loading Files
for i in range(start_fileid-1,end_fileid):
    filename = file_info[i][0]
    y, sr = librosa.core.load(path + filename)
    y = librosa.to_mono(y)
    file_info[i][1] = librosa.core.get_duration(y = y, sr=sr)

#sort on basis of length
sorted_file_info = sorted(file_info , key = lambda x: x[1])
sorted_file_info.reverse()
# for i in sorted_file_info:
#     print (i)

#rename files
for i in range(len(sorted_file_info)):
    os.rename(path + sorted_file_info[i][0], path + str(i+1) + ".aif")


