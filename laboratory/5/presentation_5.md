---
## Front matter
lang: ru-RU
title: "Лабораторная работа №5: Модель хищник-жертва"
subtitle: "*дисциплина: Математическое моделирование*"
author: "Ширяев Кирилл Владимирович"
date: 2021, 11 March

## Formatting
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
toc: false
slide_level: 2
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true

---


# Цель работы

Ознакомиться с моделью "хищник-жертва" и построить графики по этой модели.

# Задание

Для модели «хищник-жертва»:
$$\begin{cases}
\frac{dx}{dt}=-0.67x(t)+0.067x(t)y(t)\\
\frac{dy}{dt}=0.66y(t)-0.065x(t)y(t)
\end{cases}$$

Построить график зависимости численности хищников от численности жертв,
а также графики изменения численности хищников и численности жертв при
следующих начальных условиях: $x_0=9$, $y_0=19$. Найти стационарное
состояние системы.



# Выполнение лабораторной работы

# Библиотеки

Подключаю все необходимые библиотеки

```
import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
```

# Значения

Ввод значений из своего варианта (39 вариант)
```
a=0.67
b=0.067
c=0.66
d=0.065
x0=np.array([9,19])
t=np.arange(0,400,0.1)
```

# Решение

Решение системы
```
def syst(x,t):
    dx_1=-a*x[0]+b*x[0]*x[1]
    dx_2=c*x[1]-d*x[0]*x[1]
    return [dx_1, dx_2]

y=odeint(syst, x0, t)
```

# Вывод графика №1

Вывод графика зависимости численности хищников от численности жертв(рис. -@fig:003).

![Вывод графика №1](images/lab5_3.jpg){ #fig:003 width=70% }

# Вывод графика №2

Вывод графика изменения численности хищников(рис. -@fig:004).

![Вывод графика №2](images/lab5_4.jpg){ #fig:004 width=70% }

# Вывод графика №3

Вывод графика изменения численности жертв(рис. -@fig:005).

![Вывод графика №3](images/lab5_5.jpg){ #fig:005 width=70% }

# Стационарное состояние системы

Система будет стационарна в точке с координатами (10.153846153846153 10.0)

# Выводы

Я ознакомился с моделью "хищник-жертва", построила графики по этой модели и нашла стационарное состояние системы.
