import math
import random
count = 60
lvl = 1
def calcgl(l,gl=0.97):
	return math.pow(gl , l)
	
def calcc(lvl):
	c = 0
	t = True
	c1 = calcgl(lvl)
	while t :
		r = random.random()
		if r < c1 :
			t = False
		c += 1
	return c
	
def calccs(lvl):
	cs = 0
	for i in range(lvl):
		cs += calcc(i+1)
		
	return cs
	