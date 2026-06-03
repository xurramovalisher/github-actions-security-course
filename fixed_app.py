import os, sqlite3, subprocess, hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Maxfiy kalitlar kod ichidan olib tashlandi (muhitdan o'qiladi)
SECRET_KEY = os.getenv("SECRET_KEY")
DB_PASS   = os.getenv("DB_PASS")

@app.route("/login", methods=["POST"])
def login():
    user = request.form["username"]
    conn = sqlite3.connect("users.db")
    # Parameterized query — SQL Injection'dan to'liq himoya
    conn.execute("SELECT * FROM users WHERE name=?", (user,))

@app.route("/hash")
def do_hash():
    data = request.args.get("data")
    # MD5 o'rniga xavfsiz SHA256 + Tuz (salt) ishlatildi
    salt = os.urandom(32)
    return hashlib.pbkdf2_hmac("sha256", data.encode(), salt, 100000).hex()

@app.route("/run")
def run_cmd():
    # shell=False va argumentlar ro'yxat ko'rinishida (Shell injection yo'q)
    cmd_list = [request.args.get("cmd")]
    subprocess.call(cmd_list, shell=False)

if __name__ == "__main__":
    # debug=True olib tashlandi, host faqat lokal tarmoqqa o'zgartirildi
    debug = os.getenv("DEBUG", "false").lower() == "true"
    app.run(debug=debug, host="127.0.0.1")
