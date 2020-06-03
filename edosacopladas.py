from scipy.integrate import solve_ivp as ivp
import matplotlib.pyplot as plt
import numpy as np

sigma=10 #constante 
beta=8/3 #constante
ro=28 #constante

ti=0 #tempo inicial 
tf=50 #tempo final

tempo=[ti,tf] #vetor de tempo ro ivp
intervalo=np.arange(0,50,0.05) #tempo desejado
cis=[0.1,0.1,0.1] #vetor de condicoes iniciais


def edo(t, v): 
    return [sigma*(v[1]-v[0]), ro*v[0]-v[1]-v[0]*v[2],
            -beta*v[2]+v[1]*v[0]]

sol=ivp(edo,tempo,cis,method="Radau")#,method="RK45",interval)

#sol.y[0] -- x
#sol.y[1] -- y
#sol.y[2] -- z

x=sol.y[0]
y=sol.y[1]
z=sol.y[2]

plt.plot(sol.t,x,"r--")
plt.plot(sol.t,y-40,"m-")
plt.plot(sol.t,z+10,"y")

plt.grid(True)
plt.xlim(ti,tf)
plt.legend(["x(t)","y(t)","z(t)"],loc="upper left")
plt.xlabel("Tempo (s)")

plt.savefig("quartoivp.png")