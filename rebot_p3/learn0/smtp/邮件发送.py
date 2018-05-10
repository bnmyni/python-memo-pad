'''
使用python的stmplib模块发送普通文本邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#
# smtpobj = smtplib.SMTP('mmmail.aspire-tech.com', 25)
#
# rst = smtpobj.sendmail('sunke@aspirecn.com', ['356081449@qq.com'], 'python smtp 邮件发送功能测试'.encode())
# print(rst)
mail_host = 'mmmail.aspire-tech.com'
mail_port = 25
mail_user = 'sunke'
mail_pass = 'asp@123'

sender = 'sunke@aspirecn.com'
recver = ['356081449@qq.com', 'bnmyni_51@163.com']

msg = MIMEText('python smtp 邮件发送功能测试', _subtype='plain', _charset='utf-8')
msg['From'] = Header('党群工作专业邮箱<sunke@aspirecn.com>', 'utf-8')
msg['To'] = Header('Python测试邮件发送22222', 'utf-8')

subject = '党校培训'
msg['Subject'] = Header(subject, 'utf-8')


smtpobj = smtplib.SMTP()
smtpobj.connect(mail_host, mail_port)
smtpobj.login(mail_user, mail_pass)
smtpobj.sendmail(sender, recver, msg.as_string())
