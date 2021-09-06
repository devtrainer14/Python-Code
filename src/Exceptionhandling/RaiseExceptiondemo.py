'''
Created on Jun 24, 2019

@author: sipika
'''
from Exceptionhandling.CustomException import CustException
age = int(input("Enter Your Age :: "))
try:
    raise CustException(age)
except CustException as ae:
    print("Exception....",ae)
else:
    print("You can Vote")