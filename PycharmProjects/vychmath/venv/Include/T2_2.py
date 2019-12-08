import numpy

def progonka(d, e, c, b, N):
    alf = numpy.zeros(N)
    bet = numpy.zeros(N)
    x = numpy.zeros(N)

    for i in range(1,N-1):

        alf[i+1]=-e[i]/(d[i]+c[i]*alf[i])

        bet[i+1]=(-c[i]*bet[i]+b[i])/(d[i]+c[i]*alf[i])
    x[N-1]=(-c[N-1]*bet[N-1] + bet[N-1])/(d[N-1]+c[N-1]*alf[N-1])
    for i in range(N-2,0,-1):
        x[i]=alf[i+1]*x[i+1]+bet[i+1]

    return x

def obvious(t, h, u):

    for j in range(1,N-1):
        for i in range(0,N):
            u[j+1,i] = (1 -2*t/h**2)*u[j][i] + (t/h**2)*(u[j][i+1] + u[j][i-1])+t*q[i][j]

    return u

L = 1
N = 100
t = 10/N
h = L/N

bet = numpy.zeros((5, 5))
bet[0:]=0
bet[1:]=2
bet[2:]=5
print(bet)
print(numpy.max(bet))
