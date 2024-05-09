import pandas as pd
import os
import re
os.chdir(r'C:\Users\52757\Desktop\IBI1_2023-24\Practical13')         #move to the fold
matrix=pd.read_excel("BLOSUM62.xlsx")
human=open('SLC6A4_HUMAN.fa','r',encoding='UTF-8')
mouse=open('SLC6A4_MOUSE.fa','r',encoding='UTF-8')
rat=open('SLC6A4_RAT.fa','r',encoding='UTF-8')                       #read matrix and sequences
def reading(sequence):                                               #a function that remove the first line and \n from the sequences 
    Sequence=sequence.read()
    resu=re.sub(r'>.+?\n','',Sequence)
    result=re.sub(r'\n','',resu)                                     
    return(result)
Human=reading(human)
Mouse=reading(mouse)
Rat=reading(rat)
def compare(sequence1,sequence2,matrix):                           #a function that calculate similarity rate and score of two sequence
    index={'C':1,'S':2,'T':3,'P':4,'A':5,'G':6,'N':7,'D':8,'E':9,'Q':10,'H':11,'R':12,'K':13,'M':14,'I':15,'L':16,'V':17,'F':18,'Y':19,'W':20}
    same=0                                                                                  
    score=0
    for i in range(0,len(sequence1)):
        if sequence1[i]==sequence2[i]:
            same=same+1
        score=matrix.iloc[index[sequence1[i]]-1,index[sequence2[i]]]+score    #use index to find the score in excel
    same_rate=same/len(sequence1)
    print(same_rate)
    print(score)
print('the similarity and score between human and mouse are')
compare(Human,Mouse,matrix)
print('the similarity and score between human and rat are')
compare(Human,Rat,matrix)
print('the similarity and score between mouse and rat are')
compare(Mouse,Rat,matrix)



