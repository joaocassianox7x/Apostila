import numpy as np
import numpy.linalg as alg 
import matplotlib.pyplot as plt


#PRIMEIRO

n=10**2 #ordem da matriz
M=2*np.eye(n)-np.eye(n,k=-1)-np.eye(n,k=+1)

val,vec=alg.eigh(M)

plt.plot(np.abs(vec[:,0:3])**2)

plt.savefig("autovec.png")