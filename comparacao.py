import numpy as np
import matplotlib.pyplot as plt
import random as random_python
import time


j=10**5

tp=[]
tn=[]

K=range(10**4,j,100)
for n in K:
    #Python convencional
    
    tp0=time.time()
    x=[random_python.random() for i in range(n)]
    y=[(1-i**2)**0.5 for i in x]
    media=sum(y)/len(y) #somo elementos de y
                    #depois divido pelo numeoro de elementos
    tp.append(time.time()-tp0)
    
    #NumPy
    
    tn0=time.time()
    x=np.random.random(100)
    y=np.sqrt(1-x**2)
    media=np.sum(y)/len(y)
    tn.append(time.time()-tn0)

#plt.subplot(221)
#plt.plot(range(100,j,100),tp)


#plt.subplot(222)
#plt.plot(range(100,j,100),tn)

#plt.subplot(212)
tp=np.array(tp)
tn=np.array(tn)

plt.plot(K,tp,'r')
plt.plot(K,tn,'b')


plt.ylabel("Tempo Gasto (s)")
plt.xlabel("N")
plt.xlim(min(K),max(K))
plt.legend(['Python','NumPy'],loc="upper left")
plt.savefig("comparacao.png")