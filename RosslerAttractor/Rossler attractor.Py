## Plots of Rossler Attractor solved with RK4


import pylab
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f1(t, x, y, z): return -y-z
def f2(t, x, y, z): return x+a*y
def f3(t, x, y, z): return b+z*(x-c)

#a=0.2
#b=0.2
#c=5.7

a=0.1
b=0.1
c=18.

x_initial=0
y_initial=0
z_initial=0

##t_initial=0
##t_final=1000
##h=0.01

t_initial=0
t_final=100
h=0.01


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

                X+=[X[i-1]+(k11+2*k12+2*k13+k14), ]
                Y+=[Y[i-1]+(k21+2*k22+2*k23+k24), ]
                Z+=[Z[i-1]+(k31+2*k32+2*k33+k34), ]

        X_dashed=[]
        Y_dashed=[]
        Z_dashed=[]
                
        for i in range(len(time)):
                X_dashed+=[-Y[i]-Z[i], ]
                Y_dashed+=[X[i]+a*Y[i], ]
                Z_dashed+=[b+Z[i]*(X[i]-c), ]
                
##        pylab.plot(X_dashed, X, 'ko', ms=1)
##        pylab.ylabel('$\dot{X}$')
##        pylab.xlabel('X')
##        pylab.show()

##        fig=plt.figure()
##        ax=plt.axes(projection='3d')
##        ax.scatter3D(X_dashed, Y_dashed, Z_dashed, c=Z, cmap="Reds", s=10)
##        ax.scatter3D(X, Y, Z, c=Z, cmap="Reds", s=10)
##        ax.set_xlabel('$\dot{X}$')
##        ax.set_ylabel('$\dot{Y}$')
##        ax.set_zlabel('$\dot{Z}$')
##        plt.show()

        pylab.plot(time, Z, 'r-')
        pylab.ylabel('Z')
        pylab.xlabel('T')
        pylab.show()


Runge(x_initial, y_initial, z_initial, t_initial, h, t_final)