# -*- coding: utf-8 -*-
from math import sin
# a0, a1, a2, a3 -> a

x = 1. * input("Lietotāj, lūdzu ievadi argumentu (x): ")

y = sin(x)
print "sin(%.2f) = %.2f"%(x,y)

k = 0
a = (-1)**0*x**1/(1)
s = a
print "a0 = %.2f s0 = %.2f"%(a,s)

k = 1
#a = a * (-1)*x*x/(2*3)
a = a * (-1)*x*x/((2*k)*(2*k+1))
s = s + a
#print "a1 = %.2f s1 = %.2f"%(a,s)
print "a%d = %6.2f s%d = %6.2f"%(k,a,k,s)

k = 2
#a =  a * (-1)*x*x/(4*5)
a =  a * (-1)*x*x/((2*k)*(2*k+1))
s = s + a
#print "a2 = %.2f s2 = %.2f"%(a,s)
print "a%d = %6.2f s%d = %6.2f"%(k,a,k,s)

k= 3
#a = a * (-1)*x*x/(6*7)
a = a * (-1)*x*x/((2*k)*(2*k+1))
s = s + a
#print "a3 = %.2f s3 = %.2f"%(a,s)
print "a%d = %6.2f s%d = %6.2f"%(k,a,k,s)

