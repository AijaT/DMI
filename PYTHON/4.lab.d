# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

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

a = 0
b = 3 * np.pi
x = np.arange(a,b,0.5)
y = mans_cosinuss(x)
plt.plot(x,y)
plt.grid()
#plt.show()

n = len(x)
y_prim = []
for i in range(n-1):
    #print i, x[i], y[i],
    delta_y = y[i+1]-y[i]
    delta_x = x[i+1]-x[i]
    #y_prim = delta_y/delta_x
    #print y_prim
    y_prim.append(delta_y/delta_x)
    #print y_prim[i]

plt.plot(x[:n-1],y_prim,'rv')
#plt.show()

y_prim_prim - []
for i in range(n-2):
    delta_x = x[i+1]-x[i]
    delta_y_prim = y_prim[i+1]-y_prim[i]
    y_prim_prim.append(delta_y_prim/delta_x)

plt.plot(x[:n-2],y_prim_prim,'b*')
plt.show()
