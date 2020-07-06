#PRIMEIRO
import numpy as np
import time
import matplotlib.pyplot as plt

n=10**2 #ordem da matriz
#Do jeito mais tradicional

tp,tn=[],[]


execu=range(10,n,int(n/25))

for beta in execu:    
    tp0=time.time()
    M=np.zeros((beta,beta))
    for i in range(beta):
        for j in range(beta):
            if i==j:
                M[i,j]=2
                if i>0:
                    M[i-1,i]=-1
                if i!=(beta-1):
                    M[i,i+1]=-1
    tp.append(time.time()-tp0)
    
    
    #Vetorialmente
    tn0=time.time()
    M=2*np.eye(beta)-np.eye(beta,k=-1)-np.eye(beta,k=+1)
    tn.append(time.time()-tn0)
    

#plt.subplot(211)
plt.plot(execu,tp,'r')
plt.plot(execu,tn,'b')


plt.legend(["Python","NumPy"],loc='upper left')
plt.ylabel("Tempo Gasto (s)")
plt.xlabel("Ordem da Matriz")
plt.grid(True)

#plt.savefig("linalg.png")

