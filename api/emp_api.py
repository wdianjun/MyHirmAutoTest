import requests
class EmpApi:
  @classmethod
  def hirm_emp(cls,emp_headers, emp_json):
    resp = requests.post(url='http://ihrm-java.itheima.net/api/sys/user',
                            headers=emp_headers,
                            json=emp_json)
    return resp
  


if __name__ == '__main__':
  emp_headers = {'Authorization': 'ecaa06eb-b362-4a72-9a66-280cb676a6e6'}
  emp_json = {"username": "test001", "mobile": "13800000003", "workNumber": "1001"}
  res = EmpApi.hirm_emp(emp_headers, emp_json)
  print("添加结果：",res.json())