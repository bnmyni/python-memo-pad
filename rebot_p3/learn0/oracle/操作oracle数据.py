import cx_Oracle

#建立和数据库系统的连接
conn = cx_Oracle.connect('goa/goa@10.1.5.12:1522/ora10g')
#获取操作游标
cursor = conn.cursor()
#执行SQL,创建一个表
cursor.execute("""select * from t_user_code""")

for row  in cursor.fetchall():
    print('用户%s归属项目为%s' % (row[0], row[1]))
#关闭连接，释放资源
cursor.close()
#执行完成，打印提示信息
print('end')


