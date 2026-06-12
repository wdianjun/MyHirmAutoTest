import json

from config import BASE_DIR


def read_login_data():
    with open(BASE_DIR + '/data/login.json' ,"r",encoding="utf-8") as f:
        login_list = []
        data = json.load(f)
        for i in data:
            # 以下两种方法都能去掉desc
            # i.pop('desc')
            # tuple(i.values())[1:]
            res = tuple(i.values())
            login_list.append(res)
        return login_list
        # print(res)
        # print(data)


if __name__ == '__main__':
    print(read_login_data())