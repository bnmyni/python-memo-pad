import urllib.request
# response = urllib.request.urlopen('http://img.ivsky.com/img/tupian/co/201712/31/dianxian-011.jpg')
#
# html = response.read()
# with open('001.jpg', 'wb') as f:
#     f.write(html)

## 图片下载
req = urllib.request.Request('http://img.ivsky.com/img/tupian/co/201712/31/kanhai_ren-009.jpg')
response = urllib.request.urlopen(req)
html = response.read()

print(response.geturl())
print(response.info())
print(response.getcode())
with open('aa.jpg', 'wb') as f:
    f.write(html)
