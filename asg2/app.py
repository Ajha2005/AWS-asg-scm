from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "CodeBuild test app is running", 200

@app.get("/health")
def health():
    return jsonify(status="ok"), 200
