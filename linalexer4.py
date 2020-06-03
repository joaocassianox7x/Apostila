import numpy.linalg as alg 
import numpy as np
#PRIMEIRO

n=10**2 #ordem da matriz
M=2*np.eye(n)-np.eye(n,k=-1)-np.eye(n,k=+1)

INV=alg.inv(M)
DET=alg.det(M)