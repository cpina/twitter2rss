import json
import config
import sys

def check_configuration():
    if config.access_token == '' or config.access_token_secret == '' or\
        config.consumer_key == '' or config.consumer_secret == '':
        print('Check config.py file and write the Twitter keys there.')

        sys.exit(1)

def get_jsonp(content):
    return 'twitts(' + json.dumps(content) + ')'

def write_to_req(req, get_rss, search, term):
    if req.form.has_key('format'):
        output_format = req.form['format'].value
    else:
        output_format = 'rss'

    if output_format == 'rss':
        req.write(get_rss(search, term))
    elif output_format == 'json' or output_format == 'jsonp':
        req.write(get_jsonp(search))
