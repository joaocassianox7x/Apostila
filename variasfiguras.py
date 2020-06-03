
import matplotlib.pyplot as plt
from math import e
import math

n=10**5 #numero de pontos
x=[-5+i/n for i in range(n)]
y1=[i**2 for i in x]
y2=[e**(-i**2) for i in x]

plt.figure() #gera a nova figura em branco
plt.plot(x,y1,'r')
plt.title("Primeira Figura Gerada")
plt.tight_layout() #tenha o costume de sempre declarar esse camarada
plt.savefig("figura1.png") #salvar local atual


plt.figure() #gera a nova figura em branco
plt.plot(x,y2,'k')
plt.title("Segunda Figura Gerada")
plt.tight_layout() #tenha o costume de sempre declarar esse camarada
plt.savefig("figura2.png") #salvar local atual

plt.figure() #nova figura
plt.subplot(3,1,1)
plt.plot(x,y1,'y')

plt.subplot(3,1,2)
plt.plot(x,y2,'b')

plt.subplot(3,1,3)
y3=[math.sin(i) for i in x]
plt.plot(x,y3,'k')


plt.tight_layout() #tenha o costume de sempre declarar esse camarada
plt.savefig("figura3.png") #salvar local atual