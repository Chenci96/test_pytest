# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 15:10
# @Author  : Cc
# @File    : run.py
import pytest
import os
import time
from common.read_data import data
from common.read_email import send_mail

# 执行时间
# 写入执行时间
execute_time = time.strftime("%Y%m%d%H%M%S")
data.write_ini('config.ini', 'env', 'execute_time', execute_time)

if __name__ == '__main__':
    allure_dir = f'report/{execute_time}/allure_report'     # allure报告路径
    pytesthtml_dir = f'report/{execute_time}/html_report/report.html'   # pytest-html报告路径

    # 生成"allure/pytest-html"报告
    os.system(f'pytest --alluredir {allure_dir} --html={pytesthtml_dir} --self-contained-html')

    # 将pytest-html路径写入email配置文件中
    data.write_ini('config.ini', 'email', 'attachments', pytesthtml_dir)

    # 发送邮件
    # send_mail.send_mail()