## Laser threshhold model solved by Runge Kutta algorithm

import pylab
G=1
k=1
alpha=0.5
N0=1
n_initial=0.1
t_initial=0
t_final=10
h=0.001
def f(t, n): return (G*N0-k)*n-G*alpha*n**2

def Runge(n_initial, t_initial, h, t_final):
        time=list(np.arange(t_initial, t_final+h, h))
        X=[n_initial]
        
        for i in range(1, len(time)):
                p=time[i-1]
                q=X[i-1]
                k1=h*f(p, q)
                k2=h*f(p+h/2., q+k1/2.)
                k3=h*f(p+h/2., q+k2/2.)
                k4=h*f(p+h, q+k3)
                X+=[q+(k1+2*k2+2*k3+k4)/6., ]

        Y=[(G*N0-k)*i-G*alpha*i**2 for i in X]
        pylab.plot(X, Y, 'k-')
        pylab.xlabel("n-->")
        pylab.ylabel("$\dot{n}$ -->")
        pylab.show()

Runge(n_initial, t_initial, h, t_final)
