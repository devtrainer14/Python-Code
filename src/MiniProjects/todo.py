from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter.colorchooser import *
import os
from tkinter import filedialog
import datetime
import winsound
import math
file = None
def new():
    new_file()
def bold():
    # TclError exception is raised if not text is selected
    try:
        T.tag_add("BOLD", "sel.first", "sel.last")
    except TclError:
        pass
def italic():
    # TclError exception is raised if not text is selected
    try:
        T.tag_add("ITALIC", "sel.first", "sel.last")
    except TclError:
        pass
def uline():
    # TclError exception is raised if not text is selected
    try:
        T.tag_add("UNDERLINE", "sel.first", "sel.last")
    except TclError:
        pass

def del_one():
    pass
def sorta():
    pass
def sortd():
    pass
def quit():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def About():
    messagebox.showerror("Try again...!!!")

# reminder
def remind():
    root1=Tk()
    root1.title("Set reminder")
    root1.geometry("400x400")
    root1.configure(bg="white")

    def countdown(count):
        seconds = math.floor(count % 60)
        minutes = math.floor((count / 60) % 60)
        hours = math.floor((count / 3600))
        label['text'] = "Hours: " + str(hours) + " Minutes:  " + str(minutes) + " Seconds: " + str(seconds)

        if count >= 0:
            root1.after(1000, countdown, count - 1)
        else:
            for x in range(3):
                winsound.Beep(1000, 1000)
            label['text'] = "Time is up!"

    def updateButton():
        hour, minute, sec = hoursE.get(), minuteE.get(), secondE.get()
        if hour.isdigit() and minute.isdigit() and sec.isdigit():
            time = int(hour) * 3600 + int(minute) * 60 + int(sec)
            countdown(time)

    '''def hide():
        root1.withdraw()
        time_to_sleep = set_time_to_sleep.get()
        time_to_sleep = float(time_to_sleep)
        # print time_to_sleep
        time.sleep(time_to_sleep)
        show()'''
    def selectfile():
        file = filedialog.askopenfilename(initialdir='D:\Demo1\project\notes', title='Please select a directory',defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        v = StringVar(root1, value=file)
        set_file_name = Entry(root1, textvariable=v,width=20)
        set_file_name.place(x=80, y=40)

    label2 = Label(root1, text="Select File", fg="black")
    label2.place(x=10, y=40)
    button1 = Button(root1, text="Choose File", fg="black", bg="white", command=selectfile)
    button1.place(x=80, y=80)
    hoursT = Label(root1, text="Hours:")
    hoursT.place(x=10, y=120)
    hoursE = Entry(root1)
    hoursE.place(x=80, y=120)
    minuteT = Label(root1, text="Minutes:")
    minuteT.place(x=10, y=160)
    minuteE = Entry(root1)
    minuteE.place(x=80, y=160)
    secondT = Label(root1, text="Seconds:")
    secondT.place(x=10, y=200)
    secondE = Entry(root1)
    secondE.place(x=80, y=200)
    label = Label(root1)
    label.place(x=80, y=240)
    button = Button(root1, text="Start Timer", command=updateButton)
    button.place(x=70, y=280)

def save():
    '''file = open("notes.txt","w")
    file.write(T.get("1.0",END))#write from text box and overwrite



    file.close()'''
    file = None
    if  file == None:
        # save as new file
        file = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

        if file == " ":
            file = None
        else:

            # try to save the file
            file1 = open(file, "w")
            file1.write(T.get(1.0, END))
            file1.close()
            # change the window title
            root.title(os.path.basename(file) + " - Notepad")


    else:
        file1 = open(file, "w")
        file1.write(T.get(1.0, END))
        file1.close()
    T.delete('1.0', END)  # add  text to the file
def OpenFile1(name):
    print(name)
    #file = filedialog.askdirectory(parent=root, initialdir='D:\Demo1\project', title='Please select a directory')
    #file1 = filedialog.askopenfilename(initialdir= "D:\Demo1\project\notes", title="select a File", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    #file1 = os.path.basename("D:\Demo1\project\notes")
    """import os
    cwd = os.getcwd()
    print("current working dir",cwd)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("directory name",dir_path)
    
    n = "/Notes/"+name"""
    #file1 = os.path.join(dir_path,n)
    #print("file name",file1)
    file1 = "/eclipse-workspace/DemoPython/src/MiniProjects/Notes/"+name
    if file1 == "":

        # no file to open
        file1 = None
    else:
        # try to open the file
        # set the window title
        root.title(os.path.basename(file1) + " - Notepad")
        T.delete(1.0, END)

        file1= open(file1, "r")

        T.insert(1.0, file1.read())

        file1.close()
def OpenFile():
    file = filedialog.askdirectory(parent=root, initialdir='D:\Demo1\project', title='Please select a directory')
    file1 = filedialog.askopenfilename(initialdir= "D:\Demo1\project\notes", title="select a File", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])

    if file1 == "":

        # no file to open
        file1 = None
    else:
        # try to open the file
        # set the window title
        root.title(os.path.basename(file1) + " - Notepad")
        T.delete(1.0, END)

        file1= open(file1, "r")

        T.insert(1.0, file1.read())

        file1.close()
def add_image():
    pass
    #file = filedialog.askdirectory(parent=root, initialdir='D:\Demo1\project', title='Please select a directory')
    file2 = filedialog.askopenfilename(initialdir='C:\Biren\Downloads',title="select a File", filetypes=[("jpeg", "*.jpg"),('png images', '*.png'),
                   ('gif images', '*.gif'),("All Files", "*.*")])

    if file2 == " ":

        # no file to open
        file2 = None
    else:
        # try to open the file
        # set the window title
        root.title(os.path.basename(file2) + " - Notepad")
        T.delete(1.0, END)

        file = open(file2, "r")

        T.insert(1.0, file2)

        file2.close()

def cut():
        T.event_generate("<<Cut>>")

def copy():
        T.event_generate("<<Copy>>")

def paste():
        T.event_generate("<<Paste>>")
colors = [{'fg':'black', 'bg':'white'}, # color pick list
 {'fg':'yellow', 'bg':'black'}, # first item is default
 {'fg':'white', 'bg':'blue'}, # tailor me as desired
 {'fg':'black', 'bg':'beige'}, # or do PickBg/Fg chooser
 {'fg':'yellow', 'bg':'purple'},
 {'fg':'black', 'bg':'brown'},
 {'fg':'lightgreen', 'bg':'darkgreen'},
 {'fg':'darkblue', 'bg':'orange'},
 {'fg':'orange', 'bg':'darkblue'}]
def Color():
        colors.append(colors[0])  # pick next color in list
        del colors[0]  # move current to end
        T.config(fg=colors[0]['fg'], bg=colors[0]['bg'])

        def onPickFg():
            pickColor('fg')  # added on 10/02/00

        def onPickBg():  # select arbitrary color
            pickColor('bg')  # in standard color dialog

        def pickColor(part):  # this is way too easy
            (triple, hexstr) = askcolor()



root=Tk()
root.title("Sticky Notes")
root.geometry("350x350")
root.configure(bg="white")
root.resizable(True, True)

#title

'''display=Label(root, text="NOTES", bg="white")
display.pack()'''

#text button
T= Text(root, height=15, width=55)
T.pack( side=LEFT, fill=BOTH, expand = YES)
T.config(bg=colors[0]['bg'], fg=colors[0]['fg'])

#menu button
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="RECENT FILES", command=new)
filemenu.add_command(label="OPEN", command=OpenFile)
filemenu.add_command(label="SAVE", command=save)
filemenu.add_command(label="EXIT", command=quit)

#editmenu button
editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)

# To give a feature of cut
editmenu.add_command(label="Cut",  command=cut)

# to give a feature of copy
editmenu.add_command(label="Copy",  command=copy)

# To give a feature of paste
editmenu.add_command(label="Paste",   command=paste)
editmenu.add_command(label="Color", command=Color)
editmenu.add_command(label="SORT (ASC)", command=sorta)
editmenu.add_command(label="SORT(DESC)", command=sortd)
editmenu.add_command(label="DELETE", command=del_one)

#help menu button
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

#buttons
bold=Button(root, text="B", fg="black", bg="white", command=bold )
bold.place(x=40,y=280)

# bold font
bold_font = Font( weight="bold")

# configuring a tag called BOLD
T.tag_configure("BOLD", font=bold_font)

#italic
Italic=Button(root, text="I", fg="black", bg="white", command=italic)
Italic.place(x=80,y=280)
italic_font = Font( slant="italic")
T.tag_configure("ITALIC", font=italic_font)

#underline
underline=Button(root, text="U", fg="black", bg="white", command=uline)
underline.place(x=120,y=280)
underline_font = Font(underline=1)
T.tag_configure("UNDERLINE", font=underline_font)
photo = PhotoImage(file = "gallery.png")
photoimage = photo.subsample(10, 10)
image=Button(root, image = photoimage, command=add_image)
image.place(x=160,y=280)

reminder=Button(root, text="Reminder", fg="black", bg="white", command=remind)
reminder.place(x=200,y=280)


def new_file():
    root2 = Tk()
    root2.title("Sticky Notes")
    root2.geometry("350x350")
    root2.configure(bg="white")
    root2.resizable(True, True)
    def move(event):
        x1 = y.get()
        print(x1)
        OpenFile1(x1)    
    for x in os.listdir('./Notes'):
        y=StringVar()
        y.set(x)
        print("....",x)
        if (x == ' '):

            T = Text(root2, height=15, width=55)
            T.pack(side=LEFT, fill=BOTH, expand=YES)
            T.config(bg=colors[0]['bg'], fg=colors[0]['fg'])
        else:
            w = Message(root2, text=y, width=50)
            w.pack()
            
            w.bind("<Button-1>",move)
            
root.mainloop()
