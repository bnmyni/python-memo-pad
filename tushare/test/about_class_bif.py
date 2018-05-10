# -*- coding: utf-8 -*-
class A(object):
    pass

class B(A):
    pass

print(issubclass(A, A))
print(issubclass(B, A))

a = A()
print(isinstance(a, A))

b = B()
print(isinstance(b, A))


## 对象属性相关
print(hasattr(b, 'x'))

print(getattr(b, 'x', '不存在的..'))

setattr(b, 'name', 'bnmyni')
print(getattr(b, 'name', '不存在的..'))

delattr(b, 'name')

