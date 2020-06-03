#EDO y''+y'+y=sen(e**x)
import math

e=math.e
y=[]
ydot=[]
ydotdot=[]

y0=10
y0dot=math.pi

y.append(y0)
ydot.append(y0dot)

pi=0
pf=10
n=10**6
delta=(pf-pi)/n

for i in range(n):
    y.append(y[i]+delta*ydot[i])
    ydot.append(ydot[i]+delta*
    (math.sin(i*delta)-ydot[i]-y[i]))
    


import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(pi,pf,n+1)

plt.plot(t,y,'b')
plt.plot(t,ydot,'r')

plt.legend(["y(x)","y'(x)"],loc="upper right")
plt.grid(True)
plt.xlim(pi,pf)
plt.xlabel("t (s)")

plt.savefig("eulersegundaordem.png")