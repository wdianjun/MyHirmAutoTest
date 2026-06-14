import requests
class LoginApi:
  @classmethod
  def hirm_login(self,json_data):
      reqs = requests.post(url='http://ihrm-java.itheima.net/api/sys/login',
                           json=json_data)
      return reqs


if __name__ == '__main__':
  json_data = {'mobile': '13800000002', 'password': '929itheima.CN032@.20260614'}
  res = LoginApi.hirm_login(json_data)
  print(res.json())