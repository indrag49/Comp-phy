## Simulation of Elastic pendulum, solved numerically with 4th order Runge Kutta method

from math import sqrt, sin, cos
import pylab
import numpy as np
import random, pygame, sys
from pygame.locals import *

g=9.81
pi=math.acos(-1.0)
m=2.
l=2.
k=5.

def f1(t, z1, z2, z3, z4): return z3
def f2(t, z1, z2, z3, z4): return z4
def f3(t, z1, z2, z3, z4): return -(2*z4*z3+g*sin(z1))/(l+z2)
def f4(t, z1, z2, z3, z4): return (l+z2)*z3**2-k*z2/m+g*cos(z1)


z1_initial=pi/2.
z2_initial=3.
z3_initial=0.1
z4_initial=1.
t_initial=0
t_final=30
h=0.001

def Runge(z1_initial, z2_initial, z3_initial, z4_initial, t_initial, h, t_final):
        time=list(np.arange(t_initial, t_final+h, h))
        Z1=[z1_initial]
        Z2=[z2_initial]
        Z3=[z3_initial]
        Z4=[z4_initial]

        for i in range(1, len(time)):
                p=time[i-1]
                q=Z1[i-1]
                r=Z2[i-1]
                s=Z3[i-1]
                o=Z4[i-1]
                
                k11=h*f1(p, q, r, s, o)
                k21=h*f2(p, q, r, s, o)
                k31=h*f3(p, q, r, s, o)
                k41=h*f4(p, q, r, s, o)
                
                k12=h*f1(p+h/2., q+k11/2., r+k21/2., s+k31/2., o+k41/2.)
                k22=h*f2(p+h/2., q+k11/2., r+k21/2., s+k31/2., o+k41/2.)
                k32=h*f3(p+h/2., q+k11/2., r+k21/2., s+k31/2., o+k41/2.)
                k42=h*f4(p+h/2., q+k11/2., r+k21/2., s+k31/2., o+k41/2.)
                
                k13=h*f1(p+h/2., q+k12/2., r+k22/2., s+k32/2., o+k42/2.)
                k23=h*f2(p+h/2., q+k12/2., r+k22/2., s+k32/2., o+k42/2.)
                k33=h*f3(p+h/2., q+k12/2., r+k22/2., s+k32/2., o+k42/2.)
                k43=h*f4(p+h/2., q+k12/2., r+k22/2., s+k32/2., o+k42/2.)
                
                k14=h*f1(p+h, q+k13, r+k23, s+k33, o+k43)
                k24=h*f2(p+h, q+k13, r+k23, s+k33, o+k43)
                k34=h*f3(p+h, q+k13, r+k23, s+k33, o+k43)
                k44=h*f4(p+h, q+k13, r+k23, s+k33, o+k43)
                
                Z1+=[Z1[i-1]+(k11+2*k12+2*k13+k14)/6., ]
                Z2+=[Z2[i-1]+(k21+2*k22+2*k23+k24)/6., ]
                Z3+=[Z3[i-1]+(k31+2*k32+2*k33+k34)/6., ]
                Z4+=[Z4[i-1]+(k41+2*k42+2*k43+k44)/6., ]
                
        return [time, Z1, Z2, Z3, Z4]
R=Runge(z1_initial, z2_initial, z3_initial, z4_initial, t_initial, h, t_final)
theta=R[1]
r=R[2]
theta_dashed=R[3]
r_dashed=R[4]
time=R[0]

X=[]
Y=[]

##for i in range(len(r)):
##        X+=[(l+r[i])*sin(theta[i]),]
##        Y+=[(l+r[i])*cos(theta[i]),]

##pylab.plot(time, theta, '-')
##pylab.plot(time, r, 'r-')
##pylab.plot(time, theta_dashed, 'r-')
##pylab.plot(time, r_dashed, 'r-')
##pylab.plot(X, Y, 'k-')
##pylab.show()

import pygame, random, sys
from pygame.locals import *
DISPLAYSURF=pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Double Pendulum problem")

WHITE=(255, 255, 255)
RED=(255, 0, 0)
BLACK=(0, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)

DISPLAYSURF.fill(WHITE)

i=0
while True:
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.image.save(DISPLAYSURF, 'DoublePendulum.png')
                        pygame.quit()
                        sys.exit()
        
        if i==len(theta):
                pygame.image.save(DISPLAYSURF, 'DoublePendulum.png')
                pygame.quit()
                sys.exit()
        
        DISPLAYSURF.fill(WHITE)

        X+=[(l+r[i])*sin(theta[i]),]
        Y+=[-(l+r[i])*cos(theta[i]),]


        pygame.draw.circle(DISPLAYSURF, WHITE, (int(600 + 0), 200 - int(0)), 2, 0)
        pygame.draw.circle(DISPLAYSURF, BLUE, (int(600 + X[i]*40), 200 - int(Y[i]*40)), 7, 0)
        pygame.draw.line(DISPLAYSURF, BLACK, (int(600 + 0), 200 - int(0)), (int(600 + X[i]*40), 200 - int(Y[i]*40)), 2)
##        pygame.draw.circle(DISPLAYSURF, RED, (int(600 + X2[i]*40), 200 - int(Y2[i]*40)), 7, 0)
##        pygame.draw.line(DISPLAYSURF, BLACK, (int(600 + X1[i]*40), 200 - int(Y1[i]*40)), (int(600 + X2[i]*40), 200 - int(Y2[i]*40)), 2)
        
        i+=1
        pygame.display.update()
