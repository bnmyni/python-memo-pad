'''
使用python的stmplib模块发送html并且读取本地的图片替换到html中去
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart
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

## 构建一个MIMEMultipart对象作为root对象，并在root对象上面再添加一个MIMEMultipart对象
msg = MIMEMultipart('related')
msg['From'] = Header('绩效考核专用邮箱<sunke@aspirecn.com>', 'utf-8')
msg['To'] = Header('356081449@qq.com', 'utf-8')
msg['Subject'] = Header( '一季度考核结果确认', 'utf-8')
msgAlternative = MIMEMultipart('alternative')
msg.attach(msgAlternative)

## 初始化html的MIMEMultipart对象
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">百度搜索</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 读取本地的图片数据构建一个MIMEImage对象，使用MIMEImage对象替换到MIMEMultipart对象中预留的ｉｄ位置
fp = open('Jellyfish.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

smtpobj = smtplib.SMTP()
smtpobj.connect(mail_host, mail_port)
smtpobj.login(mail_user, mail_pass)
smtpobj.sendmail(sender, recver, msg.as_string())
