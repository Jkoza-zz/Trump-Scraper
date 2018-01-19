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
		'created_at' 	: datetime.datetime.fromtimestamp(float(data[0]), None), 
		'text' 			: data[1], 
		'id_str'		: data[2]
	})

client = MongoClient('ds119064.mlab.com:19064')
client['trump-tweets'].authenticate('jkoza', 'jkoza')
database = client['trump-tweets']['tweets']

file = open('output.csv')
rows = csv.reader(file,delimiter=',')

#skip the header
next(rows)

for i in rows:
	data = format_data(i)
	if (data):
		if(not database.find_one({'id_str' : data['id_str']})):
			database.insert_one(format_data(i)).inserted_id
file.close()