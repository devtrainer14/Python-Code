'''
Created on Mar 5, 2020

@author: sipika
'''
from json.decoder import JSONObject
import requests
import urllib.request, json  
from urllib.request import urlopen

def get_json():

    #https://newsapi.org/v2/everything?q=Entertainment&from=2019-06-25&sortBy=publishedAt&apiKey=285a5f0669d7462fb2246e2a3ccdabf2"
    with urllib.request.urlopen("https://cat-fact.herokuapp.com/facts/") as url:
        document = json.loads(url.read().decode())
       
   # source_path = Path("https://jsonplaceholder.typicode.com/todos")
        data = document['all']
        print("Data : ",data)
        for x in  data:
            id = x['_id']
            text = x['text']
            type = x['type']
            use = x['user']
            name = use['name']
            f = name['first']
            l = name['last']
            
            print("--- ",text)
            print("## ", type)
            print("== ",f," ",l)
       
           
            
           
    
get_json()