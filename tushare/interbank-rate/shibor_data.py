# -*- coding: utf-8 -*-
import tushare as ts

'''
获取银行间同业拆放利率数据，目前只提供2006年以来的数据。

参数说明：

year:年份(YYYY),默认为当前年份
返回值说明：

date:日期
ON:隔夜拆放利率
1W:1周拆放利率
2W:2周拆放利率
1M:1个月拆放利率
3M:3个月拆放利率
6M:6个月拆放利率
9M:9个月拆放利率
1Y:1年拆放利率
'''

df = ts.shibor_data(2018)
#直接保存
#df = ts.shibor_data(2014) #取2014年的数据
#df.sort('date', ascending=False).head(10)

print(df)