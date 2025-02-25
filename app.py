from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form["user"]
        password = request.form["password"]
        if password == "123":
            return "hello " + name 
        else:
            return "wrong password"