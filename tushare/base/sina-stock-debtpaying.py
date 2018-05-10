# -*- coding: utf-8 -*-
import tushare as ts
'''
按年度、季度获取偿债能力数据，结果返回的数据属性说明如下：

code,代码
name,名称
currentratio,流动比率
quickratio,速动比率
cashratio,现金比率
icratio,利息支付倍数
sheqratio,股东权益比率
adratio,股东权益增长率

'''
data = ts.get_debtpaying_data(2017,3)
print(data)