# import plotly.express as px 
# import plotly.graph_objects as go

import dash 
# import dash_core_components as dcc
import dash_html_components as html
# from dash.dependencies import Input, Output

import time
from sqlalchemy import create_engine
import os
import logging


#postgres env vars
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')  
HOST = 'postgres_container'
DB = 'postgres' 
PORT = '5432'


#data - postgres data containing tweets and sentiments
#postgres
engine = None
while not engine:
    try:
        URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{HOST}:{PORT}/{DB}"
        engine = create_engine(URI,echo=True)
    except:
        time.sleep(1)
        continue

query = 'select * from tweets limit 5';
results = engine.execute(query)
logging.critical([x for x in results])

#Dash
#instantiating the app
app = dash.Dash(__name__)

#languages used in the tweets
#sentiment of the tweets
#wordcloud per language
#bonus - no. of mentions over time, geography of tweet origins


# app layout
app.layout = html.Div(children=[
    html.H1("NLP Analysis of Twitter history", style={'text-align': 'center'})
])



if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)

