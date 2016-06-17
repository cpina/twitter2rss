#!/usr/bin/python

from twitter2rss import Twitter2Rss
from twython import Twython
import config
import json
import utils

# Copyright Carles Pina i Estany <carles@pina.cat> 2013, 2016
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

def get_search(term):
    """Searches for term and returns the result from Twython."""
    twython = Twython(config.consumer_key, config.consumer_secret,
        config.access_token, config.access_token_secret)

    search = twython.search(q=term)

    return search

def get_rss(term):
    rss_config = {}

    rss_config['title'] = 'Twitter Search for %s' % (term)
    rss_config['link'] = ''
    rss_config['description'] = 'Proxy between Twitter API and RSS'

    twitter2rss = Twitter2Rss(rss_config)

    for tweet in get_search(term)['statuses']:
        twitter2rss.add_tweet_from_twython(tweet)

    return twitter2rss.get_rss()

if __name__ == '__main__':
    utils.check_configuration()

    # Poor man test
    print(get_rss('mendeley'))
