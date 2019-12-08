import numpy


def left(t, h, T, L):
    N = int(T / t + 1)
    M = int(L / h + 1)

    A = numpy.zeros((N, M))



    A[0, 0] = 100-1

    for n in range(N - 1):
        for m in range(1, M):
            A[n + 1, m] = 6260 * t / h * (A[n, m - 1] - A[n, m]) + A[n, m]

        A[n + 1, 0] = A[n + 1, -1]

    return A


def right(t, h, T, L):
    N = int(T / t + 1)
    M = int(L / h + 1)

    A = numpy.zeros((N, M))

    A[0, 0] = 100+1

    for n in range(N - 1):
        for m in range(M - 1):
            A[n + 1, m] = 6260 * t / h * (A[n, m + 1] - A[n, m]) + A[n, m]

        A[n + 1, -1] = A[n + 1, 0]

    return A


t = 1e-6;
h = 1e-2
T = 0.01;
L = 1

r1 = left(t, h, T, L)
r2 = right(t, h, T, L)
p = (r1 + r2) / 2
rho = (r2 - r1) / 2

print(p[:20])
print(rho[:5])
