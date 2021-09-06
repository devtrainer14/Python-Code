'''
Created on Jun 17, 2019

@author: sipika
'''
#cursing @ btes
obj = open("curse.txt",'w')
obj.write("He is foolish person, Such type of moron people never grow in life. ")
obj = open("curse.txt","r")
s=obj.read()
obj.close()
k =["stupid","bitch","foolish","moron"]
for i in range(0,len(k)):
    if k[i] in s:
        m=""
        for  z in range(0,len(k[i])):
            m=m+"*"
        s=s.replace(k[i],m)
obj2 = open("curse1.txt","w")
obj2.write(s)
obj2.close()
