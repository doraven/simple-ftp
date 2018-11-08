#!/usr/bin/env python3

from flask import Flask, request, redirect, url_for, session

from configparser import ConfigParser
import os, shutil
import json

APP_ROOT = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
config = ConfigParser()
config.read("simple-ftp.ini")
app.config["SECRET_KEY"] = config["flask"]["SECRET_KEY"]

@app.route("/query", methods = ["GET", "POST"])
def query():
    # 判断是否登陆
    if request.method == "GET":
        if not request.args.get("get"):
            return "0"
        if request.args.get("user") in session:
            return "1"
        else:
            return "0"

    if request.method == "POST":
        form=request.form
        if "post" not in form:
            return "0"
        # 登陆
        elif form["post"] == "login":
            users = json.loads(open("users.json", "r").read())
            if form["password"] == users[form["user"]]:
                session[form["user"]] = "loggedin"
                return "1"
            else:
                return "0"
            # 判断登陆
        elif form["user"] not in session:
            return "0"
        # 上传
        elif form["post"] == "upload":
            files = request.files
            for i in files:
                file_path = "ftp-root" + form["path"] + files[i].filename
                files[i].save(file_path)
            return "1"
            # 下载
        elif form["post"] == "delete":
            for f in json.loads(form["deletefiles"]):
                fullpath = "ftp-root" + form["path"] +f
                if(os.path.isfile(fullpath)):
                    os.remove(fullpath)
                else:
                    shutil.rmtree(fullpath )
            return "1"
        elif form["post"] == "newfolder":
            fullpath = "ftp-root" + form["path"] + form["newfoldername"]
            os.mkdir(fullpath)
            return "1"
    return "0"

def log(s):
    with open("Log.txt", "a+") as f:
        f.write("\n" + s)
    return True

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8081)
