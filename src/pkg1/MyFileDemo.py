'''
Created on Feb 20, 2019

@author: sipika
'''
import webbrowser

message = """<html>
                <body>
                <div>
                    <h1>Hi, Welcome to Python</h1>
                   <p>This is my File</p>
                   
                </div>
                </body>
            </html>"""
obj=open("abcd.html","w")  

obj.write(message)  

obj.close()
webbrowser.open_new_tab('abcd.html')

obj = open("abcd.html","r")
s=obj.read()
print(s)
obj.close()
