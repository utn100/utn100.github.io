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

