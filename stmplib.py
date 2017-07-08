#!-*-coding=UTF-8-*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output
# 第三方 SMTP 服务
receiver = '11111111@qq.com'
#设置服务器
mail_host='smtp.qq.com'  
#用户名
mail_user='1111111@qq.com'
#授权码
mail_pass='授权码'
sender=mail_user
#接收邮件邮箱
receivers=[receiver]

log = 'Hello world!'
message = MIMEText(log)
message['From'] = Header(mail_user,'utf-8')
message['To']=Header(str(receivers),'utf-8')

subject='my test'
message['Subject']=Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host,465)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    smtpObj.quit()
    print ('邮件发送成功')
except smtplib.SMTPException,e:
    print (e)
