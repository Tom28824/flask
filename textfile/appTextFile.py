from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("sign-up.html")
    else:
        name = request.form["user"]
        password = request.form["password"]
        f = open("login.txt", "w")
        f.write(name + "\n")
        f.write(password)
        f.close()
        return "signup success"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        f = open("login.txt", "r")
        name = f.readline().strip()
        password = f.readline()
        if name == request.form["user"] and \
              password == request.form["password"]:
            return "hello " + name
        else:
            return "wrong password"