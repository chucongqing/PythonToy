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

if len(sys.argv) < 2 :
	rootdir = ".\\"
else:
	rootdir = sys.argv[1] 
	
def updateJsonFile(file):
	rewriteFile(file)

def resetValue(val):
	for child in val :
		
		if child != None :
			options = child["options"]
			if options != None :
				options["useMergedTexture"] = True
				
				name = options["classname"]
				if name == "ImageView" :
					if options["fileNameData"]["path"] != None:
						options["fileNameData"]["resourceType"] = 1
					else:
						options["fileNameData"]["resourceType"] = 0
				elif name == "Button" :
					if options["disabledData"]["path"] != None :
						options["disabledData"]["resourceType"] = 1
					else :
						options["disabledData"]["resourceType"] = 0
					if options["normalData"]["path"] != None :
						options["normalData"]["resourceType"] = 1
					else :
						options["normalData"]["resourceType"] = 0
					if options["pressedData"]["path"] != None :
						options["pressedData"]["resourceType"] = 1
					else :
						options["pressedData"]["resourceType"] = 0
					
					
				elif name == "Panel" or name == "ListView" or name == "ScrollView":
					if options["backGroundImageData"] != None :
						options["backGroundImageData"]["resourceType"] = 1
				elif name == "CheckBox" :
					if options["backGroundBoxData"]["path"] != None:
						options["backGroundBoxData"]["resourceType"] = 1
					else:
						options["backGroundBoxData"]["resourceType"] = 0
					
					if options["backGroundBoxDisabledData"]["path"] != None:
						options["backGroundBoxDisabledData"]["resourceType"] = 1
					else:
						options["backGroundBoxDisabledData"]["resourceType"] = 0
						
					if options["backGroundBoxSelectedData"]["path"] != None:
						options["backGroundBoxSelectedData"]["resourceType"] = 1
					else:
						options["backGroundBoxSelectedData"]["resourceType"] = 0
					
					if options["frontCrossData"]["path"] != None:
						options["frontCrossData"]["resourceType"] = 1
					else:
						options["frontCrossData"]["resourceType"] = 0
					
					
					if options["frontCrossDisabledData"]["path"] != None:
						options["frontCrossDisabledData"]["resourceType"] = 1
					else:
						options["frontCrossDisabledData"]["resourceType"] = 0
					
					
					
				elif name == "LoadingBar":
					options["textureData"]["resourceType"] = 1
				#if filedata != None :
				#	filedata["resourceType"] = 1
				#	options["fileNameData"] = filedata
				
				child["options"] = options
				
		children = child["children"]
		if children != None and len(children) > 0:
			resetValue(children)
		
		
		


def rewriteFile(f):
	jsonfile = open(f,"r",encoding='UTF-8')
	data = json.load(jsonfile)
	jsonfile.close()
	try:
		tmp = data["texturesPng"]
		tmp = []
		tmp.append("compoments.png")
		data["texturesPng"] = tmp
		data["textures"] = ["compoments.plist"]
		
		widgetTree = data["widgetTree"]
		
		children = widgetTree["children"]
		resetValue(children)
		widgetTree["options"]["useMergedTexture"] = True
		data["widgetTree"] = widgetTree
		jsonfile = open(f,"w+",encoding="UTF-8")
		jsonfile.write(json.dumps(data,sort_keys=True,indent=2))
		jsonfile.close()
	except:
		print("some thing is wrong!!!")

                
for parent,dirnames,filenames in os.walk(rootdir):
	jsonFiles = []

	for filename in filenames:                        
		#print ("1 parent is :" + parent)
		#print ("1 filename is:" + filename)

		if filename.find(".json") >0 :
			print ("file is:" + os.path.join(parent,filename))
			jsonFiles.append(os.path.join(parent,filename))
			
	if len(jsonFiles) == 0 :
		pass	
	else:
		for i in jsonFiles	:
			updateJsonFile(i)
	
