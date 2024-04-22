import numpy as np
import matplotlib.pyplot as plt
x=list(range(1,1001))
def SIR(vaccination_injection):                     #create a function SIR that with the number of vaccination injected individuals input, the list contain the daily infected individuals will return  
    susceptible=9999
    infected=1
    recovered=0
    list1=[1]
    for i1 in range(2,1001):
        increase1=0
        increase2=0
        for i2 in range(0,susceptible-vaccination_injection):
            b=0.3*infected/10000
            a=np.random.uniform(0,1)
            if b>a:
                increase1=increase1+1
        for i3 in range(0,infected):
            a=np.random.uniform(0,1)
            if a<0.03:
                increase2=increase2+1
        infected=infected+increase1-increase2
        susceptible=susceptible-increase1
        recovered=recovered+increase2
        list1.append(infected)
    return(list1)    
plt.plot(x,SIR(0),label='0')                  #With the function SIR, draw the infected plot under different vaccination injected rates
plt.plot(x,SIR(1000),label='10%')
plt.plot(x,SIR(2000),label='20%')
plt.plot(x,SIR(3000),label='30%')
plt.plot(x,SIR(4000),label='40%')
plt.plot(x,SIR(5000),label='50%')
plt.plot(x,SIR(6000),label='60%')
plt.plot(x,SIR(7000),label='70%')
plt.plot(x,SIR(8000),label='80%')
plt.plot(x,SIR(9000),label='90%')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()
plt.clf


