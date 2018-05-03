# -*- coding: utf-8 -*- 
import os
import sys
import requests
import json
import os.path


class ServerOp:
    "Use to operate Server Bwg"
    _url = "https://api.64clouds.com/v1/"
    def __init__(self):
        self.init("../secret/1.json")

    def init(self, secretFilePath):
        
        self.inited = False
        f = open(secretFilePath,"r",encoding='UTF-8')
        if f == None :
            print("secret load error")
            return
        data = json.load(f)
        f.close()
        self.veid = data['vedi']
        self.api_key = data['api_key']
        if self.veid == None or self.api_key == None :
            print("secret load error")
            return
        self.inited = True
        
        self.secret = "?veid={}&api_key={}".format(self.veid,self.api_key)
    
    def Inited(self):
        if self.inited == True :
            return True
        else:
            return False

    def Restart(self):
        if not self.Inited():
            return

        param = self._url + "restart" + self.secret
        self.http_get(param)
        
    
    def Stop(self):
        if not self.Inited():
            return

        param = self._url + "stop" + self.secret
        self.http_get(param)

    def Start(self):
        if not self.Inited():
            return
        param = self._url + "start" + self.secret
        self.http_get(param)

    def http_get(self, url):
        r = requests.get(url)
        print(r)