'''
Created on 17/mar/2014

@author: Baleani
'''

inputlist  =  ['mix', 'xyz', 'apple', 'xanadu', 'aardvark', 'sesto']  
outputlist=[]
n=len(inputlist)
print n
print inputlist[n-1]

for i in range(0,n-2): #perchè n-2???
    if inputlist[i][0]=='x':
        outputlist.append(inputlist[i])
        inputlist.remove(inputlist[i])
        
inputlist.sort()
outputlist.sort()
print outputlist+inputlist

inputlist  =  ['mix', 'xyz', 'apple', 'xanadu', 'aardvark', 'sesto']  
outputlist=[]
n=len(inputlist)
print n
print inputlist[n-1]
        
for word in inputlist:
    if word[0]=='x':
        outputlist.append(word)
        inputlist.remove(word)

inputlist.sort()
outputlist.sort()
print outputlist+inputlist