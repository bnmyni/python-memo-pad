a = 100
b = 100
c = 100

## [-5,257)之间使用的是小整数对象池，在python运行的时候已经创建了

## 大整数对象池，只预留了空间，在创建的时候创建

## python采⽤的是引⽤计数机制为主，标记-清除和分代收集两种机制为辅的策略

## cpython 解释器
## javapython解释器
# python⾥每⼀个东⻄都是对象，它们的核⼼就是⼀个结构体： PyObject
# typedef struct_object {
# int ob_refcnt;
# struct_typeobject *ob_type;
# } PyObject;

''''
引用计数垃圾回收优缺点分析
优点：
    1.简单
    2.实时，为0即可删除，无需等待
缺点：
    1.消耗大
    2.无法解决循环引用带来的致命问题（所以需要引入标记清除，分代等机制）
    
GC工作任务：
    1.为新的对象分配空间
    2.识别垃圾
    3.删除垃圾

Ruby垃圾回收机制
    1.分配机制： 先申请一个链表
    2.回收：标记--整理
'''

# import sys
# a = 'aspire'
# print(sys.getrefcount(a))

'''
触发垃圾回收的3种方式：
    1.调用gc.collect()
    2.gc模块计数器达到阀值
    3.程序退出
'''


