# -*- coding: utf-8 -*-
class Person(list):
    __sex = '人妖'
    name = 'bnmyni'
    age = 20
    address = 'china'

    def say(self, words):
        print("{0} say : {1}".format(self.name, words))

bnmyni = Person()
bnmyni.say('just do it')
bnmyni.append("aaa")
print(bnmyni)
## 私有成员变量访问方式，即python没有严格意义上的私有变量，所有的成员变量和方法都是公有的
print(bnmyni._Person__sex)