# -*- coding: UTF-8 -*-
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import logging

logging.basicConfig(filename=os.path.join(os.getcwd(), 'm.log'), level=logging.DEBUG)

def check():
    logging.debug("do check...")
    st = os.statvfs('/opt')
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    if free < total * 0.8:
        sendEmail()

def sendEmail():
    logging.debug("start send email...")
    mail_host = 'mmmail.aspire-tech.com'
    mail_port = 25
    mail_user = 'sunke'
    mail_pass = 'asp@123'

    sender = 'sunke@aspirecn.com'
    recver = ['sunke@aspirecn.com','xujing@aspirecn.com','wanglh@aspirecn.com']

    msg = MIMEText('工具链应用服务器磁盘使用率超过80%，为保证工具链应用正常运行，请及时清理磁盘。', _subtype='plain', _charset='utf-8')
    msg['From'] = Header('孙科<sunke@aspirecn.com>', 'utf-8')
    msg['To'] = Header(','.join(recver), 'utf-8')

    subject = '工具链应用服务器磁盘告警'
    msg['Subject'] = Header(subject, 'utf-8')

    smtpobj = smtplib.SMTP()
    smtpobj.connect(mail_host, mail_port)
    smtpobj.login(mail_user, mail_pass)
    smtpobj.sendmail(sender, recver, msg.as_string())

if __name__ == "__main__":
    logging.debug("start check...")
    while True:
        check()
        time.sleep(10)