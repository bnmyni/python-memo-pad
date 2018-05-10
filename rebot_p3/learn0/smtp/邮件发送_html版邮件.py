'''
使用python的stmplib模块发送html内容的邮件
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

html = """
<p>Python 邮件发送html版本的邮件请查收</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
<h1>腾讯公司</h1>
您好,孙科:<br/>
<br/>
    000779的1季度考核結果已评出，请尽快登录绩效考核管理系统确认考核结果，若超过7天未确认,系统将自动确认；
系统地址：<a href="http://www.baidu.com">（内网链接）</a><a href="http://www.zhibo8.cc">（外网链接）</a>
"""
### 如果这里_subtype='html'就是一个html格式的邮件，如果是一个plain就是一个普通格式的邮件
msg = MIMEText(html, _subtype='html', _charset='utf-8')
msg['From'] = Header('绩效考核专用邮箱<sunke@aspirecn.com>', 'utf-8')
msg['To'] = Header('356081449@qq.com', 'utf-8')

subject = '一季度考核结果确认'
msg['Subject'] = Header(subject, 'utf-8')


smtpobj = smtplib.SMTP()
smtpobj.connect(mail_host, mail_port)
smtpobj.login(mail_user, mail_pass)
smtpobj.sendmail(sender, recver, msg.as_string())
