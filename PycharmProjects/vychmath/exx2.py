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
    """Initial dispersion impulse function"""
    if a < r < b:
        return np.exp((-4 * (2 * r - (a + b)) ** 2) / ((b - a) ** 2 - (2 * r - (a + b)) ** 2))
    else:
        return 0


def v0_r(r):
    """Initial dispersion impulse function derivative"""
    return v0(r) * ((-16 * (2 * r - a - b) * ((b - a) ** 2 - (2 * r - a - b) ** 2) - 16 * (2 * r - a - b) ** 2 * (
                2 * r - (a + b))) /
                   ((b - a) ** 2 - (2 * r - (a + b)) ** 2) ** 2)


def u_r(r, t):
    return (1 - d) / 2 * r ** (-(1 + d) / 2) * v0(c * t - r - rmax) - r ** ((1 - d) / 2) * v0_r(c * t - r - rmax)


def u(I):
    h = (rmax - rmin) / I
    tau = C * h / c
    nt = int(T / tau)
    rs = np.arange(rmin - h / 2, rmax + h, h)

    A1 = [1. / h * tau ** 2 * c ** 2 * rs[i] ** (1 - d) for i in range(I + 2)]
    A2 = [(rs[i] + h / 2) ** (d - 1) / h for i in range(I + 2)]
    A3 = [(rs[i] - h / 2) ** (d - 1) / h for i in range(I + 2)]

    u0 = [rs[i] ** ((1 - d) * 0.5) * v0(-rs[i] + 1.75) for i in range(I + 2)]
    u1 = [rs[i] ** ((1 - d) * 0.5) * v0(c * tau - rs[i] + 1.75) for i in range(I + 2)]

    tmp = [0 for i in range(I + 2)]

    u_prev = u0.copy()
    u_curr = u1.copy()

    res = [[0 for _ in range(1, I + 1)] for _ in range(nt)]
    res[0] = u0[1:I + 1]

    for n in range(1, nt):
        res[n] = u_curr[1:I + 1]
        for i in range(1, I + 1):
            tmp[i] = 2 * u_curr[i] - u_prev[i] + A1[i] * (
                    A2[i] * (u_curr[i + 1] - u_curr[i]) - A3[i] * (u_curr[i] - u_curr[i - 1]))

        u_curr[0] = u_curr[1] - h * u_r(rmin, n * tau)
        u_curr[I + 1] = u_curr[I] + h * u_r(rmax, n * tau)

        u_prev = u_curr.copy()
        u_curr = tmp.copy()

    return res


def anal(I):
    global rmin, rmax, C, c
    h = (rmax - rmin) / I
    tau = C * h / c
    nt = int(T / tau)
    rs = np.arange(rmin - h / 2, rmax + h, h)
    res = [[] for _ in range(nt)]
    for n in range(nt):
        res[n] = [rs[i] ** ((1. - d) / 2) * v0(c * tau * n - rs[i] + 1.75) for i in range(1, I + 1)]
    return res


rs = np.arange(rmin - h / 2, rmax + h, h)
u0 = anal(I+2)

plt.plot(rs, u0[26])
plt.title("O22")
plt.grid()
plt.show()
'''
k1 = 3
an1 = anal(I)
print(an1)
an2 = anal(I * k1)
print(an2)
u1 = u(I)
print(u1)
u2 = u(I * k1)
print(u2)
diff1 = [[0 for _ in range(I)] for _ in range(nt)]
diff2 = [[0 for _ in range(I*k1)] for _ in range(nt*k1)]
for i in range(nt):
    for j in range(I):
        diff1[i][j] = abs(an1[i][j] - u1[i][j])
for i in range(nt*k1):
    for j in range(I*k1):
        diff2[i][j] = abs(an2[i][j] - u2[i][j])

u1_max = [0 for n in range(nt)]
u2_max = [0 for n in range(nt)]
for n in range(nt):
    u1_max[n] = max(diff1[n])
    u2_max[n] = max(diff2[n*k1])
norms = [u1_max[n] / u2_max[n] for n in range(2, nt)]

times = [i * tau for i in range(2, nt)]
plt.plot(times, norms)
plt.plot(times, [k1**2 for _ in times])
plt.grid()
plt.show()

'''