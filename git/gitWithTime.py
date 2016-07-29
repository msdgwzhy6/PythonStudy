# coding:utf-8
# yutianran 16/7/29 上午11:35

import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")

import time, datetime


class Res():
    def __init__(self, msg, date, time):
        self.msg = msg
        self.date = date
        self.time = time


class ResOuter():
    def __init__(self):
        self.resList = []
        self.lastData = ""
        self.lastTime = 0.0
        self.index = 1

    def collect(self, res):
        if res is None: return
        self.resList.append(res)

    def save(self, filename):
        path = "/Users/yutianran/Python/git/res"
        if os.path.exists(path) == False:
            os.mkdir(path)
        os.chdir(path)

        # 生成周报.txt
        fos = open(filename + '.txt', 'wb')
        for res in reversed(self.resList):
            if res.msg == "init":
                continue

            if res.date == self.lastData:
                h = (res.time - self.lastTime) / 3600.0
                x = h - int(h)
                if x < 0.5:
                    t = int(h) + 0.5
                else:
                    t = int(h) + 1
                if t > 2:
                    t = 2
                self.index += 1
                fos.write(str(self.index) + "." + res.msg + "(" + str(t) + "h)" + "\n")
                self.lastData = res.date
                self.lastTime = res.time
            else:
                t = 1
                self.index = 1
                fos.write("\n" + res.date + "\n" + "\n")
                fos.write(str(self.index) + "." + res.msg + "(" + str(t) + "h)" + "\n")
                self.lastData = res.date
                self.lastTime = res.time
        fos.close()


def parseLine(line):
    log = line.split("#")
    m = log[0]
    t = float(log[2].split(" ")[0])
    d = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t))
    r = d.split(" ")[0]
    return Res(m, r, t)


def getGirReport(name):
    path = "/Users/yutianran/Android/CarMall"
    os.chdir(path)
    cmd = 'git log --date=raw --pretty=format:"%s#%an#%ad" --no-merges --since=5.days  --author=' + name
    stream = os.popen(cmd)
    lines = stream.readlines()
    resOuter = ResOuter()
    for line in lines:
        res = parseLine(line)
        resOuter.collect(res)
    resOuter.save("周报-" + name)
    print "生成", name, "的周报:完成"


if __name__ == "__main__":
    y = 'Yutianran'  # 余天然
    l = 'Lichangbo'  # 李长波
    z = 'zhoumingche'  # 周明澈
    w = 'wangyiming'  # 王一鸣
    getGirReport(w)
