'''
Created on Jun 26, 2019

@author: sipika
'''
from Inheritance import MainDemo
class MyClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("Hello Constructor")
    
    def Func(self):
        print("My Class Function")
        print(self.a,self.b)


var = MyClass(34,'abc')
var.Func()
MainDemo.main()
