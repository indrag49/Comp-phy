## Strogatz example :3.4.2 solved by Runge kutta algorithm

import pylab
import numpy as np

x_initial=0.1
t_initial=-5
t_final=5
h=0.001

def Runge(r, x_initial, t_initial, h, t_final):
        def f(t, x): return -(r*t-t**3) 
        time=list(np.arange(t_initial, t_final+h, h))
        X=[x_initial]
        
        for i in range(1, len(time)):
                p=time[i-1]
                q=X[i-1]
                k1=h*f(p, q)
                k2=h*f(p+h/2., q+k1/2.)
                k3=h*f(p+h/2., q+k2/2.)
                k4=h*f(p+h, q+k3)
                X+=[q+(k1+2*k2+2*k3+k4)/6., ]
        return [time, X]
        pylab.show()

A=Runge(-3, x_initial, t_initial, h, t_final)
pylab.plot(A[0], A[1], 'k-')
pylab.xlabel("x -->")
pylab.ylabel("V -->")

B=Runge(0, x_initial, t_initial, h, t_final)
pylab.plot(B[0], B[1], '-')
pylab.xlabel("x -->")
pylab.ylabel("V -->")

C=Runge(5, x_initial, t_initial, h, t_final)
pylab.plot(C[0], C[1], 'r-')
pylab.xlabel("x -->")
pylab.ylabel("V -->")
pylab.title("Strogatz: Non linear dynamics, example: 3.4.2")
pylab.show()
