from scipy.integrate import solve_ivp as ivp
import matplotlib.pyplot as plt
import numpy as np

#constante
y0=10 #ci
t0=0
tf=10

def edo(t,y):
    return(np.cos(t)*y)
    
solucao=ivp(edo,(t0,tf),[y0],t_eval=np.arange(t0,tf,10**-3))

plt.plot(solucao.t,solucao.y[0],"r")
plt.grid(True)
plt.legend(["y(x)"],loc="upper right")
plt.xlim(t0,tf)
plt.title("Solução")

plt.ylabel("y(t) (m)")
plt.xlabel("t (s)")
plt.savefig("segundoivp.png")