from collections import defaultdict
import pymongo
import re

connection = pymongo.Connection()
db = connection.mydatabase
activity = db.activity

def deconv(di):
	
	qw = re.search(r'\b[A-Z]{3}\b',di)
	q= create(qw.group())
	return q

def tree(): 
	return defaultdict(tree)

def create(er):
	a= tree()
	a[er[0]][er[1]][er[2]]
	gh = nes(a)
	return gh


def nes(dd):
	if isinstance(dd, defaultdict):
	  return {k: nes(v) for k,v in dd.items()}
	else: return dd

