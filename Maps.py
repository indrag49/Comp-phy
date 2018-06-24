
import pylab
import math
import numpy as np

def Henon(a, b, x_initial, y_initial, iterations):
    
    X=[x_initial]
    Y=[y_initial]
##    X=[1.]
##    Y=[1.]
##    a=1.4
##    b=0.3

    for n in range(1, iterations+1):
        X+=[1-a*X[n-1]**2+Y[n-1], ]
        Y+=[b*X[n-1], ]

    pylab.plot(X, Y, 'ro', ms=1)
    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.show()

def Henon2(a, b, x_initial, y_initial, iterations):
    
    X=[x_initial]
    Y=[y_initial]
##    X=[1.]
##    Y=[1.]
##    a=1.4
##    b=0.3

    for n in range(1, iterations+1):
        X+=[1-a*X[n-1]**2+Y[n-1], ]
        Y+=[b*X[n-1], ]

    return X

##Henon(1.4, 0.3, 1., 1., 10001)

def bifurcation_henon(A, x_initial, y_initial, iterations):
    for a in A:
        X=Henon2(a, 0.3, x_initial, y_initial, iterations)[100:]
        pylab.plot([a]*len(X), X, 'mo', ms=2)
    pylab.xlabel('a')
    pylab.ylabel('X')
    pylab.xlim(1, 1.5)
    pylab.ylim(-0.5, 0.5)
    pylab.title('Bifurcation diagram fro Henon map')
##    pylab.show()

A1=list(np.linspace(1., 1.5, 300))
##bifurcation_henon(A1, 1., 1., 1000)

def Lozi(a, b, x_initial, y_initial, iterations):
    
    X=[x_initial]
    Y=[y_initial]
##    X=[1.]
##    Y=[1.]
##    a=1.4
##    b=0.3

    for n in range(1, iterations+1):
        X+=[1-a*abs(X[n-1])+Y[n-1], ]
        Y+=[b*X[n-1], ]

    pylab.plot(X, Y, 'ro', ms=1)
    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.show()
    
##Lozi(1.4, 0.3, 1., 1., 10001)

def Lozi2(a, b, x_initial, y_initial, iterations):
    
    X=[x_initial]
    Y=[y_initial]
##    X=[1.]
##    Y=[1.]
##    a=1.4
##    b=0.3

    for n in range(1, iterations+1):
        X+=[1-a*abs(X[n-1])+Y[n-1], ]
        Y+=[b*X[n-1], ]

    return X

def bifurcation_Lozi(A, x_initial, y_initial, iterations):
    for a in A:
        X=Lozi2(a, 0.3, x_initial, y_initial, iterations)[100:]
        pylab.plot([a]*len(X), X, 'yo', ms=2)
    pylab.xlabel('a')
    pylab.ylabel('X')
    pylab.xlim(1, 1.5)
    pylab.ylim(-0.5, 0.5)
    pylab.title('Bifurcation diagram for Lozi map')
##    pylab.show()

A2=list(np.linspace(1., 1.5, 300))
##bifurcation_Lozi(A2, 1., 1., 500)

def Mira(a, b, x_initial, y_initial, iterations):

    def F(x): return a*x+2*(1-a)*x**2/(1+x**2)

    X=[x_initial]
    Y=[y_initial]

    for n in range(1, iterations+1):
        X+=[b*Y[n-1]+F(X[n-1]), ]
        Y+=[-X[n-1]+F(X[n]), ]

    pylab.plot(X, Y, 'ro', ms=1)
    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.show()

##Mira(0.2, 1.0, 12., 0., 50001)
##Mira(0.31, 1.0, 12., 0., 50001)
##Mira(0.4, 1.0, 12., 0., 50001)
##Mira(0.7, 0.9998, 9., 0., 100001)
##Mira(0.7, 0.9998, 12.1, 0., 50001)
##Mira(0.7, 0.9998, 15., 0., 200001)

def Mira2(a, b, x_initial, y_initial, iterations):

    X=[x_initial]
    Y=[y_initial]

    for n in range(1, iterations+1):
        X+=[Y[n-1]+a*(1-0.05*Y[n-1]**2)*Y[n-1]+b*X[n-1]+2*(1-b)*X[n-1]**2/(1+X[n-1]**2), ]
        Y+=[-X[n-1]+b*X[n]+2*(1-b)*X[n]**2/(1+X[n]**2), ]

    pylab.plot(X, Y, 'o', ms=1)
    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.show()

##Mira2(0.009, math.cos(4*math.pi/5)+0.008, 0.5, 0.5, 200000)
##Mira2(0.008, -0.496, 0.5, 0.5, 200000)
##Mira2(0.008, -0.486, 0.5, 0.5, 200000)
    
def tinkerbell(a, b, c, d, x_initial, y_initial, iterations):
    X=[x_initial]
    Y=[y_initial]

    for n in range(1, iterations+1):
        X+=[X[n-1]**2-Y[n-1]**2+a*X[n-1]+b*Y[n-1], ]
        Y+=[2*X[n-1]*Y[n-1]+c*X[n-1]+d*Y[n-1], ]

    pylab.plot(X, Y, 'yo', ms=1)
    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.show()

##tinkerbell(0.9, -0.6013, 2., 0.5, -0.72, -0.64, 200000)
##tinkerbell(0.3, 0.6, 2., 0.27, -0.5, -0.64, 200000)

def logistic(r, x_initial, iterations):
    
    X=[x_initial]
    for n in range(1, iterations+1):
        X+=[r*X[n-1]*(1-X[n-1]), ]

    pylab.plot(range(iterations+1), X)
    pylab.xlabel('X')
    pylab.ylabel('t')
    pylab.show()
##logistic(3.78, 0.1, 63)

import numpy as np
def logistic2(r, x_initial, iterations):
    
    X=[x_initial]
    for n in range(1, iterations+1):
        X+=[r*X[n-1]*(1-X[n-1]), ]

    return X

def bifurcation_logistic(R, x_initial, iterations):
    for r in R:
        X=logistic2(r, x_initial, iterations)[100:]
        pylab.plot([r]*len(X), X, 'ro', ms=2)
    pylab.xlabel('r')
    pylab.ylabel('X')
    pylab.title('Bifurcation diagram for Logistic map')
##    pylab.show()

R=np.linspace(0, 4, 300)
##bifurcation_logistic(R, 0.1, 1000)

pylab.subplot(3, 1, 1)
bifurcation_henon(A1, 1., 1., 1000)

pylab.subplot(3, 1, 2)
bifurcation_Lozi(A2, 1., 1., 500)

pylab.subplot(3, 1, 3)
bifurcation_logistic(R, 0.1, 1000)

pylab.show()