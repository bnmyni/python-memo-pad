# -*- coding: utf-8 -*-
import tushare as ts

'''
获取全国影院单日票房排行数据，默认为上一日，可输入日期参数获取指定日期的数据。

参数说明：

date:日期(YYYY-MM-DD),默认为上一日
返回值说明：

Attendance 上座率
AvgPeople 场均人次
CinemaName 影院名称
RowNum 排名
TodayAudienceCount 当日观众人数
TodayBox 当日票房
TodayShowCount 当日场次
price 场均票价（元）
'''
df = ts.day_cinema() #取上一日全国影院票房排行数据
#df = ts.day_cinema('2015-12-24') #取指定日期的数据
print(df.head(10))