'''
Created on Jun 21, 2019

@author: sipika
'''
for i in range(5):
    for j in range(5):
        if i==j or i+j==4 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")