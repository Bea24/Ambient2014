'''
Created on 17/mar/2014

@author: Baleani
'''
inputlist = [(1, 7), (1, 3), (3, 4, 5), (2, 2)] 
n=len(inputlist)
len1=len(inputlist[0])
len2=len(inputlist[1])
for i in range(0,n-1):  
    if len1==len2 and inputlist[0]>inputlist[1]:
        var=inputlist[0]
        inputlist[0]=inputlist[1]
        inputlist[1]=var
    else len1!=len2: