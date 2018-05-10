# -*- coding: utf-8 -*-
# 来一只可爱的小蜘蛛吧 python 3.4 版本
import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入需要翻译的内容:")
    url = "www.baidu.com"

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.6'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'utf-8'
    data['typeResult'] = 'true'
    data = urllib.parse.urlencode(data).encode("utf-8")

    req = urllib.request.Request(url, data, head)
    ## 或者
    #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print(target)
    ##  休眠5s
    time.sleep(5)