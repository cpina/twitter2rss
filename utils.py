import json
import config
import sys

def check_configuration():
    if config.access_token == '' or config.access_token_secret == '' or\
        config.consumer_key == '' or config.consumer_secret == '':
        print('Check config.py file and write the Twitter keys there.')

        sys.exit(1)
