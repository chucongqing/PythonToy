# -*- coding: utf-8 -*- 
import os
import sys
import os.path
import json
import plistlib



print ("script name = ", sys.argv[0])

for i in range(1, len(sys.argv)):
	print ("parameter = " ,i, sys.argv[i])

  
origin_type = ".png"
replace_type = ".dds"
if len(sys.argv) < 2 :
	rootdir = ".\\"
else:
	rootdir = sys.argv[1] 
	
def updateJsonFile(file):
		replacePngToDds(file)

def replacePngToDds(file):
	print("filename",file)
	try :
		plist = plistlib.readPlist(file)
		print(plist['metadata']['textureFileName'])
		plist['metadata']['textureFileName'] = plist['metadata']['textureFileName'].replace(origin_type,replace_type)
		plist['metadata']['realTextureFileName'] = plist['metadata']['realTextureFileName'].replace(origin_type,replace_type)
		plistlib.writePlist(plist,file)
	except:
		print("something went wrong")
		

		
	
for parent,dirnames,filenames in os.walk(rootdir):
	jsonFiles = []
	pngfiles = []
		
	for filename in filenames:                        
		#print ("1 parent is :" + parent)
		#print ("1 filename is:" + filename)

		if filename.find(".plist") >0 :
			print ("file is:" + os.path.join(parent,filename))
			jsonFiles.append(os.path.join(parent,filename))
	
	if len(jsonFiles) == 0 :
		pass
	else:
		for i in jsonFiles :
			updateJsonFile(i)
	