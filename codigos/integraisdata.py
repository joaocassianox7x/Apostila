import numpy as np
import scipy.integrate as inte
import matplotlib.pyplot as plt


n=10**3 #numero de pontos
M=np.zeros((n,2)) #uma coluna para x e outra para f(x)

x=np.linspace(0,2*np.pi,n)
y=np.sin(x)**2

A=inte.trapz(y,x)
B=inte.simps(y,x)
