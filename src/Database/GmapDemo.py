'''
Created on Jul 1, 2019

@author: sipika
'''
import gmaps
import gmaps.datasets

#configure api

# import gmplot package 
#import gmplot

# GoogleMapPlotter return Map object 
# Pass the center latitude and 
# center longitude 
#gmap1 = gmplot.GoogleMapPlotter(30.3164945, 78.03219179999999, 13 ) 


# Pass the absolute path 
#gmap1.draw( "map11.html" ) 
# Python program to get a google map 
# image of specified location using 
# Google Static Maps API 

# importing required modules 
import requests 

# Enter your api key here 
api_key = "AIzaSyDDGnGXfMSJASUkudAzyIjaOXuCeWxxyN0"

# url variable store url 
url = "https://maps.googleapis.com/maps/api/staticmap?"

# center defines the center of the map, 
# equidistant from all edges of the map. 
center = "Dehradun"

# zoom defines the zoom 
# level of the map 
zoom = 10

# get method of requests module 
# return response object 
r = requests.get(url + "center =" + center + "&zoom =" +
                str(zoom) + "&size = 400x400&key =" +
                            api_key + "sensor = false") 

# wb mode is stand for write binary mode 
f = open('map11.html', 'wb') 

# r.content gives content, 
# in this case gives image 
f.write(r.content) 

# close method of file object 
# save and close the file 
f.close() 


"""
with open('api_key.txt') as f:
    api_key = f.readline()
    f.close
gmaps.configure(api_key="AIzaSyDDGnGXfMSJASUkudAzyIjaOXuCeWxxyN0")
new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)
gmaps.configure(api_key="AIzaSyDDGnGXfMSJASUkudAzyIjaOXuCeWxxyN0") # Fill in with your API key

# Get the dataset
earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
#Get the locations from the data set
locations = earthquake_df[['latitude', 'longitude']]
#Get the magnitude from the data
weights = earthquake_df['magnitude']
#Set up your map
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
print(fig)"""