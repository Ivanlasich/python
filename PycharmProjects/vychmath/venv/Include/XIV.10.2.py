import numpy



def skhem1(h, t, L, T):
    N = int(T / t +1)
    M = int(L / h +1)
    A = numpy.zeros((N, M))

    for m in range(M):
        A[0, m] = numpy.sin(4 * numpy.pi * m * h / L)

    for n in range(N - 1):
        for m in range(1, M):
            A[n + 1, m] = (A[n, m - 1] - A[n, m]) * t / h + A[n, m]
        A[n + 1, 0] = A[n + 1, -1]  #периодич усл
    return A

def skhem2(h, t, L, T):
    N = int(T / t + 1)
    M = int(L / h + 1)
    A = numpy.zeros((N, M))
    for m in range(M):
        A[0, m] = numpy.sin(4 * numpy.pi * m * h / L)

    for n in range(N - 1):
        for m in range(1, M-1):
            A[n+1,m] = t**2/(2*h**2)*(A[n,m+1]-2*A[n,m]+A[n,m-1])-t/(2*h)*(A[n,m+1]-A[n,m-1])+ A[n,m]


        A[n + 1, -1] = A[n + 1, 0]

    return A




ans1 = skhem1(0.5, 0.5, 20, 18)
ans2 = skhem1(0.25, 0.25, 20, 18)
ans3 = skhem1(0.125, 0.125, 20, 18)
ans4 = skhem1(0.5, 0.3, 20, 18)
ans5 = skhem1(0.5, 0.15, 20, 18)
ans6 = skhem1(0.5, 0.075, 20, 18)

print(numpy.max(numpy.abs(ans1 - ans3[::4, ::4])))
print(numpy.max(numpy.abs(ans2[::2, ::2] - ans3[::4, ::4])))


ans7 = skhem2(0.5, 0.5, 20, 18)
ans8 = skhem2(0.25, 0.25, 20, 18)
ans9 = skhem2(0.125, 0.125, 20, 18)
ans10 = skhem2(0.5, 0.3, 20, 18)
ans11 = skhem2(0.5, 0.15, 20, 18)
ans12 = skhem2(0.5, 0.075, 20, 18)

print(numpy.max(numpy.abs(ans7 - ans9[::4, ::4])))
print(numpy.max(numpy.abs(ans8[::2, ::2] - ans9[::4, ::4])))
