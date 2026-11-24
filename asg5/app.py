from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head><meta charset="utf-8"><title>ASG5 Container Demo</title></head>
      <body>
        <h1>ASG5: Containerized CI/CD</h1>
        <p>This Flask app is running in a Docker container.</p>
      </body>
    </html>
    """


@app.get("/health")
def health():
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
