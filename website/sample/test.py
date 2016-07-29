#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf8")

from Util import Math
u=Math()

import db

from Table import Role
from Table import User
from Table import Calc

db=db.db
db.drop_all()
db.create_all()

role_admin = Role()
role_mod = Role()
role_user = Role()
user_john = User(username='john', role=role_admin)
user_susan = User(username='susan', role=role_user)
user_david = User(username='你好', role=role_user)

db.session.add(role_admin)
db.session.add(role_mod)
db.session.add(role_user)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)
db.session.commit()

print(role_admin)
print(role_mod)
print(role_user)
print(user_john.username)
print(user_susan.username)
print(user_david.username)


# w=52
# h=163
# BMI=u.getBMI(w,h)
# Desc=u.getDesc(BMI)
# calcTable = Calc(w=w, h=h, BMI=BMI,Desc=Desc)
# print "calcTable.BMI=", calcTable.BMI
# db.session.commit()

