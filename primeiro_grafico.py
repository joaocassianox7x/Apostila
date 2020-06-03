import matplotlib.pyplot as plt #sera a chamada usual
import math as m

n=10**3

x=[i*2*m.pi/n for i in range(n)] #de 0 ate 2pi com passo 0.01
y1=[]
y2=[]
y3=[]

for i in x:
    y1.append(m.sin(i)) #criamos uma lista [sin(0),...,sin(2*pi)]
    y2.append(2+m.cos(i)) #vetor de cossenos
    y3.append(4+m.sin(i)*m.cos(i)) # produto entre senos e cossenos
    
plt.plot(x,y1,'k') #k->preto, - ->continuo
plt.plot(x,y2,'y') #y->amarelo, - ->bolinhas
plt.plot(x,y3,'r') #r->vermelho, - ->desenhos

plt.title("Sin(x)") #adiciona "Sin(x)" sobre o gráfico
plt.xlabel("X") #escreve "X" no eixo horizontal
plt.ylabel("Y") #escreve "Y" no eixo vertical
plt.legend(["Sin(x)","Cos(x)", "Sin(x)Cos(x) "]
            ,loc="upper right") #adiciona legendas em ordem de plot

plt.grid(True) #adiciona grade no fundo

plt.xlim(0,2*m.pi) #apresenta o eixo x de 0 a 2pi
plt.ylim(-1,6) #apresenta o eixo y de -1 ate 1

plt.savefig("terceirafigura.png")