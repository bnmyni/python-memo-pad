# def Test(name):
#     if name == 'foo':
#         class Foo(object):
#             pass
#         return Foo
#     else:
#         class Apple(object):
#             pass
#         return Apple
#
# class Hello(object):
#     pass
#
# t = Test('foo')
# print(type(t))
# t2 = Test('apple')
# print(type(t2))
#
# hello = Hello()
# print(type(hello))

class Animal(object):
    
    def eat(self):
        print('---eat-----')

Dog = type("Dog", (Animal,), {"name":"wangcai"})
dog = Dog()
print(dog.name)
dog.eat()

print(dog.__class__) ### 对象由类创建
print(Dog.__class__) ### l类由
print(type.__class__)