import numpy as np
import pandas as pd
import bs4
from bs4 import BeautifulSoup
import string
import csv
import codecs,json
import requests

base_url = u'https://twitter.com/'
with codecs.open('metoo_tweets.json','r','utf-8') as f:
    tweet = json.load(f)

user = [item['user'] for item in tweet]

user_df = pd.DataFrame(user,columns=['username'])

user_unique=user_df['username'].unique()

location = []
for user in user_unique:
    url = base_url + user
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    loc = soup.find('span',class_='ProfileHeaderCard-locationText')
    if hasattr(loc, 'text') == True:
        location.append(''.join(loc.text.split()))

with open('location.csv','w') as f:
    newfile=csv.writer(f)
    for item in location:
        newfile.writerow([item])	
	
