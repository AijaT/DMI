# -*- coding: utf-8 -*-
from math import sin
# a0, a1, a2, a3 -> a


x = 1. * input("Lietotāj, lūdzu ievadi argumentu (x): ")

y = sin(x)
print "sin(%.2f) = %.2f"%(x,y)

#a0 = (-1)**0*x**1/(1)
a = (-1)**0*x**1/(1)
#s = a0
s = a
print "a0 = %.2f s0 = %.2f"%(a,s)

#a1 = (-1)**1*x**3/(1*2*3)
#a1 = a0 * (-1)*x*x//(2*3)
a = a * (-1)*x*x/(2*3)
#s = s + a1
s = s + a
print "a1 = %.2f s1 = %.2f"%(a,s)

#a2 = (-1)**2*x**5/(1*2*3*4*5)
#a2 = a1 * (-1)*x*x/(4*5)
a =  a * (-1)*x*x/(4*5)
s = s + a
print "a2 = %.2f s2 = %.2f"%(a,s)

#a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
#a3 = a2 * (-1)*x*x/(6*7)
a = a * (-1)*x*x/(6*7)
s = s + a
print "a3 = %.2f s3 = %.2f"%(a,s)

