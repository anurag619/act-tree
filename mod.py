from collections import defaultdict
import pymongo
 
connection = pymongo.Connection()
db = connection.mydatabase
activity = db.activity


def con(dicn):
    """Recursively converts dictionary keys to strings."""
    if not isinstance(dicn, dict):
        return dicn
    return dict((str(k), con(v)) 
        for k, v in dicn.items())


def deconv(di):
	dicc = con(di) 
	qw = (dicc.items()[2][1])
	q= create(str(qw))
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

