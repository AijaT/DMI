 # -*- coding: utf-8 -*-
from math import sin

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    s = a
    print "Izdruka no liet.f. a0 = %.2f s0 = %.2f"%(a,s)

    while k < 3:
          k = k + 1
          a = a * (-1)*x*x/((2*k)*(2*k+1))
          s = s + a
          print "Izdruka no liet.f. a%d = %6.2f s%d = %6.2f"%(k,a,k,s)
    print "Izdruka no liet.f. Beigas!"
    return s


x = 1. * input("Lietotāj, lūdzu ievadi argumentu (x): ")

y = sin(x)
print "Standarta sin(%.2f) = %.2f"%(x,y)
yy = mans_sinuss (x)
print "Mans sin(%.2f) = %.2f"%(x,yy)







'''
k = k + 1
a = a * (-1)*x*x/((2*k)*(2*k+1))
s = s + a
print "a%d = %6.2f s%d = %6.2f"%(k,a,k,s)

k = k +1
a =  a * (-1)*x*x/((2*k)*(2*k+1))
s = s + a
print "a%d = %6.2f s%d = %6.2f"%(k,a,k,s)

k = k + 1
a = a * (-1)*x*x/((2*k)*(2*k+1))
s = s + a
print "a%d = %6.2f s%d = %6.2f"%(k,a,k,s)
'''
