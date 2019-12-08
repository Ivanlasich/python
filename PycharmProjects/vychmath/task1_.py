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
print(rs)

def v0(r):
    if a < r < b:
        return np.exp((-4 * (2 * r - (a + b)) ** 2) / ((b - a) ** 2 - (2 * r - (a + b)) ** 2))
    else:
        return 0


def u(I):
    global rmax, rmin, C, c
    h = (rmax - rmin) / I
    tau = C * h / c
    nt = int(T / tau)
    rs = np.arange(rmin - h / 2, rmax + h, h)
    print(rs)
    A1 = [1 / h * tau ** 2 * c ** 2 * rs[i] ** (1 - d) for i in range(I + 2)]
    A2 = [(rs[i] + h / 2) ** (d - 1) / h for i in range(I + 2)]
    A3 = [(rs[i] - h / 2) ** (d - 1) / h for i in range(I + 2)]

    u0 = [v0(rs[i]) for i in range(I + 2)]
    u1 = [0 for _ in range(I + 2)]

    u12 = [0 for _ in range(I + 2)]

    for i in range(1, I + 1):
        u12[i] = A1[i] * (A2[i] * (u0[i + 1] - u0[i]) - A3[i] * (u0[i] - u0[i - 1]))

    for i in range(1, I + 2):
        u1[i] = u0[i] + 0.5 * u12[i]

    tmp = u1.copy()

    res = [[0 for _ in range(I)] for _ in range(nt)]
    res[0] = u0[1:I+1]
    res[1] = u1[1:I+1]

    for i in range(1, nt):
        for j in range(1, I + 1):
            tmp[j] = 2 * u1[j] - u0[j] + A1[j] * (A2[j] * (u1[j + 1] - u1[j]) - A3[j] * (u1[j] - u1[j - 1]))
        tmp[0] = tmp[1]
        tmp[-1] = tmp[-2]
        u0 = u1.copy()
        u1 = tmp.copy()
        res[i] = u0[1:I+1]
    return res


u1 = u(I)

plt.plot(rs[0:200], u1[50])
print(tau*50)
plt.show()