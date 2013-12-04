
act-tree
========


A simple api using python framework(flask) that receives POST requests containing a id and sequence on a URL and then return a JSON string representing a Tree for a particular id. Sending a GET request to URL /app/1/ will return the JSON representing the activity tree for id = 1

specification
--------------

If a POST request is done on id=1 with activity 'ABC', GET request for the same will yield a json object that represents a tree ( A->B->C )of that perticular activty.

<ol>For representing the tree, nested dictionaries is used.
[Pymongo](http://api.mongodb.org/python/current/) <i>( Python interface of Mongodb)</i> is used to store the data.  </ol>

<b>example - </b> 


	import requests

	requests.post('http://127.0.0.1:5000/2/ABC')
	r = requests.get('http://127.0.0.1:5000/2') 
	r.text

	{\n  "app_id": "2", \n  "tree": {\n    "A": {\n      "B": {\n        "C": {}\n      }\n    }\n  }\n}


