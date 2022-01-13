# pytestDemo

本项目实现接口自动化的技术选型：**Python+Requests+Pytest+YAML+Allure/Pytest-html** ，主要是针对一个Demo接口项目来开展的，通过 Python+Requests 来发送和处理HTTP协议的请求接口，使用 Pytest 作为测试执行器，使用 YAML 来管理测试数据，使用 Allure/pytest-html 来生成测试报告。

>相关接口项目：[使用 Python+Flask+MySQL+Redis 开发简单接口实例](https://github.com/Chenci96/flaskDemo)

## 项目部署

* 首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：

```
pip3 install -r requirements.txt
```
* 根据[pytest生成测试报告](https://note.youdao.com/s/9ntzimng)笔记配置好allure/pytest-html环境

* 接着，修改 ```config/setting.ini``` 配置文件，在Windows环境下，安装相应依赖之后，在命令行窗口执行命令：

```
pytest

也可以直接运行run.py文件
```



**注意**：因为我这里是针对自己的接口项目进行测试，如果想直接执行我的测试用例来查看效果，需要提前部署上面提到的 [flaskDemo](https://github.com/wintests/flaskDemo) 接口项目。

## 项目结构

- common ====>> 各种工具类
- config ====>> 配置文件
- data ====>> 测试数据文件管理
- losg ====>> 存放log日志文件
- report ====>> 存放测试报告文件(有两种测试报告)
- testcases ====>> 测试用例
- pytest.ini ====>> pytest配置文件
- requirements.txt ====>> 相关依赖包文件

## 测试报告效果展示

在命令行执行命令：```pytest``` 运行用例后，会得到一个测试报告的原始文件，但这个时候还不能打开成HTML的报告，还需要在项目根目录下，执行命令启动 ```allure``` 服务(需提前配置好allure环境)：

```
# 需要提前配置allure环境，才可以直接使用命令行
allure serve ./report
```

最终，可以看到测试报告的效果图如下：

![image.png](https://upload-images.jianshu.io/upload_images/16853007-248f805c82dbf99c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
