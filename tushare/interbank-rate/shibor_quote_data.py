# -*- coding: utf-8 -*-
import tushare as ts

'''
获取银行间报价数据，目前只提供2006年以来的数据。

参数说明：

year:年份(YYYY),默认为当前年份
返回值说明：

date:日期
bank:报价银行名称
ON:隔夜拆放利率
ON_B:隔夜拆放买入价
ON_A:隔夜拆放卖出价
1W_B:1周买入
1W_A:1周卖出
2W_B:买入
2W_A:卖出
1M_B:买入
1M_A:卖出
3M_B:买入
3M_A:卖出
6M_B:买入
6M_A:卖出
9M_B:买入
9M_A:卖出
1Y_B:买入
1Y_A:卖出
'''

df = ts.shibor_quote_data(2017)
#直接保存
#df = ts.shibor_data(2014) #取2014年的数据
#df.sort('date', ascending=False).head(10)

print(df)