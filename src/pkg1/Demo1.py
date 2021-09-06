'''
Created on Jan 31, 2019

@author: sipika
'''
#from pkg2.module1 import demo_method
import pkg2.module1
def sort():
    a=[(2,3),(5,6),(4,1),(2,5),(9,0),(3,12)]
    b=len(a)
    for i in range(0,b):
        for j in range(i,b):
            if(a[i][1]>a[j][1]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    print(a)
        
pkg2.module1.demo_method()