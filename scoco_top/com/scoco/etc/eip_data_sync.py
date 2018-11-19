import os
import cx_Oracle
import pymssql
import xlrd
import time
os.chdir("D:\soft\instantclient_12_2")


def get_oracle_conn():
    """ 获取oralce连接"""
    tns_name = """goa/goa@(DESCRIPTION =   
                        (ADDRESS = (PROTOCOL = TCP)(HOST = 10.1.5.12)(PORT = 1522))   
                        (CONNECT_DATA =   (SERVER = DEDICATED)     
                        (SERVICE_NAME = ora10g)    )  )"""
    return cx_Oracle.connect(tns_name)


def query_mssql_data(value):
    """从eip sqlserver数据库中查询数据 , value 查询开始时间yyyy/MM/dd"""
    conn = pymssql.connect("10.2.8.25", "u_kf2", "u_kf2", "EIP_Transaction")
    curs = conn.cursor()
    sql = """
          select a.USER_NO,a.USER_Name_ZH,a.USER_LoginName,a.FULL_NAME,a.BusinessUnit,a.WorkingDate,
          a.WorkingStar,a.WorkingEnd,a.IsHoliday,a.ISDELETE 
          from View_KF2_ClockIn a where a.WorkingDate >'%s'""" % value
    curs.execute(sql)
    rows = curs.fetchall()
    return rows


def sync_work_time(value):
    """将eip中的数据同步到oracle数据库中，需要同步的数据开始时间 yyyy/MM/dd"""
    oracle = get_oracle_conn()
    curs = oracle.cursor()
    rows = query_mssql_data(value)
    for row in rows:
        sql = None
        try:
            dep3 = row[3].split("/")[3] if len(row[3].split("/")) > 3 else ""
            dep4 = row[3].split("/")[4] if len(row[3].split("/")) > 4 else dep3
            workTime = 8 if 0 == row[8] else 0
            if row[6] and row[7]:
                s = (row[7] - row[6]).seconds
                overTime = s / 3600 - 9 if 0 == row[8] else s / 3600

            sql_tmplate = """
                insert into T_FULL_TIME_DATA(user_no,user_name,login_name ,full_department,business_unit ,
                work_date , start_time, end_time, is_holiday, is_delete, work_time,over_time, 
                department3, department4, id_)values('%s','%s','%s' ,'%s','%s' ,
                to_date('%s','yyyy-mm-dd hh24:mi:ss') , '%s', '%s', '%s', '%s', %d, %.2f, '%s', '%s', '%s')
                """
            sql = sql_tmplate % (row[0], row[1], row[2], row[3], row[4], row[5],
                             row[6].strftime("%Y-%m-%d %H:%M:%S") if row[6] else None,
                             row[7].strftime("%Y-%m-%d %H:%M:%S") if row[7] else None, row[8], row[9],
                             workTime, overTime, dep3, dep4, "ID%s%s%s" % (row[1], row[5].strftime("%Y%m%d"), row[9]))
            curs.execute(sql)
            oracle.commit()
        except Exception:
            print(sql)
    curs.close()
    oracle.close()


def syn_time_ascription(value):
    """将工时数据按照项目进行拆分，需要拆分的数据开始时间 yyyy-MM-dd"""
    sql = """
    insert into t_stat_data_4project  
    select a.user_no,a.work_date,a.work_time*b.ratio_ as work_time,
        a.over_time*b.ratio_ as over_time,b.code_  
    from  T_FULL_TIME_DATA a ,t_user_project_relation b where a.user_no = b.user_no  
      and a.work_date  > to_date('%s','yyyy-MM-dd')
    """ % value
    print(sql)
    orcl = get_oracle_conn()
    curs = orcl.cursor()
    curs.execute(sql)
    orcl.commit()
    curs.close()
    orcl.close()


def get_latest_data(sql):
    """ 获取oracle数据库中最新的数据日期"""
    row = execute_sql(sql)
    return row[0]


def execute_sql(sql):
    """执行sql"""
    conn = get_oracle_conn()
    cursor = conn.cursor()
    datas = cursor.execute(sql)
    cursor.close()
    conn.close()
    return datas


def bak_table(table_name):
    """备份表"""
    bak_table_name = "%s_%s" % (table_name, time.strftime('%Y%m%d'))
    execute_sql("drop table if EXISTS %s" % bak_table_name)
    sql = "create table %s as select * from %s" % (bak_table_name, table_name)
    execute_sql(sql)


def sync_project(file):
    """ 项目，子项目信息同步"""
    excel = xlrd.open_workbook(file)
    sheet = excel.sheet_by_name("配置表")
    sql = ["insert into t_project(code_,name_,service_code,service_name)values"]
    for i in range(sheet.ncols):
        for var in sheet.col_values(i):
            if var:
                sql.append("('%s','%s','%s','%s')" % (var, var, "0000", sheet.cell(1, i).value))
    print("".join(sql))


if __name__ == "__main__":
    # start_date = get_latest_data("select max(work_date) work_date from T_FULL_TIME_DATA a ")
    # sync_work_time(start_date.strftime('%Y/%m/%d'))
    # syn_time_ascription(start_date.strftime('%Y-%m-%d'))

    file = r"C:\\Users\\sunke\\Documents\\WeChat Files\\AiyaBnmyni\\Files\\研发资源视图.xls"
    sync_project(file)
    bak_table('t_project')
