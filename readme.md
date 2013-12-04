
act-tree
========


A simple api using python framework(flask) that receives POST requests containing a id and sequence on a URL and then return a JSON string representing a Tree for a particular id. Sending a GET request to URL /app/1/ will return the JSON representing the activity tree for app_id = 1

specification
--------------

If a POST request is done on id=1 with activity 'ABC', GET request for the same will yield a json oject that represents a tree ( A->B->C )of the perticular activty.

<ol>For representing the tree, nested dictionaries is used.
Pymongo <i>( Python interface of Mongodb)</i> is used to store the data.  </ol>

<b>example - </b> 


	import requests

	requests.post('http://127.0.0.1:5000/2/ABC')
	requests.get('http://127.0.0.1:5000/2') 

{\n  "app_id": "2", \n  "tree": {\n    "A": {\n      "B": {\n        "C": {}\n      }\n    }\n  }\n}


