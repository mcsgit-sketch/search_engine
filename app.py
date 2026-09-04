from flask import Flask, render_template, request

# turn the current file into flask application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index(): 
    if request.method == "POST": 
        search = request.form.get("search") 
        if search == "": 
            return render_template("index.html")
        return render_template("search.html") 
    else: 
        return render_template("index.html")

