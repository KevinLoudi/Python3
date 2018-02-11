# Filename: test_api.py

import json

def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

def load_data():
    data = ''
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

def test_json():
    data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
    }
    save_data(data)
    name, price, share = load_data()
    print(data[name], data[price], data[share])

def say_hi():
    print('Hi, this is mymodule speaking.')

version = '0.1'

# End of test_api.py