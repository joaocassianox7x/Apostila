import math

e=math.e

def fun(x): #funcao que desejamos integrar
    return(e**(-x))

n=10**4 #numero de pontos
a=0
b=10
dx=(b-a)/n

I=0

x=[(i*b/n)-a for i in range(n)] #vetor que vai de a ate b em n pontos

A=0
for i in range(n-1):
    A+=(dx/2)*(fun(x[i+1])-fun(x[i]))