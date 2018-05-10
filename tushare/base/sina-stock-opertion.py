# -*- coding: utf-8 -*-
import tushare as ts
'''
按年度、季度获取营运能力数据，结果返回的数据属性说明如下：

code,代码
name,名称
arturnover,应收账款周转率(次)
arturndays,应收账款周转天数(天)
inventory_turnover,存货周转率(次)
inventory_days,存货周转天数(天)
currentasset_turnover,流动资产周转率(次)
currentasset_days,流动资产周转天数(天)

'''
data = ts.get_operation_data(2017,3)
print(data)