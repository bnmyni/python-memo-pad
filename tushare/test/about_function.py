# -*- coding: utf-8 -*-
# def add_1(a, b):
#     'this fuction has return'
#     return a + b
#
# def say(name, words = 'haha'):
#     print(name + '->' + words)
#
# def test(*params):
#     print(len(params))
#
# say(name='sunke', words='hehe')
#
# say(name='xijinping')
#
# test(7,'hha','sunke','heihei')
#
# def moreReturnTest():
#     status = 'normal'
#     code = 200
#     return code, status;
#
# print(moreReturnTest())

# def discount(price, rate):
#     final_price = price * rate
#     return final_price
#
# old_price = float(input("old_price:"))
# rate = float(input("rate:"))
# new_price = discount(old_price, rate)
# print("new_price:", new_price)

# ## 嵌套函数
# def fun1():
#     print("exec fun1()")
#     def fun2():
#         print("exec fun2()")
#     fun2()
#
# fun1()

## 闭包
# def funx(x):
#     def funy(y):
#         return x*y
#     return funy
#
# print(funx(8))
# print(funx(5)(8))

## 匿名函数 lambda表达式
# lambda x : 2 * x + 1
# g = lambda x : 2 *x + 1
# print(g(5))

#
# ## 过滤器  filter
# filter(lambda x : x % 2, range(10))
# ## map
# map(lambda x : x * 2, range(10))

## python 递归层数
# import sys
# sys.setrecursionlimit(2000000)

##  递归求阶层
# def factoial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factoial(n-1)
#
# print(factoial(5))

## 斐波那契数列
# def  Fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
#
# print(Fibonacci(36))

# def fibonacci_it(n):
#     n1 = n2 = n3 = 1
#     while n - 2 > 0:
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#         n -= 1
#     return n3
# print(fibonacci_it(11))

## 汉诺塔算法求解
# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         hanoi(n-1, a, c, b)
#         print(a, '-->', c)
#         hanoi(n - 1, b, a, c)
#
# hanoi(9, 'a', 'b', 'c')

# dict1 = {'a':'aaa','c':'ccc'}
# map2 = {'tt': dict1}
# print(dict1['a'])
# print(map2['tt']['c'])
# print(dict1.values())
# print(dict1.has_key('tttt'))
# print(dict1.keys())
# print(dict1.fromkeys('ccc'))
# map3 = dict()
# # print(map3)
# map3.setdefault('name','aspire')
# # print(map3.get('aaaa', 'bb'))
# print(map3)
#
# print(map3.get('name'))
# map3['hhhh'] = 'dd'
# print(map3)

# map1 = dict()
# map1['a'] = 'aspire'
# map1['b'] = 'baidu'
# map1['c'] = 'chuangwei'
#
# for idx in map1.keys():
#     print(map1[idx])
#
# print(map1.__contains__('a'))

# 文件打开模式
## r 只读 w 可写 x a 写入模式，追加 b 二进制 t 文本模式 + 可读可写模式 U 通配符
# f = open('C:\\Users\\sunke\\Desktop\\aaaa.txt', 'w')
# print(f)
# s1 = f.readline(200)
# print(s1)
# print(f.read())
# print(f.tell())
# f.seek(12,0)
# print(f.read())
# f.seek(0,0)
# print(list(f))

## 模块
# import random as rd
# a = rd.randint(40, 100)
# print(a)

import  os
# print(os.getcwd())
# file_path = 'C:\\Users\\sunke\\Desktop\\aaaa.txt'
# # os.mkdir(file_path)
# # os.rmdir(file_path)
# # os.system('cmd')
# print(os.getcwd())
# print(os.pardir)

## os.path 模块
# print(os.path.basename(file_path))
# print(os.path.dirname(file_path))
# ## 路径连接
# print(os.path.join("D:\\","A","B"))
# print(os.path.split(file_path))
# print(os.path.splitext(file_path))
# print(os.path.getsize(file_path))
# import time
# print(time.gmtime(os.path.getatime(file_path)))
# print(time.gmtime(os.path.getctime(file_path)))
# print(time.gmtime(os.path.getmtime(file_path)))


import pickle
## 写入文件
list1 = ['hhah', 12122, ['test', 'dev']]
pickle_file = open('C:\\Users\\sunke\\Desktop\\b.pkl', 'wb')
pickle.dump(list1, pickle_file)
pickle_file.close()

## 读取文件
pickle_file = open('C:\\Users\\sunke\\Desktop\\b.pkl', 'rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)
pickle_file.close()

