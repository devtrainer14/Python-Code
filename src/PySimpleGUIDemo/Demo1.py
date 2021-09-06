'''
Created on Jun 7, 2019

@author: sipika
'''
import PySimpleGUI as sg
import sqlite3
db = sqlite3.connect("MyDataBase")
print(db)
#CRUD Operations 
cur = db.cursor()
print(cur)
cur.execute("Create table if not exists tb_demo(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, address Text,phone TEXT, pass Text)")
db.commit()

# Very basic window.  Return values as a list

layout = [[sg.Image("\DemoPython\src\PySimpleGUIDemo\cake.jpg")],      
          [sg.Text('Please enter your Name, Address, Phone')],      
          [sg.Text('Name', size=(15, 1)), sg.InputText('name')],      
          [sg.Text('Address', size=(15, 1)), sg.InputText('address')],      
          [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
          [sg.Text('Password', size=(15, 1)), sg.InputText('Password')],      
          [sg.Submit(), sg.Cancel()]      
         ]

window = sg.Window('Simple data entry window').Layout(layout)         
button, values = window.Read()

print(button, values[0], values[1], values[2],values[3])

i = cur.execute("Insert into tb_demo(name,address,phone,pass) VALUES(?,?,?,?)",(values[0],values[1],values[2],values[3]))
db.commit()
if i:
 print("Successfull")
else:
 print("Try Again") 