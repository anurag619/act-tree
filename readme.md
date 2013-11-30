
act-tree
========

* status - working

A simple web server using python server side framework(flask) that receives POST requests containing app_id and sequence on a URL and then return a JSON string representing the Activity Tree for a particular app_id. Eg - sending a GET request to URL /app/1/ will return the JSON representing the activity tree for app_id = 1

If a POST request is done on app_id=1 with activity 'ABC', GET request for the same will yield a json oject that represent a tree of the perticular activty.

example - 


requests.get('http://127.0.0.1:5000/2') /n
---> {\n  "app_id": "2", \n  "tree": {\n    "A": {\n      "B": {\n        "C": {}\n      }\n    }\n  }\n}


