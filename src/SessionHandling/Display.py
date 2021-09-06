'''
Created on Jul 17, 2019

@author: sipika
'''

class MyClass(object):
    '''
    classdocs
    '''


    
        
    def CardDetails(self):
        i1 = self.cur.execute("Create table if not exists tb_card(card_id INTEGER PRIMARY KEY AUTOINCREMENT, card_holder_name Text,card_no TEXT,cvv Text, expiry Text, cust_id Integer Not Null, FOREIGN KEY (cust_id) REFERENCES tb_Emp1(id))")
        self.db.commit()
        holder_name = input("Enter Card Holder Name")
        card_no = input("Enter 14 digit card nuber")
        cvv = input("Enter CVV number")
        expire_date = input("Enter Expire Date of your card")
        i1 = self.cur.execute("Insert into tb_card(card_holder_name, card_no, cvv, expiry, cust_id) VALUES(?,?,?,?,?)",(holder_name,card_no,cvv,expire_date,self.custid))
        self.db.commit()
        if i1 :
            print("Successfull")
        else:
            print("Try Again")
   
    
    
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    def __init__(self, custid, name, email,db):
        
        self.db = db
        self.custid=custid
        self.cur = db.cursor()
        print("Welcome "+name)
        print("Email :"+email)
        MyClass.CardDetails(self)
        
        
        
        
        
        
        
        
        