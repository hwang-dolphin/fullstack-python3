# save this as app.py
from flask import (Flask, render_template)
import sys
from flask_cors import CORS


# app = Flask(__name__)
app = Flask(__name__, static_folder='build', static_url_path='/')
cors = CORS(app, resources={r"/api/name":{"origins":["https://fullstack-python3.herokuapp.com"]}})


@app.route("/")
def hello():
    #return render_template("index.html")
	return app.send_static_file('index.html')

@app.route("/blog")
def get_blog():
	return render_template("blog.html")

@app.route("/test")
def test():
    return "test"

@app.route("/hello")
def get_hello():
    return {"message":["hello world from flask"],"status":"success"}


@app.route('/api/name')
def name():
	print('hello', file=sys.stderr)

	headers = request.headers
	auth = headers["x-api-key"]
	# auth = headers.get("x-api-key")∏

	if auth == 'secretkey':
		return "Welcome, Hello World"

	else:
		return "Sorry, closed"
	#jsonify({'color':'Hello World!'})




# app.run(debug=True)



