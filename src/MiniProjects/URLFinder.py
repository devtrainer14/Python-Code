'''
Created on Jun 28, 2019

@author: sipika
'''
import re
 
with open("url_find.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print(urls)