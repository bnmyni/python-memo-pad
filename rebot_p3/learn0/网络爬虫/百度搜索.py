from urllib.parse import urlencode

# url = 'https://www.baidu.com/s?'
wd = {"wd": "百度"}
print(urlencode(wd))