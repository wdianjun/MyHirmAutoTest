import requests
resp = requests.post(url='http://ihrm-java.itheima.net/api/sys/login', json={'mobile': '13800000002', 
                       'password': '929itheima.CN032@.20260612'})
print(resp.json())