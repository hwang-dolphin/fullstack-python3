# save this as app.py
from flask import (Flask, request, render_template)
import sys
# from flask_cors import CORS


# app = Flask(__name__)
app = Flask(__name__, static_folder='build', static_url_path='/')

@app.route("/")
def home():
    #return render_template("index.html")
	return app.send_static_file('index.html')



"""
@app.route("/about")
def about():
	return {'time': 'AA About AA'}
	

@app.route("/contact")
def contact():
    return {'time': 'CC Contacto CC'}
"""




"""
@app.route("/blog")
def get_blog():
	return render_template("blog.html")
"""

@app.route('/api/name')
def name():
	headers = request.headers
	auth = headers["x-api-key"]
	# auth = headers.get("x-api-key")∏

	if auth == 'secretkey':
		return {"message":["Welcome, Hello World"]}

	else:
		return {"message":["Sorry, closed"]}
	#jsonify({'color':'Hello World!'})

"""
if __name__ == '__main__':
	app.run(debug=True)
"""



