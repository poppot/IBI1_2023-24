import numpy as np
import matplotlib.pyplot as plt
susceptible=9999
infected=1
recovered=0
list1=[1]
list2=[9999]
list3=[0]                               #set the initial value of the three types of people and create three list to contain the data
x=list(range(1,1001))
for i1 in range(0,999):
    increase1=0
    increase2=0                        #let the increase number of infected and recovered return to zero
    for i2 in range(0,susceptible):
        b=0.3*infected/10000
        a=np.random.uniform(0,1)
        if b>a:
            increase1=increase1+1
    for i3 in range(0,infected):
        a=np.random.uniform(0,1)
        if a<0.03:
            increase2=increase2+1
    infected=infected+increase1-increase2
    susceptible=susceptible-increase1     #add the increase number to corresponding group
    recovered=recovered+increase2
    list1.append(infected)
    list2.append(susceptible)
    list3.append(recovered)                #add the number of three individuals of the new day to the corresponding list
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(x,list1,label='infected')
plt.plot(x,list2,label='susceptible')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.plot(x,list3,label='recovered')
plt.legend()
plt.savefig('Practical10/SIR plot.png')    #save the plot 
plt.show()
plt.clf

