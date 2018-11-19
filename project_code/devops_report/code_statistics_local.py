#!/bin/bash/python
# -*-coding:utf-8-*-
'''
使用svn diff命令统计两个版本之间的代码行（不包含空行）
'''
import subprocess, sys, os, time, re, uuid
import MySQLdb as pymysql
#import pymysql
USERNAME = "aspbld"
PASSWORD = "bld@s8load"
EXCLUDE = r"\.(txt|dic|config|log|key|pem|crt|per|prefs|ver|gif|png|jpg|war|jar|swf|)$"


def svn_check_url_u_p(url, temp_svninfo):
    cmd = "svn info --no-auth-cache --non-interactive --username='%s' --password='%s' %s >%s"\
          % (USERNAME, PASSWORD, url, temp_svninfo)
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    (stderr_test, stdout_test) = p.communicate()
    print stderr_test
    if len(stderr_test) > 0:
        sys.exit(1)


def svn_diff_url_o_n(old_url, new_url, file_name):
    cmd = "svn  diff --no-auth-cache --non-interactive" \
          " --old=%s --new=%s --username='%s' --password='%s' >%s"\
          % (old_url, new_url, USERNAME, PASSWORD, file_name)
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    (stderr_test, stdout_test) = p.communicate()
    if len(stderr_test) > 0:
        print "svn diff Error"
        sys.exit(1)


def is_ignore_svn(file_name):
    ignore_file_pattern_svn = EXCLUDE
    match = re.search(ignore_file_pattern_svn, file_name)
    return match is not None


def get_weights(file_name):
    if file_name.endswith(".xml"):
        return 0.5
    elif file_name.endswith(".java") or file_name.endswith(".c") or file_name.endswith(".cc"):
        return 1
    elif file_name.endswith(".jsp"):
        return 0.9
    elif file_name.endswith(".sql"):
        return 0.8
    else:
        return 0.1


def insert_diff_result(zt_version, add_line, del_line, total_line, total_file, exclude_file):
    db = get_write_conn()
    cursor = db.cursor()
    cursor.execute("select _num from ops_code_statistics where _num='%s'" % zt_version)
    sql = "update ops_code_statistics set add_line=%d, del_line=%d, " \
          "total_line=%d, total_file=%d, exclude_file=%d where _num='%s'"\
          % (add_line, del_line, total_line, total_file, exclude_file, zt_version) if cursor.fetchone() else \
        """INSERT INTO ops_code_statistics(_num, add_line, del_line, total_line, total_file, exclude_file)
                 VALUES ('%s', %d, %d, %d, %d, %d)""" \
        % (zt_version, add_line, del_line, total_line, total_file, exclude_file)
    print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def main():
    print "####******Begin testing at: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), " ********####"
    _uuid = uuid.uuid1()
    f_svninfo = "svninfo.%s" % _uuid
    f_svndiff = "svndiff.%s" % _uuid
    old_url = "https://10.12.5.32:8443/svn/PCC_PROJECT/tags/PCC1.0.0.0_SSYT_28"
    new_url = "https://10.12.5.32:8443/svn/PCC_PROJECT/tags/PCC1.0.0.005_SSYT_47"
    svn_diff_url_o_n(old_url, new_url, f_svndiff)

    add_line_num = 0
    del_line_num = 0
    total_line_num = 0
    exclude_file_num = 0
    total_file_num = 0

    if len(open(f_svndiff, 'r').read()) == 0:
        print "no change"
    else:
        data = {}
        with open(f_svndiff, 'r') as svndiff:
            for line in svndiff:
                if line.startswith("Index:"):
                    key = line.split(':')[-1].strip()
                    if key not in data:
                        data[key] = [0, 0]
                if line.startswith('+') and len(line.strip()) > 1:
                    data[key][0] += get_weights(key)
                if line.startswith('+++'):
                    data[key][0] -= 1
                if line.startswith('-') and len(line.strip()) > 1:
                    data[key][1] += get_weights(key)
                if line.startswith('---'):
                    data[key][1] -= 1

        total_file_num = len(data.keys())
        for f in data.keys():
            if f == '.':
                total_file_num -= 1
            elif is_ignore_svn(f):
                print "Skipping file : ", f
                exclude_file_num += 1
            else:
                add_line_num += data[f][0]
                del_line_num += data[f][1]
        total_line_num = add_line_num + del_line_num

    #insert_diff_result(zt_version, add_line_num, del_line_num, total_line_num, total_file_num, exclude_file_num)
    print "insert result to mysql complete ,uuid:%s" % _uuid
    #os.remove(f_svninfo)
    os.remove(f_svndiff)
    print "===============start：=================\n"
    print "old_url = ",old_url
    print "new_url = ",new_url    
    print "AddLineNum = ", add_line_num, " 行"
    print "DelLineNum = ", del_line_num, " 行\n"
    print "TotalLineNum = ", total_line_num, " 行\n"
    print "TotalFileNum = ", total_file_num, " 个\n"
    print "ExcludeFileNum = ", exclude_file_num, " 个\n"
    print "=============end================="
    print "####******End of testing at: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), " **********####"


