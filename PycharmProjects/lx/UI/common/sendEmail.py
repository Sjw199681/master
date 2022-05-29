""""
功能描述：配置邮件属性，登录邮箱账号，提供对外发送邮件方法
实现逻辑
导包
1-创建sendemali类
2-实例化方法
  2-1配置邮件发件人等
3-封装邮件内容
 3-1正文
 3-2内容
4-对外提供发送邮件的方法
 4-1链接服务器
 4-2登陆
 4-3发送
 4-4关闭链接
"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib,time


class SendEmail:
    def __init__(self):
        # 发送邮箱
        self.sender = '2553022646@qq.com'
        # 接收邮箱
        self.receiver = '2553022646@qq.com'
        # 发送邮件主题
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.subject = 'UI自动化测试结果_' + t
        # 发送邮箱服务器
        self.smtpserver = 'smtp.qq.com'
        # 发送邮箱用户/密码
        self.username = '2553022646@qq.com'
        self.password = 'qjpalbgahyweecej'

    # 封装邮件内容
    def __config(self, file):
        with open(file, 'rb') as f:
            #正文
            mail_body = f.read()
            self.msg = MIMEMultipart()
            # 添加附件内容
            att = MIMEText(mail_body, 'plain', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att['Content-Disposition'] = 'attachment;filename = result.html'
            self.msg.attach(att)
            # 添加邮件的文本内容
            content = 'UI自动化测试结果 邮件发送附件...'
            self.msg.attach(MIMEText(content, 'plain', 'utf-8'))
            self.msg['Subject'] = Header(self.subject, 'utf-8')
            # 账号
            self.msg['From'] = self.sender
            # 密码
            self.msg['To'] = self.receiver

    # 对外提供发送邮件的方法
    def send(self, file):
        self.__config(file)
        try:
            #实例化
            s = smtplib.SMTP()
            # 4-1链接服务器
            s.connect(self.smtpserver)
            # 4-2登陆
            s.login(self.username, self.password)
            # 4-3发送
            s.sendmail(self.sender, self.receiver, self.msg.as_string())
        except Exception as msg:
            print('邮件发送失败！%s' % msg)
        else:
            print("发送成功")
        # 4-4关闭链接
        finally:
            s.close()


if __name__ == '__main__':
    ce = SendEmail()
    ce.send(r'/Users/bytedance/PycharmProjects/UI-appium/testreport/result.html')
