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

* Ensure Docker is installed - `https://docs.docker.com/get-docker/`
* Get Twitter Developer API creds, see [here](https://jannah.helpscoutdocs.com/article/161-register-twitter-app) for a guide on how - `https://developer.twitter.com`
* Setup the necessary env variables, see [here](https://medium.com/@himanshuagarwal1395/setting-up-environment-variables-in-macos-sierra-f5978369b255) for how to in macOS - `API_KEY, API_SECRET, POSTGRES_USER, POSTGRES_PASSWORD`
* Clone the repository - `git clone https://github.com/gadsbytom/docker_sentiment_etl.git`
* Install the file requirements - `pip install -r requirements.txt`
* Ensure env variables for 
* Navigate to the root directory
* In the terminal, run `docker-compose build`, then `docker-compose up`.