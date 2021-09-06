'''
Created on Feb 21, 2019

@author: sipika
'''
from dataclasses import replace

para=input("Enter your paragrapgh :- ")
ob=open("badwords.txt","w")
ob.write(para)
ob.close()
real=""
bad=["idiot","Foolish","Stupid"]


for i in range(0,len(bad)):
    ob1=open("badwords.txt","r")
    content=ob1.read()
    ob1.close()
    star = "*"*len(bad[i])
    real=content.upper().replace(bad[i].upper(),star)
    ob3=open("badwords.txt","w")
    ob3.write(real)
    ob3.close()


ob2=open("badwords.txt","r")
code=ob2.read()
print(code)
ob2.close()








