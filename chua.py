#Chua's attractor

import pylab
import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f1(t, x, y, z): return alpha*(y-x)-alpha*(m1*x+(m0-m1)*m.tanh(x))
def f2(t, x, y, z): return x-y+z
def f3(t, x, y, z): return -(beta*y+gamma*z)

alpha=8.4562
beta=12.0732
gamma=0.0052
m1=0.3532
m0=-1.1468


x_initial=8.82
y_initial=0.5561
z_initial=-12.6008
t_initial=0
t_final=10
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

                X+=[X[i-1]+(k11+2*k12+2*k13+k14), ]
                Y+=[Y[i-1]+(k21+2*k22+2*k23+k24), ]
                Z+=[Z[i-1]+(k31+2*k32+2*k33+k34), ]
        fig=plt.figure()
        ax=plt.axes(projection='3d')
        ax.plot3D(X, Y, Z, 'red')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()


Runge(x_initial, y_initial, z_initial, t_initial, h, t_final)