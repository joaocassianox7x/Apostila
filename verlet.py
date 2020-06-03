
y0=1 #condicoes iniciais
y0dot=0

y=[y0]

tf=10
ti=0
n=5*10**1
dt=(tf-ti)/n

def func(a): #y''
    return(-a)
    
y.append(y0+dt*y0dot) #primeiro passo por euler

for i in range(1,n):
    y.append(-y[i-1]+2*y[i]+(dt**2)*func(y[i]))
    


import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(ti,tf,n+1)
plt.plot(t,y,'r')
plt.plot(t,np.cos(t))

plt.legend(["Solução por Verlet","Solução Analítica"],loc="upper left")
plt.grid(True)
plt.xlim(ti,tf)
plt.xlabel("t (s)")

plt.savefig("verlet.png")