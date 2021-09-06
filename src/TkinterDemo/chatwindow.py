'''
Created on Jun 19, 2019

@author: sipika
'''
from tkinter import *
from nltk.chat.util import Chat, reflections
from TkinterDemo.ChattBBot import pairs

def Go():
    chat = Chat(pairs, reflections)
    user_input = entry.get()
    while user_input != quit:
        response1=chat.converse(user_input)
        Label(root,text=response1).pack()
        user_input = input(">")




root = Tk()
root.geometry("344x400") 
uname=StringVar()
entry = Entry(root,textvariable = uname)
entry.pack(side=BOTTOM)
btn=Button(root,text=">>>",command=Go).pack(side=BOTTOM)
root.mainloop()