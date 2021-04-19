from flask import Flask, request, jsonify
from script import search

app = Flask(__name__)

@app.route('/')
def home_page():
	return "Hello World"

@app.route('/api', methods=['GET'])
def api_id():
	if 'key' in request.args:
		key = request.args['key']
		search_data = search(key)
	else:
		return "Error: No Keyword field provided. Please specify an Keyword."
	returned_data = {
	"data":search_data,
	"status":True
	}
	return jsonify(returned_data)

if __name__ == '__main__':
	app.run(debug=True)