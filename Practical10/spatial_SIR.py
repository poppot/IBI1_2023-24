import numpy as np
import matplotlib.pyplot as plt
population=np.zeros((100,100))
i1=np.random.randint(0,100)
i2=np.random.randint(0,100)
population[i1,i2]=1                                             #create a population with 100*100 individuals and random select a break point
plt.imshow(population)
plt.title('the spatial SIR model of day 1')
plt.show()                                                      #show the picture of day 1
plt.cla
for t in range(2,101):
    infectedIndex = np.where(population==1)                         
    for i in range(len(infectedIndex[0])):                              #find the infectd individuals and read them one by one
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        population[x,y]=np.random.choice((1,2),1,p=[0.97,0.03])[0]       #random tranfrom the infected individuals into recovered
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):             
                if (xNeighbour,yNeighbour) != (x,y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:             #find the susceptible individuals around the infected
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[0.7,0.3])[0]  #random tranfrom the susceptible individuals into the infected
    plt.imshow(population,cmap='viridis',vmax=2,vmin=0,interpolation='nearest')
    plt.title(f'Spatial SIR Model on Day {t}')    #draw the picture of that day
    plt.show()
    plt.cla
        