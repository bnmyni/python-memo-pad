#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14
# @Author  : sunke
# @File    : func.py
# @Software: PyCharm
from log.normal import Logger
import pexpect

LIST_CMD = "_list_cmd_"

CMD_DICT = {
    "bj_ARRAY APV9650_3_10.105.5.7": ["en", "show run", " "],
    "bj_HW E8000E-X8_2_10.105.5.2": ["dis cur", " "],
    "bj_H3C M9010_2_10.105.5.5": ["dis cur", " ", "sys", "display context " + LIST_CMD, " ", ["switchto context %s", "dis cur", " ", "exit"]],
    "cd_H3C SecPath M9010_2_10.146.0.1": ["dis cur", " ", "sys", "display context " + LIST_CMD, " ", ["switchto context %s", "dis cur", " ", "exit"]],
    "cd_Eudemon8000E-X8_2_10.146.0.3": ["dis cu", " ", "sys", "dis vsys " + LIST_CMD, ["switch vsys %s", "dis cu", " ", "q"]]
    # "nj_DPtech FW1000-TE-N_2_172.19.201.77": [],
    # "nj_DPtech FW1000-TE-N_2_172.19.201.78": [],
    # "nj_DPtech FW1000-TE-N_2_172.19.201.84": [],
    # "nj_DPtech FW1000-TE-N_2_172.19.201.92": [],
    # "nj_Array APV9650_3_172.19.201.58": [],
    # "nj_Array APV9650_3_172.19.201.59": [],
    # "nj_Array APV9650_3_172.19.205.58": [],
    # "nj_Array APV9650_3_172.19.205.59": [],
}

logger = Logger(logname='ssh.log', logger="func").getlog()

class SshConnection(object):
    def __init__(self, host, port, username, password, area, device_type, net_id):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ok_flag = 1
        self.uk = "%s_%s_%s_%s" % (area, device_type, net_id, self.host)

    def connect(self):
        shell_cmd = "ssh -l %s %s -p %d" % (self.username, self.host, int(self.port))
        child = pexpect.spawn('/bin/bash', ['-c', shell_cmd])
        ssh_newkey = "Are you sure you want to continue connecting"
        i = child.expect(['[Pp]assword: ', ssh_newkey, pexpect.TIMEOUT], timeout=15)
        if i == 2:
            logger.info(self.host + ':SSH could not login.')
            self.ok_flag = 0

        if i == 1:
            child.sendline('yes')
            j = child.expect(['[Pp]assword: ', pexpect.TIMEOUT], timeout=15)
            if j == 1:
                logger.info(self.host + ':SSH could not login')
                self.ok_flag = 0

        if self.ok_flag:
            child.sendline(self.password)
            logger.debug(self.host + "LOGIN SUCCESS")

            cmd = list(CMD_DICT.get(self.uk, {}))
            logger.debug("uk:{},cmd:{}",  self.uk, cmd)

            if cmd:
                for cline in cmd:
                    if cline == " ":
                        for i in range(500):
                            child.sendline(' ')
                    ## 该命令输出为下一个命令的输入
                    if cline.endswith(LIST_CMD):
                        cline = cline.replace(LIST_CMD, "")
                    child.sendline(cline)
                # end of the cmd
                child.sendline('#@!$')
                f = open(self.uk, "w")
                child.logfile = f
                child.expect([pexpect.TIMEOUT, pexpect.EOF, "#@!$"], timeout=300)
                f.close()

                logger.info("collect data: %s -- %s" % (self.host, self.uk))

            # 关闭
            child.close(force=True)
