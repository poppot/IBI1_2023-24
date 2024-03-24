import matplotlib.pyplot as plt
dict={"Sleep":8,"Classes":6,"Study":3.5,"TV":2,"Music":1,'Exercise':3.5}    #input 'other' here
time=[8,6,3.5,2,1,3.5]
events=dict.keys()
print(dict)
plt.figure
plt.pie(time,labels=events)
plt.show()
plt.clf()