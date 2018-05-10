# -*- coding: utf-8 -*-
import tushare as ts

'''
获取贷款基础利率（LPR）数据，目前只提供2013年以来的数据。

参数说明：

year:年份(YYYY),默认为当前年份
返回值说明：

date:日期
1Y:1年贷款基础利率
'''

df = ts.lpr_data()
##df.sort('date', ascending=False).head(10)
print(df)

'''获取贷款基础利率均值数据，目前只提供2013年以来的数据。

参数说明：

year:年份(YYYY),默认为当前年份
返回值说明：

date:日期
1Y_5:5日均值
1Y_10:10日均值
1Y_20:20日均值'''

data = ts.lpr_ma_data() #取当前年份的数据
print(data)