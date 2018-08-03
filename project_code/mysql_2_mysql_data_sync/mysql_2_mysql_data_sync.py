#!/bin/bash/python
# -*-coding:utf-8-*-
'''
实现mysql-mysql的数据同步，源库只有读的权限，没有写的权限
'''
import pymysql
import time
import sys
#  单次insert记录数
MAX_INSERT_ROW = 2000


def get_read_conn():
    return pymysql.connect(host="ip1", port=3306, user="user1", passwd="passwd1", db="mysqldb1", charset='utf8')


def get_write_conn():
    return pymysql.connect(host="ip2", port=3306, user="user2", passwd="passwd2", db="mysqldb2", charset='utf8')


def read_table_data(sql):
    """从蝉道中查询数据"""
    rdb = get_read_conn()
    try:
        rcursor = rdb.cursor()
        rcursor.execute(sql)
        result = rcursor.fetchall()
        return result
    except:
        print ""
    finally:
        rdb.close()


def clear_and_bak_table(table_name):
    wdb = get_write_conn()
    wcursor = wdb.cursor()
    # bak_table_name = "%s_%s" % (table_name, time.strftime("%Y%m%d%H", time.localtime()))
    # wcursor.execute("drop table if exists %s" % bak_table_name)
    # wcursor.execute("create table %s select * from %s where 1=1" % (bak_table_name, table_name))
    wcursor.execute("delete from %s" % table_name)
    wdb.commit()
    wdb.close()


def excute_update(table_name, r_sql, w_sql, ncols):
    """全量更新表数据 """
    clear_and_bak_table(table_name)
    add_list = []
    wdb = get_write_conn()
    wcursor = wdb.cursor()

    for row in read_table_data(r_sql):
        if "zt_story" == table_name and int(row[3]) > sys.maxint:
            add_list.append((row[0], row[1], row[2], 0))
        else:
            add_list.append([row[i] for i in range(ncols)])
        if add_list.__len__() >= MAX_INSERT_ROW:
            wcursor.executemany(w_sql, add_list)
            wdb.commit()
            del add_list[:]

    if add_list:
        wcursor.executemany(w_sql, add_list)
        wdb.commit()

    wdb.close()


def update_data(table_name, cols, ncols):
    r_sql = "select %s from v_%s" % (cols, table_name)
    w_sql = "insert into %s(%s)values(%s)" % (table_name, cols, ','.join(["%s" for i in range(ncols)]))
    excute_update(table_name, r_sql, w_sql, ncols)


if __name__ == "__main__":
    while True:
        cur_time = time.strftime("%H", time.localtime())
        if cur_time == "01" or cur_time == "03":
            update_data("zt_bugs", "_id,_type,_sum", 3)
            update_data("zt_build", "_id,_num,_start_date,_end_date,_released_date,_sub_id", 6)
            update_data("zt_man_haur", "_story_id,_quantity", 2)
            update_data("zt_project", "_id,_name", 2)
            update_data("zt_story","_id,_story_id,_content,_workload", 4)
            update_data("zt_sub_project", "_id,_sub_id,_name", 3)
            print "____end____"
        time.sleep(60*50)