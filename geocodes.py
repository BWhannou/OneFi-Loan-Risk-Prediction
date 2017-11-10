import googlemaps
import pandas as pd 
import numpy as np

gmaps = googlemaps.Client(key='AIzaSyAFo6Eek7kBHuR7AuaRRVOe6Jr0B9j8hMk')

train_demographics = pd.read_csv('traindemographics.csv.xls')
test_demographics = pd.read_csv('testdemographics.csv.xls')
frames = [train_demographics,test_demographics]
demographics = pd.concat(frames)

latitude = demographics['latitude_gps']
longitude = demographics ['longitude_gps']

lg = pd.Series()
c = 0 

for i,j in zip(latitude,longitude):
    lg[i] = gmaps.reverse_geocode((i, j))[0]['address_components'][5]
    c+=1


lg.to_csv('local_government.csv', header=['customerid','lg'],index=False)