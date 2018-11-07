#!/usr/bin/env bash

cd `dirname $0`
basepath=$(pwd)

python3 $basepath/config/DeployConfig.py
