import math

y=[] #lista vazia para os valores da funcao
ydot=[] #lista vazia para as derivadas

y0=10
y.append(y0) #adicionando o ponto inicial 

n=10**5 #numero de pontos
pi=0 #ponto inicial
pf=15 #ponto final
delta=(pf-pi)/n

def edo(x):
    return(x)

for i in range(n):
    y.append(y[i]+delta*edo(y[i]))
    
import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(pi,pf,n+1)
plt.plot(t,y,'r',lw=5)
plt.plot(t,y0*np.exp(t),'b--')
plt.ylabel("y(t)")
plt.xlabel("t")


plt.legend(["Solução Numérica","Solucao Analítica"],loc="upper left")
plt.grid(True)
plt.savefig("numericanaleuler.png")