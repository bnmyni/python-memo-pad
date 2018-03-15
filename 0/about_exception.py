# -*- coding: utf-8 -*-
## 你永远不要相信你的用户
# file_name = input('请输入文件名称:')
# f = open(file_name)
#
# for line in f:
#     print(line)

def try_exce_finally_block():
    try:
        print(1/0)
    except ZeroDivisionError as reason:
        print(str(reason))
    finally:
        print("this is finally")

def raise_block():
    try:
        raise ZeroDivisionError
    except:
        print("oh my god")
    finally:
        print("don't worry")

raise_block()