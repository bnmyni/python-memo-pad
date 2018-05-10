import re
# ##  正则表达式查找同类型的数据
# # print(re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '9'))
# # . 匹配任意单个字符，换行除外
# print(re.search(r'.', 'hhe'))
# # | 或运算，匹配任意一个表达式即可
# print(re.search(r'aspire(A|B)', 'aspireA china'))
# print(re.search(r'aspire(A|B)', 'aspireB US'))
# # ^ 开始界定  类似 startWith
# print(re.search(r'^Inspire', 'aspire to Inspire'))
# #  $开始界定  类似 endWith
# print(re.search(r'Inspire$', 'aspire to Inspire'))
# () 标记一个子表达式的开始和结束位置
# print(re.search(r'(aspire)\d', 'www.aspire2aspirecn.com'))
# # 这里的(aspire)\1 相当于 aspireaspire
# print(re.search(r'(aspire)\1', 'www.aspireaspirecn.com'))
# # (aspire)\141 相当于匹配 aspirea,\141 对应的是8进制的 97
# print(re.search(r'(aspire)\141', 'www.aspireaspirecn.com'))

# [] 字符集，将括号里面的都作为一个字符串
# print(re.search(r'[.]', 'www.aspirecn.com'))
# print(re.search(r'\.', 'www.aspirecn.com'))

#  [] + ^ 使用
# 匹配a-z以外的所有字符
# print(re.findall(r'[^a-z]', 'aspire to Inspire ,China'))
# # 匹配a-z中的任意字符
# print(re.findall(r'[a-z^]', 'aspire to Inspire ,China'))

## {m,n} 重复
# print(re.search(r'aspire{3}', 'to  aspireeeeeeeeeeeeee'))
# print(re.search(r'aspire{1,4}', 'to  aspireee'))
# # 这里对应的是整体匹配
# print(re.search(r'(aspire){1,4}', 'to  aspireaspireee'))

# ### * 相当于{0,}
# print(re.search(r'(aspire)*', 'to  a2spireee'))
# ### + 相当于{1,}
# print(re.search(r'(aspire)+', 'to  aspireee'))
# ### ? 相当于{0,1}
# print(re.search(r'A?', 'to  aspire aspire'))

## 正则表达式默认是启用贪婪模式的：即在条件允许的时候，匹配跟多的内容能
# 下面语句将匹配整个的div <div> <a href="www.baidu.com">百度</a></div>
# print(re.search(r'<.+>', 'welcome <div> <a href="www.baidu.com">百度</a></div> this is div'))
#
# ### 启用非贪婪模式 在+后面加上一个问号
# print(re.search(r'<.+?>', 'welcome <div> <a href="www.baidu.com">百度</a></div> this is div'))
# print(re.search(r'(ab)\141', 'a8a9a10a11a0 aba aa 1AK'))

# \A 相当于 ^
# print(re.search(r'\Aaspire','aspire to inspire'))
# # \Z 详单有 $
# print(re.search(r'inspire\Z','heh aspire to inspire'))

## 匹配163 邮箱
email = 'aa@163.com'
result = re.match('[a-zA-Z0-9_]{4,20}@163.com', email)



