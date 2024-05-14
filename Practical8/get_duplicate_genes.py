import re
import os
os.chdir(r'C:\Users\52757\Desktop\IBI1_2023-24\Practical8')
a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r',encoding='UTF-8')           #read the file
b=a.read()                                                                
d=re.findall(r'gene:(.......).+?duplication',b)                                       #find all duplication gene name 
f=re.findall(r'gene.+?duplication.+\n([\s,\S]+?)>',b)                                 #find all sequences of duplication genes
c=''
for i in range(0,len(d)):
               c=c+'>'+d[i]+'\n'
               c=c+f[i]
g=open('duplicate_genes.fa','w',encoding='UTF-8')
g.write(c)                                                                            #write file
h=open('duplicate_genes.fa','r',encoding='UTF-8')
s=h.read()
print(s)


