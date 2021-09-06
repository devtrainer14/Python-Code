'''
Created on Jul 18, 2019

@author: sipika
'''
from urllib.request import urlopen
import urllib.request, json 
from json.decoder import JSONObject
def get_json():
    a=1
    #https://newsapi.org/v2/everything?q=Entertainment&from=2019-06-25&sortBy=publishedAt&apiKey=285a5f0669d7462fb2246e2a3ccdabf2"
    with urllib.request.urlopen("http://dataservice.accuweather.com/currentconditions/v1/202350.json?apikey=0MtkE3VBo50hwOXZr1UKLeJyqshPq31f") as url:
        document = json.loads(url.read().decode())
        
   # source_path = Path("https://jsonplaceholder.typicode.com/todos")
    
        data = document[0]
        wtext = data['WeatherText']
        temp = data['Temperature']
        metric = temp['Metric']
        value  = metric['Value']
        unit = metric['Unit']
        
        print(wtext)
        print(value,unit)
get_json()