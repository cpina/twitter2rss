import datetime
import PyRSS2Gen
import json

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

class Twitter2Rss():
    """Class that reads from Twitter and converts to RSS.
       The users needs to call Twitter2Rss.add_tweet_from_twython()
    """
    def __init__(self, rss_config):
        """ Saves the rss_config to be used on the generating step. """
        self._rss_config = rss_config
        self._rss_items = []

    def add_tweet_from_twython(self, twython):
        """Converts a Twython tweet and converts to the RSS format."""
        text = twython['text']
        screen_name = twython['user']['screen_name']
        created_at = datetime.datetime.strptime(
            twython['created_at'],'%a %b %d %H:%M:%S +0000 %Y').timetuple()
        id_str = twython['id_str']
        url = 'https://twitter.com/%s/status/%s' % (screen_name, id_str)

        tweet = {}

        tweet['text'] = text
        tweet['link'] = url
        tweet['url'] = url
        tweet['guid'] = str(id_str)
        tweet['author'] = twython['user']['screen_name']
        tweet['pubDate'] = twython['created_at']

        self._add_tweet(tweet)

    def get_rss(self):
        """Returns the RSS."""

        rss = PyRSS2Gen.RSS2(
            title = self._rss_config.get('title', 'Twitter RSS'),
            link = self._rss_config.get('link', 'http://www.twitter.com'),
            description = self._rss_config.get('description', 'Proxy between Twitter API and RSS'),
            lastBuildDate = datetime.datetime.now(),
            items = self._rss_items
        )

        return rss.to_xml('utf-8')

    def _add_tweet(self, tweet):
        """Adds a Tweet. into the feed."""

        text = tweet.get('text', 'Twitter without text')

        item = PyRSS2Gen.RSSItem(
            title = text,
            link = tweet.get('url', 'Twitter without link'),
            description = text,
            guid = PyRSS2Gen.Guid(tweet.get('guid', 'Some guid')),
            pubDate = tweet.get('pubDate', None),
            author = tweet.get('author', None)
        )

        self._rss_items.append(item)
