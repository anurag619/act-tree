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
		return "Didn't do anything with POST, but here's a message."


@app.route('/<app_id>', methods=['GET'])
def get_tree(app_id):
	entity = db.activity.find()

	if not entity:
		return jsonify({'app_id' : 'INVALID app_id',
				'tree' : {}
			})
	else:
		cont= deconv((entity))
		#co = deconv(cont)
		return jsonify({'app_id': app_id, 'tree' : str(cont) })


if __name__ == '__main__':
	app.run(debug=True)


