'''
Created on 17/mar/2014

@author: Baleani
'''
flag=1
var=int(raw_input("Inserire numero da verificare: "))
for i in range(2,var):
    if var%i==0 and i!=var:
        flag=0
if flag==1:
    print "Numero primo\n"
else:
    print "Numero non primo\n"
    