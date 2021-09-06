from tkinter import *
from tkinter import messagebox

import index.login as l
import index.regdb as r
import sqlite3

root=Tk()
root.configure(background="tan")
root.geometry("800x550")
root.title("Expense Tracker")

name=StringVar()
mail=StringVar()
pswd1=StringVar()
pswd2=StringVar()

def login_win():
    root.destroy()
    l.login_fun()
    
def data():
    
    usrname=name.get()
    emailid=mail.get()
    pswrd1=pswd1.get()
    pswrd2=pswd2.get()
    
    var=0
    if len(usrname)==None or len(usrname)<3 or (usrname).isalnum()!=True:
        messagebox.showerror(root,"Username already taken. Try another username")
        var=var+1
    x= bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", emailid))
    if x==False:
        messagebox.showinfo(root,"Invalid Email! Try again!")
        var=var+1
    if len(pswrd1)==None or (pswrd1).isalnum()!=True or len(pswrd1)<6 :
        messagebox.showinfo(root,"Password length must be six characters")
        var=var+1
    if pswrd1!=pswrd2:
            messagebox.showinfo(root,"Mismatch Password! Try again!")
            var=var+1
    if var==0:
        r.database(usrname,emailid,pswrd1)
        
img_frame=Frame(root,width=350,height=700,bg="tan")
img_frame.pack(side=LEFT)
img1=PhotoImage(file="bg.png",master = img_frame, width = 300, height = 300)

Label(img_frame,image=img1).place(x=20,y=100)

Label(root,text="Username",font="Helvetica 12 bold",bg="tan").place(x=400,y=100)
name_entry=Entry(root,textvar=name)
name_entry.place(x=550,y=100,height=25,width=200)

Label(root,text="Email",font="Helvetica 12 bold",bg="tan").place(x=400,y=150)
email_entry=Entry(root,textvar=mail)
email_entry.place(x=550,y=150,height=25,width=200)

Label(root,text="Password",font="Helvetica 12 bold",bg="tan").place(x=400,y=200)
pswd_entry1=Entry(root,textvar=pswd1,show="*")
pswd_entry1.place(x=550,y=200,height=25,width=200)

Label(root,text="Confirm Password",font="Helvetica 12 bold",bg="tan").place(x=400,y=250)
pswd_entry2=Entry(root,show="*",textvar=pswd2).place(x=550,y=250,height=25,width=200)

btn=Button(root,text="Sign Up",font="Helvetica 12 bold",width=8,command=data)
btn.place(x=530,y=300)

Label(root,text="Already have an account?",bg="tan",font="Helvetica 11 ").place(x=500,y=350)
login_link=Label(root,text="Login",font="Helvetica 12 bold underline",cursor="hand2",width=8,bg="tan")
login_link.place(x=530,y=380)
login_link.bind("<Button-1>",lambda e:login_win())

root.mainloop()