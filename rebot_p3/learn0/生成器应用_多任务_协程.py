
## 多任务-- 协程

def pro1():
    while True:
        print('---1----')
        yield None

def pro2():
    while True:
        print('---2---')
        yield None

t2 = pro2()
t1 = pro1()

while True:
    t1.__next__()
    t2.__next__()