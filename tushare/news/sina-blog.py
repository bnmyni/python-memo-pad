# -*- coding: utf-8 -*-
import tushare as ts
'''
获取sina财经股吧首页的重点消息。股吧数据目前获取大概17条重点数据，可根据参数设置是否显示消息内容，默认情况是不显示。

参数说明：

show_content:boolean,是否显示内容，默认False
返回值说明：

title, 消息标题
content, 消息内容（show_content=True的情况下）
ptime, 发布时间
rcounts,阅读次数
'''
data = ts.guba_sina(True)
print (data)

## 如果要查看内容，方法如下：
print data.ix[3]['content'] #第3条消息的内容