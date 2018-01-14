from twython import Twython, TwythonError
import csv
import os
import time
from datetime import datetime
import json
import re
import time
import sys
import dateutil.parser

fetch_count = 15000
APP_KEY = 'w1MYjVTrfmwvjuOo2ucEhTQBA'
APP_SECRET = 'DEGHc5bwRB0pNztbaVasLORrqFOiqxBnHIXT1j7qwRH7U0We3W'
OAUTH_TOKEN = "952598856767700992-3gqLYyUpByKLmJAur2sTO0Y1a6I5fPg"  
OAUTH_TOKEN_SECRET = "EkPs8IZoo5Qnt9tOjUcXSTIGNXE86QQ62G03ksmjD8VGh"  

output_file = open('output.csv', 'wb')
csv_writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)

csv_writer.writerow(['Post Time', 'Tweet URL', 'Tweet', 'Retweets', 'Favourites'])

twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()  
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

timeline = twitter.get_user_timeline(screen_name='realDonaldTrump', count=fetch_count)

for tweet in timeline:
    csv_writer.writerow([int(time.mktime(dateutil.parser.parse(tweet['created_at'].encode('utf-8')).timetuple())), "https://twitter.com/statuses/" + tweet['id_str'].encode('utf-8'), 
                        tweet['text'].encode('utf-8'), tweet['retweet_count'], tweet['favorite_count']])