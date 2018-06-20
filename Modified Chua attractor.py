## Modified Chua Attractor solved with RK4

import pylab
import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f1(t, x, y, z): return alpha*(y+b*m.sin(m.pi*x/(2*a) + d))
def f2(t, x, y, z): return x-y+z
def f3(t, x, y, z): return -beta*y

alpha=10.82
beta=14.286
a=1.3
b=.11
d=0                               


x_initial=1
y_initial=1
z_initial=0


t_initial=0
t_final=100
h=0.0001

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

        fig=plt.figure()
        ax=plt.axes(projection='3d')
        ax.plot3D(X, Y, Z, 'red')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()

Runge(x_initial, y_initial, z_initial, t_initial, h, t_final)
