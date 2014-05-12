'''
Created on 17/mar/2014

@author: Baleani
'''
lista=[]
lista_x=[]
print "Insert 4 words:"
for i in range(0,4):
    par=raw_input()
    if par[0]=='x':
        lista_x.append(par)
    else:
        lista.append(par)

lista_x.sort()
lista.sort()
print lista_x+lista