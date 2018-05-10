# -*- coding: utf-8 -*-
import tushare as ts
'''
获取个股信息地雷数据。

参数说明：

code:股票代码
date:信息公布日期
返回值说明：

title:信息标题
type:信息类型
date:公告日期
url:信息内容URL
如果获取信息内容，请调用notice_content(url)接口，把url地址作为参数传入即可。
'''
data = ts.get_notices()
print (data)