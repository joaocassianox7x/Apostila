
from scipy.integrate import solve_ivp as ivp
import matplotlib.pyplot as plt
import numpy as np

#constante
y0=10 #ci
y0dot=0
t0=0
tf=50

A=7
B=9
amp=15 #vamos usar f(t) = amp*cos(t)

def edo(t,y):
    return(y[1],-A*y[1]-B*y[0]+amp*np.cos(t))
    
solucao=ivp(edo,(t0,tf),[y0,y0dot],t_eval=np.arange(t0,tf,10**-4))

plt.plot(solucao.t,solucao.y[0],"r")
plt.plot(solucao.t,solucao.y[1],"b--")

plt.grid(True)
plt.legend(["y(x)","y'(x)"],loc="upper right")
plt.xlabel("t (s)")
plt.savefig("terceiro.png")
plt.show()