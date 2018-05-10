# -*- coding: utf-8 -*-
import tushare as ts

'''
获取单月电影票房数据，默认为上一月，可输入月份参数获取指定月度的数据。

参数说明：

date:年月(YYYY-MM),默认为上一月
返回值说明：

Irank 排名
MovieName 电影名称
WomIndex 口碑指数
avgboxoffice 平均票价
avgshowcount 场均人次
box_pro 月度占比
boxoffice 单月票房(万)
days 月内天数
releaseTime 上映日期
'''

## #取上一日的数据
data = ts.month_boxoffice()
print(data)
#df = ts.month_boxoffice('2015-10') #取2015年10月的数据