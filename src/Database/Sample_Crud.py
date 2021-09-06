'''
Created on Feb 20, 2019

@author: sipika
'''
import sqlite3
db = sqlite3.connect("MyDataBase")
print(db)
#CRUD Operations 
cur = db.cursor()
print(cur)
#Create Table
cur.execute("Create table if not exists tb_Emp1(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, pass Text,email Text)")
db.commit()


'''cur.execute("Create table if not exists tb_Salary(Sal_id INTEGER PRIMARY KEY AUTOINCREMENT, Salary TEXT,Designation Text, E_id Integer Not Null, FOREIGN KEY (E_id) REFERENCES tb_Emp(id))")
db.commit() 
'''
# Insert Query
'''
#id = int(input("Enter your Employee Id "))
var_name = input("Enter your name")
var_password = input("Enter your Pass")
var_email=input('Enter Email')
#Sal = input("Enter Salary")
#Des = input("Enter Designation")

i = cur.execute("Insert into tb_Emp1(name,pass,email) VALUES(?,?,?)",
                (var_name,var_password,var_email))
#i1 = cur.execute("Insert into tb_Salary(Salary, Designation,E_id) VALUES(?,?,?)",(Sal,Des,id))
db.commit()
if i:
 print("Successfull")
else:
 print("Try Again") 


cur.execute("Select * from tb_Emp1 where id = 1")
for i1 in cur:
    
    print ('{0}, {1}, {2}'.format(i1[1],i1[2],i1[3]))
    
db.commit()
'''
cur.execute("Select * from tb_Emp1 where id = 1")
for i1 in cur:
    
    print ('{0}, {1}, {2}'.format(i1[1],i1[2],i1[3]))
    
db.commit()






