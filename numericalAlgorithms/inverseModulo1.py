#Author: Indranil Ghosh, Physics Department, Jadavpur University

# Finds the inverse modulo using Newton's method
def inverse_newton(p, a, n, x_ini):
        x=x_ini
        i=2
        while i<n:
                s=(a*(x**2))%(p**i)
                x*=2
                x-=s
                i*=2              
        s=(a*(x**2))%(p**n)
        x*=2
        x-=s
        return (x%(p**n))
print(inverse_newton(7., 5., 8, 3))