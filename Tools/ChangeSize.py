import os
import sys
import shlex

from os import listdir
from os.path import isfile, join

mypath = ".\\"
imgmagic = "E:\Program Files\ImageMagick-7.0.2-Q16\magick.exe"
command = " -resize 128x128! "
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"
	
for filename in onlyfiles :
	if (filename.find(".jpg") > 0 or filename.find(".png") > 0 ) and filename.find(".meta")  == -1 :
		cmd = '\"' + imgmagic +'\"'  + " convert " + filename + command + filename
		
		print(cmd)
		os.system(cmd)