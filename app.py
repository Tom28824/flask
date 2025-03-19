from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("sign-up.html")
    else:
        name = request.form["user"]
        password = request.form["password"]
        return "signup success"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if "bob" == request.form["user"] and \
              "123" == request.form["password"]:
            return "hello " + request.form["user"]
        else:
            return "wrong password"
        
if __name__ == "__main__": 
    app.run(debug=True)