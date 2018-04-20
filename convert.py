from subprocess import call
import re
from os import walk
f = []

path = "C:\\Users\\aksha\\Desktop\\Music_Information_Retrieval\\DataBase\\Instruments"
directory = walk(path)

for i in directory:
    for j in i[2]:
        if ".aif" in j:
            call('ffmpeg -i ' + i[0] + "//" + j + ' -acodec pcm_s16le -ac 1 -ar 22050 ' + i[0] + "//" + j[:-4] + '.wav')