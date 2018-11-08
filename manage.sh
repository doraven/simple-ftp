#!/usr/bin/env bash
# 管理用户，用于新建和删除用户

cd `dirname $0`
basepath=$(pwd)

python3 config/user-manage.py
