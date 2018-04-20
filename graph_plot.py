import pandas as pd
import matplotlib.pyplot as plt
import numpy
import sklearn
import sklearn.preprocessing

path = "C:\\Users\\aksha\\Desktop\\Music_Information_Retrieval\\DataSet\\"

df1 = pd.read_csv(path + "Trumpet_Vib_DataSet.csv", index_col="File")
df2 = pd.read_csv(path + "Flute_Vib_DataSet.csv", index_col="File")
df3 = pd.read_csv(path + "Sop_Saxophone_Vib_DataSet.csv", index_col="File")
plot_data = []
feature = ["ZCR", "RMSE", "S_Cent", "S_Band","S_Roll", "MFCC"]
index = 0
d1zcr = []
d1rmse = []
d2zcr = []
d3zcr = []

for i in range(1,59):
    # plot_data = df1[feature[index] + str(i)]
    # plt.plot(plot_data, 'ro')
    d1zcr.append(df1[feature[index] + str(i)])
    d1rmse.append(df1[feature[index+1] + str(i)])

# print(d1zcr[0])

for i in range(1,31):
    # plot_data = df2[feature[index] + str(i)]
    # plt.plot(plot_data, 'bo')
    d2zcr.append(df2[feature[index] + str(i)])

for i in range(1,46):
    # plot_data = df3[feature[index] + str(i)]
    # plt.plot(plot_data, 'yo')
    d3zcr.append(df3[feature[index] + str(i)])

feature_table = numpy.vstack((d1zcr[0], d1rmse[0]))
# print(feature_table[1])
# print(feature_table[0])
scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1, 1))
training_features1 = scaler.fit_transform(feature_table[1])
training_features0 = scaler.fit_transform(feature_table[0])
# print(training_features.min(axis=0))
# print(training_features.max(axis=0))
# print (d1zcr[0])
print (training_features1)
print (training_features0)

# plt.figure()
# print(feature_table[:])
# plt.scatter(training_features0, training_features1, c='b')
# plt.scatter(training_features[10:,0], training_features[10:,1], c='r')
plt.xlabel('Zero Crossing Rate')
plt.ylabel('Spectral Centroid')
# plt.hist(d1zcr[0], color='b', range=(0, 0.2), alpha=0.5, bins=20)
plt.show()