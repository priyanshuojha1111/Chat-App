from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect
from model import create_post, fetch_posts, authenticate_user

app = Flask(__name__)

@app.route("/post", methods=["GET", "POST"])
def postpage():
	if request.method == "POST":
		username = request.form.get("username", None)
		content = request.form.get("content", None)
		dt = datetime.now()
		if username and content:
			create_post(username, content, dt)

	posts = fetch_posts()
	return render_template("index.html", posts=posts)

@app.route("/", methods=["POST", "GET"])
def homepage():
	return render_template("login.html")

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		username = request.form.get("username", None)
		password = request.form.get("password", None)
		if username and password:
			if authenticate_user(username, password):
				return redirect(url_for("postpage"))
		else:
			return redirect(url_for("/"))

@app.route("/registerPage", methods=["POST", "GET"])
def registerPage():
	return render_template("register.html")

if __name__ == "__main__":
	app.run(debug=True)