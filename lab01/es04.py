'''
Created on 17/mar/2014

@author: Baleani
'''
string=raw_input("Insert a word: ")
letter=string[0]
print letter
word=string[1:]
print word
word=word.replace(letter,"*")
print letter+word