import random #pacote de numeros aleatorio do python
import math #pacote com constantes importantes
import numpy as np
pi=math.pi
res=pi/4 #resultado analitico

def func(x):
    return(math.sqrt(1-x**2))
n=10**4 #convergência pequena
media=0




er=[]
intervalo=range(10,n,int(n/1000))
for j in intervalo:
    
    media=0
    for i in range(j): #random.random() retorna um número 
                       #aleatório entre 0 e 1
        media+=func(random.random())
    Integral=media*1/j #produto entre a media e o intervalo
    
    
    '''
    integral=np.sum((1*((np.random.random(j)**2+np.random.random(j)**2)<=1)))/j
    '''
    erro=((res-Integral)**2)**0.5
    er.append(erro)
    
    
    
    

import matplotlib.pyplot as plt
plt.plot(intervalo,er)
plt.ylabel("Erro (n)")
plt.xlabel("n")
plt.grid(True)
plt.savefig("montecarlofigconvergencia.png")