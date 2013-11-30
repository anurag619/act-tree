from flask import Flask, jsonify, request
from mod import *

app = Flask(__name__)

@app.route('/<app_id>/<seq>', methods=['POST'])
def home(app_id,seq):
	if request.method == "POST":
		d={}
		d["app"]=app_id
		d["act"]=seq
		activity.insert(d)
		return "post made"

@app.route('/<app_id>', methods=['GET'])
def get_tree(app_id):
	f= {}
	f["app"]=app_id
	entity = db.activity.find_one(f)

	if not entity:
		return jsonify({'app_id' : 'INVALID app_id',
				'tree' : {} })
	else:
		cont= deconv((str(entity)).encode('utf-8'))
		entity['act']= cont
		return jsonify({'app_id': app_id, 'tree' : entity['act'] })


if __name__ == '__main__':
	app.run(debug=True)


