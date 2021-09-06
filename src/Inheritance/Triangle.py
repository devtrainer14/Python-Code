'''
Created on Feb 12, 2019

@author: sipika
'''

from . import Polygon

class MyClass(Polygon.MyClass):
    '''
    classdocs
    '''


    def __init__(self,a,b,c):
      super().__init__(a,b,c)
      
      
      
    def area(self):
        self.display()
        s = self.a+self.b+self.c/2
        print("Area = ",s)
        
        