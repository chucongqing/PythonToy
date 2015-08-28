# -*- coding: utf-8 -*- 
import os
import sys
import os.path
import json
import plistlib



print ("script name = ", sys.argv[0])

for i in range(1, len(sys.argv)):
	print ("parameter = " ,i, sys.argv[i])

  
origin_type = ".dds"
replace_type = ".png"
if len(sys.argv) < 2 :
	rootdir = ".\\"
else:
	rootdir = sys.argv[1] 
	
def updateJsonFile(file,files):
	for i in files:
		changeFile(file,i)
		
def changeFile(file,f_replace):
	if file.find(".ExportJson") > 0 :
		jsonFile = open(file, "r",encoding='UTF-8')
		data = json.load(jsonFile)
		jsonFile.close()
		try:
			tmp = data["config_png_path"]
			for i in range(len(tmp)):
				tmp[i] = tmp[i].replace(origin_type,replace_type)
			data["config_png_path"] = tmp
		
			jsonFile = open(file, "w+",encoding='UTF-8')
			jsonFile.write(json.dumps(data))
			jsonFile.close()
		except:
			print("some thing wrong")
		
	elif file.find(".plist") >0:
		try:
			plist = plistlib.readPlist(file)
			plist['metadata']['textureFileName'] = plist['metadata']['textureFileName'].replace(origin_type,replace_type)
			plist['metadata']['realTextureFileName'] = plist['metadata']['realTextureFileName'].replace(origin_type,replace_type)
			plistlib.writePlist(plist,file)
		except:
			print("wrong 2")
		
	
for parent,dirnames,filenames in os.walk(rootdir):
	jsonFiles = []
	pngfiles = []
		
	for filename in filenames:                        
		#print ("1 parent is :" + parent)
		#print ("1 filename is:" + filename)
		print ("file is:" + os.path.join(parent,filename))
		if filename.find(origin_type) > 0 :
			pngfiles.append(os.path.join(parent,filename))
		if filename.find(".plist") >0 or filename.find(".ExportJson") >0 :
			jsonFiles.append(os.path.join(parent,filename))
	
	if len(pngfiles) == 0 or len(jsonFiles) == 0 :
		pass
	else:
		for i in jsonFiles :
			updateJsonFile(i,pngfiles)
	