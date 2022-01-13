# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 16:40
# @Author  : Cc
# @File    : read_data.py

import yaml
import json
import os
from configparser import RawConfigParser,ConfigParser
from common.read_log import log

class ReadFileData():
    def __init__(self):
        # 获取项目根目录路径
        self.base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def load_yaml(self, file_name, dir_name='data'):
        '''
        读取yaml文件
        file_name:文件名
        dir_name='data':目录名
        '''
        # 拼接文件路径
        file_path = os.path.join(self.base_path, dir_name, file_name)

        log.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    def load_json(self, file_name, dir_name='config'):
        '''
        读取Json文件
        file_name:文件名
        dir_name='data':目录名
        '''
        # 拼接文件路径
        file_path = os.path.join(self.base_path, dir_name, file_name)

        log.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        return data

    def load_ini(self, file_name, dir_name='config'):
        '''
        读取ini文件
        file_name:文件名
        dir_name='data':目录名
        '''
        # 拼接文件路径
        file_path = os.path.join(self.base_path, dir_name, file_name)
        log.info("加载 {} 文件......".format(file_path))

        # config = ConfigParser()    # 一般情况下使用该方法
        config = RawConfigParser()   # 有特殊字符时，使用该方法

        # 读取文件
        config.read(file_path, encoding="UTF-8")
        return config

    def write_ini(self, file_name, section, option, value, dir_name='config'):
        '''
        写入ini文件
        file_name:文件名
        dir_name:目录名
        section:模块名
        option:键
        value：值
        '''
        # 拼接文件路径
        file_path = os.path.join(self.base_path, dir_name, file_name)
        print(file_path)
        log.info("加载 {} 文件......".format(file_path))
        config = ConfigParser()
        config.read(file_path, encoding="UTF-8")
        # 判断文件中是否有"section"
        if config.has_section(section):
            config.set(section, option, value)
            config.write(open(file_path, 'w', encoding='utf-8'))
        else:
            config.add_section(section)
            config.set(section, option, value)
            config.write(open(file_path, 'w', encoding='utf-8'))
        log.info('写入{}文件成功,写入值为：section={},option={},value={}'.format(file_path, section, option, value))

data = ReadFileData()

if __name__ == '__main__':
    # 查询单个key值内容
    # data = data.load_yaml("api_test_data.yml")["test_get_all_user_info"]
    # print('数据：{}'.format(data))

    # 查询文件所有内容
    data = data.load_ini("config.ini").get('env', 'login')
    print('数据：{}'.format(data))

    # 写入数据
    # A = data.write_ini("config.ini", 'env', 'Cookie', '111123')
    # print('数据：{}'.format(A))