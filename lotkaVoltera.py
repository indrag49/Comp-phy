#Lotka-Volterra predator-prey model

import pylab
import numpy as np
import math as m

def f1(t, x, y): return a*x-b*x*y
def f2(t, x, y): return d*x*y-c*y

a=1.5
b=1.
c=3.
d=1.

x_initial=10.
y_initial=4.

t_initial=0
t_final=20
h=0.0001


def Runge(x_initial, y_initial, t_initial, h, t_final): 
        time=list(np.arange(t_initial, t_final+h, h))
        X=[x_initial]
        Y=[y_initial]        
        
        for i in range(1, len(time)):
                p=time[i-1]
                q=X[i-1]
                r=Y[i-1]

                k11=h*f1(p, q, r)
                k21=h*f2(p, q, r)

                k12=h*f1(p+h/2., q+k11/2., r+k21/2.)
                k22=h*f2(p+h/2., q+k11/2., r+k21/2.)
                
                k13=h*f1(p+h/2., q+k12/2., r+k22/2.)
                k23=h*f2(p+h/2., q+k12/2., r+k22/2.)
                
                k14=h*f1(p+h, q+k13, r+k23)
                k24=h*f2(p+h, q+k13, r+k23)

                X+=[X[i-1]+(k11+2*k12+2*k13+k14)/6., ]
                Y+=[Y[i-1]+(k21+2*k22+2*k23+k24)/6., ]

        pylab.plot(time, X, 'r-')
        pylab.plot(time, Y, 'g-')
        pylab.ylabel('X, Y')
        pylab.xlabel('T')
        pylab.show()

        pylab.plot(X, Y, '--')
        pylab.show()


Runge(x_initial, y_initial,t_initial, h, t_final)
