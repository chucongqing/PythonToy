# -*- coding: utf-8 -*- 
import os
import os.path

'''
print ("script name = ", sys.argv[0])
for i in range(1, len(sys.argv)):
	print ("parameter = " ,i, sys.argv[i])
'''

# Walk through the given dir
def walk(dir, callback):
    for parent,dirnames,filenames in os.walk(dir):     
        for filename in filenames:                        
            #print ("1 parent is :" + parent)
            #print ("1 filename is:" + filename)
            #print ("file is:" + os.path.join(parent,filename))
            fullpath = os.path.join(parent,filename)
            callback(parent, filename, fullpath)

