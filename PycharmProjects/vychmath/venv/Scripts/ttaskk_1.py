import numpy as np
from matplotlib import pyplot as plt

rmin = 0
rmax = 1.8
a = 0.6 #из условия
b = 1.2 #из условия

I = 200 #кол-во точек
d = 2 #размерность
C = 0.75
c = 1.5 #в условии
T = 1.
h = (rmax - rmin) / I
tau = C * h / c
nt = int(T / tau) #шаг времени
rs = np.arange(rmin - h / 2, rmax + h, h) #сетка
print(rs)