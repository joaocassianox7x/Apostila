from scipy.integrate import solve_ivp as ivp

ci=[1,0] #condicoes iniciais
t0=0 #tempo inicial
tf=10 #tempo final

def edo(t,y): #primeiro parametro deve ser o tempo
    return(y[1],-(y[0]+y[1]))

resposta=ivp(edo,(t0,tf),ci)
t=resposta.t #retorna os pontos no tempo
y=resposta.y[0]
ydot=resposta.y[1]