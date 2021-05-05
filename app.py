from flask import Flask, request, jsonify # Flask app
from collections import OrderedDict # object create
import requests, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
	return 'Hello, World!'

@app.route('/info/get', methods=['GET'])
def getTest():
	file_data = OrderedDict()
	file_data["name"] = "yoolee"
	file_data["age"] = 28
	file_data["info"] = {'cm':171, 'like':'me'}
	file_data["data"] = request.args.get('data')
	return jsonify(file_data)

@app.route('/info/post', methods=['POST'])
def postTest():
	file_data = OrderedDict()
	file_data["name"] = "yoolee"
	file_data["age"] = 28
	file_data["info"] = {'cm':171, 'like':'me'}
	file_data["data"] = request.get_json()
	return jsonify(file_data)

@app.route('/request', methods=['POST'])
def requestPostTest():
	headers = {'Content-Type':'application/json'}
	datas = request.get_json()
	res = requests.post("http://localhost:4000/info/post", headers=headers, json=datas, verify=False)
	return res.json()

@app.route('/request', methods=['GET'])
def requestGetTest():
	datas = OrderedDict()
	datas["data"] = request.args.get('data')
	res = requests.get("http://localhost:4000/info/get", params=datas)
	return res.json()

if __name__ == '__main__':
	app.run(debug=True, port=4000)

