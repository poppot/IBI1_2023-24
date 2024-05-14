import os
import pandas as pd
import matplotlib. pyplot as plt
import numpy as np
os.chdir(r'C:\Users\52757\Desktop\IBI1_2023-24\Practical7')
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.iloc[0:101:10,3])                                 #read0,10,20...100
a=dalys_data.iloc[0:6840,0]                                        #read contries all lines
print(a)
b=[]
d=[]
for i in a:
    if i=='Afghanistan':                                           #find all Afghanistan and return a true or false list
        b.append(1==1)
    else:
        b.append(1==2)
c=dalys_data.iloc[b,3]                                             #through the true or false list find all Afghanistan
print(c)
for i in range(0,6840):
    if a[i]=='China':                                               #find all china
        d.append(1==1)
    else:
        d.append(1==2)
e=dalys_data.iloc[d,3]
f=dalys_data.iloc[d,2]
meanchina=str(np.mean(e))
print('the average DALYS in China is '+meanchina) #the dalys in 2019 is smaller than the mean value
plt.figure()
plt.bar(f,e)
plt.ylabel("DALYS")
plt.xlabel('years')
plt.title('DALYS over time in China')
plt.show()
g=dalys_data.iloc[0:6840,2]                        #the column of years
meanworld=[]
h=[]
for i1 in range(1990,2020):
    for i2 in range(0,6840):
        if g[i2]==i1:
            h.append(1==1)
        else:
            h.append(1==2)
    j=dalys_data.iloc[h,3]                         #a list of the dalys in a certain year
    meanworld.append(np.mean(j))
    h=[]
plt.figure()
plt.bar(f,meanworld)
plt.ylabel("DALYS")
plt.xlabel('years')
plt.title('DALYS over time in World')
plt.show()
plt.clf()




