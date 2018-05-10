class Test(object):

    def __init__(self):
        print('init')
        self.__money = 100

    ## 使用装饰器
    @property
    def money(self):
        print('get')
        return self.__money

    ## 说明该方法是money属性的set方法
    @money.setter
    def money(self,value):
        print('set')
        self.__money = value

test = Test()
test.money = 999
print(test.money)


