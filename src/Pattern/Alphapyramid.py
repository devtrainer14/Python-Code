'''
Created on Jan 22, 2020

@author: sipika
'''
for i in range(1,5):
    k=96
    for j in range(1,8):
        
        if j>=5-i and j<=3+i:
            if j<=4:
                k=k+1
            else:
                k=k-1
            print(chr(k),end=" ")
        else:
            print(" ",end=" ")
            
    print(" ")