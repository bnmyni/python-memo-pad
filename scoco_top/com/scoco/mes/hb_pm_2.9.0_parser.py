import pymysql
import gzip
import ftplib
import time
import re
import os

cols_list = list()
FILE_FILTER = "PM-ENB-EUTRANCELLTDD-4A-V2.9.0-%s-15"
FTP_HOST, FTP_PORT, FTP_USER, FTP_PWD = '10.212.228.197', 21, 'ftpuser', 'HWcmcc_567%'
FTP_REMOTE_PATH = "/HE/WX/ZT/SJZomc4/PM/%s"
FTP_LOCAL_PATH = "C:\\Users\\Administrator\\Desktop\\tmp\\%s"
FILE_CHARSET, LINE_SPLIT_CHAR, COL_SPLIT_CHAR, LINE_END_CHAR = "UTF-8", "|", "=", "\n"
DB_HOST, DB_USER, DB_PWD, DB_DATABASE, DB_CHARSET = "10.12.19.190", "root", "tmchamster", "multinet", 'utf8'

header_list = ["startTime",
               "Dn",
               "UserLabel",
               "HO.SuccOutInterEnbS1",
               "HO.SuccOutInterEnbX2",
               "HO.SuccOutIntraEnb",
               "HO.AttOutInterEnbS1",
               "HO.AttOutInterEnbX2",
               "HO.AttOutIntraEnb",
               "PDCP.UpOctUl",
               "PDCP.UpOctDl",
               "RRC.ConnMax",
               "RRU.PuschPrbAssn",
               "RRU.PuschPrbTot",
               "RRU.PdschPrbAssn",
               "RRU.PdschPrbTot",
               "RRC.SuccConnEstab",
               "RRC.AttConnReestab",
               "RRC.AttConnEstab",
               "ERAB.NbrSuccEstab",
               "ERAB.NbrAttEstab",
               "ERAB.NbrReqRelEnb",
               "ERAB.NbrReqRelEnb.Normal",
               "ERAB.HoFail",
               "ERAB.NbrLeft",
               "ERAB.NbrFailEstab"
               ]


def excute(gz_file, target_file):
    file_name = ungz_file(gz_file)
    parse_header(file_name)
    parse_file(file_name, target_file)
    load_csv_file(target_file)


def parse_file(file_name, target_file):
    target_write = open(target_file, 'w', encoding=FILE_CHARSET)
    with open(file_name, encoding=FILE_CHARSET) as f:
        for line in f.readlines()[2:]:
            row = list()
            for idx in cols_list:
                if idx == 1:
                    tmp = line.split(LINE_SPLIT_CHAR)[idx].split(",")
                    for t in tmp:
                        row.append(
                            t.split(COL_SPLIT_CHAR)[1] if len(t.split(COL_SPLIT_CHAR)) > 1 else t.split(COL_SPLIT_CHAR)[
                                0])
                else:
                    row.append(line.split(LINE_SPLIT_CHAR)[idx])
            row.append("1")
            row.append(LINE_END_CHAR)
            target_write.write(LINE_SPLIT_CHAR.join(row))
    target_write.flush()
    target_write.close()
    f.close()


def parse_header(file_name):
    """
    初始化数据库与header表头的对应关系
    :param file_name: csv文件
    :return: 返回初始化后列表顺序
    """
    line = open(file_name, encoding=FILE_CHARSET).readlines()[1:2][0]
    headers = line.split(LINE_SPLIT_CHAR)
    for h in header_list:
        cols_list.append(headers.index(h))


def load_csv_file(file_name):
    # 打开数据库连接
    db = pymysql.connect(DB_HOST, DB_USER, DB_PWD, DB_DATABASE, charset=DB_CHARSET, local_infile=1)
    cursor = db.cursor()
    sql = "load data local infile '%s' into table pm_lte_eutrancelltdd_zte " \
          "character set utf8 fields terminated by '|' lines terminated by '\\n'" % file_name
    print(sql)
    cursor.execute(sql)
    db.commit()
    db.close()


def ungz_file(file_name):
    """
    解压gz文件
    :param file_name: 需要解压的文件
    :return: 解压后的文件
    """
    target_file = file_name.replace(".gz", "")
    g_file = gzip.GzipFile(file_name)
    open(target_file, "wb").write(g_file.read())
    g_file.close()
    return target_file


def ftp_connect():
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PWD)
    return ftp


def ftp_download_file(ftp, remote_file, local_file):
    fp = open(local_file, 'wb')
    ftp.retrbinary('RETR ' + remote_file, fp.write, 4096)
    ftp.set_debuglevel(0)
    fp.close()


def get_remote_files(ftp, dir_name):
    if not ftp:
        return None

    if dir_name:
        ftp.cwd(dir_name)
    return ftp.nlst()


def get_file_filter():
    least_time = int(int(time.time()) / 900)
    return FILE_FILTER % time.strftime("%Y%m%d%H%M00", time.localtime(least_time * 900))


def get_download_files(ftp, dir_name):
    remote_files = get_remote_files(ftp, dir_name)
    file_filter = get_file_filter()
    print("file_filter = %s" % file_filter)
    rst_files = list()
    for file in remote_files:
        if re.search(file_filter, file):
            rst_files.append(file)
    return rst_files


def clean_data_before_download():
    db = pymysql.connect(DB_HOST, DB_USER, DB_PWD, DB_DATABASE, charset=DB_CHARSET)
    cursor = db.cursor()
    sql = "insert into pm_lte_eutrancelltdd_zte_his select * from pm_lte_eutrancelltdd_zte "
    print(sql)
    cursor.execute(sql)
    db.commit()
    db.close()


if __name__ == "__main__":
    while True:
        ts = int(time.strftime("%M", time.localtime()))
        if ts % 13 == 0 and ts > 0:
            remote_path = FTP_REMOTE_PATH % time.strftime("%Y%m%d%H", time.localtime())
            local_path = FTP_LOCAL_PATH % time.strftime("%Y%m%d%H", time.localtime())
            clean_data_before_download()
            print("开始下载pm数据......")
            ftp = ftp_connect()
            file_list = get_download_files(ftp, remote_path)
            print("需要下载的文件列表:%s" % file_list)
            download_done_files = list()
            if file_list:
                for file in file_list:
                    ftp_download_file(ftp, remote_path + "/" + file, local_path + "/" + file)
                    download_done_files.append(local_path + "/" + file)

                for file in download_done_files:
                    excute(file, file.replace(".gz", ""))
            print("pm数据更新完成......")
        else:
            time.sleep(50)
