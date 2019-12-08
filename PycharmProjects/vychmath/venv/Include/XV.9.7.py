import numpy

def f(x, y):
    if((x-0.5)**2 + (y-0.5)**2 > 1/9):
        return -2;
    return 0

def cross(N, N_iter, u):
    R = numpy.zeros((N, N))
    h = 1 / N
    x = numpy.zeros(N)
    y = numpy.zeros(N)
    for j in range(N):
        y[j] = j * h
        for i in range(N):
            x[i] = i * h
            R[i][j] = f(x[i], y[j])

    for k in range (N_iter):
        for j in range(1, N-1):
            for i in range(1, N-1):
                u[i][j] =  (1/4)*(u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1]+R[i][j]*h*h)
    #        D[k:]=u[k:]
    return u


def nine_point(N, N_iter, u):
    h = 1 / N
    R = numpy.zeros((N, N))
    x = numpy.zeros(N)
    y = numpy.zeros(N)
    for j in range(N):
        y[j] = j * h
        for i in range(N):
            x[i] = i * h
            R[i][j] = f(x[i], y[j])
    for k in range(N_iter):
        for j in range(1, N - 1):
            for i in range(1, N - 1):
                u[i][j] = (3 / 14) * (u[i - 1][j] + u[i + 1][j]) + (3/14)*(u[i][j-1] + u[i][j+1]) + (1/28)*(u[i-1][j+1] + u[i-1][j-1] + u[i+1][j+1] + u[i+1][j-1]) +(3/14)*R[i][j]*h*h
    return u



N = 120
U = numpy.zeros((N, N))
for i in range(1,N-1):
    for j in range(1,N-1):
        U[i][j]=2
A = cross(N,25,U)
B = nine_point(N,25,U)
print(A)
print("  ")
print(B)