from tkinter import *
from tkinter import ttk
from nltk.chat.util import Chat, reflections
import chatbot.ChattBBot
import threading
import random

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

def send(event):
    global submit_thread
    submit_thread = threading.Thread(target=submit)
    submit_thread.daemon = True
    progressbar.start()
    submit_thread.start()
    sid1.after(20, check_submit_thread)



def check_submit_thread():
    if submit_thread.is_alive():
        sid1.after(20, check_submit_thread)

    else:
        progressbar.stop()

def submit():

    from chatbot import ChattBBot
    chat=Chat(ChattBBot.pairs, reflections)
    user_input = entry1.get()


    while (entry1.get!="quit"):
        entry3.get = entry3.get + 100
        entry2.get=entry3.get + 50


        # To set label,entry or message according to you


        labelr = Label(sid1,text=user_input, font="bold",bg="white",fg="black", wrap=200)
        labelr.place(x=350, y=entry3.get)
        poo = Label(sid1, image=phto)
        poo.place(x=45, y=entry2.get-30 )


        if user_input != quit:
            print(user_input)
            response1 = chat.converse(user_input)
            print(response1)
            labelr=Label(sid1,text=response1,font="helvetica",bg="blanched almond",fg="black",wrap=200)
            labelr.place(x=100,y=entry2.get)

            entry1.delete(0, END)
            if response1==None:
                list1=["Thank you so much", "I really appreciate", "Excuse me.","I’msorry."," What do you think?"," How does that sound?","That sounds great.", "(Oh)never mind.", "I’m learning English.", "I don’t understand.",
                 " Could you repeat that please?"," Could you please talk slower?", "Thank you.That helps a lot."," What does it mean?"," How do you spell that?",
                 " Whatdo you mean?", "Nice to meet you."," Where are you from?", "What do you do?"," How can I help you?"]
                y=random.choice\
                    (list1)

                labelr = Label(sid1, text=y, font="helvetica", bg="blanched almond", fg="black", wrap=200)
                labelr.place(x=100, y=entry2.get)
                entry1.delete(0, END)

        return










sid1.geometry("10000x10000")
sid1.title("login")
progressbar = ttk.Progressbar(sid1, mode='indeterminate')
progressbar.grid(column=1, row=0, sticky=W)


bi=PhotoImage(file="tex.png")
background_label =Label(sid1, image=bi)
background_label.place(x=0, y=0, relwidth=1, relheight=1,)

label1=Label(sid1,text="Hi, I'm Gullu and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ",width=65,bg="white",font="bold")
label1.place(x=450,y=5)

entry1=Entry(sid1,width=20,font="bold",bg="white",fg="black")
entry1.bind("<Return>",send)
entry1.place(x=600,y=500)
entry2=Entry(sid1,width=20,font="bold",bg="black",fg="white")
entry2.get=0
entry3=Entry(sid1,width=20,font="bold",bg="black",fg="white")
entry3.get=0




butt=Button(sid1)
photob=PhotoImage(file="butt.png")
butt.config(image=photob,width="200",height="50",activebackground="black",command=send)
butt.place(x=600,y=550)

phto = PhotoImage(file="h.png")










sid1.mainloop()



