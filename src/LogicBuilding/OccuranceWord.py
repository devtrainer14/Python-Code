'''
Created on Jun 19, 2019

@author: sipika
'''
str="98889888"
dup = []
for x in str:
    if x not in dup:
        c=str.count(x,0,len(str))
        dup.append(x)
        print(x+" : ",c)
    
        
        
'''from chatbot import demo
 demo()
'''
        