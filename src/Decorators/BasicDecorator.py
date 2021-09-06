'''
Created on May 16, 2019

@author: sipika
'''

def first(msg):
    print(msg)    

first("Hello")

second = first
second("Hello")

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

print(operate(dec,10))