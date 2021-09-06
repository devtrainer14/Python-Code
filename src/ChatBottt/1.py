from tkinter import *
from chatbot import ChattBBot

sid=Tk()
sid.geometry("10000x10000")
bi=PhotoImage(file="bg.png")
labelb=Label(sid,image=bi)
labelb.place(x=0, y=0, relwidth=1, relheight=1,)
go=Button(sid)
photo=PhotoImage(file="go.png")
go.config(image=photo,width="200",height="100",activebackground="black",command=sid.destroy)


go.place(x=600,y=550)
sid.mainloop()
sid1=Tk()
def send():
    chat=Chat(pairs, reflections)
    user_input = input(">")
    while user_input != quit:
        response1 = chat.converse(user_input)
        print(response1)
        user_input = input(">")

    return


sid1.geometry("10000x10000")
sid1.title("login")


bi=PhotoImage(file="tex.png")
background_label =Label(sid1, image=bi)
background_label.place(x=0, y=0, relwidth=1, relheight=1,)

label1=Label(sid1,text="Whats your name",width=20,bg="white",font="bold")
label1.place(x=5,y=5)

entry1=Entry(sid1,width=20,font="bold",bg="black",fg="white")
entry1.place(x=150,y=50)


butt=Button(sid1)
photob=PhotoImage(file="butt.png")
butt.config(image=photob,width="200",height="50",activebackground="black",command=send)


butt.place(x=600,y=550)


sid1.mainloop()

