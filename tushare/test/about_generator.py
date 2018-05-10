# -*- coding: utf-8 -*-
# 测试一个生成器
# def myGen():
#     print('exec generator...')
#     yield 1
#     yield 2
#
# # 调用生成器
# g = myGen()
# print(next(g))
# print(next(g))

##  菲波拉契数列  这个在python 2有问题
# def feiber():
#     a = 0
#     b = 1
#     while True:
#         a = b
#         b = a + b
#         yield a
#
# f = feiber()
# print(next(f))
#
# #  列表推导器
# a = [i for i in  range(100) if not i % 2 and i % 3]
# print(a)
# ## 字典推导器
# ab = {i : i % 2 == 0 for i in range(100)}
# print(ab)
#
# # 构造器推导器
# e = (i for i in range(10))
# print(next(e))
#
# print(sum( i for i in range(10) if i % 3))
