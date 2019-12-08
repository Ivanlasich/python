import numpy as np
from matplotlib import pyplot as plt

rmin = 0
rmax = 1.8
d = 2
C = 0.75
c = 1.5
T = 1.5
I=200
h = (rmax - rmin) / I
tau = C * h / c
n = int(T / tau)
times = [i * tau for i in range(n)]
approx = [2.5 for i in range(n)]
def r(I):
    h = (rmax - rmin) / I
    rs = np.arange(rmin - h / 2, rmax + h / 2, h)
    return rs


def v0(r):
    a = 0.6
    b = 1.2

    if a < r < b:
        return np.exp((-4 * (2 * r - (a + b)) ** 2) / ((b - a) ** 2 - (2 * r - (a + b)) ** 2))
    else:
        return 0



def u(I):
    h = (rmax - rmin) / I
    tau = C * h / c
    n = int(T / tau)
    rs = r(I)

    u = np.zeros((n, I + 1))

    for j in range(0, I + 1):
        u[0][j] = v0(rs[j])

    for j in range(1, I):
        u[1][j] = 2 * u[0][j] - u[0][j] + (1 / h * tau ** 2 * c ** 2 * rs[j] ** (1 - d)) * (
                    (((rs[j] + h / 2) ** (d - 1)) * (u[0][j + 1] - u[0][j]) / h) - (
                        ((rs[j] - h / 2) ** (d - 1)) * (u[0][j] - u[0][j - 1]) / h))

    for i in range(1, n - 1):
        for j in range(1, I):
            u[i + 1][j] = (2 * u[i][j]) - (u[i - 1][j]) + (1 / h * tau ** 2 * c ** 2 * rs[j] ** (1 - d)) * (
                        (((rs[j] + h / 2) ** (d - 1)) * (u[i][j + 1] - u[i][j]) / h) - (
                            ((rs[j] - h / 2) ** (d - 1)) * (u[i][j] - u[i][j - 1]) / h))

        u[i + 1][1] = u[i + 1][0]
        u[i + 1][I] = u[i + 1][I - 1] = 0
    return u;

def norm_C(u1,u2,u3):
    max1 = 0
    pr1 = 0

    max2 = 0
    pr2 = 0

    n = len(u1)
    m = len(u1[0])
    a = np.zeros(n)
    for i in range(0,n):
        for j in range(0, m):
            pr1 = abs(u1[i][j]-u2[i*3][j*3])
            pr2 = abs(u2[i*3][j*3] - u3[i * 9][j * 9])
            if (pr1 > max1):
                max1 = pr1
            if (pr2 > max2):
                max2 = pr2
        a[i] = max1/max2

    return a

def norm_L2(u1,u2,u3):
    pr1 = 0
    pr2 = 0

    n = len(u1)
    m = len(u1[0])
    a = np.zeros(n)
    for i in range(0,n):
        for j in range(0, m):
            pr1 +=abs(u1[i][j] - u2[i*3][j*3])**2
            pr2 +=abs(u2[i*3][j*3] - u3[i*9][j*9])**2

        a[i] = (np.sqrt(pr1))/(np.sqrt(pr2))

    return a








u1 = u(200)
u2 = u(600)
u3 = u(1800)
u = norm_C(u1, u2, u3)
s = norm_L2(u1, u2, u3)

print(s)
plt.plot(times, approx)
plt.plot(times, u)
plt.plot(times, s)
plt.show()
