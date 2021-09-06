'''
Created on Jul 9, 2019

@author: sipika
'''
def STRING(strr):
    u,l=0,0
    s=list(strr)
    for i in s:
        if i==" ":
            continue
        elif i==i.upper():
            u=u+1
        elif i==i.lower():
            l=l+1
    print("Uppercase : ",u)
    print("Lowercase : ",l)
    return
strr1=input("Enter a string :     ")
STRING(strr1)