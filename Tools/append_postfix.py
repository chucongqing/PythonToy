#nothing

import sys
import os
import os.path


postfix = ".txt"
rootdir = ".\\"
TYPES =0  # 0 add 1 remove

if len(sys.argv) >= 2 :
	TYPES = int(sys.argv[1])


def RemovePostFix(fileName, postFix,offSet):
	idx = fileName.find(postFix)
	if idx != -1 :
		idx = idx + offSet
		newName = fileName[:idx]
		os.rename(fileName,newName)
	
def AppendPostFix(fileName):
	global TYPES
	if TYPES == 0 :
		if fileName.find(".lua.txt") != -1 :
			return
		else:
			newName = fileName + ".txt"
			os.rename(fileName,newName)

	elif TYPES == 1:
		RemovePostFix(fileName, ".lua.txt",4)
		RemovePostFix(fileName, ".meta.txt",5)
		
		
			


for parent,dirnames,filenames in os.walk(rootdir):
	Files = []   
	parten = ""
	for filename in filenames:
		if TYPES == 0:
			parten = ".lua"
		elif TYPES == 1:
			parten = ".lua.txt"

		if filename.find(parten) != -1 :
			if filename.find(".meta") == -1 :
				Files.append(os.path.join(parent, filename))
		else:
			pass
	
	if len(Files) == 0 :
		pass
	else:
		for f in Files:
			AppendPostFix(f)