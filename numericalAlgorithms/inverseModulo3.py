# Author: Indranil Ghosh, Physics Department, Jadavpur University

# Finds the inverse modulo using Fixed Point method

def inverse_fixedpoint(p, a, n, x_ini):
        x=x_ini
        j=1
        i=3
        while i<n:
                s=((1-a*x)*(2-a*x))%(p**i)
                x+=x*s
                j+=1
                i=3**j
        s=((1-a*x)*(2-a*x))%(p**n)
        x+=x*s
        return x%(p**n)
print(inverse_fixedpoint(5., 3., 8, 2))