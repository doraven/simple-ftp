#!/usr/bin/env bash

cd `dirname $0`
basepath=$(pwd)

#如果venv文件夹不存在，则创建文件夹
#这里因为没有使用venv，卡了劳资半天，fuck u
if [ ! -d "venv" ]; then
    virtualenv -p /usr/bin/python3 venv
    ./venv/bin/pip install -r requirements.txt
fi

python3 $basepath/config/DeployConfig.py

sudo ln -s  -f $basepath/config/simple-ftp_uwsgi.ini /etc/uwsgi/apps-available/

sudo ln -s -f $basepath/config/simple-ftp_nginx.conf /etc/nginx/conf.d/
