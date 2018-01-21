#Author: Indranil Ghosh, Physics Department, Jadavpur University

# Finds the inverse modulo using Secant method

from sympy import fibonacci
def inverse_secant(p, a, n, x0, x1):
        l=[fibonacci(i) for i in range(3, 20)]
        j=0
        i=l[j]
        while i<n:
                s=(a*(x1*x0))%(p**i)
                x=x1+x0
                x0=x1
                x1=x
                x1-=s
                j+=1
                i=l[j]
        s=(a*(x1*x0))%(p**n)
        x=x1+x0
        x0=x1
        x1=x
        x1-=s
        return (x1%(p**n))   
print(inverse_secant(2., 3., 16, 1, 1))