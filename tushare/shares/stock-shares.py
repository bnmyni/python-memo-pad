# -*- coding: utf-8 -*-
import tushare as ts
'''返回值说明：

code：股票代码
name：股票名称
c_name：行业名称'''
print('行业分类')
print(ts.get_industry_classified())

'''返回值说明：

code：股票代码
name：股票名称
c_name：概念名称'''

print('概念分类')
print(ts.get_concept_classified())

'''按地域对股票进行分类，即查找出哪些股票属于哪个省份。

参数说明：

file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。
返回值说明：

code：股票代码
name：股票名称
area：地域名称'''

print('地域分类')
print(ts.get_area_classified())

''''获取中小板股票数据，即查找所有002开头的股票

参数说明：

file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。
返回值说明：

code：股票代码
name：股票名称'''
print('中小板股票分类')
print(ts.get_sme_classified())

'''获取创业板股票数据，即查找所有300开头的股票

参数说明：

file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。
返回值说明：

code：股票代码
name：股票名称'''

print('创业板股票分类')
print(ts.get_gem_classified())

'''获取风险警示板股票数据，即查找所有st股票

参数说明：

file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。
返回值说明：

code：股票代码
name：股票名称'''

print('创业板股票分类')
print(ts.get_st_classified())

'''获取沪深300当前成份股及所占权重

返回值说明：

code :股票代码
name :股票名称
date :日期
weight:权重'''
print('沪深300成份及权重')
print(ts.get_hs300s())

'''获取上证50成份股

返回值说明：

code：股票代码
name：股票名称'''
print('上证50成份股')
print(ts.get_sz50s())

'''获取中证500成份股

返回值说明：

code：股票代码
name：股票名称'''

print('中证500成份股')
print(ts.get_zz500s())

'''获取已经被终止上市的股票列表，数据从上交所获取，目前只有在上海证券交易所交易被终止的股票。

返回值说明：

code：股票代码
name：股票名称
oDate:上市日期
tDate:终止上市日期'''
print('终止上市股票列表')
print(ts.get_terminated())

''''获取被暂停上市的股票列表，数据从上交所获取，目前只有在上海证券交易所交易被终止的股票。

返回值说明：

code：股票代码
name：股票名称
oDate:上市日期
tDate:暂停上市日期'''
print('暂停上市的股票列表')
print(ts.get_suspended())