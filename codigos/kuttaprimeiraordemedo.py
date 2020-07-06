y0=5 #valor inicial

t0=0 #ponto inicial
tf=10 #ponto final

n=10**5 #numero de pontos
dt=(tf-t0)/n

y=[]
y.append(y0)

def func(a,b): #a=y e b=t
    return(-a+b)

for i in range(n):
    t=i*dt #t
    #print(t)
    k1=func(y[i],t)
    k2=func(y[i]+k1*dt/2,t)
    k3=func(y[i]+k2*dt/2,t+dt/2)
    k4=func(y[i]+k3*dt,t+dt)
    y.append(y[i]+(dt/6)*(k1+k4+2*(k2+k3)))
    
    
    
    
import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(t0,tf,n+1)


plt.plot(t,t-1+3.5*np.exp(-t),'r')
plt.plot(t,y,'b')


plt.legend(["Solução Analítica","Solução por RK4"],loc="upper left")
plt.grid(True)
plt.xlim(t0,tf)
plt.xlabel("t (s)")

plt.savefig("rk4primeiraordem.png")