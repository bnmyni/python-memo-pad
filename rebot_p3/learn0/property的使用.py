
class Test(object):
    def __init__(self):
        print('init')
        self.__num = 100

    def getNum(self):
        print('getNum')
        return self.__num

    def setNum(self, value):
        print('setNum')
        self.__num = value

    ### 使用property
    num = property(getNum, setNum)

test = Test()
# print(test.getNum())
# test.setNum(200)
# print(test.getNum())

## 这里是需要调用init和setNum方法
test.num = 3000
## 这里需要调用init和getNum方法
print(test.num)