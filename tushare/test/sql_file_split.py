# -*- coding: utf-8 -*-
import sys
import os
num = 0
fnum = 0
path = 'E:\MES\MES_PROJECT\MES_1.0.0.0\script\MES_1.0.0.0\ddl_1_mes.sql'
fname = 'ddl_%d.sql' % fnum
fw = open(fname, 'w')

fd = open(path)
for line in fd:
    line = line.strip()
    num = num + 1
    if line :
        if line.endswith(";") and num > 100000:
            num = 0
            fw.close()
            fnum = fnum + 1
            fname = 'ddl_%d.sql' % fnum
            fw = open(fname, 'w')
        fw.write(line)
fw.close()


