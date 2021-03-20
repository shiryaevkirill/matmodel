import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

a = 0.01
b = 0.02

N = 12800
I = 180
R = 58
S = N - I - R

t = np.arange(0,400,0.01)

v = [S,I,R]

def f1(v,t):
    dS = 0
    dI = -1*b*v[1]
    dR = b*v[1]
    return [dS,dI,dR]

def f2(v,t):
    dS = -1*a*v[0]
    dI = a*v[0] - b*v[1]
    dR = b*v[1]
    return [dS,dI,dR]

res = odeint(f2,v,t)

plt.plot(t, res[:,0])
plt.plot(t, res[:,1])
plt.plot(t, res[:,2])

plt.legend(('S(t)','I(t)','R(t)'))

plt.show()