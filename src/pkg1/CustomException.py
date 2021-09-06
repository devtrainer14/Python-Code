'''
Created on Feb 5, 2019

@author: sipika
'''

class CustomException(Exception):
    '''
    classdocs
    '''


    def __init__(self, age):

        if(age>18):
           print("Valid for Vote")
        else:
            print("Not Valid for Vote")
        