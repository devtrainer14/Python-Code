'''
Created on May 31, 2019

@author: sipika
'''
from tkinter import *
from tkinter.constants import BOTTOM


def login():
    print("login")
    root1 = Toplevel(root)
    root1.title("Login")
    root1.geometry("344x400")
    uname = StringVar()
    upass = StringVar()
   
    Label(root1,text = "Enter Username ").pack()
    Entry(root1,textvariable = uname).pack()
    Label(root1,text = "Enter Password").pack()
    Entry(root1,textvariable = upass).pack() 
    Label(root1,text = " ").pack()
    frame = Frame(root1,bg="CYAN")
    
    Button(root1,text="Submit", bg="White", height=1, width=10, font = ("Calibiri", 12)).grid(row=0,column=150,sticky=W)
    Button(frame,text="Cancel", bg="White", height= 1, width=10, font = ("Calibiri", 12)).pack(side = LEFT,expand=YES)
    frame.pack(fill=BOTH)



def Reg():
    print("Register")


root = Tk()
root.geometry("344x400")
root.title("Notes")
Label(text="MY APP", bg="Black",fg="White", height=2, width=300,font = ("Calibiri", 12)).pack()
Label(text = " ").pack()
Button(text="Login", bg="CYAN", height=2, width=50, font = ("Calibiri", 12), command = login).pack()
Label(text = " ").pack()
Button(text="Register", bg="CYAN", height=2, width=50,font = ("Calibiri", 12), command = Reg ).pack()

root.mainloop()

