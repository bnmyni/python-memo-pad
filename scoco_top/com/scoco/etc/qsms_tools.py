# -*- coding: utf-8 -*-
from qcloudsms_py import SmsSingleSender
from qcloudsms_py import SmsMultiSender
from qcloudsms_py.httpclient import HTTPError


appid = 1400137637
appkey = "de9f39790286d61c9a21f7e1dfbcba65"
phone_numbers = ["13530853995", "18938092312"]
template_id = 188025
sms_sign = "孙科技术分享"


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



def send_more_with_template(params):
    msender = SmsMultiSender(appid, appkey)
    # params = ["8888", "登录", "0"]
    try:
        result = msender.send_with_param(86, phone_numbers, template_id, params, sign=sms_sign, extend="", ext="")
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

    print(result)


if __name__ == "__main__":
    # send_one_with_template()
    send_more_with_template()