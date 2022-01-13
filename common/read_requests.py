# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 17:27
# @Author  : Cc
# @File    : read_requests.py

import requests
import json as complexjson

from common.read_data import data
from common.read_log import log


class ReadRequset(object):
    def __init__(self):
        # 获取当前环境URL
        self.api_root_url = data.load_ini('config.ini').get('env', 'api_root_url')
        print(self.api_root_url)
        self.session = requests.session()

    def request(self, method, url, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        self.request_log(method, url,  data, json, params, headers, files, cookies)

        if method.upper() == "GET":
            return self.session.get(url, **kwargs)
        if method.upper() == "POST":
            return requests.post(url, data, json, **kwargs)
        if method.upper() == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method.upper() == "DELETE":
            return self.session.delete(url, **kwargs)
        if method.upper() == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)

    def request_log(self, method, url, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        log.info("接口请求地址 ==>> {}".format(url))
        log.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        log.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        log.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        log.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        log.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        log.info("接口上传附件 files 参数 ==>> {}".format(files))
        log.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))

read_requset = ReadRequset()
if __name__ == '__main__':
    method = 'POST'
    url = "/register"
    headers = {"Content-Type": "application/json"}
    data = {"username": "测试test","password": 123456,"sex": 1,"telephone": 13599999999,"address": "深圳市宝安区"}
    res = read_requset.request(method=method, url=url, json=data, headers=headers)
    print(res.json())