# coding:utf-8
import re
import sys
import time, datetime

reload(sys)
sys.setdefaultencoding("utf-8")

import os

if __name__ == "__main__":
    cmd = 'adb pull data/data/com.che.chechengwang/databases/car.db /Users/yutianran/Desktop'
    os.popen(cmd)
    print "获取db文件:完成"
