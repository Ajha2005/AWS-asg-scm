import os
from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    env = os.getenv("APP_ENV", "staging")
    version = os.getenv("APP_VERSION", "1")
    return f"<h1>ASG 4 — {env.title()}</h1><p>Version {version}</p>"
