import numpy as np
from matplotlib import pyplot as plt

rmin = 0.1
rmax = 1.8
a = 0.6
b = 1.2

I = 50
d = 1
C = 0.8
c = 1.5
T = 0.5
h = (rmax - rmin) / I
tau = C * h / c
nt = int(T / tau)
rs = np.arange(rmin - h / 2, rmax + h, h)




def v0(r):
    if a < r < b:
        return np.exp((-4 * (2 * r - (a + b)) ** 2) / ((b - a) ** 2 - (2 * r - (a + b)) ** 2))
    else:
        return 0


def v0_r(r):
    return v0(r) * ((-16 * (2 * r - a - b) * ((b - a) ** 2 - (2 * r - a - b) ** 2) - 16 * (2 * r - a - b) ** 2 * (
                2 * r - (a + b))) /
                   ((b - a) ** 2 - (2 * r - (a + b)) ** 2) ** 2)


def u_r(r, t):
    return (1 - d) / 2 * r ** (-(1 + d) / 2) * v0(c * t - r - rmax) - r ** ((1 - d) / 2) * v0_r(c * t - r - rmax)


def u(I):
    h = (rmax - rmin) / I
    tau = C * h / c
    n = int(T / tau)
    rs = np.arange(rmin - h / 2, rmax + h, h)

    u = np.zeros((n, I+2))

    for j in range(0, I+2):
        u[0][j] = rs[j] ** ((1 - d) * 0.5) * v0(-rs[j] + 1.75)


    for j in range(1, I+1):
        u[1][j] = rs[j] ** ((1 - d) * 0.5) * v0(c * tau - rs[j] + 1.75)
    u[1][0] = u[1][1]
    u[1][I+1] =u[1][I]



    for i in range(1,n-1):
        for j in range(1, I+1):
            u[i+1][j] = (2*u[i][j])-(u[i-1][j]) + (1/h * tau ** 2 * c ** 2 * rs[j] ** (1 - d))*((((rs[j] + h / 2) ** (d - 1))*(u[i][j+1]-u[i][j])/h) -  (((rs[j] - h / 2) ** (d - 1)) * (u[i][j]-u[i][j-1])/h))

        u[i+1][0] = u[i][1] - h * u_r(rmin, n * tau)
        u[i+1][I+1] = u[i][I] + h * u_r(rmax, n * tau)

    return u

def anal(I):
    global rmin, rmax, C, c
    h = (rmax - rmin) / I
    tau = C * h / c
    nt = int(T / tau)
    rs = np.arange(rmin - h / 2, rmax + h, h)
    res = [[] for _ in range(nt)]

    for n in range(nt):
        res[n] = [rs[i] ** ((1. - d) / 2) * v0(c * tau * n - rs[i] + 1.75) for i in range(0, I + 2)]
    return res


def norm_C(u1,u2,u3,u4):
    n = len(u1)
    m = len(u1[0])
    a = np.zeros(n)
    for i in range(0,n):
        max1 = 0.00001
        max2 = 0.00001
        k = 2
        for j in range(1, m-1):
            pr1 = abs(u1[i][j]-u2[i][j])
            pr2 = abs(u3[i*3][k] - u4[i*3][k])
            k = k + 3
            if (pr1 > max1):
                max1 = pr1
            if (pr2 > max2):
                max2 = pr2
        a[i] = max1/max2

    return a



times = [i * tau for i in range(nt)]
'''
rs = np.arange(rmin - h / 2, rmax + h, h)
u0 = anal(I)
u1 = u(I)
print(len(u0))
plt.plot(rs, u0[26])
plt.plot(rs, u1[26])
plt.title("O22")
plt.grid()
plt.show()

'''
rs = np.arange(rmin - h / 2, rmax + h, h)
#u0 = u(200)
an1 = anal(I)
print(an1[0])
k1 = 3
an2 = anal(I * 3)
u1 = u(I)
u2 = u(I * 3)
a =norm_C(u1,an1,u2,an2)
plt.plot(times, [9 for _ in times])
plt.plot(times, a)
plt.title("O22")
plt.grid()
plt.show()
