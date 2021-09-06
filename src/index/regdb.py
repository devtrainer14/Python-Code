from tkinter import *
import sqlite3
from tkinter import messagebox



def database(u,e,p):
    root=Tk()
    db=sqlite3.connect("MyDatabase")
    cur=db.cursor()
    
    cur.execute("create table if not exists signup(username TEXT UNIQUE,email TEXT PRIMARY KEY,password TEXT)")
    db.commit()
    
    #password=reg.open().
    
    i=cur.execute("Insert into signup(username,email,password) VALUES(?,?,?)",(u,e,p))
    db.commit()
    
    
    if i:
        messagebox.showinfo(root,"Registered Successfully")
    else:
        messagebox.showinfo(root,"Try again!")
    ''''y=cur.execute("delete from signup")
    
    db.commit()
    #print(cur.total_changes)
    if y:
        print("Successful")
    
    else:
        print("unsuccessful")'''
        
    root.mainloop()

