#Duffing Attractor

import pylab
import numpy as np
import math as m

def f3(t, x, y): return y
def f4(t, x, y): return x-x**3-a*y+b*m.cos(w*t)

a=0.1875
b=0.564
w=1.5

x_initial=0.
y_initial=0.


t_initial=0
t_final=1000
h=0.01


def Runge1(x_initial, y_initial, t_initial, h, t_final): 
        time=list(np.arange(t_initial, t_final+h, h))
        X=[x_initial]
        Y=[y_initial]        
        
        for i in range(1, len(time)):
                p=time[i-1]
                q=X[i-1]
                r=Y[i-1]

                k11=h*f3(p, q, r)
                k21=h*f4(p, q, r)

                k12=h*f3(p+h/2., q+k11/2., r+k21/2.)
                k22=h*f4(p+h/2., q+k11/2., r+k21/2.)
                
                k13=h*f3(p+h/2., q+k12/2., r+k22/2.)
                k23=h*f4(p+h/2., q+k12/2., r+k22/2.)
                
                k14=h*f3(p+h, q+k13, r+k23)
                k24=h*f4(p+h, q+k13, r+k23)

                X+=[X[i-1]+(k11+2*k12+2*k13+k14), ]
                Y+=[Y[i-1]+(k21+2*k22+2*k23+k24), ]

                
        pylab.plot(X, Y, 'ko', ms=1)
        pylab.ylabel('Y')
        pylab.xlabel('X')
        pylab.show()


Runge1(x_initial, y_initial,t_initial, h, t_final)