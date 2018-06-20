# Richardson's Model of Arm race

import pylab
import numpy as np
import math as m

def f1(t, x, y): return a*y-m*x+r
def f2(t, x, y): return b*x-n*y+s

##a=2.
##b=2.
##m=5.
##n=5.
##r=5.
##s=5.

a=2.
b=2.
m=1.
n=1.
r=-2.
s=-2.

t_initial=0
t_final=100
h=0.001


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


        pylab.plot(X, Y, 'r-')
        
##Runge(-2., -2.,t_initial, h, t_final)
##Runge(-2., -0.35,t_initial, h, t_final)
##Runge(-2., 2.5,t_initial, h, t_final)
##Runge(-2., 5,t_initial, h, t_final)
##Runge(0.75, 5.,t_initial, h, t_final)
##Runge(3., 5.,t_initial, h, t_final)
##Runge(5., 5.,t_initial, h, t_final)
##Runge(5., 3.,t_initial, h, t_final)
##Runge(5., 0.75, t_initial, h, t_final)
##Runge(5., -2.,t_initial, h, t_final)
##Runge(2.5, -2.,t_initial, h, t_final)


## The case where the path of each trajectory depends on the initial variables
for x in np.arange(-2., 6.):
        for y in np.arange(-2, 6.):
                Runge(x, y, t_initial, h, t_final)

pylab.xlim(-2, 5)
pylab.ylim(-2, 5)
pylab.xlabel('X->')
pylab.ylabel('Y->')
pylab.show()
