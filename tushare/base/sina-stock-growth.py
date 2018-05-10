# -*- coding: utf-8 -*-
import tushare as ts
'''
按年度、季度获取成长能力数据，结果返回的数据属性说明如下：

code,代码
name,名称
mbrg,主营业务收入增长率(%)
nprg,净利润增长率(%)
nav,净资产增长率
targ,总资产增长率
epsg,每股收益增长率
seg,股东权益增长率

'''
data = ts.get_growth_data(2017,3)
print(data)