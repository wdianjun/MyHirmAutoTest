# AI 协作规则

## 我的学习背景

- 我正在学习接口自动化。
- 当前重点是 pytest + requests + Allure。
- 我希望 AI 像老师一样讲清楚原理，而不是只给代码。

## 协作偏好

- 修改代码前，先说明为什么要改。
- 尽量结合当前项目文件讲解。
- 代码示例要简单，适合练手项目。
- 不要一次性大改项目结构。
- 如果有多个方案，优先选择最适合初学者理解的方案。
- 解释时尽量用中文。

## 当前项目重点文件

- `scripts/test_login_params_log.py`：当前主要测试用例文件。
- `api/login_auto_api.py`：登录接口封装。
- `common/assert_common.py`：公共断言。
- `common/read_data.py`：测试数据读取。
- `data/login.json`：登录测试数据。
- `pytest.ini`：pytest 和 Allure 配置。

## 下次让 AI 恢复上下文的提示词

可以这样说：

```text
请先阅读 docs/progress.md、docs/allure-notes.md、docs/ai-rules.md，
然后结合 scripts/test_login_params_log.py 继续教我 Allure。
```

## 当前学习路线

1. 理解 pytest 如何执行接口测试。
2. 理解参数化测试如何读取 `data/login.json`。
3. 理解 Allure 报告的生成流程。
4. 学习 `feature`、`story`、`title`、`step`。
5. 学习 `allure.attach`。
6. 学习失败用例如何通过 Allure 报告排查。
