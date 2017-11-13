import multiprocessing as mp
from multiprocessing import Pool
import csv
import requests
import string
import pandas as pd
import numpy as np
import geopy
from geopy.geocoders import Nominatim

with open('location.csv','r') as f:
    location = [line.rstrip() for line in f]
#Remove empty lines
location_n = [item for item in location if item != "b''"]
#Get location item in correct string type
location_clean =[]
for item in location_n:
    length = len(item)
    location_clean.append(item[2:(length-1)])
	
#Running parallel batches using multiprocessing
#Create lists of 100 locations for each
location_list = []
for i in np.arange(0,100001,100):
    location = location_clean[i:(i+100)]
    location_list.append(location)

geolocator = Nominatim(timeout=50)

output = mp.Queue()
def work(location,output):
    code=[]
    for item in location:
        location_code = geolocator.geocode(item)
        if hasattr(location_code, 'latitude') == True:
            code.append((location_code.latitude, location_code.longitude))
    output.put(code)

processes = [mp.Process(target=work, args=(location,output)) for location in location_list]

for p in processes:
    p.start()
for p in processes:
    p.join()

results = [output.get() for p in processes]
result_list =[]
for result in results:
    result_list += [item for item in result]
    
with open('geocode.csv','w') as f:
    newfile = csv.writer(f)
    for item in result_list:
        newfile.writerow([item])

