from twython import Twython, TwythonError
import requests
import urllib2
import csv
import os
import time
from datetime import datetime
import json
import re
import time
import sys
from bs4 import BeautifulSoup
import dateutil.parser

fetch_count = 150
APP_KEY = 'KGWjAFUIvPL1AAMWrVHZxI0sW'
APP_SECRET = 'esPOox4alt3B3pRS17N8NkzI3BDPRKgAQ1QHHX5Kbf7XTq3zIX'
OAUTH_TOKEN = "714312642-OptKpqfFjoVSrehqvdpB3GdtRfV3SNkAZhZ44bAy"  
OAUTH_TOKEN_SECRET = "RuIVUCbcYoIKcyXhjxP091ECIZMIL0ezoVqGZWUY6Z636"  

if __name__ == "__main__":
    output_file = open(sys.argv[1], 'wb')
    csv_writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)
    csv_writer.writerow(['Post Time', 'Tweet URL', 'Tweet', 'Retweets', 'Favourites'])
    
    twitter = Twython(APP_KEY, APP_SECRET)
    auth = twitter.get_authentication_tokens()  
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter.verify_credentials()

    name = url.rsplit('/', 1)[1]
    timeline = twitter.get_user_timeline(screen_name=name, count=fetch_count)

    for tweet in timeline:
        csv_writer.writerow([int(time.mktime(dateutil.parser.parse(tweet['created_at'].encode('utf-8')).timetuple())), "https://twitter.com/statuses/" + tweet['id_str'].encode('utf-8'),
                            tweet['text'].encode('utf-8'), tweet['retweet_count'], tweet['favorite_count']])