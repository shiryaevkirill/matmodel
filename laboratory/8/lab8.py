import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

M0_1 = 3.3
M0_2 = 2.3
p_cr = 22
N = 33
q = 1
tau1 = 22
tau2 = 11
p1 = 6.6
p2 = 11.1


a1 = p_cr/(tau1*tau1*p1*p1*N*q);
a2 = p_cr/(tau2*tau2*p2*p2*N*q);
b = p_cr/(tau1*tau1*tau2*tau2*p1*p1*p2*p2*N*q);
c1 = (p_cr-p1)/(tau1*p1);
c2 = (p_cr-p2)/(tau2*p2);


v = [M0_1,M0_2]
t = np.arange(0,30,0.01)

def f1(v,t):
    dM_1 = v[0] - (b/c1)*v[0]*v[1] - (a1/c1)*v[0]*v[0]
    dM_2 = (c2/c1)*v[1] - (b/c1)*v[0]*v[1] - (a2/c1)*v[1]*v[1]
    return [dM_1,dM_2]

res = odeint(f1,v,t)
plt.plot(t,res[:,0])
plt.plot(t,res[:,1])
plt.show()

def f2(v,t):
    dM_1 = v[0] - (b / c1) * v[0] * v[1] - (a1 / c1) * v[0] * v[0]
    dM_2 = (c2 / c1) * v[1] - (b/c1 + 0.00093) * v[0] * v[1] - (a2 / c1) * v[1] * v[1]
    return [dM_1, dM_2]

res2 = odeint(f2,v,t)
plt.plot(t,res2[:,0])
plt.plot(t,res2[:,1])
plt.show()