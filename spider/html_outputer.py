# -*- coding: UTF-8 -*-
'''
Created on 2016-3-22

@author: CaoPeng
'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', mode='w')
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset=\"UTF-8\">")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")
        count = 0
        for data in self.datas:
            print "%s" % count
            fout.write("<tr>")
            fout.write("<td>%d</td>" % count)
            fout.write("<td>%s</td>" % data['url'])
            print "<td>%s</td>" % data['title']
            fout.write("<td>%s</td>" % data['title'])
            print "<td>%s</td>" % data['summary']
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
            count = count + 1

        fout.write("</table>")
        fout.write("</html>")
        fout.write("</html>")


import html_parser


def test():
    new_urls, new_data = html_parser.test()
    html_outputer = HtmlOutputer()
    html_outputer.collect_data(new_data)
    html_outputer.output_html()


# test()
