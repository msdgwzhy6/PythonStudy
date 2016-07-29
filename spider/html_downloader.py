# coding=utf-8

import urllib2

class HtmlDownloader():
    def __init__(self):
        pass
    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        html_read = response.read()
        return html_read


def test():
    url = u"http://baike.baidu.com/view/21087.htm"
    downLoader = HtmlDownloader()
    html_read = downLoader.download(url)
    return html_read

# print test()



