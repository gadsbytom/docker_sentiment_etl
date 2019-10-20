import time
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.tweets
collection = db.tweetcollection
