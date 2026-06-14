import logging

import pytest

from api.login_auto_api import LoginApi
from common.assert_common import assert_login_common
from common.log_common import init_log_config
from common.read_data import read_login_data
from config import BASE_DIR


class TestLogin:
    # 初始化日志
    init_log_config(BASE_DIR + '/log/hirm_login.log',interval=3,backupCount=7)
    # 参数化
    filename = BASE_DIR + '/data/login.json'
    @pytest.mark.parametrize('desc,req_data,status_code,success,code,message',read_login_data(filename))
    def test_hirm_login_success(self,desc,req_data,status_code,success,code,message):
        # json_data = {'mobile': '13800000002', 'password': '929itheima.CN032@.20260612'}
        resp = LoginApi.hirm_login(req_data)
        # print(desc + ':',resp.json())
        # 输出日志
        logging.info(f"{desc}:{resp.json()}")
        assert_login_common(resp,status_code,success,code,message)

        # 1.对读数据的方法上传文件进行参数化
        # 2.打印日志



