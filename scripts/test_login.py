from api.login_auto_api import LoginApi
from common.assert_common import assert_login_common


class TestLogin:
    @classmethod
    def test_hirm_login_success(self):
        json_data = {'mobile': '13800000002', 'password': '929itheima.CN032@.20260613'}
        resp = LoginApi.hirm_login(json_data)
        print("登录成功",resp.json())
        assert_login_common(resp,200,True,10000,"操作成功！")
        # 断言
        # assert 200 == resp.status_code
        # assert True == resp.json().get('success')
        # assert 10000 == resp.json().get('code')
        # assert "操作成功！" in resp.json().get('message')



