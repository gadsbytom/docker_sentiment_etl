from tweepy import OAuthHandler, Cursor, API
from tweepy.streaming import StreamListener
import logging
import time
import pymongo
import os


conn = 'mongodb'
client = pymongo.MongoClient(conn)
db = client.tweets
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')


def authenticate():
    """function for twitter authentication"""
    auth = OAuthHandler(API_KEY, API_SECRET)
    return auth


if __name__ == '__main__':
    auth = authenticate()
    api = API(auth)

    while True:

        cursor = Cursor(
        api.user_timeline,
        id = 'legaltech_news',
        tweet_mode = 'extended')

        for status in cursor.items(100):
            time.sleep(1)
            text = status.full_text

            # take extended tweets into account
            if 'extended_tweet' in dir(status):
                text =  status.extended_tweet.full_text
            if 'retweeted_status' in dir(status):
                r = status.retweeted_status
                if 'extended_tweet' in dir(r):
                    text =  r.extended_tweet.full_text

            tweet = {
                'text': text,
                'username': status.user.screen_name,
                'followers_count': status.user.followers_count
            }

            logging.critical(tweet)
            db.collections.legaltech.insert_one(tweet)

