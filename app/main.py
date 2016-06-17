from app import app

from twitter2rss import Twitter2Rss
import PyRSS2Gen
import config
import json
import utils
import twitter_user_timeline
import twitter_search

@app.route('/search/<term>')
def search(term):
    return twitter_search.get_rss(term)

@app.route('/user_timeline/<screen_name>')
def user_timeline(screen_name):
    return twitter_user_timeline.get_rss(screen_name)


