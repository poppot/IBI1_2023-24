import re
a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r',encoding='UTF-8')
b=a.read()
z=re.sub(r'\n','',b)
d=re.findall(r'gene:(.......).*duplication',b)
f=re.findall(r'gene.+?duplication.+\n([\s,\S]+?)>',b)
print(f)
c=''
for i in range(0,len(d)):
               c=c+d[i]+'\n'
               c=c+f[i]
g=open('duplicate_genes.fa','w',encoding='UTF-8')
g.write(c)
h=open('duplicate_genes.fa','r',encoding='UTF-8')
print(h)


