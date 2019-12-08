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

u = u(200)

print(tau*125)
plt.plot(rs, u[125])
plt.title("O22")
plt.grid()
plt.show()
