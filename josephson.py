## Program by: Indranil Ghosh, Jadavpur University, Physics Department

## Dynamics of superconducting Josephson Junstions, Strogatz: Non-linear Dynamics and Chaos

import pylab
import numpy as np
import math as m

Ic=10**-6
R=1.0
hbar=1.0545718*10**(-34)
e=1.6*10**(-19)
C=1.
A=hbar*C/(2*e)
B=hbar/(2*e*R)
a=A/Ic
b=B/Ic

x1_initial=0
x2_initial=1.

t_initial=0
t_final=100
h=0.01



def Runge(x1_initial, x2_initial, t_initial, h, t_final): 
        time=list(np.arange(t_initial, t_final+h, h))
        I_=list(np.linspace(0, 3, len(time)))
        x1=[x1_initial]
        x2=[x2_initial]
        v=[0]
        
        for i in range(1, len(time)):
                def f1(t, x1, x2): return x2
                def f2(t, x1, x2): return (I_[i]-b*x2-m.sin(x1))/a
                
                p=time[i-1]
                q=x1[i-1]
                r=x2[i-1]

                k11=h*f1(p, q, r)
                k21=h*f2(p, q, r)

                k12=h*f1(p+h/2., q+k11/2., r+k21/2.)
                k22=h*f2(p+h/2., q+k11/2., r+k21/2.)
                
                k13=h*f1(p+h/2., q+k12/2., r+k22/2.)
                k23=h*f2(p+h/2., q+k12/2., r+k22/2.)
                
                k14=h*f1(p+h, q+k13, r+k23)
                k24=h*f2(p+h, q+k13, r+k23)

                x1+=[x1[i-1]+(k11+2*k12+2*k13+k14)/6., ]
                x2+=[x2[i-1]+(k21+2*k22+2*k23+k24)/6., ]

                v+=[0 if I_[i]<=1 else hbar*x2[i]/(2*e*Ic*R), ]
                
        pylab.plot(I_, v, 'k-')
        pylab.ylim(-1, 4)
        pylab.ylabel('V/RIc')
        pylab.xlabel('I/Ic')
        pylab.show()

Runge(x1_initial, x2_initial, t_initial, h, t_final)
