"""connects to Mongo, pulls tweets, adds sentiment analysis, and loads into Postgres"""

import os
import time
import pymongo
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sqlalchemy import create_engine
import logging


#postgres env vars
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')  
HOST = 'postgres_container'
DB = 'postgres' 
PORT = '5432'

# mongodb
client = None
while not client:
    try:
        client = pymongo.MongoClient("mongodb", port=27017)
        db = client.tweets
        collection = db.tweetcollection
    except:
        time.sleep(1)
        continue

# postgres
engine = None
while not engine:
    try:
        URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{HOST}:{PORT}/{DB}"
        engine = create_engine(URI,echo=True)
    except:
        time.sleep(1)
        continue

#create tweet+sentiment table
engine.execute('''CREATE TABLE IF NOT EXISTS tweets (
    tweets TEXT,
    sentiment FLOAT(16)
);
''')

def get_tweets():
    """extract a tweet from Mongo, or return nothing"""
    tweet = list(collection.find())
    if tweet:
        return tweet[0]
    else:
        return ""

def calc_sentiment(tweet):
    """calculate the sentiment of the tweet, or return a neutral score"""
    s  = SentimentIntensityAnalyzer()
    if tweet:
        sentiment = s.polarity_scores(tweet['text'])
        return sentiment['compound']
    else:
        return 0.0

def write_to_postgres(tweet, sentiment):
    """insert a row of tweet + sentiment into Postgres"""
    engine.execute(f"""INSERT INTO tweets VALUES ('{tweet}', {sentiment});""")

while True:
    tweet = get_tweets()
    sent = calc_sentiment(tweet)
    write_to_postgres(tweet, sent)
    time.sleep(5)
