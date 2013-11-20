twitter2rss in Python
=====================

Introduction
------------
This is a very simple (it's mainly a hack, without much error handling and
without any reporting at all) set of scripts in Python CGIi that provides
search and user timelines from Twitter to RSS (using the same RSS format).

Twitter dropped support for RSS outputs (at least user time lines and search).
twitter2rss connects to Twitter using the Twitter API, requests a search query
or user time line and outputs RSS.

This approach is very similar to what http://www.twitter-rss.com/ page does. Two problems with twitter-rss.com:
 * it doesn't refresh often enough for my needs
 * only supports user timelines, not searches, as I wanted

Main Features
-------------
 * No database required (everything is fetched from Twitter. Yes,
   this could cause too many requests)
 * I'm afraid that not much error handling
 * 2 endpoints:
     http://your-server/twitter/user_timeline.py?screen_name=YourFriend
     http://your-server/twitter/search.py?q=mendeley
 * By default: the output is for RSS readers. Add &format=json and the output
   is in Json.

Installation / Usage
--------------------
1. git clone https://github.com/cpina/twitter2rss.git
2. pip install twython     # or `easy_instal feedparser`l
3. pip install feedparser  # or `easy_install feedparser`
3. read config.py (contains instructions how to get the `oauth_tokens`)
4. Test with `./user_timeline.py` and `./search.py`
5. In the Apache configuration I enabled `mod_python` for the directory where
I copied the scripts:
<pre>
    <Directory /var/www/carles.pina.cat/twitter>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride None
        Order allow,deny
        allow from all
        AddHandler mod_python .py
        PythonHandler mod_python.publisher
        PythonDebug On
        DirectoryIndex index.py
    </Directory>
</pre>
Let me know if it's useful or if you have some problems.

Carles Pina i Estany - carles@pina.cat, 2013
