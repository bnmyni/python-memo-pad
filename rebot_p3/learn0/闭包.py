
# 在一个函数里面定义一个内部函数，并且内部函数用到了外层函数的变量，外部函数变量和内部函数统称为闭包
# def test(value):
#     def test_in(value_in):
#         return value + value_in
#     return test_in
#
#
# rst = test(100)
#
# print(rst(100))
# print(rst(200))

## 闭包的运用  : 构造 f(x) = x + 1 线性方程
def fn(a, b):
    def line(x):
        return a*x + b
    return line

line1 = fn(1, 1)
print(line1(5))