from tkinter import *
from tkcalendar import DateEntry
import index.expense as e
import index.weekly as w
import index.monthly as m
import index.yearly as y
import index.alldata as a
import sqlite3
import datetime
from tkinter import messagebox

def income_fun():
    
    root=Tk()
    root.configure(background="tan")
    root.geometry("750x550")
    root.title("Expense Tracker")
    
    amount=IntVar()
    source=StringVar()
    date=StringVar()

    def add_expense():
        root.destroy()
        e.expense_fun()
        
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
        
    def income_db():
        a=amount.get()
        d=date.get()
        s=source.get()
        d=date.get()
        ind=d.rfind('/')
        d=d[:ind+1]+'20'+d[ind+1:]
        dt=datetime.datetime.strptime(d,'%d/%m/%Y').strftime('%Y-%m-%d')
    
        
        db=sqlite3.connect("MyDatabase")
        cur=db.cursor()
    
        cur.execute("create table if not exists income(amount NUMBER ,source TEXT,date DATE)")
        db.commit()
    
        i=cur.execute("Insert into income(amount,source,date) VALUES(?,?,?)",(a,s,dt))
        #cur.execute("delete from expense")
        db.commit()
        
        '''i=cur.execute("drop table income")
        db.commit()'''
    
    
        if i:
            messagebox.showinfo(root,"Added Successfully")
        else:
            messagebox.showinfo(root,"Try again!")
    
    
    menubar=Menu(root)
    ie=Menu(menubar,tearoff=0)
    ie.add_command(label="Income")
    ie.add_command(label="Expense",command=add_expense)

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

    img=PhotoImage(file="income.png")
    Label(img_frame,image=img).place(x=20,y=100)

    Label(root,text="Amount",font="Helvetica 12 bold",bg="tan").place(x=400,y=150)
    amount_entry=Entry(root,textvariable=amount)
    amount_entry.place(x=500,y=150,height=25,width=200)
    
    Label(root,text="Source",font="Helvetica 12 bold",bg="tan").place(x=400,y=200)
    source_entry=Entry(root,textvariable=source)
    source_entry.place(x=500,y=200,height=25,width=200)
    
    Label(root,text="Date",font="Helvetica 12 bold",bg="tan").place(x=400,y=250)
    date_entry=DateEntry(root,textvariable=date)
    date_entry.place(x=500,y=250,height=25,width=200)
    
    btn=Button(root,text="Add",font="Helvetica 12 bold",width=8,command=income_db)
    btn.place(x=480,y=330)
    
    root.mainloop()
    
#income_fun()