import types
class Person(object):

    __f = 600

    def __init__(self, name, age):
        self.name = name
        self.age = age

def c():
    print('---c---')

p = Person('xiaohong', 22)
## 动态添加属性
p.a = 90
## 动态添加方法
p.c = c
p.c()
print(p.a)

## 绑定一个带self的方法
def eat(self):
    print('%s 正在吃饭' % self.name)
## 这里会失败，因为没有self
# p.eat = eat
p.eat = types.MethodType(eat, p)
p.eat()

## 动态添加的属性都是public的，无法添加私有属性
p.__d = 400
print(p.__d)

