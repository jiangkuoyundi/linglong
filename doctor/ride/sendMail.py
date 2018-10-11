#!/usr/bin/env python
#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
def sendMail(mail_msg):
    sender = 'liyinghui@linglongtech.com'
    receivers = ["liyinghui@linglongtech.com","738805997@qq.com"]
    # cc = '425804945@qq.com'
    subject = 'Doctor自动化测试报告_'+time.strftime("%Y-%m-%d %H:%M", time.localtime())
    smtpserver = 'smtp.exmail.qq.com'
    username = 'liyinghui@linglongtech.com'
    password = '2018lL'


    #中文需参数‘utf-8'，单字节字符不需要
    msg = MIMEText(mail_msg,'html','utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] =  ','.join(receivers)
    # msg['Cc'] = cc

    # 连接邮件服务器
    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')
    # 登录发送
    smtp.login(username, password)
    smtp.sendmail('liyinghui@linglongtech.com',receivers, msg.as_string())

    smtp.quit()
    smtp.close()

if __name__ == '__main__':
    i = 100
    s='邮件内容 ' \
      '<br> 1，今日测试通过用例数 %s ；'\
      '<br> 2，失败用例数 %s ；' \
      '<br> '% (str(i),str(i))

    sendMail(s)