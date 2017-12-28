#Author: Indranil Ghosh, Jadavpur University, Physics Department

#Gauss Jacobi algorithm for solving a set of linear equations

import numpy as np
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

## Applying Gauss-Jacobi iteration scheme
def GJ(A, X, epsilon):
        assert len(A)==len(X)
        """ X is an array of initial values """
        A=decompose(A)
        r=len(A)
        b=A.T[r:].T
        A=A.T[:r].T
        X_new=np.zeros(r)
        c=0
        while c<=100:
                for i in range(r):
                        a=np.copy(A[i,])
                        a[i]=0
                        X_new[i]=(b[i]-sum(a*X))/A[i,i]
                if ((abs(X_new-X)<=epsilon)==0).sum()==0: return (X_new)
                X=X_new
                c+=1
        return("Maximum iteration reached!!")

##A=np.array(([4., 1., 1., 2.], [1., 5., 2., -6.], [1., 2., 3., -4.]))
##X=np.array([0.5, -0.5, -0.5])

A=np.array(([26., 2., 2., 12.6], [2., 3., 17.,6.0], [3., 27., 1., -14.3]))
X=np.zeros(3)

##A=np.array(([1., 20., 1., -18.], [25., 1., -5., 19.], [3., 4., 8., 7.]))
##X=np.zeros(3)
print(GJ(A, X, 0.0001))