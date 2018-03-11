## Author: Indranil Ghosh, Jadavpur University, Physics Department
## Insect Outbreak Model, from Non-Linear Dynamics and Chaos by Steven Strogartz 


import pylab
import numpy as np

N_initial=250 # initial budworm population to start with
R=10. # Growth rate
K=100.0 # Carrying capacity
B=.3
A=.3
t_initial=0
t_final=100
h=0.01

def f(t, N): return R*N*(1-N/K)-B*N**2/(A**2+N**2)

def Runge(N_initial, t_initial, h, t_final): 
        time=list(np.arange(t_initial, t_final+h, h))
        n=[N_initial]
        
        for i in range(1, len(time)):
                p=time[i-1]
                q=n[i-1]
                k1=h*f(p, q)
                k2=h*f(p+h/2., q+k1/2.)
                k3=h*f(p+h/2., q+k2/2.)
                k4=h*f(p+h, q+k3)
                n+=[q+(k1+2*k2+2*k3+k4), ]
        n_dashed=[R*i*(1-i/K)-B*i**2/(A**2+i**2) for i in n]
        pylab.plot(time, n)
##        pylab.plot(n, n_dashed)
        pylab.show()

Runge(N_initial, t_initial, h, t_final)
        return(P)
                                                       
print(KMP(S1, S2))               

