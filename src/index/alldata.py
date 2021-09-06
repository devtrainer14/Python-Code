from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3

def all_data():

    root=Tk()
    root.title("All Transactions")
    root.geometry("700x500")
    root.resizable(0,0)
    root.configure(background="tan")
    Label(root,text="All Transactions",bg="tan",font="Calibari 12 bold underline").place(x=250,y=30)
    db=sqlite3.connect("MyDatabase")
    cur=db.cursor()
    cur.execute("select * from expense")
    result=cur.fetchall()
    if result:
        Label(root,text="Amount",font="Calibari 10 bold underline",bg="tan").place(x=150,y=70)
        Label(root,text="Category",font="Calibari 10 bold underline",bg="tan").place(x=300,y=70)
        Label(root,text="Date",font="Calibari 10 bold underline",bg="tan").place(x=450,y=70)
        r=100
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
#all_data()
