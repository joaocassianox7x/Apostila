from scipy.integrate import solve_ivp as ivp
import matplotlib.pyplot as plt
import numpy as np
#constantes
t0=0
tf=10
y0=5 #ci para funcao
y0dot=0.1 #condicao inicial para a derivada
w=2

#definir o sistema
def edo(t,y):
    return(y[1],-y[1]-(w**2)*np.sin(t))

solucao=ivp(edo,(t0,tf),[y0,y0dot])

solucao2=ivp(edo,(t0,tf),[y0,y0dot],t_eval=np.linspace(t0,tf,2**10))


plt.plot(solucao.t,solucao.y[0],'r') #y1
plt.plot(solucao.t,solucao.y[1],'b') #y1dot

plt.plot(solucao2.t,10+solucao2.y[0],'y') #y1
plt.plot(solucao2.t,10+solucao2.y[1],'g') #y1dot




plt.legend(["y1(x)","y'1(x)","y2(x)","y'2(x)"],loc='upper right')

plt.savefig("plotsemdense.png")