# save this as app.py
from flask import (Flask, render_template)

# app = Flask(__name__)
app = Flask(__name__, static_folder='build', static_url_path='/')

@app.route("/")
def hello():
    #return render_template("index.html")
	return app.send_static_file('index.html')

@app.route("/blog")
def get_blog():
	return render_template("blog.html")
# app.run(debug=True)



