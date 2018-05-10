# -*- coding: utf-8 -*-
import tushare as ts
'''
pandas将数据保存为MicroSoft Excel文件格式。

常用参数说明：

excel_writer: 文件路径或者ExcelWriter对象
sheet_name:sheet名称，默认为Sheet1
sep : 文件内容分隔符，默认为,逗号
na_rep: 在遇到NaN值时保存为某字符，默认为’‘空字符
float_format: float类型的格式
columns: 需要保存的列，默认为None
header: 是否保存columns名，默认为True
index: 是否保存index，默认为True
encoding: 文件编码格式
startrow: 在数据的头部留出startrow行空行
startcol :在数据的左边留出startcol列空列

'''
df = ts.get_hist_data('000875')
#直接保存
df.to_excel('D:/000875.xlsx')

#设定数据位置（从第3行，第6列开始插入数据）
##df.to_excel('c:/day/000875.xlsx', startrow=2,startcol=5)