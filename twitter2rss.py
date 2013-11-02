
import datetime
import feedformatter
import json

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

class Twitter2Rss():
    """Class that reads from Twitter and converts to RSS.
       The users needs to call Twitter2Rss.add_tweet_from_twython()
    """
    def __init__(self, rss_config):
        """Creates the new object based on rss_config."""
        self.feed = feedformatter.Feed()

        self.feed.feed['title'] = rss_config.get('title', 'Twitter RSS')
        self.feed.feed['link'] = rss_config.get('link',
            'http://www.twitter.com')

        self.feed.feed['author'] = rss_config.get('author', 'Twitter feed')
        self.feed.feed['description'] = 'Proxy between Twitter API and RSS'

    def add_tweet_from_twython(self, twython):
        """Converts a Twython tweet and converts to the RSS format."""
        text = twython['text'].encode('ascii', 'ignore')
        screen_name = twython['user']['screen_name']
        created_at = datetime.datetime.strptime(
            twython['created_at'],'%a %b %d %H:%M:%S +0000 %Y').timetuple()
        id_str = twython['id_str']
        url = 'https://twitter.com/%s/status/%s' % (screen_name, id_str)

        tweet = {}

        tweet['text'] = text
        tweet['link'] = url
        tweet['url'] = url
        tweet['pubDate'] = created_at
        tweet['guid'] = str(id_str)
        tweet['author'] = twython['user']['screen_name']

        self._add_tweet(tweet)

    def rss(self):
        """Returns the RSS."""
        return self.feed.format_rss2_string(pretty=True)

    def _add_tweet(self, tweet):
        """Adds a Tweet. into the feed."""
        feed_item = {}

        text = tweet.get('text','Twitter without text').\
            encode('ascii', 'ignore')

        feed_item['title'] = text
        feed_item['description'] = text
        feed_item['link'] = tweet.get('url', 'Some link')
        feed_item['pubDate'] = tweet.get('pubDate', None)
        feed_item['guid'] = tweet.get('guid', 'Some guid')
        feed_item['author'] = tweet.get('author', 'The Author2')

        self.feed.items.append(feed_item)

