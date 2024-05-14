import re
import os
os.chdir(r'C:\Users\52757\Desktop\IBI1_2023-24\Practical8')
genes=(open('duplicate_genes.fa','r',encoding='UTF-8')).read()
repeat_genes=str(input('input the repeat genes:'))
gene_name=re.findall(r'Y......',genes)
genes=re.sub(r'\n','',genes)
genes=re.sub(r'Y......','\n',genes)
index=r'{}(?={})'.format(repeat_genes[0],repeat_genes[1:])
roll=0
content=''
for i in genes.splitlines():
    list1=re.findall(index,i)
    if list1!=[]:
        content=content+gene_name[roll]+'\n'+i+'\n'+str(len(list1))+'\n'
    roll=roll+1
filename=repeat_genes+'_duplicate_genes.fa'
file=open(filename,'w',encoding='UTF-8')
file.write(content)