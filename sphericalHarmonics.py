##Author: Indranil Ghosh, Jadavpur University, Physics Department

## Calculation of the Spherical Harmonics

from sympy.core.cache import cacheit
from sympy import *
import pylab
import numpy as np

x=Symbol('x')
@cacheit
def P(l, m, x): return simplify((-1)**m*factorial2(2*m - 1)*sqrt((1 - x**2)**m) if l==m else x*(2*m + 1)*P(m, m, x) if l - m == 1 else (x*(2*l - 1)*P(l - 1, m, x) - (l + m - 1)*P(l - 2, m, x))/(l - m))

def Y(l, m, theta, phi): return sqrt((2*l + 1)*factorial(l - m)/(4*pi*factorial(l + m)))*P(l, m, cos(theta))*exp(I*m*phi)
def real_Y(l, m, theta, phi): return re(Y(l, m, theta, phi))

def plot_P(l, m):
    X=[]
    p=[]
    for x in np.linspace(-1, 1, 100):
        X+=[x, ]
        p+=[P(l, m, x), ] 
    pylab.plot(X, p, 'r-')
    pylab.xlabel("x -->")
    pylab.ylabel("P(l, m, x) -->")
    pylab.show()


def Plot_Y(l):
    T=[]
    H=[]
    phi=0
    for theta in np.linspace(0, float(pi), 100):
        T+=[theta, ]
        H+=[real_Y(l, l, theta, phi), ]
    pylab.plot(T, H, 'r-')
    pylab.xlabel("Theta-->")
    pylab.ylabel("Spherical harmonics -->")
    pylab.ylim(-0.6, 0.6)

for l in range(11): Plot_Y(l)
pylab.title("Spherical Harmonics with increasing values of L")
pylab.show()

