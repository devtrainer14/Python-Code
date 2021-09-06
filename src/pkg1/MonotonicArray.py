'''
Created on Mar 15, 2019

@author: sipika
'''
st=0
dec=0
lis1=[6,4,4,3,2,1]
for i in range(0,len(lis1)-1):
    if lis1[i]>lis1[i+1]:
        st+=1
        continue
    elif lis1[i]<lis1[i+1]:
        dec+=1
if ((len(lis1)-1)==st) or (dec == len(lis1)-1):    
    print("monotony")        
else:
    print ("not monotony")
"""arr = [1,3,4,7]
flag = True
if(arr[0]>arr[1]):
    for x in range(0,len(arr)-1):
        if(arr[x]>arr[x+1]):
            Flag = True
       
        else:
            Flag = False
            break
else:    
    for x in range(0,len(arr)-1):
        if(arr[x]<arr[x+1]):
            Flag = True
       
        else:
            Flag = False
            break
        
print(Flag)"""

