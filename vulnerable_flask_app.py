import os, sqlite3, subprocess, hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

SECRET_KEY = "hardcoded_jwt_secret_123"
DB_PASS   = "admin123"

@app.route("/login", methods=["POST"])
def login():
    user = request.form["username"]
    conn = sqlite3.connect("users.db")
    q = f"SELECT * FROM users WHERE name='{user}'"
    conn.execute(q)

@app.route("/hash")
def do_hash():
    data = request.args.get("data")
    return hashlib.md5(data.encode()).hexdigest()

@app.route("/run")
def run_cmd():
    cmd = request.args.get("cmd")
    subprocess.call(cmd, shell=True)

@app.route("/fetch")
def fetch_url():
    url = request.args.get("url")
    import requests
    return requests.get(url, verify=False).text

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
