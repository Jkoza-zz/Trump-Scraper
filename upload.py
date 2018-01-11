import sys
import pymongo
from pymongo import MongoClient
import re
import csv
import operator
import json
import datetime
import dateutil.parser as parser
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", help="file to upload")
	parser.add_argument("-i", "--ip", help="ip of database")
	parser.add_argument("-u", "--username", help="username")
	parser.add_argument("-p", "--password", help="password")
	parser.add_argument("-db", "--database", help="database")
	parser.add_argument("-c", "--collection", help="collection")

	return parser.parse_args()

def configure_db(arguments):
	host = str(arguments.ip)
	username = str(arguments.username)
	password = str(arguments.password)
	database = str(arguments.database)
	collection = str(arguments.collection)

	client = MongoClient(host)
	client[database].authenticate(username, password)
  	return client[database][collection]

def format_data(data):
	if (data[5]):
		return ({
			'post_time' 	: datetime.datetime.fromtimestamp(float(data[0]), None), 
			'updated_time' 	: datetime.datetime.fromtimestamp(float(data[1]), None),
			'scraped_time' 	: datetime.datetime.fromtimestamp(float(data[2]), None), 
			'post_url'		: data[3], 
			'media_url'		: data[4], 
			'article_no'	: data[5], 
	        'poster_name'	: data[6], 
	        'post_type'		: data[7], 
	        'message'		: data[8], 
	        'description'	: data[9], 
	        'likes_count'	: data[10], 
	        'repost_count'	: data[11], 
	        'comments'		: data[12], 
	        'source'		: data[13],
	        'reach'			: data[14],
	        'engagement'	: data[15],
	        'user_shares'	: data[16]
		})

	return	{}

if __name__ == "__main__":

	arguments = parse_arguments()
	database = configure_db(arguments)
	file = open(str(arguments.file))
	rows = csv.reader(file,delimiter=',')
	#skip the header
	next(rows)
	
	for i in rows:
		data = format_data(i)
		if (data):
			database.insert_one(format_data(i)).inserted_id

	file.close()