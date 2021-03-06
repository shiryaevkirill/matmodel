import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# первая задача

w = 1.2
g = 0

x0 = 0.2
y0 = -0.2

t0 = 0.0;
tmax = 55;
dt = 0.05

t = np.arange(t0,tmax+dt,dt)

v0 = [x0,y0]

def y(v,t):
    x,y = v
    return [y,-1*np.power(w,2)*x - g * y]

ans_1 = odeint(y,v0,t);

fig1, ax1 = plt.subplots()

# фазовый портрет
ax1.plot(ans_1[:,0], ans_1[:,1])

fig4, ax4 = plt.subplots()

# решение уравнения
ax4.plot(t, ans_1[:,0])
ax4.plot(t, ans_1[:,1])


# вторая
w = 4.3
g = 2

ans_2 = odeint(y,v0,t);

fig2, ax2 = plt.subplots()

# фазовый портрет
ax2.plot(ans_2[:,0], ans_2[:,1])

fig5, ax5 = plt.subplots()

# решение уравнения
ax5.plot(t, ans_2[:,0])
ax5.plot(t, ans_2[:,1])


# третья

w = 7.5
g = 7.4


def f(t):
    return 2.2 * cos(0.6*t)


def y_2(v,t):
    x,y = v
    return [y_2,-1*np.power(w,2)*x - g * y - f(t)]



ans_3 = odeint(y,v0,t);

fig3, ax3 = plt.subplots()

# фазовый портрет
ax3.plot(ans_3[:,0], ans_3[:,1])

fig6, ax6 = plt.subplots()

# решение уравнения
ax6.plot(t, ans_3[:,0])
ax6.plot(t, ans_3[:,1])


plt.show()

