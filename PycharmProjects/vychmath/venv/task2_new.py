import numpy as np
from matplotlib import pyplot as plt

rmin = 0
rmax = 1.8
a = 0.6
b = 1.2
d = 2
C = 0.75
c = 1.5
T = 1.
I = 200
h = (rmax - rmin) / I
tau = C * h / c
n = int(T / tau)
rs = np.arange(rmin - h / 2, rmax + h, h)



def v0(r):
    if a < r < b:
        return np.exp((-4 * (2 * r - (a + b)) ** 2) / ((b - a) ** 2 - (2 * r - (a + b)) ** 2))
    else:
        return 0


def u(I):
    h = (rmax - rmin) / I
    tau = C * h / c
    n = int(T / tau)
    rs = np.arange(rmin - h / 2, rmax + h, h)

    u = np.zeros((n, I+2))

    for j in range(0, I+2):
        u[0][j] = v0(rs[j])

    for j in range(1, I+1):
        u[1][j] = u[0][j] + 0.5*(1/h * tau ** 2 * c ** 2 * rs[j] ** (1 - d))*((((rs[j] + h / 2) ** (d - 1))*(u[0][j+1]-u[0][j])/h) -  (((rs[j] - h / 2) ** (d - 1)) * (u[0][j]-u[0][j-1])/h))
    u[1][0] = u[1][1]
    u[1][I+1] =u[1][I]



    for i in range(1,n-1):
        for j in range(1, I+1):
            u[i+1][j] = (2*u[i][j])-(u[i-1][j]) + (1/h * tau ** 2 * c ** 2 * rs[j] ** (1 - d))*((((rs[j] + h / 2) ** (d - 1))*(u[i][j+1]-u[i][j])/h) -  (((rs[j] - h / 2) ** (d - 1)) * (u[i][j]-u[i][j-1])/h))

        u[i+1][0] = u[i][1]
        u[i+1][I+1] = u[i][I]

    return u

def norm_L2(u1,u2,u3):

    n = len(u1)
    m = len(u1[0])
    a = np.zeros(n)
    for i in range(0,n):
        k = 2
        k_1 = 5
        pr1 = 0
        pr2 = 0
        for j in range(1, m-1):
            pr1 +=abs(u1[i][j] - u2[i*3][k])**2
            pr2 +=abs(u2[i*3][k] - u3[i*9][k_1])**2
            k = k + 3
            k_1 = k_1 + 9
        a[i] = (np.sqrt(pr1))/(np.sqrt(pr2))

    return a

def norm_C(u1,u2,u3):
    n = len(u1)
    m = len(u1[0])
    a = np.zeros(n)
    for i in range(0,n):
        max1 = 0
        max2 = 0
        k = 2
        k_1 = 5
        for j in range(1, m-1):
            pr1 = abs(u1[i][j]-u2[i*3][k])
            pr2 = abs(u2[i*3][k] - u3[i * 9][k_1])
            k = k + 3
            k_1 = k_1 + 9
            if (pr1 > max1):
                max1 = pr1
            if (pr2 > max2):
                max2 = pr2
        a[i] = max1/max2

    return a


def rs(I):
    h = (rmax - rmin) / I
    tau = C * h / c
    n = int(T / tau)
    print(n)
    rs = np.arange(rmin - h / 2, rmax + h, h)
    return rs

times = [i * tau for i in range(n)]
u1=u(200)
u2=u(600)
u3=u(1800)
a = norm_C(u1,u2,u3)
a1 = norm_L2(u1,u2,u3)

plt.plot(times, a)
plt.plot(times, a1)
plt.plot(times, [9 for _ in times])
plt.title("O22")
plt.grid()
plt.show()
