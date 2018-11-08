#!/usr/bin/env  python3

from configparser import ConfigParser

if __name__ == "__main__":
    config = ConfigParser()
    config.read("simple-ftp.ini")

    cfg = config["simple-ftp"]

    config_files = ["config/simple-ftp_nginx.conf", "config/simple-ftp_uwsgi.ini"]

    for c in config_files:
        with open(c + ".dist","r") as dist ,\
                    open(c, "w") as conf:
            confs = dist.read()
            for s in cfg:
                k = s.upper()
                confs =confs.replace("{{%s}}" % k, cfg[k])
            conf.write(confs)
