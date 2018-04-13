'''
import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()
'''

import zipfile
import os

root_dir = ".\\"
tmp_dir = "E:\\java_check_temp\\"

number = 0
def unzipfile(filename):
    global tmp_dir
    if filename.find(".zip") > 0:
        zip_ref = zipfile.ZipFile(filename,"r")
        tmp_now = tmp_dir + str(number)
        number = number + 1
        zip_ref.extractall(tmp_now)
        

def gothrough(rootdir, dealfunc):
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:                        
            #print ("1 parent is :" + parent)
            #print ("1 filename is:" + filename)
            print ("file is:" + os.path.join(parent,filename))
            '''
            if filename.find(origin_type) > 0 :
                pngfiles.append(os.path.join(parent,filename))
            if filename.find(".plist") >0 or filename.find(".ExportJson") >0 :
                jsonFiles.append(os.path.join(parent,filename))
            '''
            dealfunc(filename)
        
      