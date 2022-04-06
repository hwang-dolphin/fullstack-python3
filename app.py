# save this as app.py
from flask import (Flask, request, render_template, jsonify)
import os

import sys
from flask_cors import CORS

from functools import wraps
import datetime
import jwt


# app = Flask(__name__)
app = Flask(__name__, static_folder='build', static_url_path='/')
cors = CORS(app, resources={r"/*":{"origins":"*"}})
#cors = CORS(app, resources={r"/*":{"origins":["https://www.hwangtech.com","http://portalmanager.zonicdesign.com"]}})

app.config['SECRET_KEY'] = 'JustDemonstrating'

"""
def check_for_token(func):
	@wraps(func)
	def wrapped(**args, **kwargs):
		token = request.args.get('token')

		if not token:
			return jsonify({'message': 'Missing token'}), 403


		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		
		except:
			return jsonify({'message': 'Invalid token'}), 403

		return func(*args, **kwargs)
	return wrapped
			

@app.route("/protected")
def protected():
	if not session.get('logged_in'):
		return "not logged in"

	else:
		return "currently logged in"


@app.route("/public")
def public():
	return "anyone can view this"


@app.route("/auth")
@check_for_token
def authorized():
	return "This is only viewable with a token"
"""

@app.route("/login")
def login():

	token = jwt.encode({
		'user': 'robert',
		'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)

	},

	#app.config['SECRET_KEY'])
   
    "secret", algorithm="HS256")

	return jsonify({'token': token})


@app.route("/")
def home():
	return app.send_static_file('index.html')

    # this one doesn't work
	#return render_template("index.html")
	

@app.route("/about")
def about():
	return {'time': 'about api working'}
	

@app.route("/contact")
def contact():
    return {'time': 'contact api working'}



@app.route("/security")
def security():
    if 'Authorization' in request.headers:
        customHeader = request.headers['Authorization']
      	
        jwtToken = customHeader.split(" ")
        
        try:
            decoded = jwt.decode(jwtToken[1], "secret", algorithms=['HS256'])

        except:
            return {'time': 'no token found'}
 

       #print(decoded["user"])
        return {'time': decoded["user"]}

    else:
        return {'time': 'security api not working'}



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

	if auth == 'SecretKey2814':
		return {"message":["New Good Morning!"]}

	else:
		return {"message":["Closed"]}
		#return {"message":[auth]}
	#jsonify({'color':'Hello World!'})


# run code only for development, not production

#if __name__ == '__main__':
#    app.run(debug=True)

"""
https://www.youtube.com/watch?v=e-_tsR0hVLQ
Intermediate Flask Tutorial: Implementing JSON Web Tokens (JWT)
Live Python 
"""

# reference: https://medium.com/@apcelent/json-web-token-tutorial-with-example-in-python-df7dda73b579

# https://fullstack-python3.herokuapp.com/api/name
