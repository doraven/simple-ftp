#!/usr/bin/env  python3
# 管理用户的创建和删除
import json, os, shutil

USR_M_PROMPT = "\n\n###  \n\
(r)ename:重命名 + 序号 + 新名字；\n\
(p)assword:改密码 + 序号 + 新密码\n\
(d)elete:删除 + 序号；\n\
输入操作："

if __name__ == "__main__":
    users = {}
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            fs = f.read()
            if fs:
                users = json.loads(fs)

    while(True):
        ipt = input("\n###  (1)创建用户；\t(2)用户管理；\t (q)退出 \n\t：").lower()

        if ipt == "1":
            usr = input("用户名：").strip()
            if not usr:
                print("无效用户名")
            elif usr in users:
                print("该用户已存在")
            else:
                pw = input("  密码：")
                users[usr] = pw
                # 建立文件夹
                os.mkdir("ftp-root/%s" % usr)

                with open("users.json", "w") as f:
                    f.write(json.dumps(users, indent = 4))
                print("用户  < %s >  创建成功" % usr)

        elif ipt == "2":
            usr_list = list(users.keys())
            if not usr_list:
                print("当前无用户")
            else:
                print("当前用户如下：\n")
                for k in range(len(usr_list)):
                    if k%4 == 3 :
                        print("(%d).%s" % (k, usr_list[k]), end = "\n")
                    else:
                        print("(%d).%s" % (k, usr_list[k]), end = "\t")
                cmd = input(USR_M_PROMPT).lower()
                cmd_split = cmd.split(' ')
                cs = [i for i in cmd_split if i]
                if len(cs) <= 1:
                    continue
                usr = usr_list[int(cs[1])]

                    # rename
                if cs[0][0] == 'r':
                    n_usr = cs[2]
                    if n_usr not in usr_list:
                        confirm = input("确认更改  < %s >  至  < %s >  吗？(y)" % (usr, n_usr)).lower()
                        users[n_usr] = users[usr]
                        del users[usr]
                        with open("users.json", "w") as f:
                            f.write(json.dumps(users, indent = 4))
                        shutil.move("ftp-root/%s" % usr, "ftp-root/%s" % n_usr)
                        print("已更改用户名  < %s >  至  < %s >  " % (usr, n_usr))
                    else:
                        print("该用户已存在，请重命名")

                    # change password
                elif cs[0][0] == "p":
                    old_pw = users[usr]
                    print("< %s > 的密码 为：||  %s  || "  % (usr, old_pw))
                    if len(cs) !=3:
                        continue
                    confirm = input(" 确认更改吗？(y):").lower()
                    if len(cs) > 2 and confirm =="y":
                        users[usr] = cs[2]
                        with open("users.json", "w") as f:
                            f.write(json.dumps(users, indent = 4))
                        print("已更改用户  < %s >  的密码 ||  %s  || 至 ||  %s  ||  "
                                                % (usr, old_pw, cs[2]))
                    # delete
                elif cs[0][0] == 'd':
                    confirm = input("确认删除  < %s >  吗？(y):" % usr).lower()
                    if confirm == "y":
                        del users[usr]
                        with open("users.json", "w") as f:
                            f.write(json.dumps(users, indent = 4))
                        shutil.rmtree("ftp-root/%s" % usr)
                        print("已删除用户  < %s >  " % usr)
                    else:
                        print("未删除")
        elif ipt == "q":
            break
