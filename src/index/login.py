from tkinter import *
from tkinter import messagebox
import sqlite3
import index.home as h

def login_fun(): 
    root=Tk()
    root.configure(background="tan")
    root.geometry("650x450")
    root.title("Expense Tracker")
    
    uname=StringVar()
    pswd=StringVar()
    
    def login_db():
        usrname=uname.get()
        pswrd=pswd.get()
        db=sqlite3.connect("MyDatabase")
        cur=db.cursor()
        cur.execute("select * from signup where username= ? and password= ?",(usrname,pswrd))
        db.commit()
        result=cur.fetchall()
        if result:
            root.destroy()
            h.open()
        else:
            messagebox.showinfo(root,"Invalid username or password!Try again")

    img_frame=Frame(root,width=300,height=300,bg="tan")
    img_frame.pack(side=LEFT,anchor=N)

    login_img=PhotoImage(file="loginicon.png",master=img_frame,width=200,height=200)
    Label(img_frame,image=login_img).place(x=20,y=100)

    Label(root,text="Username",font="Helvetica 12 bold",bg="tan").place(x=270,y=130)
    name_entry=Entry(root,textvariable=uname).place(x=370,y=130,height=25,width=200)
    
    Label(root,text="Password",font="Helvetica 12 bold",bg="tan").place(x=270,y=170)
    pswd_entry=Entry(root,show="*",textvariable=pswd).place(x=370,y=170,height=25,width=200)
    
    btn=Button(root,text="Login",font="Helvetica 12 bold",width=8,command=login_db)
    btn.place(x=400,y=230)
    
    root.mainloop()
    
#login_fun()