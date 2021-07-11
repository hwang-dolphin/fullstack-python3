# save this as app.py
from flask import (Flask, render_template)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/blog")
def get_blog():
	return render_template("blog.html")
# app.run(debug=True)



