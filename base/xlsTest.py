# coding:utf-8
import re
import sys
import time, datetime

reload(sys)
sys.setdefaultencoding("utf-8")

import os

import tablib
head= ['area', 'user', 'recharge']
print "head=",head

data = [
    ('1', 'Rooney', 20),
    ('2', 'John', 30),
]
print "data=",data

class Item():
    def __init__(self,head1,head2,head3):
        self.head1=head1
        self.head2=head2
        self.head3=head3


head=[]
# data=[]

for i in range(1,4):
    head.append("head"+str(i))
print "head=",head

for j in range(1,5):
    head1="data"+str(j)+"#"+str(1)
    head2="data"+str(j)+"#"+str(2)
    head3="data"+str(j)+"#"+str(3)
    item=str(Item(head1,head2,head3))
    print "item=",item
    data.append(item)
print "data=",data

file = tablib.Dataset(*data, headers=head)

#然后就可以通过下面这种方式得到各种格式的数据了。
# data.xlsx
# data.xls
# data.ods
# data.json
# data.yaml
# data.csv
# data.tsv
# data.html

#增加行
# data.append(['3', 'Keven',18])
#增加列
# data.append_col([22, 20,13], header='Age')
#删除行
# del data[1:3]
#删除列
# del data['Age']

print file.csv
print file.json

open('xxx.xls', 'wb').write(file.xls)