'''
Created on Jun 25, 2019

@author: sipika
'''
from tkinter import *
import time


root = Tk()

def close():
   root.destroy()

def show():
   root.deiconify()
   button.config(text = 'Close', command = close)
   root.after(1000, hide)

def hide():

   root.withdraw()
   time_to_sleep = set_time_to_sleep.get()
   time_to_sleep = float(time_to_sleep)
   #print time_to_sleep
   time.sleep(time_to_sleep)
   show()



set_time_to_sleep = Entry(root)
set_time_to_sleep.pack(side=LEFT)
button = Button(text = 'Set Time', command = hide)
button.pack()

root.mainloop()