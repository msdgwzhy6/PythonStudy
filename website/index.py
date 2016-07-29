# coding=utf-8

import sys
import os

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask.ext.sqlalchemy import SQLAlchemy

from Form import CalcForm
from Util import Math

# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")

# 配置Flask
app = Flask(__name__)
u = Math()

# 配置数据库
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#创建表
class Calc(db.Model):
    __tablename__ = 'calcs'
    id = db.Column(db.Integer, primary_key=True)
    w = db.Column(db.Float)
    h = db.Column(db.Float)
    BMI = db.Column(db.Float)
db.drop_all()
db.create_all()

#检查表是否创建成功
calc=Calc(w=52,h=165,BMI=u.getBMI(52,165))
print "calc.BMI=", calc.BMI
db.session.add(calc)
db.session.commit()

print Calc.query.all()


@app.route('/')
def index():
    return redirect(url_for('index01'))

@app.route('/index01')
def index01():
    return render_template('index01.html');

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        myForm = CalcForm(request.form)
        if myForm.validate():
            w = myForm.w.data
            h = myForm.h.data
            BMI = u.getBMI(int(w), int(h))
            Desc = u.getDesc(BMI)
            print "Desc=", Desc
            calcTable = Calc(w=w, h=h, BMI=BMI)
            print "calcTable.BMI=", calcTable.BMI
            db.session.add(calcTable)
            db.session.commit()
            return render_template('index.html', w=w, h=h, tvBMI=BMI, tvDesc=Desc)
        else:
            Desc = "请输入正确的身高和体重"
            return render_template('index.html', tvDesc=Desc)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008, debug=True)
