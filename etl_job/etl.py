
import time
import pymongo
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sqlalchemy import create_engine

client = pymongo.MongoClient("mongodb")
db = client.tweets
collection = db.tweetcollection

conn = 'postgres://postgres@postgresdb:5432/postgres'

engine = create_engine(conn4)
engine.execute('''CREATE TABLE IF NOT EXISTS tweets (
    tweets TEXT,
    sentiment FLOAT(16)
);
''')

def get_tweets():
    tweets = list(collection.find())
    if tweet:
        return tweets[0]
    return ""

def calc_sentiment(tweet):
    s  = SentimentIntensityAnalyzer()
    if tweet:
        sentiment = s.polarity_scores(tweet['text'])
        return sentiment['compound']
    return 0.0

def write_to_postgres(tweet, sentiment):
    engine.execute(f"""INSERT INTO tweets VALUES ('{tweet["text"]}', {sentiment});""")

while True:
    tweet = get_tweets()
    sent = calc_sentiment(tweet)
    write_to_postgres(tweet, sent)
    time.sleep(10)
