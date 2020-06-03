#CODIGO PARA FFT EM PYTHON

import math

pi=math.pi
e=math.e

def func(x): #funcao a qual desejamos a transformada
    return(math.e**x)

N=2**11+1 #numero de pontos
x0=0 #ponto inicial
xf=100 #ponto final
L=xf-x0 #comprimento

dx=L/N
x=[L*i/N-x0 for i in range(N)] #vai de 0 ate 10, com intervalo L/n 

k=[2*pi*i/L for i in x]
dk=k[1]-k[0]
k=k[:-1] #retiramos o ultimo ponto devido as condicoes de
    #periodicidade, repare que ele e importante para o dk, 
    #mas deve ser retirado para o calculo da transformada
    
#agora faremos a transformada
F=[]

for n in range(len(k)):
    #print(n)
    cte=e**(-1j*k[n]*x[0])*(1/(N**0.5)) #termo constante
    Fn=0
    for j in range(N-1):
        Fn+=func(x[j])*e**(-2*1j*pi*j*n*(1/N))
    Fn*=cte
    F.append(Fn)
    
    
import numpy as np
import matplotlib.pyplot as plt


plt.plot(k,np.real(F))
plt.plot(k,np.imag(F))
plt.plot(k,(np.abs(F))**2)
plt.grid(True)
plt.legend(["Parte Real","Parte Imaginária"," Módulo Quadrado"],loc="upper center")
plt.xlim(k[0],k[-1])
plt.xlabel("K")
plt.savefig("fftimplementacaopropria.png")