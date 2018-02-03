##Author: Indranil Ghosh, Jadavpur University, Physics Department

## Bairstow's root finding method

import numpy as np
import cmath as cm

def GJ(A, b):
      Aug=np.concatenate((A, b), axis=1)
      row=len(A)
      col=len(A[0])
      for i in range(col-1):
              m=Aug[i, i]
              k=i
              for R in range(i, row):
                  if Aug[R, i]>m:
                          m = Aug[R, i]
                          k = R
              t=np.copy(Aug[i,])
              Aug[i,]=Aug[k,]
              Aug[k,]=t
              for j in range(i+1,row):
                      s=Aug[j,i]/Aug[i, i]
                      Aug[j,]-=Aug[i,]*s
      for i in range(row): Aug[i,]/=Aug[i, i]
      d=1
      for r in range(row-2,-1,-1):
              for k in range(r, -1, -1): Aug[k,]=Aug[k,]-Aug[k, k+d]*Aug[k+d]
              d+=1
      return(Aug.T[row:].T)

def Bairstow(Pol, r, s, epsilon, Max_steps):
        """Pol is a list of coefficients of a given Polynomial in float"""
        R=r
        S=s
        n=len(Pol)
        N=n-1
        p=1
        while True:
            b=[0]*n
            c=[0]*n
            b[N]=Pol[N]
            b[N-1]=Pol[N-1]+r*b[N]
            for i in range(N-2, -1, -1):b[i]=Pol[i]+r*b[i+1]+s*b[i+2]
##            print("b=",b)
            
            c[N]=b[N]
            c[N-1]=b[N-1]+r*c[N]
            for i in range(N-2, -1, -1):c[i]=b[i]+r*c[i+1]+s*c[i+2]
##            print("c=",c)
            
##            A=np.array(([c[2], c[3]], [c[1], c[2]]))
##            x=np.array(([-b[1]], [-b[0]]))
##            rs=GJ(A, x) # Using the Gauss-Jordan algorithm
##            print("rs=",rs)
            
##            del_r, del_s=rs.item(0), rs.item(1)
            del_s=(c[1]*b[1]-c[2]*b[0])/(c[2]**2-c[1]*c[3])
            del_r=-(b[1]+c[3]*del_s)/c[2]
            r+=del_r
            s+=del_s
##            print("r=",r)
##            print("s=",s)

            
            eps_r=abs(del_r/r)*100
            eps_s=abs(del_s/s)*100
##            print("eps_r=",eps_r)
##            print("eps_s=",eps_s)
            b1=b[:]
            if (eps_r<epsilon and eps_s<epsilon): break
            
            p+=1
##            print(p)
            
        X, Y=(r+cm.sqrt(r**2+4*s))/2., (r-cm.sqrt(r**2+4*s))/2.
        if len(b1)==5:
                A=b1[4]
                B=b1[3]
                C=b1[2]
                return [X, Y]+[(-B+cm.sqrt(B**2-4*A*C))/2, (-B-cm.sqrt(B**2-4*A*C))/2]
        elif len(b1)==4:
                A=b1[3]
                B=b1[2]                
                return [X, Y]+[-B/A]
        elif len(b1)>5: return [X, Y]+Bairstow(b1[2:], r, s, epsilon, Max_steps)
        
##print(Bairstow([4, -10, 10, -5, 1] , 0.5, -0.5, 0.01, 15))
##print(Bairstow([-1., 0., 0., -1., -1., 0., 1.] , 0.1, 0.1, 0.01, 20))
#print(Bairstow([1., -1., 0., 1.] , 0.1, 0.1, 0.01, 20))
print(Bairstow([6., 11., -33., -33., 11., 6.], 0.1, 0.1, 0.01, 20))