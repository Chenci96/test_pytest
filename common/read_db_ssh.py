# coding = UTF-8
'''
@File : read_db_ssh.py
@Time : 2020/11/20 1:42 PM 
@Author : Cc
'''

import os
import paramiko
import pymysql
from sshtunnel import SSHTunnelForwarder
from common.read_data import data

class SSH_DB():
    def __init__(self):
        # 读取配置文件
        self.data = data.load_ini("config.ini")
        # 配置跳板机
        self.ssh_host = self.data.get('ssh', 'ssh_host')
        self.ssh_port = int(self.data.get('ssh', 'ssh_port'))
        self.ssh_keyfile = self.data.get('ssh', 'ssh_keyfile')
        self.ssh_keypw = str(self.data.get('ssh', 'ssh_keypw'))
        self.ssh_name = self.data.get('ssh', 'ssh_name')

        # 配置数据库
        self.host = self.data.get('mysql', 'mysql_host')
        self.port = int(self.data.get('mysql', 'mysql_port'))
        self.user = self.data.get('mysql', 'mysql_user')
        self.password = self.data.get('mysql', 'mysql_passwd')
        self.db = self.data.get('mysql', 'mysql_db')

        # 获取项目根目录路径
        self.base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 拼接文件路径
        self.file_path = os.path.join(self.base_path, "config.ini")

    # 链接跳板机
    def ssh_db(self, sql):
        # 获取密钥文件路径   (秘钥地址,密码短语)
        # key_path = os.path.join(self.file_path, self.ssh_keyfile)
        # private_key = paramiko.RSAKey.from_private_key_file(key_path, self.ssh_keypw)

        with SSHTunnelForwarder(
                # 指定ssh登录的跳转机的host,port
                ssh_address_or_host=(self.ssh_host, self.ssh_port),
                # 跳板机密钥文件
                # ssh_pkey=private_key,

                # 跳板机账户密码
                ssh_username=self.ssh_name,
                # 如果是通过密码访问，可以把下面注释打开，将密钥注释即可。
                ssh_password=self.ssh_keypw,

                # 设置A机器的数据库服务地址及端口
                remote_bind_address=(self.host, self.port)
                ) as server:

            db = pymysql.connect(host='127.0.0.1',  # 此处必须是必须是127.0.0.1，代表C机器
                                 port=server.local_bind_port,
                                 user=self.user,
                                 passwd=self.password,
                                 db=self.db,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor  # 以字典形式返回操作结果,默认为元组形式
                                 )

            cur = db.cursor()  # 使用cursor()获取游标

            cur.execute(sql)  # 使用execute()方法执行sql语句
            data = cur.fetchall()  # 获取所有记录列表
            # data1 = cur.fetchone()       # 使用 fetchone() 方法获取一条数据

            # 关闭数据库/游标
            db.close()
            cur.close()

            return data

db = SSH_DB()

if __name__ == '__main__':
    # print(db.ssh_db("select * from dsp_business_pool.dsp_talent_review limit 1;"))
    print(db.ssh_db("SELECT COUNT(*) as sum FROM t_trm_publish WHERE `type` = 1 AND `status` = 1;"))