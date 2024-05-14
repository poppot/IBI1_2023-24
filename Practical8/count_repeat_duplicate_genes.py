import re
import os
os.chdir(r'C:\Users\52757\Desktop\IBI1_2023-24\Practical8')
genes=(open('duplicate_genes.fa','r',encoding='UTF-8')).read()                             #open the duplicate genes
repeat_genes=str(input('input the repeat genes:'))                                         #receive the repeat genes
gene_name=re.findall(r'Y......',genes)                                                     #find the name of genes
genes=re.sub(r'\n','',genes)                                                               #delete all line break
genes=re.sub(r'Y......','\n',genes)                                                        #replace gene name with line break to split sequences with line break
index=r'{}(?={})'.format(repeat_genes[0],repeat_genes[1:])                                 
roll=0
content=''
for i in genes.splitlines():                                                               #read the sequences line by line
    if i!='':                                                                              #the first line is \n
        list1=re.findall(index,i)                                                          #find repeat sequence
        content=content+'>'+gene_name[roll]+' (the times of repetition:'+str(len(list1))+')'+'\n'+i+'\n'    
        roll=roll+1
filename=repeat_genes+'_duplicate_genes.fa'                                                
file=open(filename,'w',encoding='UTF-8')
file.write(content)                                                                        #create a file