import json


def get_data():
    file = open('data.json', 'r')
    data = json.loads(file.read())
    file.close()
    return data

def get(key):
    return get_data()[key]


def set(key, value):
    data = get_data()
    data[key] = value
    file = open('data.json', 'w')
    file.write(json.dumps(data))
    file.close()
