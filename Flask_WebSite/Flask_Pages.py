from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
#Rendering a template
def template():
	return render_template("index.html")

	@app.route("/about")
#Rendering about templage
def template():
	return render_template("about.html")