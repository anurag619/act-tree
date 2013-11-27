from collections import defaultdict
import pymongo
 
connection = pymongo.Connection()
db = connection.mydatabase
activity = db.activity


def con(dicn):
    """Recursively converts dictionary keys to strings."""
    if not isinstance(dictionary, dict):
        return dictn
    return dictn((str(k), con(v)) 
        for k, v in dictn.items())


def deconv(di):
	q= create(str(di.items()[0][1]))
	return q

def tree(): 
	return defaultdict(tree)

def create(er):
	a= tree()
	b = nes(a[er[0]][er[1]][er[2]])

	return b


def nes(dd):
	if isinstance(dd, defaultdict):
	  return {k: nes(v) for k,v in dd.items()}
	else: return dd

