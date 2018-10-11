#!/usr/bin/env python
#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
def sendMail(mail_msg):
    sender = 'liyinghui@linglongtech.com'
    receivers = ["liyinghui@linglongtech.com","sunyuxin@linglongtech.com","zhengdayang@linglongtech.com","wangchengtao@linglongtech.com"]
    subject = 'Doctor自动化测试报告_'+time.strftime("%Y-%m-%d %H:%M", time.localtime())
    # smtpserver = 'smtp.exmail.qq.com'
    username = 'liyinghui@linglongtech.com'
    password = '2018@lingLONG'
    # password = password.encode('Unicode')
    # 不带附件的邮件
    msg = MIMEText(mail_msg, 'html', 'utf-8')

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] =  ','.join(receivers)

    # 连接邮件服务器
    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')
    # 登录发送
    smtp.login(username, password)
    smtp.sendmail('liyinghui@linglongtech.com',receivers, msg.as_string())

    smtp.quit()
    smtp.close()

# 主函数，被调用时不用。单独使用时使用。
# if __name__ == '__main__':
#     i = 100
#
#     s='邮件内容 ' \
#       '<br> 1，今日测试通过用例数 %s ；'\
#       '<br> 2，失败用例数 %s ；' \
#       '<br> '% (str(i),str(i))
#
        # sendMail(s)