'''
Created on Feb 5, 2019

@author: sipika
'''
data = 50
try: 
    data = data/0
except ZeroDivisionError: 
    print('Cannot divide by 0 ', end = '') 
else: 
    print('Division successful ', end = '') 

try: 
    data = data/5
except: 
    print('Inside except block ', end = '') 
else: 
    print('GFG', end = '') 



data = 50
try: 
    data = data/10
except ZeroDivisionError: 
    print('Cannot divide by 0 ', end = '') 
finally: 
    print('GeeksforGeeks ', end = '') 


value = [1, 2, 3, 4] 
data = 0
try: 
    data = value[4] 
except IndexError: 
    print('GFG', end = '') 
except: 
    print('GeeksforGeeks ', end = '') 
    
 
   
value = [1, 2, 3, 4, 5] 
try: 
    value = value[5]/0
except (IndexError, ZeroDivisionError): 
    print('GeeksforGeeks ', end = '') 
else: 
    print('GFG ', end = '') 
finally: 
    print('Geeks ', end = '') 







