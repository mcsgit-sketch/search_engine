from flask import Flask, render_template, request

# turn the current file into flask application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index(): 
    if request.method == "POST": 
        return render_template("search.html", search = request.form.get("search"))
    else: 
        return render_template("index.html")

