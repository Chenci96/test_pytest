# coding = UTF-8
'''
@File : read_log.py
@Time : 2020/11/18 4:52 PM 
@Author : Cc
'''

import os
import logging
import time
from logging.handlers import TimedRotatingFileHandler

# 获取项目文件名
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "logs")
# 判断文件是否存在
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

# 命名log文件名
log_file_path = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))

def logs():
    # 创建日志收集器
    logger = logging.getLogger('logs')
    # 设置日志收集器等级
    logging.root.setLevel(logging.NOTSET)

    # 日志输出格式
    formatter = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

    """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
    if not logger.handlers:  # 避免重复日志
        # 创建输出到控制台的输出渠道
        console_handler = logging.StreamHandler()
        # 获取控制台输出格式
        console_handler.setFormatter(formatter)
        # 设置控制台收集器等级
        console_handler.setLevel('DEBUG')
        # 添加到收集器中
        logger.addHandler(console_handler)
        # 每天重新创建一个日志文件，最多保留backup_count份
        file_handler = TimedRotatingFileHandler(filename=log_file_path,     # 文件名
                                                when='D',
                                                interval=1,
                                                backupCount=5,  # 最多存放日志的数量
                                                delay=True,
                                                encoding='UTF-8')
        # 获取文件输出格式
        file_handler.setFormatter(formatter)
        # 设置文件输出等级
        file_handler.setLevel('DEBUG')
        logger.addHandler(file_handler)
    return logger


log = logs()

if __name__ == '__main__':
    log.info("---测试开始---")
    log.debug("---测试结束---")

