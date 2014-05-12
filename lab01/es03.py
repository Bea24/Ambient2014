'''
Created on 17/mar/2014

@author: Baleani
'''
string=raw_input("Insert a word: ")
print string
n=len(string)
if n<2:
    print "\"\"\n"
else:
    print (string[0]+string[1]+string[n-2]+string[n-1])