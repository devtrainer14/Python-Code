'''
Created on Jul 17, 2019

@author: sipika
'''
import urllib.request
import requests

import sqlite3
from SessionHandling import Display

sname = ""
semail=""

def display(n,e):
    print("Welcome "+n)
    print("Email :"+e)
    
db = sqlite3.connect("MyDataBase")
print(db)
#CRUD Operations 
cur = db.cursor()
print(cur)
var_name = input("Enter Username")
var_pass = input("Enter Password")

cur.execute("Select * from tb_Emp1 where name = ? and pass=?",(var_name,var_pass))
i = cur.fetchall()
for x in i:
    sid=x[0]
    sname = x[1]
    semail = x[3]
db.commit()
Display.MyClass(sid,sname,semail,db)
    


    
    

    