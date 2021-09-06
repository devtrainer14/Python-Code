'''
Created on May 3, 2019

@author: sipika
'''
import random

house = int(input('enter number of houses'))
a=[]
for i in range(0,house):
    x = int(input("Enter ticket value of {0} member".format((i+1))))
    a.append(x)
print(a)
large = 0
listpair=[]
for x in range(len(a)-1,0,-1):
    sum = (a[x]+a[x-2])
    print(sum)
    if sum>=large:
        large = sum
        if a[x]<0:
            listpair.append([a[x-2]])
        elif a[x-2]<0:
            listpair.append([a[x]])
        else:
            listpair.append([a[x],a[x-2]])
        print(listpair)
    if (x-2)==0:
        break
#print(large)
#print("Winner Pair = ",end= "")
#print("winnerpair = {0} {1}".format(listpair[0][0],listpair[0][1]))
#for i in range(0,len(listpair[0])):
    #print(listpair[0][i],end=" ")
max=listpair[0][0]
for i in listpair:
    for x in i:
        if x > max:
            max = x
print(max)
for i in listpair:
    for x in i:
        if x == max:
            print("Winnerpair = ",i)
            break
        
            
    

            
