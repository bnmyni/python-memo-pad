import urllib.request
import os
import random

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')

    iplist = ['47.91.139.78', '50.233.137.34', '116.11.254.37', '50.233.137.32']
    proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    print(html[a:b])
    return html[a: b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    imgs_addrs = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b != -1:
            imgs_addrs.append(html[a+9: b+4])
        else:
            b = a + 9
        a = html.find('img src=', b)

    for each in imgs_addrs:
        print(each)
    return imgs_addrs

def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(url_open(each))

def download_img(folder = 'ooxx', pages = 10):
    os.rmdir(folder)
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = 'http://jandan.net/ooxx/page-%d#comments' % page_num
        print('find_imgs url:', page_url)
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_img()