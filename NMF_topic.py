import codecs,json,csv
import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk import bigrams
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF

punctuation = list(string.punctuation)
letter = list(string.ascii_lowercase)
stop = stopwords.words('english') + punctuation + ['&amp;','rt', 'via','the','"i','we','0',"metoo","???",'2'] + letter

with codecs.open('metoo_tweets.json','r') as f:
    tweet=json.load(f)
tweet_text = [item['text'] for item in tweet]


def tweet_clean(tweet):
    tweet_remove = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    return " ".join([word for word in tweet_remove.lower().split() if word not in stop])

text = [tweet_clean(item['text']) for item in tweet]

no_features = 1000

tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(text)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()

no_topics = 5
nmf = NMF(n_components=no_topics, random_state=1, init='nndsvd').fit(tfidf)
nmf_W = nmf.transform(tfidf)

no_top_words = 10
no_top_tweet = 5

top_topic=[]

for topic_idx, topic in enumerate(nmf.components_):
    top_topic.append(" ".join([tfidf_feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))
    top_doc_indices = np.argsort(nmf_W[:,topic_idx])[::-1][0:no_top_tweet]
    for doc_index in top_doc_indices:
        top_topic.append(tweet_text[doc_index])

with open('NMF_topic.csv','w') as f:
    newfile = csv.writer(f)
    for item in top_topic:
        newfile.writerow([item])


