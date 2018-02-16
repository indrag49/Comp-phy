## Simulation of Double Pendulum, solved numerically with 4th order Runge Kutta method

from math import sqrt, sin, cos
import pylab
import numpy as np

g=9.8
pi=3.14159265359
m1=2.
m2=1.
l1=3.
l2=6.

def f1(t, z1, z2, z3, z4): return z3
def f2(t, z1, z2, z3, z4): return z4
def f3(t, z1, z2, z3, z4): return (-m2*l1*z3**2*sin(z1-z3)*cos(z1-z2)+g*m2*sin(z2)*cos(z1-z2)-m2*l2*z4**2*sin(z1-z2)-(m1+m2)*g*sin(z1))/(l1*(m1+m2)-m2*l1*(cos(z1-z2))**2)
def f4(t, z1, z2, z3, z4): return (m2*l2*z4**2*sin(z1-z2)*cos(z1-z2)+g*sin(z1)*cos(z1-z2)*(m1+m2)+l1*z3**2*sin(z1-z2)*(m1+m2)-g*sin(z2)*(m1+m2))/(l2*(m1+m2)-m2*l2*(cos(z1-z2))**2)

##z1_initial=3*pi/4.
##z2_initial=pi/2.
z1_initial=pi/2.
z2_initial=2*pi
z3_initial=0.2
z4_initial=0.022
t_initial=0
t_final=11
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
theta1=R[1]
theta2=R[2]
theta1_dashed=R[3]
theta2_dashed=R[4]
time=R[0]

X1=[l1*sin(i) for i in theta1]
Y1=[-l1*cos(i) for i in theta1]
X2=[l1*sin(theta1[i])+l2*sin(theta2[i]) for i in range(len(theta1))]
Y2=[-l1*cos(theta1[i])-l2*cos(theta2[i]) for i in range(len(theta1))]

##pylab.plot(time, theta1, '-')
##pylab.plot(time, theta2, 'r-')
##pylab.plot(time, theta1_dashed, 'k-')
##pylab.plot(time, theta2_dashed, 'g-')

##pylab.plot(X1, Y1, 'k-')
##pylab.plot(X2, Y2, 'r-')
##pylab.show()

import pygame, random, sys
from pygame.locals import *
DISPLAYSURF=pygame.display.set_mode((800, 800))
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
        
        if i==len(theta1):
                pygame.image.save(DISPLAYSURF, 'DoublePendulum.png')
                pygame.quit()
                sys.exit()
        
        DISPLAYSURF.fill(WHITE)

        X1+=[l1*sin(theta1[i]), ]
        Y1+=[-l1*cos(theta1[i]), ]
        X2+=[l1*sin(theta1[i])+l2*sin(theta2[i]), ]
        Y2+=[-l1*cos(theta1[i])-l2*cos(theta2[i]), ]

        pygame.draw.circle(DISPLAYSURF, WHITE, (int(400 + 0), 200 - int(0)), 2, 0)
        pygame.draw.circle(DISPLAYSURF, BLUE, (int(400 + X1[i]*40), 200 - int(Y1[i]*40)), 7, 0)
        pygame.draw.line(DISPLAYSURF, BLACK, (int(400 + 0), 200 - int(0)), (int(400 + X1[i]*40), 200 - int(Y1[i]*40)), 2)
        pygame.draw.circle(DISPLAYSURF, RED, (int(400 + X2[i]*40), 200 - int(Y2[i]*40)), 7, 0)
        pygame.draw.line(DISPLAYSURF, BLACK, (int(400 + X1[i]*40), 200 - int(Y1[i]*40)), (int(400 + X2[i]*40), 200 - int(Y2[i]*40)), 2)
        

        i+=1
        pygame.display.update()
