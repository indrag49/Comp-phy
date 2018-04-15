import math as M
import pylab
def dft(fr, fi):
        n=len(fr)
        gr=[0]*n
        gi=[0]*n
        x=2*M.pi/n
        for i in range(n):
                for j in range(n):
                        q=x*j*i
                        gr[i]+=fr[j]*M.cos(q)+fi[j]*M.sin(q)
                        gi[i]+=fi[j]*M.cos(q)-fr[j]*M.sin(q)
        return [gr, gi]
#We perform the DFT of f(x)=x*(1-x)

n=128
m=8
x=[0]*n
fr=[0]*n
fi=[0]*n
h=10./(n-1)
f0=1/M.sqrt(n)

for i in range(n):
        x[i]=h*i
        fr[i]=M.sin(x[i])
        fi[i]=0
L=(dft(fr, fi))
gr=L[0]
gi=L[1]
pylab.plot(x, fr, 'k-')
pylab.plot(x, gr, 'r-')
pylab.show()

#Inverse fourier transform

for i in range(n):
        gr[i]=f0*gr[i]
        gi[i]=-f0*gi[i]
        fr[i]=0
        fi[i]=0
L=(dft(gr, gi))
fr=L[0]
fi=L[1]
pylab.plot(x, fr, 'k-')
pylab.plot(x, gr, 'r-')
pylab.show()