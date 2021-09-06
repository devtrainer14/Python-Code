'''
Created on Jul 22, 2019

@author: sipika
'''
import os
obj = open("my File/file.txt",'w')
obj.write("Hello, my Sample file. My first program")
obj.close()
obj = open("my File/file.txt",'r+')
var = obj.read()
obj.seek(30)
obj.write(" Overwritten m       data ")

obj.close()
obj = open("my File/file.txt",'a')

obj.write("Appended Data")
print(obj.tell())

obj.close()



