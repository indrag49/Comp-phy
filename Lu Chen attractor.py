import pylab
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f1(t, x, y, z): return a*(y-x)
def f2(t, x, y, z): return x-x*z+c*y+u
def f3(t, x, y, z): return x*y-b*z

a=36.
b=3.
c=20.
u=5.

x_initial=.1
y_initial=.3
z_initial=-.6

t_initial=0
t_final=100
h=0.001


def Runge(x_initial, y_initial, z_initial, t_initial, h, t_final): 
        time=list(np.arange(t_initial, t_final+h, h))
        X=[x_initial]
        Y=[y_initial]
        Z=[z_initial]
        
        
        for i in range(1, len(time)):
                p=time[i-1]
                q=X[i-1]
                r=Y[i-1]
                s=Z[i-1]

                k11=h*f1(p, q, r, s)
                k21=h*f2(p, q, r, s)
                k31=h*f3(p, q, r, s)

                k12=h*f1(p+h/2., q+k11/2., r+k21/2., s+k31/2.)
                k22=h*f2(p+h/2., q+k11/2., r+k21/2., s+k31/2.)
                k32=h*f3(p+h/2., q+k11/2., r+k21/2., s+k31/2.)
                
                k13=h*f1(p+h/2., q+k12/2., r+k22/2., s+k32/2.)
                k23=h*f2(p+h/2., q+k12/2., r+k22/2., s+k32/2.)
                k33=h*f3(p+h/2., q+k12/2., r+k22/2., s+k32/2.)
                
                k14=h*f1(p+h, q+k13, r+k23, s+k33)
                k24=h*f2(p+h, q+k13, r+k23, s+k33)
                k34=h*f3(p+h, q+k13, r+k23, s+k33)

                X+=[X[i-1]+(k11+2*k12+2*k13+k14)/6., ]
                Y+=[Y[i-1]+(k21+2*k22+2*k23+k24)/6., ]
                Z+=[Z[i-1]+(k31+2*k32+2*k33+k34)/6., ]

##        fig=plt.figure()
##        ax=plt.axes(projection='3d')
##        ax.plot3D(X, Y, Z, 'red')
##        ax.set_xlabel('X')
##        ax.set_ylabel('Y')
##        ax.set_zlabel('Z')
##        plt.show()

        pylab.subplot(3, 2, 1)
        pylab.plot(X, Y)
        pylab.xlabel('X')
        pylab.ylabel('Y')

        pylab.subplot(3, 2, 2)
        pylab.plot(X, Z, 'r-')
        pylab.xlabel('X')
        pylab.ylabel('Z')

        pylab.subplot(3, 2, 3)
        pylab.plot(Y, Z, 'g-')
        pylab.xlabel('Y')
        pylab.ylabel('Z')

        pylab.subplot(3, 2, 4)
        pylab.plot(time, X, 'y-')
        pylab.xlabel('time')
        pylab.ylabel('X')
            
        pylab.subplot(3, 2, 5)
        pylab.plot(time, Y, 'r-')
        pylab.xlabel('time')
        pylab.ylabel('Y')

        pylab.subplot(3, 2, 6)
        pylab.plot(time, Z)
        pylab.xlabel('time')
        pylab.ylabel('Z')

        pylab.show()



Runge(x_initial, y_initial, z_initial, t_initial, h, t_final)