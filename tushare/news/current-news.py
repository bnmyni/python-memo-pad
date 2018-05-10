# -*- coding: utf-8 -*-
import tushare as ts
'''获取即时财经新闻，类型包括国内财经、证券、外汇、期货、港股和美股等新闻信息。数据更新较快，使用过程中可用定时任务来获取。

参数说明：

top:int，显示最新消息的条数，默认为80条
show_content:boolean,是否显示新闻内容，默认False
返回值说明：

classify :新闻类别
title :新闻标题
time :发布时间
url :新闻链接
content:新闻内容（在show_content为True的情况下出现）

如果需要单独获取新闻内容，可以调用latest_content(url)方法，将上一步获取到的新闻链接传递进来

'''
data = ts.get_latest_news(80, show_content=True)
print (data[['url']])