## 将多个的execel文件合并成一个文件
import xlrd
import xlsxwriter
import os

def open_xls(file):
    fh = xlrd.open_workbook(file)
    return fh

def get_sheet(fh):
    return fh.sheets()

def get_sheet_rows(fh, sheet):
    table = fh.sheets()[sheet]
    return table.nrows

def get_file_content(fh, shnum, f_row):
    table = fh.sheets()[shnum]
    num = table.nrows
    for row in range(num):
        if f_row > 0 and row == 0:
            continue
        rdata = table.row_values(row)
        rst_data.append(rdata)
    return rst_data

def get_shnum(fh):
    x = 0
    sh = get_sheet(fh)
    for sheet in sh:
        x += 1
    return x

def get_file_list(path):
    file_array = []
    f_list = os.listdir(path)
    for filename in f_list:
        if os.path.splitext(filename)[1] == '.xls':
            file_array.append(filename)
    print("共有%d个文件需要合并" % len(file_array))
    return file_array

if __name__ == '__main__':
    excel_path = "C:\\Users\\sunke\\Desktop\\ebee"
    file_array = get_file_list(excel_path)
    rst_data = []
    for f_row in range(len(file_array)):
        fl = file_array[f_row]
        fh = open_xls(excel_path + "\\" + fl)
        x = get_shnum(fh)
        print('%s需要合并%d sheet的数据需要合并' % (fl, x))
        for idx in range(x):
            rvalue = get_file_content(fh, idx, f_row)
    rst_file = "C:\\Users\\sunke\\Desktop\\ebee\\rst\\rst.xlsx"
    wb1 = xlsxwriter.Workbook(rst_file)
    ws = wb1.add_worksheet()
    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c = rvalue[a][b]
            ws.write(a, b, c)
    wb1.close()
    print('合并完成')



