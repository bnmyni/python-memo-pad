# -*- coding: utf-8 -*-
import time as t
class MyTimer(object):
    '简易计时器'
    flag = False
    count = 0
    def __str__(self):
        if self.flag:
            print("计时器已开启")
        else:
            print("请开启计时器")

    def __add__(self, other):
        return self.count + other

    def start(self):
        if self.flag:
            print("计时器已开启")
        else:
            self.s = t.localtime()

    def stop(self):
        if self.flag:
            self.e = t.localtime()
        else:
            print("计时器已关闭")