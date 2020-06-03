import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rand

n=10**4
x=rand.random(n) #vetor de n numeros aleatorios entre 0 e 1
x=2*x-1 #novo vetor, com numeros entre -1 e 1

y=-1+2*rand.random(n) #vetor com numeros entre -1 e 1

plt.scatter(x,y)

plt.savefig("scatter2.png")