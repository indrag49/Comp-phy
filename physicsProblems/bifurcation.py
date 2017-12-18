##Author: Indranil Ghosh, Jadavpur University, Physics Department

import pylab
def bifurcation(x_, r_):
        """putting the initial value of x_ as 0.0 plots a straight line parallel to x-axis. So put x>=0.1, for example set x_=0.l and r_=2.4"""
        x=[x_]
        r=[r_]
        dr=0.00001
        for i in range(1, 160001):
                x+=[r[i - 1]*x[i - 1]*(1 - x[i - 1]), ]
                r+=[r[i - 1] + dr, ]
        pylab.title("Bifurcation diagram of logistics map")
        pylab.xlabel("r -->")
        pylab.ylabel("Xn -->")
        pylab.xlim(2.3, 4)
        pylab.plot(r, x, 'ko', ms=1)
        pylab.show()
        
bifurcation(0.1, 2.4)

