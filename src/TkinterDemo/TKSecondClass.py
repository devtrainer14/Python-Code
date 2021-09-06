'''
Created on Jun 18, 2019

@author: sipika
'''
from tkinter import *
from PIL import Image
from PIL import ImageTk
import TkinterDemo.NewWin as obj
import sqlite3
from tkinter import messagebox


def ForgotPass():
    def CloseCurrentWin():
        root.destroy()
        obj.NewWin()
    def forget():
        db = sqlite3.connect("MyDataBase")
        cur = db.cursor()
        email1 = entry8.get()
        new_pass=entry9.get()
        print(email1)
        print(new_pass)
        
        sql = "update tb_emp1 set password=? where email=?"
        print(sql)
        i=cur.execute(sql,(new_pass,email1))
        print(i)
        db.commit()
        if i:
            messagebox.showinfo("Title", "Successfully Registered..!!")
        else:
            messagebox.showinfo("Title", "Try Again..!!")
  
    
    root = Tk()
    root.geometry("400x400")
    root.title("Forget password")
    email=StringVar()
    password=StringVar()
    label7 = Label(root, text="Create new password", fg="black")
    label7.place(x=100, y=5)
    label8 = Label(root, text="Enter Email", fg="black", width=20)
    label8.place(x=20, y=40)
    entry8 = Entry(root, text=email, width=30)
    entry8.place(x=100, y=40)
    label9 = Label(root, text=" New Password", fg="black", width=20)
    label9.place(x=20, y=80)
    entry9 = Entry(root, text=password, show="*", width=30)
    entry9.place(x=100, y=80)
    button = Button(root, text="Submit", command=forget, bg="black", fg="white")
    button.place(x=200, y=320)

#pip install pillow