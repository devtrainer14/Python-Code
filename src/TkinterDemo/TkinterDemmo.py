'''
Created on Jul 5, 2019

@author: sipika
'''
from tkinter import *
from tkinter import messagebox

def Go():
    from TkinterDemo import NewWin
    
    root.dstroy()
    
root = Tk()
root.geometry("400x400")

ent = StringVar()

label = Label(root,text="My First Tkinter Demo", bg = "Green", fg="white")
#label.pack(side=BOTTOM,fill=X)
label.grid(row=1,column=1)
entry = Entry(root,text=ent )
entry.grid(row = 1,column=2)
btn= Button(root,text= "Submit", command=Go)
btn.grid(row=0,column=1)
mainloop()