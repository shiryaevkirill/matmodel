import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import sin,cos

N = 1150
n = 12

# ___1___
# a1 = 0.67
# a2 = 0.000067
# t = np.arange(0,5,0.1)

# ___2___
# a1 = 0.000076
# a2 = 0.76
# t = np.arange(0,0.02,0.00001)

# ___3___
a1 = 0.76
a2 = 0.67
t = np.arange(0,0.5,0.01)

dn_max = [-1,-1]


def f(n,t):
    dn = (a1 + a2*n)*(N-n)
    global dn_max
    if dn >  dn_max[0]:
         dn_max = [dn,t]
    return dn

def f3(n,t):
    dn = (a1*sin(t)+a2*cos(t)*n)*(N-n)
    return dn


res = odeint(f3,n,t)

print(dn_max[1])

plt.plot(t,res[:,0])
plt.show()
