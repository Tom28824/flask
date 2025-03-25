from flask import Flask, render_template, request
import sqlite3
import hashlib
app = Flask(__name__)

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
            return "login success"
        else:
            return "login failed"
        
if __name__ == "__main__": 
    app.run(debug=True)