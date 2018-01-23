##Author: Indranil Ghosh, Jadavpur University, Physics Department

## LU decomposition 

import numpy as np
import pandas as pd
def LU(A):
        row=len(A)
        col=len(A[0])
        L=np.identity(row)
        for i in range(col-1):
                m=A[i, i]
                k=i
                for R in range(i, row):
                        if A[R, i]>m:
                                m=A[R, i]
                                K=R
                t=np.copy(A[i, ])
                A[i,]=A[k,]
                A[k,]=t
                for j in range(i+1, row):
                        s=A[j, i]/A[i,i]
                        A[j,]-=A[i,]*s
                        L[j,i]=s
        U=np.copy(A)
        return {'L':L, 'U':U}
A=np.array(([2., 4., 3.], [1., -2., -2.], [-3., 3., 2.]))
print(LU(A))