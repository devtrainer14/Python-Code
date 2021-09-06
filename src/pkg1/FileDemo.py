'''
Created on Feb 6, 2019

@author: sipika
'''
import sys,os
"""obj=open("abcd.txt","w+")  
obj.write("Hi, This is my new text \n") 
obj.close() 
value = input("Enter to Print")"""
obj1=open("welcome.png","r+b")  
s=obj1.read()  
#print(s)
"""s = str(s)
s1 = value.upper()

s1="\n"+s1
obj1.seek(3) #To write something at particular location
obj1.write(s1)
print(s1)  """
obj1.close()
"""obj=open("abcd.txt","a")  
obj.write(s1)  
obj.close() """
path = "D:/Pythonprog/directory"
os.mkdir(path)
print(os.getcwd())

