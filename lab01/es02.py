'''
Created on 17/mar/2014

@author: Baleani
'''

n=int(raw_input("Inserire un numero: "))
if n==1 or n==0:
    print "1"
else:
    x=0
    y=1
    print"1"
    for i in range(1,n):
        res=x+y
        print res
        x=y
        y=res