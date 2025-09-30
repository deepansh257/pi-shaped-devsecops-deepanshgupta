from flask import Flask, request, jsonify
import sqlite3
import os

# Insecure: hardcoded secret (this is intentional for the exercise)
# FIX-ME: Move SECRET_KEY to environment variable and don't store secrets in code.
SECRET_KEY = "SUPER_SECRET_KEY_12345"

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Simple in-memory sqlite DB file
DB = "users.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return "Vulnerable Flask App - Demo"

@app.route("/register", methods=["POST"])
def register():
    # Insecure: storing plaintext passwords
    username = request.form.get("username")
    password = request.form.get("password")
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO users (username,password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok", "user": username})

@app.route("/eval")
def insecure_eval():
    # Insecure: using eval on user input (dangerous)
    code = request.args.get("code", "")
    try:
        result = eval(code)   # intentionally insecure
        return jsonify({"result": str(result)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    init_db()
    # Don't use debug=True in production
    app.run(host="0.0.0.0", port=5000)
