import sys
import pymongo
from pymongo import MongoClient
import re
import csv
import operator
import json
import datetime
import dateutil.parser as parser

def format_data(data):
	return ({
		'post_time' 	: datetime.datetime.fromtimestamp(float(data[0]), None), 
		'tweet' 		: data[1], 
		'post_id'		: data[2]
	})

client = MongoClient('localhost:27017')
database = client['tweets']['tweets']

file = open('output.csv')
rows = csv.reader(file,delimiter=',')

#skip the header
next(rows)

for i in rows:
	data = format_data(i)
	if (data):
		database.insert_one(format_data(i)).inserted_id

file.close()