from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
import datetime
from tkinter import messagebox
import index.income as i
import index.home as h
import index.weekly as w
import index.monthly as m
import index.yearly as y
import index.alldata as a
import sqlite3


def expense_fun():
    
    root=Tk()
    root.configure(background="tan")
    root.geometry("750x550")
    root.title("Expense Tracker")
    
    amount=IntVar()
    
    def week_trans():
        root.destroy()
        w.week()
        
    def month_trans():
        root.destroy()
        m.month()
    
    def year_trans():
        root.destroy()
        y.year()
    
    def all_trans():
        root.destroy()
        a.all_data()
    
    def expense_db():
        a=amount.get()
        d=date_entry.get()
        ind=d.rfind('/')
        d=d[:ind+1]+'20'+d[ind+1:]
        print(d)
        dt=datetime.datetime.strptime(d,'%m/%d/%Y').strftime('%Y-%m-%d')
        print(dt)
        c=combo.get()
        db=sqlite3.connect("MyDatabase")
        cur=db.cursor()

        cur.execute("create table if not exists expense(amount NUMBER ,email TEXT,date DATE)")
        db.commit()
    
        
        i=cur.execute("Insert into expense(amount,email,date) VALUES(?,?,?)",(a,c,dt))
        db.commit()
        
        '''i=cur.execute("delete from expense") 
        db.commit() 
        '''
        '''i=cur.execute("drop table expense")
        db.commit()''' 
    
        if i:
            messagebox.showinfo(root,"Added Successfully")
        else:
            messagebox.showinfo(root,"Try again!") 
    
    def add_income():
        root.destroy()
        i.income_fun()
    
    
    menubar=Menu(root)
    ie=Menu(menubar,tearoff=0)
    ie.add_command(label="Income",command=add_income)
    ie.add_command(label="Expense")

    menubar.add_cascade(label="Income/Expense",font="none 10 bold",menu=ie)

    t=Menu(menubar,tearoff=0)
    t.add_command(label="Weekly",command=week_trans)
    t.add_command(label="Monthly",command=month_trans)
    t.add_command(label="Yearly",command=year_trans)
    t.add_command(label="All Transactions",command=all_trans)
    menubar.add_cascade(label="Transactions",font="none 10 bold",menu=t)

    r=Menu(menubar,tearoff=0)
    r.add_command(label="Pie Chart")
    r.add_command(label="Bar Graph")

    menubar.add_cascade(label="Report",font="none 10 bold",menu=r)

    root.config(menu=menubar)

    img_frame=Frame(root,width=420,height=420,bg="tan")
    img_frame.pack(side=LEFT,anchor=N)
   

    img=PhotoImage(file="expense.png")
    Label(img_frame,image=img).place(x=20,y=100)

    label1=Label(root,text="Amount",font="Helvetica 12 bold")
    label1.place(x=400,y=150)
    label1.configure(background="tan")
    
    amount_entry=Entry(root,textvariable=amount)
    amount_entry.place(x=500,y=150,height=25,width=200)
    
    label=Label(root,text="Category",font="Helvetica 12 bold")
    label.place(x=400,y=200)
    label.configure(background="tan")
    
    combo=Combobox(root) 
    combo['values']= ('Shopping','Holidays', 'Entertainment', 'Grocery','Kids','Travel','Food','Medicine','Others') 
    combo.current(0) #set the selected item
    combo.place(x=500,y=200,height=25,width=200)
    
    label2= Label(root,text="Date",font="Helvetica 12 bold")
    label2.configure(background="tan")
    label2.place(x=400,y=250)
    
    date_entry=DateEntry(root)
    date_entry.place(x=500,y=250,height=25,width=200)
    
    btn=Button(root,text="Add",width=8,font="Helvetica 12 bold",command=expense_db)
    btn.place(x=480,y=330)
    
    root.mainloop()
    

expense_fun()