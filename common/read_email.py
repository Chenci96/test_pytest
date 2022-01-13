# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 10:41
# @Author  : Cc
# @File    : read_email.py
import os
import time
import yagmail
from common.read_log import log
from common.read_data import data

execute_time = time.strftime("%Y%m%d")
datas = data.load_ini('config.ini')


class SendMail(object):
    def __init__(self, host, port, user, password, to_mail, attachments=None, headers=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.to_mail = to_mail
        self.attachments = attachments
        self.headers = headers
        self.base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def send_mail(self):
        '''
        pa
        host    # 服务器地址
        port    # 端口号
        user    # 账号
        password    # 密码
        to_mail # 发送对象
        '''

        try:
            # 链接邮箱服务器
            yag = yagmail.SMTP(host=self.host,
                              port=self.port,
                              user=self.user,
                              password=self.password,)

            # 邮箱正文
            contents = ['This is the body, and here is just text http://somedomain/image.png',
                        'You can find an audio file attached.', '/local/path/song.mp3']

            # 发送邮件
            subject = '{}自动化测试报告'.format(execute_time)

            attachments = os.path.join(self.base_path,self.attachments)
            yag.send(to=self.to_mail,
                     subject=subject,
                     contents=contents,
                     attachments=self.attachments,
                     headers=eval(self.headers)
                     )
            log.info('---{}---邮件发送完毕'.format(subject))

            # 关闭服务器链接
            yagmail.SMTP.close(yag)
        except Exception as e:
            log.error("邮件发送失败：{}".format(e))

send_mail = SendMail(host=datas.get('email', 'host'),
                     port=datas.get('email', 'port'),
                     user=datas.get('email', 'user'),
                     password=datas.get('email', 'password'),
                     to_mail=datas.get('email', 'to_mail'),
                     attachments=datas.get('email', 'attachments'),
                     headers=datas.get('email', 'headers')
                      )

if __name__ == '__main__':
    send_mail.send_mail()