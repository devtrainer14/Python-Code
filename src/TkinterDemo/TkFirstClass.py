'''
Created on Jun 17, 2019

@author: sipika
'''
from tkinter import *
from tkinter import messagebox

import sqlite3

global entry
global entry1  

def LoginWin():  
    verr=""    
    def login():
        uname1=entry.get()
        pass1 = entry1.get()
        db = sqlite3.connect("MyDataBase")
        cur = db.cursor()
        cur.execute("Select * from tb_Emp1 where email= ? and password = ? ",(uname1,pass1))
        db.commit()
        result=cur.fetchall()
        if result:
            messagebox.showinfo("Successfully LoggedIn", "Welcome "+uname1)
        else:
            messagebox.showerror("Something Went Wrong", "Please Try Again..!!")
       
        ''' for x in cur:   To display the data from database
    
            print ('{0},{1}, {2}'.format(x[1],x[2],x[3]))'''
    
       
        
        '''chk = checkvar1.get()
        if chk==1:
            verr=uname1'''
      
    def CloseCurrentWin():
        root.destroy()
        from TkinterDemo import TKSecondClass as obj 
        obj.ForgotPass()      
  
    root = Tk()
    #root.minsize(width=334, height=400) # Can't minimize the window in this case
    #root.maxsize(width=334, height=400) # Can't maximize the window in this case
    #root.geometry("344x400")  # Default Window, Can adjust according to need
    root.configure(background="Black")
    
    photo1 = PhotoImage(file='login.png')# supports only gif nd png images 
    Label(root, image=photo1,bg='blue' ).grid(row=0,column=0,columnspan=2)
    uname = StringVar()
    password = StringVar() 
    checkvar1=IntVar()
    # label = Label(root, text="Login Form",bg = 'black', fg='white',font=("Calibiri", 16,'bold'))
    # 
    # label.grid(row=1,column=0,columnspan=2)
    # Label(root, text="",bg='black' ).grid(row=2,column=150)
    # Label(root, text="",bg='black' ).grid(row=3,column=150)
    
    #label.pack()
    label1 = Label(root, text="Enter Uname",width=20)
    label1.grid(row=4,column=0)
    #label1.pack()
    entry = Entry(root,textvariable = uname)
    entry.grid(row=4,column=1)
    Label(root, text="  ",bg='black' ).grid(row=3,column=0)
    label2 = Label(root, text="Enter Password",width=20)
    label2.grid(row=6,column=0)
    entry1=Entry(root,textvariable = password,show="*")
    entry1.grid(row=6,column=1)
    
    #side=LEFT,fill = Y
    # Label(text = " ").pack()
    # Label(text = " ").pack()
    Button(text="Login", bg="black",fg='white' ,
           font = ("Calibiri", 16,'bold'), activeforeground = "green",activebackground = "pink",command = login).grid(row=8,column=0,columnspan=2)
    
    chkbtn1 = Checkbutton(root, text = "Remember Password", variable = checkvar1, 
                          onvalue = 1, offvalue = 0, height = 2, width = 25,bg='black',
                          fg='white',selectcolor='blue')
    chkbtn1.grid(row=7,column=0)
    button1 = Button(root, text="Forgot Password",width=20,fg='white',bg = 'black',command=CloseCurrentWin)
    button1.grid(row=7,column=1)
    root.mainloop()
    
LoginWin()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    