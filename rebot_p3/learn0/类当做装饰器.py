'''
class Test(object):
    def __call__(self, *args, **kwargs):
        print('call  test')

t = Test()
t() ### 类里面定义了__call__方法，那么对象就可以直接作为方法进行执行
'''

### 装饰器是用一个可执行方法去装饰另外一个方法
## 由于类有了__call__方法以后，类的对象也变成了一个可执行的方法了，因此类装饰器相当于创建了一个类对象，而类对象又是可以执行的方法
class Test(object):
    def __init__(self, func):
        print('--init Test---')
        self.__func = func
    def __call__(self, *args, **kwargs):
        print('---装饰器功能---')
        self.__func()

@Test
def show():
    print('---show----')

show()
