import pytest
from testcases.conftest import api_data

# @pytest.fixture()如果不写参数，默认就是scope="function"，它的作用范围是每个测试用例来之前运行一次
@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return api_data.get(testcase_name)
