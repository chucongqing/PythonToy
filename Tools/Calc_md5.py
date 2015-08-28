# -*- coding: utf-8 -*- 
import os,sys,hashlib
import os.path

ignorelist = [".meta",".py","files.txt","md5file.txt"]

print("script name = ",sys.argv[0])
for i in range(1, len(sys.argv)):
	print ("parameter = " ,i, sys.argv[i])

if len(sys.argv) < 2 :
	rootdir = ".\\"
else:
	rootdir = sys.argv[1] 


md5file = open("md5file.txt","w")
def calculateMd5(fullpath):
	m = hashlib.md5()
	f = open(fullpath,'rb')
	all_txt = f.read()
	m.update(all_txt)
	md5value = m.hexdigest()
	
	str = fullpath + '|' + md5value + '\n'
	str = str.replace(".\\","")
	md5file.write(str)
	f.close()

def isIgnored(filename):
	for  i in ignorelist :
		if filename.find(i) >= 0 :
			return True
	return False

for parent,dirnames,filenames in os.walk(rootdir):
	for filename in filenames:
		print ("file is:" + os.path.join(parent,filename))
		if isIgnored(filename) ==  False:
			calculateMd5(os.path.join(parent,filename))


md5file.flush()
md5file.close()
