'''
Created on Mar 15, 2019

@author: sipika
'''
list = [15,9,8,1]
n= 11
mul=1
for i in list:
    mul = i*mul
    print (mul)

res = mul%n
print(res)