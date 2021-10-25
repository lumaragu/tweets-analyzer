import pandas as pd
from flask import Flask

app = Flask(__name__)

def get_tweet_count():
    df = pd.io.json.read_json('tweets.jsonl', lines=True)
    df = df.loc[:, ['created_at','coordinates']]
    df.dropna(subset = ["coordinates"], inplace=True)
    return len(df.index)

@app.route('/count')
def count():
    count = get_tweet_count()
    return f'There are {count} tweets'

@app.route('/')
def hello():
    return 'Hello World!'