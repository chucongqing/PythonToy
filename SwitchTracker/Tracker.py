import requests
import re

from Utils import SendMsg
from bs4 import BeautifulSoup

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"

headers = {'User-Agent': ua}
url = "https://www.amazon.co.jp/gp/product/B01N5QLLT3"
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text,"html.parser")

ret = soup.find(id="priceblock_ourprice")

s = str(ret)

price = int(re.sub("[^0-9]", "", s))

if price < 40000 :
	nowPrice = "现在价格："
	nowPrice += str(price)
	SendMsg(nowPrice,nowPrice)