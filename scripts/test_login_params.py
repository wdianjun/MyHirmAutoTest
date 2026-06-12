import pytest

from api.login_auto_api import LoginApi
from common.assert_common import assert_login_common
from common.read_data import read_login_data


class TestLogin:
    # 参数化
    @pytest.mark.parametrize('desc,req_data,status_code,success,code,message',read_login_data())
    def test_hirm_login_success(self,desc,req_data,status_code,success,code,message):
        # json_data = {'mobile': '13800000002', 'password': '929itheima.CN032@.20260612'}
        resp = LoginApi.hirm_login(req_data)
        print(desc + ':',resp.json())
        assert_login_common(resp,status_code,success,code,message)
        # 断言
        # assert 200 == resp.status_code
        # assert True == resp.json().get('success')
        # assert 10000 == resp.json().get('code')
        # assert "操作成功！" in resp.json().get('message')

        # 1.对读数据的方法上传文件进行参数化
        # 2.打印日志



