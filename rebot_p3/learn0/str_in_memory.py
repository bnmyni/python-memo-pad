
import sys
d = 'aspire'
## 获取字符串的引用数
print(sys.getrefcount('aspire'))
e = 'aspire'
print(sys.getrefcount('aspire'))
f = e
print(sys.getrefcount('aspire'))
d = 1
print(sys.getrefcount('aspire'))
e = f = 3
print(sys.getrefcount('aspire'))
## 批量赋值&& 删除
a, b, c = 'aspire', 'inspire', 'china'
del a, b, c

# 常用的方法
# type() help() dir()

