# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
from middleware.handler import Handler


def send_mail(report_path, project_name):
    '''发送邮件'''

    with open(report_path,'rb') as f:
        # 读取测试报告正文，作为邮件正文
        mail_body = f.read()

    now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    # 获取邮箱服务地址

    hd = Handler()
    smtp_server = hd.yaml['email']['smtp_server']

    try:
        # 启动163邮箱服务
        smtp = smtplib.SMTP(smtp_server, 25)
        # 获取发件人信息
        sender = hd.yaml['email']['smtp_sender']
        # 发件人邮箱授权码
        password = hd.yaml['email']['smtp_sender_password']
        # 接收人邮箱
        receiver = hd.yaml['email']['smtp_receiver']
        # 登陆
        smtp.login(sender,password)

        msg = MIMEMultipart()
        # 编写html类型的邮件正文，MIMEtext() 用于定义邮件正文
        # 发送
        text = MIMEText(mail_body,'html','utf-8')

        # 定义邮件正文标题
        text['Subject'] = Header(project_name + '接口测试报告','utf-8')
        msg.attach(text)

        # 发送附件
        # Header 用于定义邮件主题，主题加上时间，防止主题重复导致发送失败

        msg['Subject'] = Header('【测试用例执行结果】：'+ project_name+'测试报告'+ now,'utf-8')
        msg_file = MIMEText(mail_body,'html','utf-8')

        # 构造MIMEBase对象做为文件附件内容并附加到根容器
        msg_file['Content-Type'] = 'application/octet-stream'
        msg_file['Content-Disposition'] = 'attachment; file_name="测试报告.html"'
        msg.attach(msg_file)

        # 定义发件人
        msg['From'] = sender
        # 定义收件人
        msg['To'] = receiver

        smtp.sendmail(msg['From'],msg['To'].split(';'),msg.as_string())
        smtp.quit()
        return True
    except smtplib.SMTPException as e:
        print(str(e))
        return False

