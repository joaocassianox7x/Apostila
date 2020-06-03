'''

import numpy as np

def pfft(x, y): #definimos a funcao transformada
    dx=x[1]-x[0] #encontramos o delta k
    N=len(x) #numero de pontos
    k=np.linspace(-np.pi/dx, np.pi/dx, N+1) #dominio em k
    k=k[:-1] #tiramos o ultimo ponto, devido as c.c periodicas
    yk=np.fft.fft(y, norm='ortho')#transformada de fourier
    yk*=np.exp(-1j*k*x[0]) #adicionamos a fase
    return k,yk
def ipfft(k, yk): #transformada inversa de fourier
    dk=k[1]-k[0]
    N=len(k)
    x=np.linspace(-dk/np.pi, dk/np.pi, N+1)
    x=x[:-1]
    y=np.fft.ifft(yk, norm='ortho') #transformada inversa
    y*=np.exp(+1j*k*x[0]) #adicionamos a fase
    return x, y

x1=np.linspace(-15*np.pi, 15*np.pi, 256 + 1)
x1=x1[:-1]
y1=np.sin(x1)
k1, yk1=pfft(x1, y1) #retorna da derivada e 
'''

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-100,100,2**12+1)
dx=x[1]-x[0]
x=x[:-1] #retira o ultimo ponto
y=np.sin(x)+np.cos(x)


k=np.linspace(-np.pi/dx,np.pi/dx,len(x))
yk=np.fft.fftshift(np.fft.fft(y,norm="ortho"))
yk*=np.exp(1j*x[0]*k)

plt.subplot(221)
plt.plot(k,np.real(yk),'b')
plt.legend(["Parte Real"],loc='upper right')
plt.xticks([],[]) #retira eixo x
plt.xlim(-10,10)

plt.subplot(222)
plt.plot(k,np.imag(yk),'r')
plt.legend(["Parte Imaginária"],loc='lower right')
plt.xticks([],[]) #retira eixo x
plt.xlim(-10,10)

plt.subplot(212)
plt.plot(k,(np.abs(yk))**2,'m')
plt.legend(["Módulo Quadrado"],loc='upper right')
plt.xlim(-10,10)

plt.tight_layout()
plt.savefig('transformadaplot.png')