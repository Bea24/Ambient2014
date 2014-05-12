'''
Created on 17/mar/2014

@author: Baleani
'''
list=[]
for i in range(0,4):
    string=raw_input("Insert a word: ")
    list.append(string)
    
count=0
for i in range(0,4):
    if len(list[i])>=2 and list[i][0]==list[i][len(list[i])-1]:
        count+=1

print ("Output = %d" %count)