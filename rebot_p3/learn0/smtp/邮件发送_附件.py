'''
使用python的stmplib模块发送带有附件的邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
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

msg = MIMEMultipart()
msg['From'] = Header('绩效考核专用邮箱<sunke@aspirecn.com>', 'utf-8')
msg['To'] = Header('356081449@qq.com', 'utf-8')
subject = '一季度考核结果确认'
msg['Subject'] = Header(subject, 'utf-8')

msg.attach(MIMEText('第三季度考核确认', _subtype='plain', _charset='utf-8'))

# att1 = MIMEText(open('C:\\Users\\sunke\\Desktop\\Jenkins  api构建接口.docx', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="api构建接口.docx"'
# msg.attach(att1)

## 另外一种发送附件的方式
words = MIMEApplication(open('C:\\Users\\sunke\\Desktop\\Jenkins  api构建接口.docx', 'rb').read())
words.add_header("Content-Disposition", 'attachment', filename='api构建接口.docx')
msg.attach(words)

smtpobj = smtplib.SMTP()
smtpobj.connect(mail_host, mail_port)
smtpobj.login(mail_user, mail_pass)
smtpobj.sendmail(sender, recver, msg.as_string())
