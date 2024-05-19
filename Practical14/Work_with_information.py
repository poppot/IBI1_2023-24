import xml.sax
import os
import xml.dom.minidom
from datetime import datetime
import matplotlib.pyplot as plt
os.chdir(r'C:\Users\52757\Desktop\IBI1_2023-24\Practical14')
begin=datetime.now()                                                              #time starts for SAX API
class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.dictionary={'m':0,'b':0,'c':0}
        self.term=''                                                             #Create a variable to store the tags
    def startElement(self, name, attrs):
        self.term = name                                                         #give current tag to the variable
    def characters(self, content):
        if self.term=='namespace':                                               
            if content=='biological_process':                                    #if the tag is 'namespace', add 1 to the correspond term
                self.dictionary['b']=self.dictionary['b']+1
            if content=='molecular_function':
                self.dictionary['m']=self.dictionary['m']+1
            if content=='cellular_component':
                self.dictionary['c']=self.dictionary['c']+1
parser = xml.sax.make_parser()                                                  #return a parser
handler = MyHandler()
parser.setContentHandler(handler)
parser.parse("go_obo.xml")                                                      #open the file
print('API')
print('term number of biological process is '+str(handler.dictionary['b']))
print('term number of molecular function is '+str(handler.dictionary['m']))
print('term number of cellular component is '+str(handler.dictionary['c']))
over=datetime.now()
time=over-begin                                                                #calculate the time
print('DOM cost '+str(time))
begin=datetime.now()                                                           #time start for DOM
DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection=DOMTree.documentElement                                             #a root for all nodes
children=collection.childNodes
dictionary={'m':0,'b':0,'c':0}
for item in children:                                                          #find 'term' in the nodes
    if item.nodeType==item.ELEMENT_NODE:
        if item.tagName=='term':
            children1=item.childNodes
            for term in children1:
                if term.nodeType==term.ELEMENT_NODE and term.tagName=='namespace':
                    if term.firstChild.data=='biological_process':                     #if the tag is 'namespace', add 1 to the correspond term
                        dictionary['b']=dictionary['b']+1
                    if term.firstChild.data=='molecular_function':
                        dictionary['m']=dictionary['m']+1
                    if term.firstChild.data=='cellular_component':
                        dictionary['c']=dictionary['c']+1
print('DOM')
print('term number of biological process is '+str(dictionary['b']))
print('term number of molecular function is '+str(dictionary['m']))
print('term number of cellular component is '+str(dictionary['c']))
over=datetime.now()
time=over-begin
print('DOM cost '+str(time))                                                            #calculate the time
print('the SAX API is faster')
plt.figure()
ax1=plt.subplot(221)
x1=['biological process',' molecular function is','cellular component']
x2=[handler.dictionary['b'],handler.dictionary['m'],handler.dictionary['c']]
x3=[dictionary['b'],dictionary['m'],dictionary['c']]
plt.bar(x1,x2)
plt.ylabel("number of terms")
plt.xlabel('terms')
ax2=plt.subplot(222)
plt.bar(x1,x3)               
plt.show()
plt.clf
