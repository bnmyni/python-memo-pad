
# conn = pymssql.connect(host='10.2.8.25',port=1433, database='EIP_Transaction', user='u_kf2', password='u_kf2')
# cur = conn
# sql = 'select count(*) from View_KF2_ClockIn'
# cur.excute(sql)
# data = cur.fetchall()
#
# print(data)
import pymssql
conn = pymssql.connect(host = '10.2.8.25', port = 1433, user = 'u_kf2', password = 'u_kf2',database = "EIP_Transaction")
cursor = conn.cursor()
# cursor.execute("""select getdate()""")
# row=cursor.fetchone()
# while row:
#     print("sqlserver version:%s"%(row[0]))
#     row=cursor.fetchone()
#
# conn.close()
sql = """ select a.USER_NO,a.USER_Name_ZH,a.USER_LoginName,a.FULL_NAME,a.BusinessUnit
,a.WorkingDate,a.WorkingStar,a.WorkingEnd,a.IsHoliday,a.ISDELETE
 from View_KF2_ClockIn a where a.WorkingDate >= """
cursor.execute(sql)
rows = cursor.fetchone()

while rows:
    print(rows[0])
    rows = cursor.fetchone()