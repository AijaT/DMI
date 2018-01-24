#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import cos 
import numpy as np
import matplotlib.pyplot as plt


'''
# vērtību attēlošana
def mans_cosinuss(x):
    k = 0
    a = 1
    S = a
    while k < 500:
        k = k + 1
        R = (-1)*x*x/(2*k*(2*k-1)*4)
        a = a * R
        S = S + a
    return S

a = 1.57
b = 4.71
x = np.arange(a,b,0.01)
y = mans_cosinuss(x)
plt.plot(x,y)
plt.grid()
plt.show()

delta_x = 1.e-7 # 0.001 ir tas pats ka 1.e-3
funa = mans_cosinuss(a)
funb = mans_cosinuss(b)
if funa * funb > 0:
    print "[%.2f,%.2f] intervālā sakņu nav"%(a,b),
    print "vai šajā intervālā ir pāru sakņu skaits"
    exit()
print "Turpinājums, kad sakne ir:"
print "Vērtības intervāla galapunktos - ",
print "f(%.2f)=%.2f un f(%.2f)=%.2f"%(a,funa,b,funb)

k = 0
while b-a > delta_x:
    k = k + 1
    x = (a+b)/2
    funx = mans_cosinuss(x)
    print "%3d. a=%.5f f(%.5f)=%8.5f b=%.5f"%(k,a,x,funx,b)
    if funa * funx > 0:
        a = x
    else:
        b = x
print "Rezultāts:"
print "a=%.9f f(%.9f)=%12.9f b=%.9f"%(a,x,funx,b)
print "Aprēķins veikts ar %d iterācijām"%(k)
'''


#Rekurences reizinātāja zīmēšana
'''
print "                        (-1)!      "
print "R = (-1) * 2*k *  ---------------- " 
print "                    2*k * (2*k-1)  "
'''


#Funkcijas zīmēšana parādot to terminālī

'''
print   "500"
print "------"
print "\      "
print " \       k    2*k         "
print "  \   (-1) * x           "
print "   \  ________________   "
print "   /            2*k          "
print "  /   (2*k)! * 2                    "
print " /                       "
print "/                        "
print "------"
print    "k=0"
'''



#funkcijas grafika zīmēšana
'''
def mans_cosinuss(x):
	k=0
	a=1
	S=a
	print "Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S)

	while k < 500:
	    k = k + 1
	    R = (-1)*x*x/(2*k*(2*k-1)*4)
	    a = a * R
	    S = S + a
	   # print "Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S)


	print "Izdruka no liet.f. Beigas!"
	return S

x = np.arange (0.0, 6.18, 0.01)
y = np.cos(x/2)
yy = mans_cosinuss(x)

plt.plot(x,y)
plt.plot(x,yy)
plt.show()
'''



#funkcijas aprēķināšana
'''
print "Sveiks, lietotāj! Tagad Jūs redzēsiet funkcijas aprēķinu izmantojot izvirzījumu Teilora rindā. Sekojiet norādēm!"

def mans_cosinuss(x):
	k=0
	a=1
	S=a
	print "Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S)

	while k < 500:
	    k = k + 1
	    R = (-1)*x*x/(2*k*(2*k-1)*4)
	    a = a * R
	    S = S + a
	    print "Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
	print "Izdruka no lietotāja funkcijas"
	return S

x = 1 * input("Lietotāj, lūdzu ievadi argumentu (x): ")
y = cos(x/2)
print "standarta cos(%.2f) = %6.2f"%(x,y)
yy = mans_cosinuss(x)
print type(yy)
print "mans cos(%.2f) = %6.2f"%(x,yy)
'''
