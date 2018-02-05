#Author: Indranil Ghosh, Physics Department, Jadavpur University

# Symbolic Gram-Schmidt Orthogonalisation

from sympy import Symbol, integrate, conjugate, sqrt
x=Symbol('x')
def inner(f1, f2, w, a, b):
    """ f1 and f2 are linearly independent functions that are orthonormal
    and w is the weight. This calculates <f1(x)|f2(x)>, with a and b the
    limits"""
    f=conjugate(f1)*f2*w
    return integrate(f, (x, a, b))

def ortho(p, w, a, b): return p/sqrt(inner(p, p, w, a, b))

def y(n): return x**n

def Gram_Schmidt(n, w, a, b):
    Y=[y(0)]+[0]*(n-1)
    psi=[Y[0]]+[0]*(n-1)
    phi=[ortho(psi[0], w, a, b)]+[0]*(n-1)
    for i in range(1, n):
        Y[i]=y(i)
        psi[i]=Y[i]-sum([phi[j]*inner(phi[j], Y[i], w, a, b) for j in range(i-1, 0, -1)])
        print(psi)
        phi[i]=ortho(psi[i], w, a, b)
        print(phi)
    return (phi)