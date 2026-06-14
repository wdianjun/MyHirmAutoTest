import json

from config import BASE_DIR
from common.json_schema_validator import validate_json_by_schema


def read_login_data(filename):
    # --- JSON Schema validation ---
    schema_file = BASE_DIR + '/data/login_schema.json'
    validate_json_by_schema(filename, schema_file)

    with open(filename, "r", encoding="utf-8") as f:
        login_list = []
        data = json.load(f)
        for i in data:
            res = tuple(i.values())
            login_list.append(res)
        return login_list


if __name__ == '__main__':
    print(read_login_data(BASE_DIR + '/data/login.json'))
