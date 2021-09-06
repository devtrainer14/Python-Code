'''
Created on May 16, 2019

@author: sipika
'''
def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

#Outputs "Hello"
new()
#///////////////////////////////////////////////

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def make_pretty1(func):
    def inner():
        print("I got decorated1111")
        func()
    return inner

@make_pretty
@make_pretty1
def ordinary():
    print("I am ordinary")
#data = make_pretty(ordinary)
ordinary()

"""
@make_pretty
def ordinary():
    print("I am ordinary")
    
#is equivalent to
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)"""