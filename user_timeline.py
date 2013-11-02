#!/usr/bin/python

from twitter2rss import Twitter2Rss
from twython import Twython
import config
import utils

# Copyright Carles Pina i Estany <carles@pina.cat> 2013
#
# This file is part of twitter2rss
#
# twitter2rss is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# twitter2rss is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with twitter2rss.  If not, see <http://www.gnu.org/licenses/>.

def get_user_timeline(screen_name):
    """Returns the feed for this screen_name."""
    twython = Twython(config.consumer_key, config.consumer_secret,
        config.access_token, config.access_token_secret)

    user_timeline = twython.get_user_timeline(screen_name=screen_name)

    return user_timeline

def get_rss(user_timeline, screen_name):
    rss_params = {}

    rss_params['title'] = 'Twitter / %s' % (screen_name)
    rss_params['link'] = 'https://www.twitter.com/%s' % (screen_name)
    rss_params['author'] = screen_name

    twitter2rss = Twitter2Rss(rss_params)

    for tweet in user_timeline:
        twitter2rss.add_tweet_from_twython(tweet)

    return twitter2rss.rss()

def index(req):
    """Process the CGI request."""
    screen_name = req.form['screen_name'].value

    user_time_line = get_user_timeline(screen_name)

    utils.write_to_req(req, get_rss, user_time_line, screen_name)

if __name__ == '__main__':
    utils.check_configuration()
    # Poor's man test
    search = get_user_timeline('rvidal')
    print get_rss(search, 'rvidal')
