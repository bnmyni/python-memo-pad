# -*- coding: utf-8 -*-
## 通过属性访问属性
class Test(object):
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, size):
        self.size = size
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)

# t = Test()
# t.x = 1
# print(t.x)
print 'hahh', 'heihei'