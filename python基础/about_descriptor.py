class MyDescriptor(object):
    def __get__(self, instance, owner):
        print("geting")

    def __set__(self, instance, value):
        print('seting')

    def __delete__(self, instance):
        print('del ... ')

class Test(object):
    x = MyDescriptor()


t = Test()
t.x = 'xxxxx'
print(t.x)
del t.x