import matplotlib.pyplot as plt
from math import e

x=[-5+10*i/10**4 for i in range(10**4)] #vai de -5 a 5
y1=[i**2 for i in x] #parabola
y2=[i for i in x] #reta
y3=[e**(-i**2) for i in x] #gaussiana
y4=[e**-i for i in x]

plt.subplot(2,2,1) #de quatro plots, esse será o primeiro
plt.plot(x,y1,'r') #vermelho

plt.subplot(2,2,2) #de quatro plots, esse será o segundo
plt.plot(x,y2,'b') #azul

plt.subplot(2,2,3) #de quatro plots, esse será o terceiro
plt.plot(x,y3,'y') #amarelo

plt.subplot(2,2,4) #de quatro plots, esse será o quarto
plt.plot(x,y4,'k') #preto

plt.tight_layout()
plt.savefig('exemploplot1.png')
