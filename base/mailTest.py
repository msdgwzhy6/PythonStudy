# coding:utf-8
import re
import sys
import time, datetime

reload(sys)
sys.setdefaultencoding("utf-8")

import os

import smtplib
from email.mime.text import MIMEText

_user = "yutianran@che.com"
_pwd = "ytr@0113"
_to = "630709658@qq.com"

# 使用MIMEText构造符合smtp协议的header及body
msg = MIMEText("我是用Python脚本发送的")
msg["Subject"] = "周报"
msg["From"] = _user
msg["To"] = _to

s = smtplib.SMTP_SSL("qiye.aliyun.com",)  # 连接smtp邮件服务器,端口默认是25
s.login(_user, _pwd)  # 登陆服务器
s.sendmail(_user, _to, msg.as_string())  # 发送邮件
s.close()


