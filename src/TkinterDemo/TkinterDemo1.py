'''
Created on Jul 24, 2019

@author: sipika
'''
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("500x400")

def GO():
    root.destroy()
    messagebox.showinfo("Title", name.get())
    #from TkinterDemo.TkFirstClass import LoginWin
    #LoginWin()

label = Label(root, text = "This is my first app", bg="Black", fg= "white")
#label.pack(side='right')
label.grid(row = 0, column=0, columnspan=2)
name = StringVar()
label = Label(root, text = "Enter Your Name", bg="Black", fg= "white")
label.grid(row = 2, column=0)

entry = Entry(root, text = name , bg="Black", fg= "white")
#label.pack(side='right')
entry.grid(row = 2, column=2)

btn = Button(root,text = 'OK',command=GO, fg = 'black' )
btn.grid(row = 4, column=1)
mainloop() 