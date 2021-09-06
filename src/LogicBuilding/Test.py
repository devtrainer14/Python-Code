'''
Created on Jul 9, 2019

@author: sipika
'''
'''
a=input("Enter first word : ")
b=input("Enter second number : ")
a=list(a)
b=list(b)
c=0
if(len(a)==len(b)):
    for i in a:
        for j in b:
            if(i==j):
                b.remove(j)
                c=c+1
                break
        else:
            print("It is not anagram")
            break
    if(c==len(a)):
        print("It is anagram")
else:
    print("It is not anagram")'''


#################################################################
#Craete a list containing duplicates and a new list having no duplicates 
'''li=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
li1=[]
for i in li:
    if i not in li1:
        li1.append(i)
print(li1)'''


