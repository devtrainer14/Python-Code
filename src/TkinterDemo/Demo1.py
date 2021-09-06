'''
Created on May 28, 2019

@author: sipika
'''
from tkinter import *
from tkinter.constants import BOTTOM
from _sqlite3 import Row
root = Tk()
topframe = Frame(root)
topframe.pack(side=TOP)

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

bottomframe = Frame(root,bg="CYAN",)
bottomframe.pack(fill=X)

def onclick():
    root.destroy()
#root.minsize(width=334, height=400) # Can't minimize the window in this case
#root.maxsize(width=334, height=400) # Can't maximize the window in this case
root.geometry("344x400")  # Default Window, Can adjust according to need
label = Label(root, text="My First GUI", bg="cyan")

label.pack(side=LEFT,fill = Y)

# a_button = Button(root, text="A Button") 
# a_button.grid(row=0, column=1, padx=10, pady=10)
# a_button.pack()
# 
# label1 = Label(root, text="Colored Demo", fg="red", bg="cyan")
# label1.pack(side = BOTTOM,fill=X)

btn1 = Button(topframe, text="File", fg= "blue" )
btn1.pack(side=LEFT)
btn2 = Button(topframe, text="Edit", fg= "blue" )
btn2.pack(side=LEFT)
btn3 = Button(topframe, text="View", fg= "blue" )
btn3.pack(side=LEFT)
btn4 = Button(topframe, text="Navigate", fg= "blue" )
btn4.pack(side=LEFT)

text = Text(bottomframe, width=20,height=1,font=2,bg="red")

text.pack()
# Everything will be inside this
root.mainloop()


