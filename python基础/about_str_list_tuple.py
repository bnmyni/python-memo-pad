# -*- coding: utf-8 -*-
# str1 = "帅哥，您好！"
#
# print(str1[:])
#
# print(len(str1))
#
# str2 = "aspirecn.com"
#
# print(str2.capitalize())
#
# print(str2.swapcase())
# print("SUNKE".lower())
# print("sunke bnmyni".count('n'))
# print("sunke".encode('utf-8'))
# print("sunke".endswith('sunke'))
# print( "sunke".find('ke'))
# print("sunke".index('un'))
# print('13323'.isalnum())
# print('13323'.isdigit())
# print(' '.isspace())
# print(' 1'.isspace())
# print('Aspire In Inspire'.istitle())
# str1 = 'sky'
# print(str1.join('1234567890'))
# print('  sky'.lstrip())
# print('  sky  '.lstrip())
# print('aspire in inspire'.partition('in'))
# print('sunke'.replace('s','p',6))
# print("sunke  in sunke".split())
# print('Aspire'.swapcase())
# print('Aspire'.translate())

## 格式化
# str9 = 'haha';
# str8 = 'i';
# print("{0} love you {1}".format(str8, str9))
# print("{a} love you {b}".format(a = str8, b = str9))
# print("{0} love you {b}".format(str8, b = str9))
# print('{{0}}'.format(str9)) ## 不会被format
# print('{0:.1f}{1}'.format(27.658, 'GB'))
#
# #输出对应的asc码
# print('%c' % 97)
# print('%c %c %c' % (97, 98, 99))
# ## 格式化字符串
# print('%s' % '煞笔')
# ## 格式化整数
# print('%d + %d = %d' % (4, 5, 4+5))
# ## 进制换算
# print('%o' % 8)
# print('%x' % 160)
# print('%X' % 160)
# print('%f' % 234.7834)
# print('%e' % 234.7834)
# print('%E' % 234.7834)
# print('%G' % 23423294729374323.7834)
#
# ## 格式化操作辅助命令
# ##  % m.nf
# print('%5.2f' % 234.7834)
# print('%.2e' % 234.7834)
# print('%10d' % 1)
# print('%+10d' % 1)
# print('%-10d' % 1)
# ## 显示为8进制
# print('%#o' % 72323)
# ## 显示为16进制
# print('%#X' % 72323)
# ##填充
# print('%-010d' % 5)
# print('%+010d' % 5)

a = list()
print(a)

b = 'this is a list'
b = list(b)
print(b)
print(len(b))
print(max(b))

tuple1 = (1,9,2,32,3,2,43,4)
print(min(tuple1))
print(sum(tuple1))
print(sorted(tuple1))
