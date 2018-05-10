
class Test(object):
    __x = 10

a = Test()
## 访问私有属性
print(a._Test__x)

##  在类里面有下划线的模块在使用from module import * 的无法将带有下划线的属性导入