# Allure 学习笔记

## 一句话理解

Allure 是测试报告工具，不是测试框架。

在当前项目中：

```text
pytest 负责执行测试
allure-pytest 负责收集测试结果
allure 命令负责生成可视化报告
```

## 当前项目中的 Allure 流程

1. 执行 pytest。
2. pytest 根据 `pytest.ini` 中的配置生成 Allure 原始结果。
3. 原始结果保存到 `reports/allure-results`。
4. 使用 Allure 命令生成可视化报告。
5. 可视化报告保存到 `reports/allure-report`。

## pytest.ini 中的 Allure 配置

```ini
addopts = -s --html=reports/login_report.html --self-contained-html --clean-alluredir --alluredir=reports/allure-results
```

重点参数：

- `--alluredir=reports/allure-results`：指定 Allure 原始结果目录。
- `--clean-alluredir`：每次运行前清空旧的 Allure 原始结果。

## 常用命令

执行测试：

```bash
pytest
```

生成 Allure HTML 报告：

```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

临时启动 Allure 报告服务：

```bash
allure serve reports/allure-results
```

## 当前项目已使用的 Allure 写法

### feature

```python
@allure.feature("登录模块")
class TestLogin:
```

含义：报告中的大功能模块。

### story

```python
@allure.story("HRM系统登录")
```

含义：大模块下面的具体功能点。

### severity

```python
@allure.severity(allure.severity_level.BLOCKER)
```

含义：测试用例的重要程度。

常见级别：

- `BLOCKER`：阻塞级别
- `CRITICAL`：严重级别
- `NORMAL`：普通级别
- `MINOR`：较低级别
- `TRIVIAL`：很低级别

### dynamic.title

```python
allure.dynamic.title(desc)
```

含义：动态设置每条测试用例的标题。

当前项目里，`desc` 来自 `data/login.json`，例如：

- 登录成功
- 手机号未注册
- 密码错误
- 手机号为空

### step

```python
with allure.step("发送登录请求"):
    resp = LoginApi.hirm_login(req_data)

with allure.step("校验响应"):
    assert_login_common(resp, status_code, success, code, message)
```

含义：把测试过程拆成可读的步骤，方便在报告中查看。

## 下一步重点：attach

`allure.attach` 可以把请求参数、响应结果、日志、截图等内容放进报告。

接口自动化中最常用的是把请求和响应放进报告：

```python
import json
import allure

allure.attach(
    json.dumps(req_data, ensure_ascii=False, indent=2),
    "请求参数",
    allure.attachment_type.JSON
)

allure.attach(
    json.dumps(resp.json(), ensure_ascii=False, indent=2),
    "响应结果",
    allure.attachment_type.JSON
)
```

学习 `attach` 后，报告会更适合排查接口问题。
