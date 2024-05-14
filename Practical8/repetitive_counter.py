import re
seq ='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
a=re.findall(r'G(?=TGTGT)',seq)                                       #find repeat sequence
b=re.findall(r'G(?=TCTGT)',seq)
print('The number of GTGTGT sequence is ',len(a))
print('The number of GTCTGT sequence is ',len(b))
