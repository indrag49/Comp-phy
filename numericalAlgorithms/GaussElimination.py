#Author: Indranil Ghosh, Jadavpur University, Physics Department

#Gauss Elimination algorithm

import numpy as np     
##A = np.array(([1., 10., -1.], [2., 3., 20.], [10., -1., 2.]))
##b = np.array(([3.], [7.], [4.]))

##A=np.array(([2., 1., 1., -2.], [4., 0, 2., 1.], [3., 2., 2., 0], [1., 3., 2., -1.]))
##b=np.array(([-10.], [8.], [7.], [-5.]))

##A=np.array(([3.15, -1.96, 3.85], [2.13, 5.12, -2.89], [5.92, 3.05, 2.15]))
##b=np.array(([12.95], [-8.61], [6.88]))

A=np.array(([2.,2., 1.], [4., 3., 3.], [1., 1., 1.]))
b=np.array(([1.], [2.], [3.]))
def GE(A, b):
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
      print(Aug)
      x=np.zeros(row)
      for i in range(row-1, -1, -1): x[i]=(Aug[i,row]-sum([Aug[i, j]*x[j] for j in range(i+1, row)]))/Aug[i, i]
      return(x[::-1])
print(GE(A, b))  
