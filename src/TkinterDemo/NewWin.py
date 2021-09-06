'''
Created on Jun 19, 2019

@author: sipika
'''
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
def infowin():
    messagebox.showinfo("Title", v.get())
    

root = Tk()
root.geometry("300x400")
root.resizable(0, 0)
#img=Image.open("https://entertainment.inquirer.net/files/2019/06/Screen-Shot-2019-06-25-at-12.16.06-PM.png")
#img=img.resize((250,250),Image.ANTIALIAS)
#photo1=ImageTk.PhotoImage(img)
v = StringVar()
btn = Button(root, text="Submit",bg='Red',command=infowin).pack()
Radiobutton(root, text="Python",padx = 20, variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Perl",padx = 20, variable=v, value=2).pack(anchor=W)
root.mainloop()


"""
Tkinter includes several other message boxes:

showerror()
showwarning()
showinfo()"""