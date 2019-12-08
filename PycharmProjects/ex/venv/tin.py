import numpy as np
from matplotlib import pyplot as plt

rmin = 0
rmax = 1.8
a = 0.6
b = 1.2

I = 200
d = 2
C = 0.75
c = 1.5
T = 1.
h = (rmax - rmin) / I
tau = C * h / c
nt = int(T / tau)
rs = np.arange(rmin - h / 2, rmax + h, h)


def v0(r):

    if a < r < b:
        return np.exp((-4 * (2 * r - (a + b)) ** 2) / ((b - a) ** 2 - (2 * r - (a + b)) ** 2))
    else:
        return 0

print(rs)