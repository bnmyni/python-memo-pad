# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
import tushare as ts
'''
pandas提供了将数据便捷存入关系型数据库的方法，在新版的pandas中，主要是已sqlalchemy方式与数据建立连接，支持MySQL、Postgresql、Oracle、MS SQLServer、SQLite等主流数据库。本例以MySQL数据库为代表，展示将获取到的股票数据存入数据库的方法,其他类型数据库请参考sqlalchemy官网文档的create_engine部分。

常用参数说明：

name:表名，pandas会自动创建表结构
con：数据库连接，最好是用sqlalchemy创建engine的方式来替代con
flavor:数据库类型 {‘sqlite’, ‘mysql’}, 默认‘sqlite’，如果是engine此项可忽略
schema:指定数据库的schema，默认即可
if_exists:如果表名已存在的处理方式 {‘fail’, ‘replace’, ‘append’},默认‘fail’
index:将pandas的Index作为一列存入数据库，默认是True
index_label:Index的列名
chunksize:分批存入数据库，默认是None，即一次性全部写人数据库
dtype:设定columns在数据库里的数据类型，默认是None

'''
df = ts.get_tick_data('600848', date='2014-12-22')
engine = create_engine('mysql://user:passwd@127.0.0.1/db_name?charset=utf8')

#存入数据库
df.to_sql('tick_data',engine)

#追加数据到现有表
#df.to_sql('tick_data',engine,if_exists='append')