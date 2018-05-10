import urllib.request
import random

url = 'http://www.whatismyip.com.tw'
## 代理使用三部曲
iplist = ['47.91.139.78','50.233.137.34', '116.11.254.37', '50.233.137.32']

print(random.choice(iplist))

proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)