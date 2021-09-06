'''
Created on Aug 5, 2019

@author: sipika
'''
# Import database module.
from firebase import firebase

# Get a database reference to our blog.
import firebase_admin
from firebase_admin import credentials

if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('service-account.json') 
    default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://chatmessanger-38750.firebaseio.com'})
    
fbconn= firebase.FirebaseApplication('https://chatmessanger-38750.firebaseio.com//')

while True:
    name = input("Enter Your Name")
    email = input("Enter Email")
    Alter_email = input("Enter Any Alternative Email")
    contact = input("Enter Contact")
    
    data_to_upload={
        'Name' : name,
        'Email' : email, 
        'Contact' : contact}
    
    child_to_upload={
        'Name' : name,
        'Email' : email, 
        'Contact' : contact}
    
    result = fbconn.post('/MyInfo/',data_to_upload)
    print(result)
    
  
# To get Data from fireBase
i=0
result = fbconn.get('/MyInfo',None)
print(result)
for id in result:
    i=i+1
    print(i , id)
print("len of data",len(result))


#result = fbconn.get('/MyInfo/-LlVf45j2X4Qm6QBaoTP',None)
#