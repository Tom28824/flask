from flask import Flask, render_template, request, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'random'

con = sqlite3.connect("login.db")
cur = con.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS user(
                name VARCHAR(10)NOT NULL PRIMARY KEY,
                password VARCHAR(20)NOT NULL
                )""")
con.commit()
con.close()

@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("sign-up.html")
    else:
        con = sqlite3.connect("login.db")
        cur = con.cursor()
        hash = hashlib.sha256(request.form["password"].encode()).hexdigest()
        cur.execute(""" INSERT INTO user(name, password)
                        VALUES(?,?)""",
                        (request.form["user"], hash))
        con.commit()
        con.close()
        return "signup success"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        con = sqlite3.connect("login.db")
        cur = con.cursor()
        hash = hashlib.sha256(request.form["password"].encode()).hexdigest()
        cur.execute("   SELECT * FROM user WHERE name = ? AND password = ?",
                        (request.form["user"], hash))
        user = cur.fetchone()
        print(user)
        if user:
            session["user"] = request.form["user"]
            return render_template("welcome.html")
        else:
            return "login failed"
        
@app.route("/password",methods=["GET", "POST"])
def password():
    if request.method == "GET":
        if "user" in session:
            return render_template("password.html")
        else:
            return render_template("index.html")
    else:
        con = sqlite3.connect("login.db")
        cur = con.cursor()
        hash = hashlib.sha256(request.form["password"].encode()).hexdigest()
        cur.execute(""" UPDATE user SET password = ? WHERE name = ?""",
                        (hash, session["user"]))
        con.commit()
        con.close()
        return "password changed"

@app.route("/w")
def welcome():
    return render_template("welcome.html") 

@app.route("/logout")
def logout():
    session.pop("user", None)
    return render_template("index.html")   
        
if __name__ == "__main__": 
    app.run(debug=True)
