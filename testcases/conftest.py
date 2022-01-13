# -*- coding: utf-8 -*-
# @Time    : 2021/12/31 17:48
# @Author  : Cc
# @File    : conftest.py

import time
import pytest
import os
from common.read_data import data
from _pytest.runner import runtestprotocol

# 获取当前项目路径
from common.read_log import log

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# 获取yaml文件内容
def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))   # 标记为skip后，该用例不会执行
    else:
        return yaml_data
# base_data = get_data("base_data.yml")
api_data = get_data("api_test_data.yml")
# scenario_data = get_data("scenario_test_data.yml")

# 增加allure测试报告中的环境信息
def pytest_sessionfinish(session):
    root_dir = session.config.rootdir
    allure_report_dir = "{}\\report\\{}\\allure_report".format(root_dir, data.load_ini('config.ini').get('env', 'execute_time'))
    # 判断allure文件是否生成
    if os.path.exists(allure_report_dir):
        systemversion = 'SystemVersion={}\n'.format(data.load_ini('config.ini').get('env', 'system_version'))
        pythonversion = 'PythonVersion={}\n'.format(data.load_ini('config.ini').get('env', 'python_version'))
        baseUrl = 'BaseUrl={}\n'.format(data.load_ini('config.ini').get('env', 'api_root_url'))
        project_name = 'ProjectName={}\n'.format(data.load_ini('config.ini').get('env', 'project_name'))
        tester = 'Tester={}\n'.format(data.load_ini('config.ini').get('env', 'tester'))
        file = open(f"{allure_report_dir}\\environment.properties", "w", encoding='UTF-8')  # 在allure报告路径中生成配置文件，并写入配置信息
        file.write(systemversion)   # 执行环境
        file.write(pythonversion)   # python版本
        file.write(baseUrl)         # 脚本执行URL
        file.write(project_name)    # 项目名
        file.write(tester)          # 执行人
        file.close()
        # 生成"allure"html文件
        os.system(f'allure generate {allure_report_dir} -o {allure_report_dir}\\html --clean')
    else:
        log.warning(f"{allure_report_dir},文件路径不存在")