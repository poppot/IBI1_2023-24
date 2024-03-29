import os
import pandas as pd
import matplotlib. pyplot as plt
import numpy as np
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.iloc[0:101:10,3])
a=dalys_data.iloc[0:6840,0]
print(a)
b=[]
d=[]
for i in range(0,6840):
    if a[i]=='Afghanistan':
        b.append(1==1)
    else:
        b.append(1==2)
c=dalys_data.iloc[b,3]
print(c)
for i in range(0,6840):
    if a[i]=='China':
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
g=dalys_data.iloc[0:6840,2]
meanworld=[]
h=[]
for i1 in range(1990,2020):
    for i2 in range(0,6840):
        if g[i2]==i1:
            h.append(1==1)
        else:
            h.append(1==2)
    j=dalys_data.iloc[h,3]
    meanworld.append(np.mean(j))
    h=[]
plt.figure()
plt.bar(f,meanworld)
plt.ylabel("DALYS")
plt.xlabel('years')
plt.title('DALYS over time in World')
plt.show()
plt.clf()




