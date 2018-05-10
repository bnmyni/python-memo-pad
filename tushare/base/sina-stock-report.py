# -*- coding: utf-8 -*-
import tushare as ts
'''
按年度、季度获取业绩报表数据。数据获取需要一定的时间，网速取决于您的网速，请耐心等待。结果返回的数据属性说明如下：

code,代码
name,名称
esp,每股收益
eps_yoy,每股收益同比(%)
bvps,每股净资产
roe,净资产收益率(%)
epcf,每股现金流量(元)
net_profits,净利润(万元)
profits_yoy,净利润同比(%)
distrib,分配方案
report_date,发布日期

'''
#获取2014年第3季度的业绩报表数据
data = ts.get_report_data(2017,3)
print(data)