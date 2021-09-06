from tkinter import *
from tkcalendar import DateEntry
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
def week_pie():

    '''root=Tk()
    root.title("Weekly Report")
    root.geometry("700x500")
    root.resizable(0,0)
    root.configure(background="tan")'''
    '''list1=list()
    list2=list()'''
    db=sqlite3.connect("MyDatabase")
    cur=db.cursor()
    cur1=db.cursor()
    cur.execute("select sum(amount) from expense where date > date('now','-7 days')")
    cur1.execute("select sum(amount) from income where date >= date('now','-1 months')")
    result=cur.fetchall()
    result1=cur1.fetchall()
    print(result)
    print(result1)
    #print(len(result))
    w,h=1,len(result)
    '''list1=[[0 for x in range(w)] for y in range(h)]
    list2=[[0 for x in range(w)] for y in range(h)]'''
    '''data = [['E001', 'M', 34, 123, 'Normal', 350],
        ['E002', 'F', 40, 114, 'Overweight', 450],
        ['E003', 'F', 37, 135, 'Obesity', 169],
        ['E004', 'M', 30, 139, 'Underweight', 189],
        ['E005', 'F', 44, 117, 'Underweight', 183],
        ['E006', 'M', 36, 121, 'Normal', 80],
        ['E007', 'M', 32, 133, 'Obesity', 166],
        ['E008', 'F', 26, 140, 'Normal', 120],
        ['E009', 'M', 32, 133, 'Normal', 75],
        ['E010', 'M', 36, 133, 'Underweight', 40] ] '''
 
    #Label(root,text="Pie Chart",bg="tan",font="Calibari 12 bold underline").place(x=250,y=30)
    '''i=0
    for row in result:
        list1[i][0]=row[0]
        list1[i][1]=row[1]
        list1[i][2]=row[2]
        i+=1
    for row in result1:
        list2[i][0]=row[0]
        i+=1'''
       
    #print(result)    
    #print(data)
    #df = pd.DataFrame(data, columns = ['Amount', 'Category', 'Date'] )
    df = pd.DataFrame(result,result1, columns = ['Expense'])
    #df1 = pd.DataFrame(result1, columns = ['Income',])
    # create histogram for numeric data
    df.hist()
    #df1.hist()
    # show plot
    plt.show()
   
   
    #root.mainloop()
week_pie()