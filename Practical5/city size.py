import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=[8,6]
uk_cities=[0.56,0.62,0.04,9.7]
ch_cities=[0.58,8.4,29.9,22.2]
uk_cities.sort()
ch_cities.sort()
print(uk_cities)
print(ch_cities)
x1=['Stirling','Edinburgh','Glasgow','London']
x2=['Haining','Hangzhou','Shanghai','Beijing']
plt.figure()
ax1=plt.subplot(221)
plt.bar(x1,uk_cities)
plt.ylabel("population")
plt.xlabel('UK cities')
plt.title('population of UK cities')
ax2=plt.subplot(222)
plt.bar(x2,ch_cities)
plt.ylabel("population")
plt.xlabel('Chinese cities')
plt.title('population of Chinese cities')
plt.show()
plt.clf