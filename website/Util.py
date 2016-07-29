# coding=utf-8
class Math():
    def __init__(self):
        self

    def getBMI(self, w, h):
        BMI = w / pow(h / 100.0, 2)
        return BMI

    def getDesc(self, BMI):
        if BMI < 18.5:
            res = "偏瘦"
        elif BMI >= 18.5 and BMI < 25:
            res = "正常体重"
        elif BMI >= 25 and BMI < 30:
            res = "偏胖"
        elif BMI >= 30 and BMI > 35:
            res = "轻度肥胖"
        elif BMI >= 35 and BMI < 40:
            res = "中度肥胖"
        elif BMI > 40:
            res = "重度肥胖"
        return res
