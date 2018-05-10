## 不借助中间值来交换a，b的值
a = 10
b = 20
a = a + b
b = a - b
a = a - b

## python的方式
a, b = b, a