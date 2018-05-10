# -*- coding: utf-8 -*-
class CountList(object):
    '模拟一个不可变列表的计数'
    def __init__(self, *args):
        self.values = [x for x in args]
        self.cunt = [0]* len(self.values)
    def __len__(self):
        return len(self.values)
    def __getitem__(self, item):
        self.cunt[item] += 1
        return self.values[item]

t = CountList(1,2,3,4,5)
print(t.__len__())
print (t[2])
print (t[2])
print(t.cunt[2])

