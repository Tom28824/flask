from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get("user")
    password = request.args.get("password")
    if name ==None:
        return render_template("index.html")
    elif password =="123":
        return "Hello " + name
    else:
        return "wrong password"
