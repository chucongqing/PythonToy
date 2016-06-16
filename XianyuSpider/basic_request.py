# -*- coding: utf-8 -*- 
import os,sys,hashlib
import os.path

import requests

url = "http://news.163.com/rank/"

response = requests.get(url)
content = requests.get(url).content #string

print content.decode("gbk")