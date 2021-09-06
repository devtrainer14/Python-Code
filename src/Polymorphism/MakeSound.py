'''
Created on Feb 14, 2019

@author: sipika
'''
from Polymorphism import Bear,Dog
def makesound(animaltype):
    animaltype.sound()
    
    
bearobj = Bear.MyClass()
dogobj = Dog.MyClass()
bearobj.sound()
makesound(dogobj)