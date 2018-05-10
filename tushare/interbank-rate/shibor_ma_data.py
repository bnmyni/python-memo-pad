# -*- coding: utf-8 -*-
import tushare as ts

'''
获取Shibor均值数据，目前只提供2006年以来的数据。

参数说明：

year:年份(YYYY),默认为当前年份
返回值说明：

date:日期
其它分别为各周期5、10、20均价，请参考上面的周期含义
'''

df = ts.shibor_ma_data()
#直接保存
#df = ts.shibor_data(2014) #取2014年的数据
#df.sort('date', ascending=False).head(10)

print(df)