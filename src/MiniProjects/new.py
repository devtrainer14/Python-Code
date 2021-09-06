from tkinter import *
'''from translate import Translator'''
from tkinter import filedialog
import requests
root = Tk()
root.title("Translator")
root.geometry("580x360")
root.resizable(0, 0)
photo = PhotoImage(file="nw1.png")
w = Label(root, image=photo)
w.pack()


def click():
    root.fileName = filedialog.askopenfilename(filetypes=(("txt", "*.txt"), ("All files", "*.*")))
    print(root.fileName)
    file = open(root.fileName,'r+')
    s = file.read()
   # print(s)
    entry2.insert(INSERT,s)
    file.close()
    file1 = open('myfile.txt','w')
    out_file=entry3.cget('text')
    file1.write(out_file)
    file1.close()


dict1 = {'English': 'en', 'Spanish': 'es', 'Hindi': 'hi', 'French': 'fr', 'German': 'de', 'Punjabi': 'pa'}
checked = StringVar()
checked.set("English")
drop = OptionMenu(root, checked, "English", "Spanish", "Hindi", "French", "German", "Punjabi")
drop.place(x=170, y=80)
checked1 = StringVar()
checked1.set("Hindi")
drop1 = OptionMenu(root, checked1, "English", "Spanish", "Hindi", "French", "German", "Punjabi")
drop1.place(x=335, y=80)


label1 = Label(root, text="Language Converter", font=("arial", 10, "bold"), fg="blue")
label1.place(x=230, y=10)
label2 = Label(root, text="Input", width=15)
label2.place(x=40, y=167)
label3 = Label(root, text="Output", width=15)
label3.place(x=40, y=240)

entry2 = Text(root, width=31, height=3)
entry2.place(x=170, y=150)
'''scroll = Scrollbar(entry2)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=entry2.yview)'''

entry3 = Label(root, width=35, height=3, bg="white", anchor="nw", wraplength=220)
entry3.place(x=170, y=230)


def open1():
    in_lang = checked.get()
    out_lng = checked1.get()
    inn = entry2.get("1.0", 'end-1c')
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}".format(dict1[in_lang],dict1[out_lng],inn)
    try:
        r = requests.get(url)
        r.raise_for_status()
        translation = r.json()[0][0][0]
        entry3.config(text=translation)
    except Exception as e:
        entry3.config(text="Translation Failed")


def speech():
    def GO(self):
        import speech_recognition as sr
        import pyaudio
        import os
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=1)
        with mic as source:
            audio = r.listen(source)
            lng = {'English': 'en-IN', 'Spanish': 'es-SP', 'Hindi': 'hi-IN', 'French': 'fr-FR', 'German': 'de',
                   'Punjabi': 'pa-IN'}
            # ['hi-IN', 'en-GB', 'en-IN', 'fr-FR', 'el-GR', 'es-SP']
            print(checked3.get())
            entry2.insert(INSERT, r.recognize_google(audio, language=lng[checked3.get()]))
            print(r.recognize_google(audio))

    checked3 = StringVar()
    checked3.set("Choose your Language")
    drop = OptionMenu(root, checked3, "English", "Spanish", "Hindi", "French", "German", "Punjabi",command=GO)
    drop.place(x=450,y=165)



def s():

    import pyttsx3

    def my_speak_cloud(message):
        engine = pyttsx3.init()
        engine.say('{}'.format(message))
        engine.runAndWait()
    message=entry3.cget("text")
 #entry3.cget('translation')
    my_speak_cloud(message)

b1 = Button(root, text="Translate", command=open1)
b1.place(x=260, y=290)
b2 = Button(root, text="Translate Whole File", fg="blue", command=click)
b2.place(x=230, y=330)
b3=Button(root,text="Speak",fg="red",command=speech)
b3.place(x=450,y=165)
b4=Button(root,text="speak",fg="red",command=s)
b4.place(x=450,y=240)

root.mainloop()