import tkinter as tk
import random

# --- data ---

Quotes= ["""Never express yourself more clearly than you can think. Neils Bohrs""",
""""If you can't get rid of the skeleton in your closet,   you'd best teach it to dance.- George Bernard Shaw (1856-1950)""",
"""When you are content to be simply yourself and don't compare or compete, everybody will respect you.~ Lao-Tzu """]

# --- functions ---

def key(event):
    root.destroy()

def change_text():

    # change text 
    c.itemconfig(t, text=random.choice(Quotes))

    # repeat after 2000ms (2s)
    root.after(2000, change_text)
    
# --- main ---

root = tk.Tk()
#root.attributes('-fullscreen', True)

root.bind("<Key>",key)
root.geometry("344x400")

c = tk.Canvas(root, bg='black')
c.pack(expand=1, fill=tk.BOTH)
t = c.create_text(50, 50,
                  anchor=tk.CENTER,
                  font=("Calibri",15,"italic"), 
                  fill='red',
                  width=root.winfo_screenwidth()*0.8,
                  text='' # empty string
                  )

# set first text
change_text()


root.mainloop()