# -*- coding: utf-8 -*-
import tushare as ts

'''
pandas的DataFrame和Series对象提供了直接保存csv文件格式的方法，通过参数设定，轻松将数据内容保存在本地磁盘。

常用参数说明：

path_or_buf: csv文件存放路径或者StringIO对象
sep : 文件内容分隔符，默认为,逗号
na_rep: 在遇到NaN值时保存为某字符，默认为’‘空字符
float_format: float类型的格式
columns: 需要保存的列，默认为None
header: 是否保存columns名，默认为True
index: 是否保存index，默认为True
mode : 创建新文件还是追加到现有文件，默认为新建
encoding: 文件编码格式
date_format: 日期格式
注：在设定path时，如果目录不存在，程序会提示IOError，请先确保目录已经存在于磁盘中

'''

df = ts.get_hist_data('000875')
#直接保存
df.to_csv('D:/000875.csv')

#选择保存
#df.to_csv('c:/day/000875.csv',columns=['open','high','low','close'])