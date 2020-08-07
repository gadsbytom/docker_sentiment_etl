
import time
import pymongo
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sqlalchemy import create_engine

client = pymongo.MongoClient("mongodb")
db = client.tweets
collection = db.tweetcollection

# conn = 'postgres://postgres@postgresdb:5432/postgres'
#
# engine = create_engine(conn)

engine = None
while not engine:
    try:
        engine = create_engine("postgres://postgres:1234@postgresdb:5432")
    except:
        continue


engine.execute('''CREATE TABLE IF NOT EXISTS tweets (
    tweets TEXT,
    sentiment FLOAT(16)
);
''')

def get_tweets():
    tweet = list(collection.find())
    if tweet:
        return tweet[0]
    return ""

def calc_sentiment(tweet):
    s  = SentimentIntensityAnalyzer()
    if tweet:
        sentiment = s.polarity_scores(tweet['text'])
        return sentiment['compound']
    return 0.0

def write_to_postgres(tweet, sentiment):
    engine.execute(f"""INSERT INTO tweets VALUES ('{tweet}', {sentiment});""")

while True:
    tweet = get_tweets()
    sent = calc_sentiment(tweet)
    write_to_postgres(tweet, sent)
    time.sleep(10)
