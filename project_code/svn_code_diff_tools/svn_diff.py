#!/bin/bash/python
# -*-coding:utf-8-*-
'''
使用svn diff命令统计两个版本之间的代码行（不包含空行）
'''
import subprocess, sys, os, time, re, uuid
import MySQLdb as pymysql
USERNAME = "sunke"
PASSWORD = "asp@123"
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


def insert_diff_result(_uuid, add_line, del_line, total_line, total_file, exclude_file):
    db = pymysql.connect(host="10.1.3.33",port=3306, user="dev_ops", passwd="dev_ops", db="dev_ops", charset='utf8')
    cursor = db.cursor()
    sql = """INSERT INTO t_code_couter(_uuid, add_line, del_line, total_line, total_file, exclude_file)
             VALUES ('%s', %d, %d, %d, %d, %d)""" % (_uuid, add_line, del_line, total_line, total_file, exclude_file)
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
    print "old_url:%s;new_url:%s" % (sys.argv[1].strip(), sys.argv[2].strip())
    old_url = sys.argv[1].strip()
    new_url = sys.argv[2].strip()
    if len(old_url) == 0 or len(new_url) == 0:
        print "SVN_REPOSITORY_URL is null"
        sys.exit(1)

    svn_check_url_u_p(old_url, f_svninfo)
    svn_check_url_u_p(new_url, f_svninfo)

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

    insert_diff_result(_uuid, add_line_num, del_line_num, total_line_num, total_file_num, exclude_file_num)
    print "insert result to mysql complete ,uuid:%s" % _uuid
    os.remove(f_svninfo)
    os.remove(f_svndiff)
    print "===============start：=================\n"
    print "AddLineNum = ", add_line_num, " 行"
    print "DelLineNum = ", del_line_num, " 行\n"
    print "TotalLineNum = ", total_line_num, " 行\n"
    print "TotalFileNum = ", total_file_num, " 个\n"
    print "ExcludeFileNum = ", exclude_file_num, " 个\n"
    print "=============end================="
    print "####******End of testing at: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), " **********####"


if __name__ == "__main__":
    main()