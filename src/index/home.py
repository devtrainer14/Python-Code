from tkinter import *
from PIL import Image
from PIL import ImageTk
import index.income as i
import index.expense as e
import index.weekly as w
import index.monthly as m
import index.yearly as y
import index.alldata as a

def open():

    root=Tk()
    root.title("Expense and Income Recorder")
    root.geometry("700x500")
    root.resizable(0,0)
#root.configure(background="tan")
    imag=Image.open("home.png")
    background_image=ImageTk.PhotoImage(imag)
    background_label =Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def add_income():
        root.destroy()
        i.income_fun()
    
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
    
    menubar=Menu(root)
    ie=Menu(menubar,tearoff=0)
    ie.add_command(label="Income",command=add_income)
    ie.add_command(label="Expense",command=add_expense)

    menubar.add_cascade(label="Income/Expense",menu=ie)
    
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

    root.mainloop()


#open()