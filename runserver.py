#!/usr/bin/env python3

from flask import Flask
from configparser import ConfigParser
import os

APP_ROOT = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

@app.route("/query")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
