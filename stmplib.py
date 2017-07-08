#!-*-coding=UTF-8-*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output

receiver = '1905318603@qq.com'
mail_host='smtp.qq.com'
mail_user='1905318603@qq.com'
mail_pass='ayrelbgneusefdgc'
sender=mail_user
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
