# -*- coding: utf-8 -*- 
import os
import sys
import os.path

# parten1 parten_change 

rootdir = ".\\"

parten1 = sys.argv[1]
parten2 = sys.argv[2]
	
for parent,dirnames,filenames in os.walk(rootdir):
	for filename in filenames:  
		print("> "+filename)
		if filename.find(parten1) >= 0 :
			#chongmingming
			fn = os.path.join(parent,filename)
			fnnew = os.path.join(parent,filename.replace(parten1,parten2))
			os.rename(fn,fnnew)
		
	