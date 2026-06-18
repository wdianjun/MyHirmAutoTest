import allure
import requests


class LoginApi:
    @classmethod
    @allure.step("POST /api/sys/login")
    def hirm_login(self, json_data):
        reqs = requests.post(url='http://ihrm-java.itheima.net/api/sys/login',
                             json=json_data)
        return reqs


if __name__ == '__main__':
    json_data = {'mobile': '13800000002', 'password': '929itheima.CN032@.20260618'}
    res = LoginApi.hirm_login(json_data)
    print(res.json())
