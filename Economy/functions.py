import math

def getpv(cf,intrest,years):
	return cf / math.pow(1+intrest, years)