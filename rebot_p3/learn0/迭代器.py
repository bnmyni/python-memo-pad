
## 可迭代对象　list tuple set dict str

## 判断是否是一个可以迭代的对象
from collections import Iterable
from collections import Iterator
# a = [1,5,32,323]
# print(isinstance(a, Iterable))
#
# b = 'aspire to inspire'
# print(isinstance(b, Iterable))


####### 是否为迭代器######
isinstance((x for x in range(10)), Iterator)

