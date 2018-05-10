# -*- coding: utf-8 -*-
import tushare as ts
'''
按年度、季度获取盈利能力数据，结果返回的数据属性说明如下：

code,代码
name,名称
roe,净资产收益率(%)
net_profit_ratio,净利率(%)
gross_profit_rate,毛利率(%)
net_profits,净利润(万元)
esp,每股收益
business_income,营业收入(百万元)
bips,每股主营业务收入(元)

'''
data = ts.get_profit_data(2017,3)
print(data)