# -*- coding: utf-8 -*-
import urllib2
import random
import re
import com.scoco.etc.qsms_tools as smsTools
import time
from qcloudsms_py import SmsSingleSender
from qcloudsms_py import SmsMultiSender
from qcloudsms_py.httpclient import HTTPError


appid = 1400137637
appkey = "de9f39790286d61c9a21f7e1dfbcba65"
phone_numbers = ["13530853995", "18938092312"]
template_id = 188025
sms_sign = "孙科技术分享"


def get_etc_price():
    url = 'https://www.feixiaohao.com/currencies/ethereum-classic/'
    ua_list = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
    ]
    user_agent = random.choice(ua_list)
    headers = {"User-Agent": user_agent}
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()
    # 下面是python 3 的
    # req = urllib.request.Request(url)
    # req.add_header('User-Agent', user_agent)
    # response = urllib.request.urlopen(req)
    # content = str(response.read(), "utf8")
    return re.search("<div class=coinprice>￥[\d\.]+", content).group().split("￥")[1]

    
def send_one_with_template(etc_price):
    template_id = 188004
    ssender = SmsSingleSender(appid, appkey)
    params = [etc_price]
    try:
        result = ssender.send_with_param(86, phone_numbers[0], template_id, params, sign=sms_sign, extend="", ext="")
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

    print(result)
    

if __name__ == "__main__":
    while True:
        etc_price = get_etc_price()
        print(etc_price)
        if float(etc_price) >= float(120):
            smsTools.send_one_with_template(etc_price)
        time.sleep(60*5)
