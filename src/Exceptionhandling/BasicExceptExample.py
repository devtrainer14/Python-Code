'''
Created on Feb 15, 2019

@author: sipika
'''
from builtins import ZeroDivisionError, ArithmeticError
list = [1,2,3,4]

try:
    print(list[9]/0)
except ArithmeticError:
    print("Arithmetic Error")
except ZeroDivisionError:
    print("Zero Division Error")
except NameError:
    print("Name Error")
except Exception as e:
    print("Unknown Error",e)
else:
    print("Error not in list")   
def show():
    print("rest code is running properly")
    
show()