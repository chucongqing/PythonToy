#-*- coding: utf-8 -*-
from socket import *
	
ip1 = "139.196.42.165"
ip2 = "10.1.10.115"

class TcpClient:
	prkey="00de0d543d866bd94a0c0a0b4e6fe1c7475665234b5e88d63493f0611e1d06be9614f73af5a1ac890f44970e1887993f83e3c4ba3bd52939d8662e9b5735cc70b6e921378caf46a3d34f0791b774cf2d58df436e90ddeb49c56945ef338b319f25d15d9259368f6c5a16765fa5bb4c9c7a7148a941679880cefc8de4157d82bdf472f13e78ae9e085563d47bfba87faa50ea421bf3b4a428d0ff20a6846a94a775c695247c609d041105b0fdf8ee03401cb209c8c2dab3c93ce213fef2a22fb917dc52b18526322a7e6dca9a53e7f612d702fad2cb2777b851a08e2bc3f9b5e5e07930385bcd2281e8e6ec68bc6410ad73eddb8ac019ab5c4d2c1a621f01bfc1"
	
	host = ip1
	
	port = 3633
	buffSize = 102400
	keylist = []
	tt = []
	addr = (host,port)
	
	def __init__(self):
		self.Encript()
		
	def Auto(self,ip = None,port = None):
		if ip != None :
			self.host = ip
		if port != None:
			self.port = port
			
		self.Rc()
		self.Cm()
		
	def Rc(self):
		self.client = socket(AF_INET, SOCK_STREAM)
		self.client.settimeout(3)
		self.addr = (self.host,self.port)
		self.client.connect(self.addr)
		
	def Cm(self):
		while(True):
			data = input('>')
			if not data :
				self.client.close()
				break
			self.CheckCmd(data)
			#self.Send(data)
			data = self.client.recv(self.buffSize)
			if not data :
				self.client.close()
				break
			print(data.decode('ASCII'))
			
	def CheckCmd(self,data):
		if data[0:1] == "l" :
			account = data[1:len(data)]
			if account == "" :
				account = "A01 234|0000|1|1"
			else:
				account = "A01 " + account + "|0000|1|1"
			print("Head = >" + account)
			self.Send(account)
		elif data[0:2] == "h1" :
			self.Send("H01")
		else :
			self.Send(data)
	def Encript(self):
		i = 0
		while( i < len(self.prkey)):
			doublebytestr = self.prkey[i:i+2]
			#print(doublebytestr)
			n = int(doublebytestr,16)
			self.keylist.append(bytes([n]))
			self.tt.append(n)
			i = i+2
		
	
			
	def Send(self,s):
		
		ab = bytearray(s,"ASCII")
		msg = bytearray()
		for i in range(len(ab)):
			byte = ab[i:i+1]
			byte = int.from_bytes(byte, byteorder='little')			
			enbyte = self.keylist[byte]			
			msg += enbyte
		msg += b'\n'
		msg += b'\0'
		#print(msg)
		self.client.sendall(msg)
		
	
if __name__ == '__main__':
	client = TcpClient()
	a = client.Auto