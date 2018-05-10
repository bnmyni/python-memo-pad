'''
通过__slots  来限定对象，不允许类的对象动态的添加属性，即去python动态性质
'''
class DbConn(object):
    __slots__ = ('name','age')


d = DbConn()
## 这里就直接报错了，无法添加
d.address = 44
print(d.address)