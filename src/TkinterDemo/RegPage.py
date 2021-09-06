'''
Created on Jun 20, 2019

@author: sipika
'''
from tkinter import *
import sqlite3
from tkinter import messagebox
from TkinterDemo import TkFirstClass as obj


root=Tk()
root.geometry("400x400")
root.title("Registeration Form")
checkvar1=IntVar()
v=IntVar()
def chkbtn_method():
    print(checkvar1.get())
def CloseCurrentWin():
    root.destroy()
    obj.LoginWin()
def register():
    db = sqlite3.connect("MyDataBase")
    cur = db.cursor()
    print(cur)
    #Create Table
    cur.execute("Create table if not exists tb_Emp1(id INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT, name Text,phone Text,address Text,password Text,gender TEXT)")
    db.commit()
    
    email1= entry2.get()
    name1= entry3.get()
    phone1= entry4.get()
    address1 = entry5.get()
    password1 = entry6.get()
    gen1=v.get()
    if gen1==1:
        gen="Male"
    else:
        gen = "Female"
    i = cur.execute("Insert into tb_Emp1(email,name,phone,address,password,gender) VALUES(?,?,?,?,?,?)",(email1,name1,phone1,address1,password1,gen))
    db.commit()
    if i:
        messagebox.showinfo("Title", "Successfully Registered..!!")
    else:
        messagebox.showinfo("Title", "Try Again..!!")


label1=Label(root, text="Registeration Form", fg="black")
label1.place(x=100, y=5)
label2=Label(root, text=" Email Id", fg="black", width=10)
label2.place(x=20,y=40)
entry2=Entry(root, text="enter your email id",width=30)
entry2.place(x=100, y=40)
label3=Label(root, text=" Name", fg="black", width=10)
label3.place(x=20,y=80)
entry3=Entry(root, text="enter your Name",width=30)
entry3.place(x=100, y=80)
label4=Label(root, text=" Phone No", fg="black", width=10)
label4.place(x=20,y=120)
entry4=Entry(root, text="enter your phone no",width=30)
entry4.place(x=100, y=120)
label5=Label(root, text=" Address", fg="black", width=10)
label5.place(x=20,y=160)
entry5=Entry(root, text="enter your address",width=30)
entry5.place(x=100, y=160)
label6=Label(root, text=" Password", fg="black", width=10)
label6.place(x=20,y=200)
entry6=Entry(root, text="enter your password",width=30)
entry6.place(x=100, y=200)
chkbtn=Checkbutton(root, text="Remember Password", variable=checkvar1, onvalue=1 ,offvalue= 0, width=20, command=chkbtn_method, fg="black")
chkbtn.place(x=20, y=240)
label7=Label(root, text="Gender", fg="black", width=10)
label7.place(x=20, y=280)
rdbtn=Radiobutton(root, text="Male", variable=v, value=1, fg="black")
rdbtn.place(x=100, y=280)
rdbtn=Radiobutton(root, text="Female", variable=v,value=2, fg="black")
rdbtn.place(x=160, y=280)
button=Button(root,  text="REGISTER", command=register, bg="black", fg="white")
button.place(x=150, y=320)
button=Button(root,  text="Signin", command=CloseCurrentWin, bg="Grey", fg="white")
button.place(x=350, y=5)
root.mainloop()