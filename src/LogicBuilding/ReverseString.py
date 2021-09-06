'''
Created on May 2, 2019

@author: sipika
'''
str = "I am an Indian"
print(list(str))
list = str.split(" ")
print (list)

for i in range(len(list)-1,-1,-1):
    print(list[i].capitalize(), end=" ")



    