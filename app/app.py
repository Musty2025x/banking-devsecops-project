from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Bank API Running",
        "environment": os.getenv("ENV", "dev")
    })

@app.route("/balance")
def balance():
    return jsonify({
        "account_id": "123456",
        "balance": 1000
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
