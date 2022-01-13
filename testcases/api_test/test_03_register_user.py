# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 16:58
# @Author  : Cc
# @File    : test_03_register_user.py

import pytest
import allure
import os
from common.read_log import log
from testcases.conftest import api_data
from common.read_requests import read_requset


@allure.step("步骤1 ==>> 注册用户")
def step_1(title, method, url, headers, data, except_result, except_code, except_msg):
    log.info("步骤1 ==>> 注册用户：{}".format(title, method, url, headers, data, except_result, except_code, except_msg))


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户注册模块")
class TestGetOneUserInfo(object):

    @allure.story("用例--用例--注册用户信息")
    @allure.description("该用例是针对获取用户注册接口的测试")
    @allure.issue("https://www.baidu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.baidu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("【{title}】")
    @pytest.mark.single
    @pytest.mark.parametrize("title, method, url, headers, data, except_result, except_code, except_msg",
                             api_data["test_register_user"])
    def test_get_one_user_info(self, title, method, url, headers, data, except_result, except_code, except_msg):
        log.info("*************** 开始执行用例 ***************")
        step_1(title, method, url, headers, data, except_result, except_code, except_msg)
        res = read_requset.request(method=method, url=url, json=data, headers=headers)
        success = False
        if res.json()['code'] == 0:
            success = True
        else:
            error = '接口返回码是：【{}】\n\t\t预期返回码是：【{}】 \n\t\t返回信息：【{}】'.format(res.json()["code"], except_code, res.json()["msg"])
        msg = res.json()["msg"]
        response = res
        log.info("注册用户信息 ==>> 返回结果 ==>> \n{}".format(response.text))
        assert response.status_code == 200
        assert success == except_result, error
        log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, response.json().get("code")))
        assert response.json().get("code") == except_code
        assert except_msg in msg
        log.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':

    pytest.main(["-q", "-s", "test_03_register_user.py"])
    os.system('allure generate report/ -o report/html --clean')