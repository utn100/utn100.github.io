import string
import csv
import codecs,json
import datetime
import pandas as pd
import numpy as np


with codecs.open('metoo_tweets.json','r','utf-8') as f:
    tweet = json.load(f)

at=[]
hashtag=[]
month=[]
day=[]
retweet = []
like=[]
reply=[]

for item in tweet:
    hashtag.append(','.join([word for word in item['text'].split() if '#' in word]))
    month.append(pd.to_datetime(item['timestamp']).month)
    day.append(pd.to_datetime(item['timestamp']).day)
    at.append(','.join([word for word in item['text'].split() if '@' in word]))
    retweet.append(item['retweets'])
    like.append(item['likes'])
    reply.append(item['replies'])

df = pd.DataFrame({'month':month,'day':day,'hashtag':hashtag,'tagged_ID':at,'retweets':retweet,'likes':like,'replies':reply})

df['date'] = df.apply(lambda df:str(df['month']) + "/" +str(df['day']),axis=1)
df.drop('day',axis=1,inplace=True)
df.drop('month',axis=1,inplace=True)
df.to_csv('date_table.csv',sep='\t')    
   
