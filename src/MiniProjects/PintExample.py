'''
Created on Jun 28, 2019

@author: sipika
'''
from units import unit
metre = unit('m')
print(metre(7) + metre(11))

def change(in_unit,unit_val):
    var = unit(unit_val)
    return var(in_unit)
    
print(change(23,'gm'))