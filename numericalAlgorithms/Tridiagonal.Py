##Author: Indranil Ghosh, Jadavpur University, Physics Department

## Tridiagonal method

import numpy as np

##A=np.array(([9., 1., 0], [4., -7., 2.], [0., 3., 8.]))
##d=np.array(([5.], [6.], [2.]))

A=np.array(([6., 0, 0, 0, 0, 0, 0], [1., 4., 1., 0.,0.,0.,0.], [0., 1., 4., 1., 0., 0.,0.], [0., 0., 1., 4., 1., 0., 0.], [0., 0., 0., 1., 4., 1., 0.], [0., 0., 0., 0., 1., 4., 1.], [0., 0., 0., 0., 0., 0., 6.]))
d=np.array(([0.], [1.], [2.], [-6.], [2.], [1.], [0.]))

#check whether the augmented matrix is diagonally dominant
def check(A):
        r=len(A)
        c=len(A[0])
        A=A.T[:r].T
        for i in range(r):
                if abs(A[i, i])<sum(abs(A[i,]))-abs(A[i,i]): return 0
        return 1

## Making a matrix diagonally dominant
def decompose(A):
        r=len(A)
        c=len(A[0])
        if check(A)==1: return(A)
        for i in range(r):
                m=abs(A[i,i])
                k=i
                for j in range(c-1):
                        if abs(A[i, j])>m:
                                m=abs(A[i, j])
                                k=j
                t=np.copy(A[k,])
                A[k,]=A[i,]
                A[i,]=t
        return(decompose(A))

def TD(A, d):
        A=decompose(A)
        n=len(A)
        a=np.array([])
        b=np.array([])
        c=np.array([])
        for i in range(1, n-1):
                b=np.append(b, A[i, i])
                a=np.append(a, A[i, i-1])
                c=np.append(c, A[i, i+1])
        a=np.append(0, a)
        a=np.append(a, A[n-1, n-2])
        b=np.append(A[0,0], b)
        b=np.append(b, A[n-1, n-1])
        c=np.append(A[0, 1], c)
        c=np.append(c, 0)
        C=np.array([0.]*n)
        D=np.array([0.]*n)
        X=np.array([0.]*n)
        C[0]=c[0]/b[0]
        D[0]=d[0]/b[0]
        for i in range(1,n):
                C[i]=c[i]/(b[i]-a[i]*C[i-1])
                D[i]=(d[i]-a[i]*D[i-1])/(b[i]-a[i]*C[i-1])
        X[n-1]=D[n-1]
        for l in range(n-2, -1, -1):X[l]=D[l]-C[l]*X[l+1]
        return (X)
                
print(TD(A, d))