## Sentiment Analysis in a Docker Compose Pipeline:
---
### Description:
#### A docker compose pipeline which does the following:

* Collects tweet data from Twitter's API, Tweepy, based on specified keywords

* Loads the data into a MongoDB database

* Carries out sentiment analysis on a sample of the tweets, and stores the transformed data into a Postgres database

---
### Resources

* Root - Docker Compose folder. Create

    * docker_compose.yml - A yaml file describing the containers required for the project to run, as well as their dependenciesm

    * tweet_collector - Docker container for tweet collection

        * Dockerfile - the dockerfile required to build this image
        * get_tweets.py - functionality which creates an OAUTH connection to twitter's api, scrapes data based on input keywords, and stores results in a Mongo db
        * requirements.txt - list of python dependencies
    * etl_job - Docker container

        * Dockerfile -  the dockerfile required to build this image
        * etl.py - functionality which pulls tweets from Mongo, adds Vader Sentiment Poliarity Scores to them, then stores the resulted transformed data in PostgreSQL db
        * requirements.txt - list of python dependencies

---
### How to Use:

* Install the file requirements using the python dependencies listed herein:
* Clone the repository here
* Navigate to the root directory
* In the terminal, run `docker-compose build`, then `docker-compose up`.
