'''
Created on Jul 15, 2019

@author: sipika
'''
# Program to display Calender
import calendar  
# Enter the month and year  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
  
# display the calendar  
print(calendar.month(yy,mm))  