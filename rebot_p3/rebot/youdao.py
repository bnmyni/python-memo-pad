### 有道翻译
##
import urllib.request
import urllib.parse
import json
import time
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
## 设置 user-agent
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

data ={}
data['i']= 'i love you'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTIME'
data['typoResult'] = 'false'
data = urllib.parse.urlencode(data).encode('utf-8')

print(data)
req = urllib.request.Request(url, data, head)
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
# 休眠1s
time.sleep(1)
print(json.loads(html))