def get_write_conn():
    """获取数据库连接"""
    return pymysql.connect(host="10.1.3.33", port=3306, user="dev_ops", passwd="dev_ops", db="dev_ops", charset='utf8')


def get_current_version(product, component):
    """根据产品+组件名称查询蝉道中的版本号"""
    conn = get_write_conn()
    cursor = conn.cursor()
    arg1 = '%' + product + '%'
    arg2 = '%' + component + '%'
    sql = "select _num from zt_build a where a._num like '%s' and a._num like '%s' order by a._start_date desc limit 1 " % (arg1, arg2)
    cursor.execute(sql)
    conn.close()
    return cursor.fetchone()[0]


def get_svn_ls_log(vss_path):
    """执行svn ls 命令并将输出内容生成文件,执行成功返回文件名称"""
    file_name = "svn_ls.log"
    cmd = "svn ls %s > %s" % (vss_path, file_name)
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    (stderr_test, stdout_test) = p.communicate()
    print stderr_test
    if len(stderr_test) > 0:
        sys.exit(1)
    return file_name


def get_pre_version(product, component, zt_version, vss_path):
    """获取zt_version版本的前一个版本"""
    f = get_svn_ls_log(vss_path)
    num_list = list()

    for line in open(f, 'r'):
        p = "(%s)(\d)+.(\d)+.(\d)+.(\d)+_(%s)_SSYT_(\d)+" % (product, component) if component \
            else "(%s)(\d)+.(\d)+.(\d)+.(\d)+_SSYT_(\d)+" % product
        m = re.search(p, line)
        new_num = m.group() if m else None
        if new_num:
            num_list.append(new_num)

    num_list.sort(lambda x, y: cmp(''.join([i.rjust(14, '0') for i in x.split('_SSYT_')[0].split('.')]), ''.join([i.rjust(14, '0') for i in y.split('_SSYT_')[0].split('.')])))
    num_list.sort(lambda x, y: cmp(''.join([i.rjust(3, '0') for i in x.split('_SSYT_')]), ''.join([i.rjust(3, '0') for i in y.split('_SSYT_')])))
    # 排序后，如果最后一个版本比单前的版本要高，则不再计算代码量
    svn_version = num_list[-1].split('_SSYT_')[0]
    if svn_lt_zt_version(product, component, svn_version, zt_version):
        return None
    for x in num_list[::-1]:
        if not x.startswith(zt_version):
            return x


def svn_lt_zt_version(product, component, svn_version, zt_version):
    """判断svn的版本号是否已经大于蝉道的版本号，如果svn的版本号大于蝉道的版本号，则不再计算代码量"""
    svn_v = svn_version.replace(product, '').replace(component, '').replace('_', '')
    zt_v = zt_version.replace(product, '').replace(component, '').replace('_', '')
    return ''.join([i.rjust(4, '0') for i in svn_v.split('.')]) > ''.join([i.rjust(4, '0') for i in zt_v.split('.')])


def get_svn_path(product, component, baseline, vss_path):
    zt_version = get_current_version(product, component)
    pre_version = get_pre_version(product, component, zt_version, vss_path)
    return "/".join([vss_path, baseline]), "/".join([vss_path, pre_version]), zt_version


if __name__ == "__main__":
    main()
