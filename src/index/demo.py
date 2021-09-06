from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Weekly Transactions")
root.geometry("700x500")
root.resizable(0,0)
root.configure(background="tan")
db=sqlite3.connect("MyDatabase")
cur=db.cursor()
cur.execute("select * from expense where date >= date('now','-7 days')")
result=cur.fetchall()
if result:
    Label(root,text="Amount",font="Calibari 10 bold",bg="tan").place(x=150,y=50)
    Label(root,text="Category",font="Calibari 10 bold",bg="tan").place(x=300,y=50)
    Label(root,text="Date",font="Calibari 10 bold",bg="tan").place(x=450,y=50)
    r=80
    for row in result:
        label1=Label(root,text=row[0],bg="tan")
        label1.place(x=150,y=r)
        label2=Label(root,text=row[1],bg="tan")
        label2.place(x=300,y=r)
        label2=Label(root,text=row[2],bg="tan")
        label2.place(x=450,y=r)
        r+=20                       
else:
    messagebox.showinfo(root,"No data exists")
    
root.mainloop()