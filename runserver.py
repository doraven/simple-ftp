#!/usr/bin/env python3

from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

from configparser import ConfigParser
import os
import json

APP_ROOT = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

@app.route("/query", methods = ["GET", "POST"])
def query():
    dic ={}
    if request.method == "POST":
        form=request.form
        files = request.files
        for i in form:
            dic[i] = form[i]
        for i in files:
            file_path = "ftp-root" + request.form["path"] + secure_filename(files[i].filename)
            files[i].save(file_path)
            dic["saved"] = file_path
        # filename = secure_filename(file.filename)
    with open("Log.txt", "w") as f:
        f.write(str(dic))
    return json.dumps(dic)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8081)
