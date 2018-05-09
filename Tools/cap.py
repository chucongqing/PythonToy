import Tools.helper.path
import zipfile
import xml.etree.ElementTree as ET
walk = Tools.helper.path.walk
#callback(parent, filename, fullpath)
#p = "f:\\Dev\\Unity\\Tank\\NewUI\\Client\\config\\韩国\\android\\Assets\\Plugins\\Android\\"
p="f:\\Dev\\Unity\\Tank\\NewUI\\Client\\Assets\\"
def deal(parent, filename, fullpath):
    if filename.find(".meta") < 0 and filename.find(".aar") > 0 :
        #print("read > " + fullpath)
        zf = zipfile.ZipFile(fullpath)
        mf = zf.open('AndroidManifest.xml')
        root = ET.fromstring(mf.read())
        mf.close()
        zf.close()

        pp = 0
        for pm in root.findall('uses-permission'):
            if pp == 0 :
                print(fullpath)
                pp = 1
            if pm.attrib != None:
                for key in pm.attrib:
                    print(key+" >> "+pm.attrib[key])
        

def run():
    walk(p, deal)