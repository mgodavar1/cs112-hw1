from flask import Flask 
from flask import request

app = Flask(__name__)

@app.route("/hello")
def hello():
		if 'name' in request.args:
			return 'Hello ' + request.args['name'] + '!'
		else:
			return 'Hello user!'


@app.route("/check", methods = ['GET', 'POST'])
def checkget():
	if request.method == 'POST':
		return 'This is a POST request'
	else:
		return 'This is a GET request'	

if __name__ == '__main__':
	app.run(port = 8080, debug = True)
