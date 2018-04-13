import math

#现值
def getpv(cf,intrest,years):
	return cf / math.pow(1+intrest, years)

#利息计算
def getintrest(pv, intrest, years):
	return  pv * math.pow( 1 + intrest, years) - pv

#固定还款现值的计算
def getfixpv(p,  intrest,years):
	t = 0
	py = p/years
	t = t + py
	years = years - 1
	for i in range(years):
		t = t + getpv(py, intrest,i + 1)
	return t

#非复利
def getintresttotal(pv,intrest,years):
	t = 0
	for i in range(years):
		t = t + getintrest(pv,intrest,1)
	return t
#复利
def getintrestrep(pv,intrest,years):
	o = pv
	for i in range(years):
		n = getintrest(pv,intrest,1)
		pv = pv + n
	return pv - o


#stock present value calc
# pn next year stock price
# si stock intrest 
# re invest reward 
def stock_pv(pn,si,re):
	return si/(1+re) + pn/(1+re)

#gorden increase model
def g_inc_model(si,sig,re):
	return si*(1+sig)/(re - sig)