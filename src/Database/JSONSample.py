'''
Created on Jun 25, 2019

@author: sipika
'''
from json.decoder import JSONObject
import requests
import urllib.request, json   
from tkinter import *
import base64
from urllib.request import urlopen
from tkinter.tix import *

root = Tk()
root.geometry("500x500")
"""scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)
mylist1 = Listbox(root, yscrollcommand=scrollbar.set)"""

frame = Frame(width="500",height="500")
frame.pack()
swin = ScrolledWindow(frame, width=500, height=500)
swin.pack()
win = swin.window


#canv = Canvas(root, width=80, height=80, bg='white')
#canv.grid(row=2, column=3)
def get_json():
    a=1
    #https://newsapi.org/v2/everything?q=Entertainment&from=2019-06-25&sortBy=publishedAt&apiKey=285a5f0669d7462fb2246e2a3ccdabf2"
    with urllib.request.urlopen("http://dataservice.accuweather.com/currentconditions/v1/202350.json?apikey=0MtkE3VBo50hwOXZr1UKLeJyqshPq31f") as url:
        document = json.loads(url.read().decode())
    
   # source_path = Path("https://jsonplaceholder.typicode.com/todos")
    
        data = document[0]
        wtext = data['WeatherText']
        etext = data['EpochTime']
        print(wtext,etext)
        w = Message(win, text=wtext, width=500, fg="Red")
        w.pack()
    
    """for x1 in article:
       
        author = x1['author']
        
        title = x1['title']
        print(title)
        description = x1['description']
        url = x1['url']
        urlToImage = x1['urlToImage']
        #image_byt = urlopen(urlToImage).read()
        #img = base64.encodestring(image_byt)
        publishedAt = x1['publishedAt']
        content = x1['content']
        
        w = Message(win, text=title, width=500, fg="Red")
        w.pack()
        w1 = Message(win, text=author, width=500,fg="blue")
        w1.pack()
        w2 = Message(win, text=description, width=500,fg="Orange")
        w2.pack()
        #Label(root,text=title).place(x=10,y=a)
        #mylist.insert(END, str(a)+".  "+title+"/n" )
        #mylist1.insert(END,str(a)+".  "+title+"\n"+description+"\n" )
        #photo = PhotoImage(data=img)
    
        #canv.create_image(20,20, anchor=NW, image=photo)
       
    a+=1
    mylist1.pack(fill=BOTH)
    mylist.pack(fill=BOTH)
    scrollbar.config(comma nd=mylist1.yview)
    scrollbar.config(command=mylist.yview)""" 
get_json()
mainloop()