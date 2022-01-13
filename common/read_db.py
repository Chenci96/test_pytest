# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 17:09
# @Author  : Cc
# @File    : read_db.py

import pymysql
import os
from common.read_data import data
from common.read_log import log

# 获取项目根目录路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 拼接文件路径
data_file_path = os.path.join(BASE_PATH, "config", "config.ini")
data = data.load_ini(data_file_path)["mysql"]

# 获取mysql配置
DB_CONF = {
    "host": data["MYSQL_HOST"],
    "port": int(data["MYSQL_PORT"]),
    "user": data["MYSQL_USER"],
    "password": data["MYSQL_PASSWD"],
    "db": data["MYSQL_DB"]
}

class MysqlDb():

    def __init__(self, db_conf=DB_CONF):
        # 通过字典拆包传递配置信息，建立数据库连接
        self.conn = pymysql.connect(**db_conf,
                                    autocommit=True,
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor()

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        log.info("执行sql：[{}]".format(sql))
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        log.info("执行sql结果：{}".format(data))
        return data

    def execute_db(self, sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            log.info("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()


db = MysqlDb(DB_CONF)
if __name__ == '__main__':

    sql = "SELECT * FROM user"
    print(db.select_db(sql))