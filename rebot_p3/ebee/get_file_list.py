import glob
import os
from numpy import *
import xlrd

filearray = []
address_Excel="C:\\Users\\sunke\\Desktop\\ebee"
f_list = os.listdir(address_Excel)
for filename in f_list:
    if os.path.splitext(filename)[1] == '.xls':
       filearray.append(filename )
print("共有%d个文件需要合并" % len(filearray))
ge = len(filearray)
matrix = [None] * ge

for i in range(ge):
    fname = filearray[i]
    bk = xlrd.open_workbook(fname)
    try:
        sh = bk.sheet_by_name("Sheet")
    except:
        print("在文件%s中没有找到sheet，读取文件数据失败" % fname)
    nrows = sh.nrows
    matrix[i] = [0] * (nrows - 1)

    ncols = sh.ncols
    for m in range(nrows - 1):
        matrix[i][m] = ["0"] * ncols

    for j in range(1, nrows):
        for k in range(0, ncols):
            matrix[i][j - 1][k] = sh.cell(j, k).value

import xlwt

# 下面是把表头写上
filename = xlwt.Workbook()
sheet = filename.add_sheet("hel")

for i in range(0, len(title)):
    if title[i][-1] == "*":
        crs = 1
        sheet.write_merge(0, 0, i, crs + i, title[i])
        # sheet.write(0, i, title[i][-2])
    elif i >= 4:
        merge_leng = i + 1
        sheet.write(0, merge_leng, title[i])
    else:
        sheet.write(0, i, title[i])

# 求和前面的文件一共写了多少行
zh = 1
for i in range(ge):
    for j in range(len(matrix[i])):
        for k in range(len(matrix[i][j])):
            sheet.write(zh, k, matrix[i][j][k])
        zh = zh + 1
print("我已经将%d个文件合并成1个文件，并命名为%s.xls." % (ge, file))
filename.save(filedestination + file + ".xls")