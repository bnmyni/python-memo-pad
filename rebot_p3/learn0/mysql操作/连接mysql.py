''' 使用python 连接ｍｙｓｑｌ 进行crud操作 '''

import pymysql

db = pymysql.connect('10.1.3.33', 'root', 'root', 'hdc')
cursor = db.cursor()
#
# sql = '''
#     create table t_user(
#     id int,
#     name varchar(200))
#     '''
##  查询
# sql = 'select version()'
sql = "insert into t_user(id,name) values(%d,'%s')" % (2,'aspire')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

### query
query = 'select id, name from t_user'
cursor.execute(query)
for row in cursor.fetchall():
    id = row[0]
    name = row[1]
    print('id : %d; name: %s' % (id, name))

## update
update = "update t_user set name='%s' where id=%d" % ('china', 1)
cursor.execute(update)
# print('update row count : ' + cursor.rowcount())
db.commit()


## delete
delete = "delete from t_user where id = %d" % (2)
cursor.execute(delete)
# print('delete row count : ' + cursor.rowcount())
db.commit()


print('-'*40)
query = 'select id, name from t_user'
cursor.execute(query)
# print('query2 row count : ' + cursor.rowcount())
for row in cursor.fetchall():
    id = row[0]
    name = row[1]
    print('id : %d; name: %s' % (id, name))
