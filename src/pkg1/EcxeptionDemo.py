'''
Created on Feb 5, 2019

@author: sipika
'''
import sys
from pkg1.CustomException import CustomException

"""
list = [0,65,98]
try:
   # a = 45/list[0]
    f = open("abcd.txt","r")
   # print(a)
except ZeroDivisionError:
    print("Arithmetic Exception",sys.exc_info()[0])
except IndexError:
    print("Index Exception",sys.exc_info()[0])
except FileNotFoundError:
    print("File not Find",sys.exc_info()[0])
else:
    print("else block")
print("Hello My Program")
"""
   
age = 20

try:
    raise CustomException(age)
except CustomException as e:
    print("Age is ", e)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    