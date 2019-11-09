from flask import Flask, render_template
app = Flask(__name__)

#Rendering Home template
@app.route("/")
def home():
	title = "Home"
	return render_template("index.html", title=title)	



if __name__=="_main_":
    app.run(debug=True)