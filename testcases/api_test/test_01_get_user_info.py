# -*- coding: utf-8 -*-
# @Time    : 2021/12/31 17:41
# @Author  : Cc
# @File    : test_01_get_user_info.py


import pytest
import allure
import os
from common.read_data import data
from common.read_log import log
from testcases.conftest import api_data
from common.read_requests import read_requset



@allure.step("步骤1 ==>> 获取所有用户信息")
def step_1(title, method, url, except_result, except_code, except_msg):
    log.info("步骤1 ==>> 获取所有用户信息{}".format(title, method, url, except_result, except_code, except_msg))

@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取全部用户信息模块")
class TestGetUserInfo(object):

    """获取用户信息模块"""
    @allure.story("用例--获取全部用户信息")
    @allure.description("该用例是针对获取所有用户信息接口的测试")
    @allure.issue("https://www.baidu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.baidu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("【{title}】")
    @pytest.mark.single
    @pytest.mark.parametrize("title, method, url, except_result, except_code, except_msg", api_data["test_get_all_user_info"])
    def test_get_all_user_info(self, title, method, url, except_result, except_code, except_msg):
        log.info("*************** 开始执行用例 ***************")
        step_1(title, method, url, except_result, except_code, except_msg)
        # 接口调用
        res = read_requset.request(method, url)
        # print(res.__dict__)
        success = False
        if res.json()["code"] == 0:
            success = True
        else:
            error = '接口返回码是：【{}】\n\t\t预期返回码是：【{}】 \n\t\t返回信息：【{}】'.format(res.json()["code"], except_code, res.json()["msg"])
        msg = res.json()["msg"]
        response = res
        log.info("查看全部用户 ==>> 返回结果 ==>> \n{}".format(response.text))
        assert response.status_code == 200
        assert success == except_result, error
        log.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, response.json().get("code")))
        assert response.json().get("code") == except_code
        assert except_msg in msg
        log.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':

    pytest.main(["-q", "-s", "test_01_get_user_info.py"])
    os.system('allure generate report/ -o report/html --clean')
