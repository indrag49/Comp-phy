##Author: Indranil Ghosh, Jadavpur University, Physics Department

import random, pylab

def estimate_Pi(N):
    c=0
    for i in range(1, N+1):
        x=random.random()
        y=random.random()
        if x**2 + y**2 <= 1: c+=1
    return 4.*c/N

def plot_func(n):
    N=[]
    V=[]
    for i in range(1, n+1, 50):
        V+=[estimate_Pi(i), ]
        N+=[i, ]
    pylab.plot(N, V, 'r-')
    pylab.xlabel("N-->")
    pylab.ylabel("V-->")
    pylab.show()

