import pandas as pd
import operator
import string
import csv
from collections import Counter
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk import bigrams
import codecs,json

punctuation = list(string.punctuation)
letter = list(string.ascii_lowercase)
stop = stopwords.words('english') + punctuation + ['&amp;','rt', 'via','the','"i','we','0',"metoo","???"] + letter


with codecs.open('metoo_tweets.json','r','utf-8') as f:
    tweet = json.load(f)
text = [item['text'] for item in tweet]
with open('metootweets_text.csv','w') as f:
    new = csv.writer(f)
    for item in text:
        new.writerow([item])

with open('metootweets_text.csv','r') as f:
    text = [line.rstrip() for line in f]

count_word = Counter()
count_bigram = Counter()
count_hashtag = Counter()
count_at = Counter()

for item in text:
    item_l = str.lower(item) #convert to lower case
    word = [term for term in item_l.split() 
            if (term not in stop) and ('#' not in term) and ('\\'not in term)]
    bigram = bigrams(word)
    count_word.update(word)
    count_bigram.update(bigram)
    hashtag = [term for term in item_l.split() 
               if ('#'in term) and ('metoo' not in term)]
    count_hashtag.update( hashtag)
    at = [term for term in item_l.split()
          if ('@'in term) and ('metoo' not in term)]
    count_at.update(at)

word = count_word.most_common(1000)
word_table = pd.DataFrame()
word_table['name'] = [item[0] for item in word]
word_table['frequency'] = [item[1] for item in word]
word_table.to_csv('word_table.csv', sep='\t')

hashtag = count_hashtag.most_common(1000)
hashtag_table = pd.DataFrame()
hashtag_table['name'] = [item[0] for item in hashtag]
hashtag_table['frequency'] = [item[1] for item in hashtag]
hashtag_table.to_csv('hashtag_table.csv', sep='\t')

at_people = count_at.most_common(1000)
at_table =  pd.DataFrame()
at_table['name'] = [item[0] for item in at_people]
at_table['frequency'] = [item[1] for item in at_people]
at_table.to_csv('at_table.csv', sep='\t')

bigram = count_bigram.most_common(1000)
bigram_table = pd.DataFrame()
bigram_table['name'] = [item[0] for item in bigram]
bigram_table['frequency']=[item[1] for item in bigram]
bigram_table.to_csv('bigram_table.csv', sep='\t')

##Generating wordcloud
import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
%matplotlib inline

#Preclean data for word cloud and convert to appropriate dictionary for word cloud
#Convert top 100 words to dictionary with each key is each word and value is frequencyword_table_top = word_table.head(100)
word_dic = word_table_top.set_index('name')['frequency'].to_dict()
del word_dic["it's"],word_dic['de'],word_dic['que'],word_dic['la'],word_dic['don\xe2\x80\x99t'],word_dic['2'],word_dic['\xe2\x80\xa6'],word_dic['\xe2\x80\xa6"'],word_dic['it\xe2\x80\x99s'],word_dic['i\xe2\x80\x99m']

item=[]
for i in range(3,1000):
    if "yotam" in hashtag_table['name'][i]:
        hashtag_table[hashtag_table['name']=='#yotambien']['frequency'] += hashtag_table['frequency'][i]
        item.append(i)
    if "balancetonporc" in hashtag_table['name'][i]:
        hashtag_table[hashtag_table['name']=='#balancetonporc']['frequency'] += hashtag_table['frequency'][i]
        item.append(i)
hashtag_table.drop(hashtag_table.index[item],inplace=True)

hashtag_table_top = hashtag_table.head(100)
hash_dic = hashtag_table_top.set_index('name')['frequency'].to_dict()
del  hash_dic['#']
hash_dic['#RamBhajanKaisiDiwali']= hash_dic.pop('"#\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae\xe0\xa4\xad\xe0\xa4\x9c\xe0\xa4\xa8_\xe0\xa4\xac\xe0\xa4\xbf\xe0\xa4\xa8_\xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x80\xe0\xa4\xa6\xe0\xa5\x80\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xb2\xe0\xa5\x80')
hash_dic['#Deepawali'] = hash_dic.pop('#\xe0\xa4\xa6\xe0\xa5\x80\xe0\xa4\xaa\xe0\xa4\xbe\xe0\xa4\xb5\xe0\xa4\xb2\xe0\xa5\x80')

hash_dic['#RamBhajanKaisiDiwali'] = hash_dic['#RamBhajanKaisiDiwali']+hash_dic['#\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae\xe0\xa4\xad\xe0\xa4\x9c\xe0\xa4\xa8_\xe0\xa4\xac\xe0\xa4\xbf\xe0\xa4\xa8_\xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x80\xe0\xa4\xa6\xe0\xa5\x80\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xb2\xe0\xa5\x80']
del hash_dic['#ericnam'], hash_dic['#\xec\x97\x90\xeb\xa6\xad\xeb\x82\xa8'], hash_dic['#\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae\xe0\xa4\xad\xe0\xa4\x9c\xe0\xa4\xa8_\xe0\xa4\xac\xe0\xa4\xbf\xe0\xa4\xa8_\xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x80\xe0\xa4\xa6\xe0\xa5\x80\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xb2\xe0\xa5\x80']
hash_dic['shiori']=hash_dic.pop('#\xe8\xa9\xa9\xe7\xb9\x94') 

at_table = pd.read_csv('at_table.csv', sep='\t')
at_table_top = at_table.head(100)
at_dic = at_table_top.set_index('name')['frequency'].to_dict()
del  at_dic['@']

#Plot word clouds
wc = WordCloud(width=4000,height=4000, relative_scaling=0.5,normalize_plurals=True,background_color='black').generate_from_frequencies(word_dic)
wc1 = WordCloud(width=4000,height=4000,relative_scaling=0.5,normalize_plurals=True,background_color='black').generate_from_frequencies(hash_dic)
wc2 = WordCloud(width=4000,height=4000,relative_scaling=0.5,normalize_plurals=True,background_color='black').generate_from_frequencies(at_dic)
fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(50,50))
ax1.imshow(wc,cmap='rainbow')
ax2.imshow(wc1,cmap='plasma')
ax3.imshow(wc2,cmap='viridis')
ax1.axis("off")
ax2.axis("off")
ax3.axis("off")
plt.savefig('Wordcloud.png',dpi=100)

