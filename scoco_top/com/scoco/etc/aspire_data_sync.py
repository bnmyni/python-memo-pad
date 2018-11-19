import xlrd

def read_excel(file):
    excel = xlrd.open_workbook(file)
    # print(excel.sheet_names())
    sheet = excel.sheet_by_name("配置表")
    for i in range(sheet.ncols):
        if i > 6:
            print(sheet.col_values(i))


def sync_user():
    pass


def sync_project():
    excel = xlrd.open_workbook(file)
    sheet = excel.sheet_by_name("配置表")
    for i in range(sheet.ncols):
        if i > 6:
            print(sheet.col_values(i))


def sync_user_project_relation():
    pass


if __name__ == "__main__":
    file = r"C:\\Users\\sunke\\Documents\\WeChat Files\\AiyaBnmyni\\Files\\研发资源视图.xls"
    read_excel(file)