'''
Created on Jun 24, 2019

@author: sipika
'''
class CustException(Exception):
    def __init__(self,age):
        if(age<18):
            print("You are not valid for vote")
        else:
            print("You can vote")
        
    