#!/usr/bin/env bash

cd `dirname $0`
basepath=$(pwd)

#如果venv文件夹不存在，则创建文件夹
#这里因为没有使用venv，卡了劳资半天，fuck u
if [ ! -d "venv" ]; then
    virtualenv -p /usr/bin/python3 venv
    ./venv/bin/pip install -r requirements.txt
fi

if [ ! -f "simple-ftp.ini" ];then
  cp simple-ftp.ini.dist simple-ftp.ini
  echo "请编辑好simple-ftp.ini文件后重新deploy"
  exit
fi

python3 $basepath/config/DeployConfig.py

sudo ln -s  -f $basepath/config/simple-ftp_uwsgi.ini /etc/uwsgi/apps-available/

sudo ln -s -f $basepath/config/simple-ftp_nginx.conf /etc/nginx/conf.d/

sudo nginx -s reload

echo "安装完毕，使用manage.sh脚本编辑用户和用户密码"
