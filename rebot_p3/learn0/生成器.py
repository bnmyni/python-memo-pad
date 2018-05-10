'''
将一个需要大内存的列表，通过单步生成的方式来逐个生成

## 如果直接构造一个 x for x in range(999999999999999999999999)
# g = (x for x in range(999999999999999999999999))
# print(next(g))
# print(next(g))

## 通过生成器来生成菲波拉碶数列
## 第一版
def fab(max):
    n , a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1

# fab(5)

def fab2(max):
    n , a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n += 1
    return L


def fab3(max):
    n , a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

# for n in fab3(5):
#     print(n)

f = fab3(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
'''
# def test():
#     i  =  0
#     while i < 5:
#         if i == 0:
#             tmp = yield i
#         else:
#             yield i
#         i += 1
# t = test()
# ## 可以使用__next__也可以使用send去获取生成器里面的值
# print(t.send(None))
# print(t.send('aspire'))


