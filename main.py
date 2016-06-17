from twitter2rss import Twitter2Rss
from flask import Flask
import PyRSS2Gen
import config
import json
import utils
import twitter_user_timeline
import twitter_search

# Use the system with:
#   gunicorn main:app
# or:
#   export FLASK_APP=main.py
#   flask run

app = Flask(__name__)

@app.route('/search/<term>')
def search(term):
    return twitter_search.get_rss(term)

@app.route('/user_timeline/<screen_name>')
def user_timeline(screen_name):
    return twitter_user_timeline.get_rss(screen_name)


