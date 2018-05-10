# -*- coding: utf-8 -*-
import tushare as ts

'''
获取单日电影票房数据，默认为上一日的电影票房，可输入参数获取指定日期的票房。

参数说明：

date: 日期（YYYY-MM-DD）,默认为上一日
返回值说明：

AvgPrice 平均票价
AvpPeoPle 场均人次
BoxOffice 单日票房（万）
BoxOffice_Up 环比变化 （%）
IRank 排名
MovieDay 上映天数
MovieName 影片名
SumBoxOffice 累计票房（万）
WomIndex 口碑指数
'''

## #取上一日的数据
data = ts.day_boxoffice('2018-01-01')
print(data)
#df = ts.day_boxoffice('2015-12-24')  #取指定日期的数据