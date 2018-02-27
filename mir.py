import librosa.display, librosa.util, librosa.core
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import csv
import nltk

start_fileid = 1
end_fileid = 106

filename = []
name = ""
for i in range(start_fileid,end_fileid+1):
    name = "guitar (" + str(i) + ").mp3"
    filename.append(name)

# Loading Files
y = []
sr = []
for i in range(start_fileid-1,end_fileid):
    y_temp, sr_temp = librosa.core.load("C:\\Users\\aksha\\Desktop\\Music_Information_Retrieval\\DataBase\\Instruments\\Guitar\\" + filename[i])
    y.append(y_temp)
    sr.append(sr_temp)

features = []

# '''
for i in range(start_fileid-1,end_fileid):
    arr = []
    temp_arr = []
    temp_features = []

    # Category A - 1 row 2D array
    arr.append(librosa.feature.zero_crossing_rate(y[i], hop_length=2048))
    arr.append(librosa.feature.rmse(y[i], hop_length=2048))
    arr.append(librosa.feature.spectral_centroid(y[i], sr[i], hop_length=2048))
    arr.append(librosa.feature.spectral_bandwidth(y[i], sr[i], hop_length=2048))
    arr.append(librosa.feature.spectral_rolloff(y[i], sr[i], hop_length=2048))

    # Category B - Multi row 2d array
    arr.append(librosa.feature.mfcc(y[i], sr[i]))

    for j in arr:
        if len(j) > 1:
            for k in j:
                temp_arr.append(sum(k))
            temp_features.append(temp_arr)
        else:
            temp_features.append(j[0])
    features.append(temp_features)

# for i in features:
    # print(i)
# '''

# '''
fileid_counter = 1
header_flag = 0
dict_feature = {}
for fileid in features:
    count = 1
    fieldnames = ["File"]
    for key in dict_feature.keys():
        dict_feature[key] = 0
    dict_feature["File"] = fileid_counter
    for feature in fileid:
        i = 1
        for element in feature:
            if count == 1:
                dict_feature["ZCR"+str(i)] = element
                fieldnames.append("ZCR"+str(i))
            if count == 2:
                dict_feature["RMSE"+str(i)] = element
                fieldnames.append("RMSE"+str(i))
            if count == 3:
                dict_feature["S_Cent"+str(i)] = element
                fieldnames.append("S_Cent"+str(i))
            if count == 4:
                dict_feature["S_Band"+str(i)] = element
                fieldnames.append("S_Band"+str(i))
            if count == 5:
                dict_feature["S_Roll"+str(i)] = element
                fieldnames.append("S_Roll"+str(i))
            if count == 6:
                dict_feature["MFCC"+str(i)] = element
                fieldnames.append("MFCC"+str(i))
            i = i+1
        count = count+1
    fileid_counter = fileid_counter+1
    
    with open("Guitar_DataSet.csv", 'a', newline='') as csvfile:
        if header_flag == 0:
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerow(dict_feature)
            header_flag = 1
        else:
            writer = csv.writer(csvfile)
            writer.writerow(dict_feature.values())
        csvfile.close()

# arr = librosa.feature.tonnetz(y, sr)
# rfeatures=np.hstack(arr,arr1)
# features=np.vstack(features,rfeatures)
# librosa.feature.melspectrogram
# librosa.feature.spectral_contrast

# plt.figure()
# librosa.display.waveplot(y[0], sr[0])
# plt.plot()
# plt.show()