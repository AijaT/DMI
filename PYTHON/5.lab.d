import random
import numpy as np
import matplotlib.pyplot as plt

def mans_cosinuss(x):
    y = np.cos(x)
    return y

N = 100000
x = []
y = []
a = 0
b = np.pi
c = -1
d = 1

for i in range(N):
    x.append(random.uniform(a,b))
for i in range (N):
y.append(random.uniform(c,d))

red_x = []
red_y = []
green_x = []
green_y = []

for i in range(N):
    if (y[i] < mans_cosinuss(x[i]) and > 0) \
    or (y[i] > mans_cosinuss(x[i]) and < 0):
	green_x.append(X[i])
	green_y.append(y[i])
    else:
	red_x.append(x[i])
	red_y.append(x[i])

plt.plot(green_x, green_y, 'go')
plt.plot(red_x,red_y,'rv')
plt.grid()
plt.show()

areaRect = (b-a)* (d-c)
areaCos = areaRect * len(green_x) / N
print areaCos
