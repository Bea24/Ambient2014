'''
Created on 24/mar/2014

@author: Baleani
'''
import string 
import random

txt=raw_input("Inserire nome file:\n")
n=int(raw_input("Inserire numero parole:\n"))
par=raw_input("Inserire parola con cui iniziare:\n")

file_txt=open(txt)
file2=file_txt.read()

to_remove = string.punctuation + string.digits +string.whitespace
for i in range(0, len(to_remove)):
    file2= file2.replace(to_remove[i]," ")

lista=file2.split(" ")

dic={}


for i in range(0, len(lista)-1):
    if i==0:
        dic[lista[i]]=[]
        dic[lista[i]].append(i+1)
    else:
        key=lista[i]
        if (dic.get(key)!= None):
            dic[lista[i]].append(lista[i+1])
        else:
            dic[lista[i]]=[]
            dic[lista[i]].append(i+1)

print par
word1=par

for i in range(n-1):
    word=par
    word1=random.choice(dic[par])
    print word1

            
    