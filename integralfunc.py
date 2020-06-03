import numpy as np
import scipy.integrate as inte    

def func(x): #funcao a ser integrada
    return(np.sin(x)**2) 

def func2(x,t):
    return(np.sin(x)**2+np.sin(t)**2)
    
def func3(x,t,z):
    return(np.exp(np.cos(x*t*z)**2))
    
A=inte.quad(func,0,5) #integra de 0 a 5
B=inte.dblquad(func2,0,5,0,1) #integra x de 0 a 5
                              #integra t de 0 a 1
C=inte.tplquad(func3,0,1,0,np.pi,0,10) #x e [0,1]
                                       #t e [0,np.pi]
                                       #z e [0,10]
