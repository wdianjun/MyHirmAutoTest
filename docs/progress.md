# 项目进度

## 当前目标

学习接口自动化练手项目，并重点理解 pytest + requests + Allure 的使用方式。

## 当前项目情况

- 项目类型：接口自动化练手项目
- 当前重点接口：HRM 登录接口
- 测试框架：pytest
- 请求库：requests
- 数据驱动：读取 `data/login.json`
- 断言封装：`common/assert_common.py`
- 接口封装：`api/login_auto_api.py`
- 当前主要测试文件：`scripts/test_login_params_log.py`
- pytest 配置文件：`pytest.ini`

## 已完成内容

- 已经有登录接口封装：`LoginApi.hirm_login`
- 已经有登录测试数据：`data/login.json`
- 已经有参数化测试：`pytest.mark.parametrize`
- 已经有公共断言方法：`assert_login_common`
- 已经接入基础日志：`common/log_common.py`
- 已经接入 Allure 基础配置：
  - `--alluredir=reports/allure-results`
  - `--clean-alluredir`
- 已经使用 Allure 标记：
  - `@allure.feature("登录模块")`
  - `@allure.story("HRM系统登录")`
  - `@allure.severity(...)`
  - `allure.dynamic.title(desc)`
  - `with allure.step(...)`

## Allure 当前理解

- `reports/allure-results` 是 pytest 执行后生成的 Allure 原始结果目录。
- `reports/allure-report` 是通过 Allure 命令生成的可视化报告目录。
- `feature` 表示大模块。
- `story` 表示模块下的具体功能。
- `title` 表示每条测试用例在报告里的标题。
- `step` 表示测试过程中的关键步骤。
- `severity` 表示用例重要程度。

## 下一步计划

- 学习 `allure.attach`
- 把请求参数添加到 Allure 报告
- 把响应结果添加到 Allure 报告
- 理解失败用例在 Allure 报告中如何排查
- 学习 Allure 报告常用命令
- 整理一份适合当前项目的 Allure 使用模板

## 下次恢复上下文时可以这样说

请先阅读：

- `docs/progress.md`
- `docs/allure-notes.md`
- `docs/ai-rules.md`
- `scripts/test_login_params_log.py`
- `api/login_auto_api.py`
- `pytest.ini`

然后继续教我 Allure，并结合当前项目讲解。
