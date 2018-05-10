##  运用闭包，把一个函数作为变量传入到闭包体里面
##  类似拦截器，切面编程
def w1(func):
    def inner():
        f2()
        func()
    return inner

def f2():
    print('-----findbug----')

### 在使用 @w1 的时候，一定要把w1函数定义在前面，否则会报错
## 这里的  @w1是一个装饰器，@w1 等价于 rst = w1(f1)
@w1
def f1():
    print('----f1-----')

f1()
