import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get('username')
    
    # VULNERABLE: SQL Injection
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    
    # VULNERABLE: Cross-Site Scripting (XSS)
    return "<h1>Welcome back, " + username + "</h1>"

if __name__ == "__main__":
    app.run()
