'''
Created on Jun 26, 2019

@author: sipika
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""listt=[]
for x in range(0,len(a),2):
   listt.append(a[x])
print(listt)"""

#List Comprehention : for loop just shifted to the end of the 
#list comprehension, and the part before the for keyword is 
#the thing to append to the end of the new list.

listt=[a[x] for x in range(0,len(a),2)]
print(listt)

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2019 - year for year in years_of_birth]
print(ages)
