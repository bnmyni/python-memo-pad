# -*- coding: utf-8 -*-
# 来一只可爱的小蜘蛛吧 python 2.7 版本
import urllib2
import os
url = 'http://www.baidu.com'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
html = response.read()

print html

saveDir = 'images'

os.mkdir(saveDir)
os.chdir(saveDir)