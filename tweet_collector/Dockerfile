FROM python:3.6-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD . /app

CMD ["python", "get_tweets.py"]
