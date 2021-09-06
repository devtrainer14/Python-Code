'''
Created on Feb 12, 2019

@author: sipika
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self,a,b,c):
        self.a = a
        self.b,self.c=b,c
        """    def getData(self, a, b, c):
        self.a = a
        self.b,self.c=b,c
        """
    def display(self):
        print("a = ",self.a)
        print("b = ",self.b)
        print("c = ",self.c)