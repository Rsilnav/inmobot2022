import json


def get_data():
    f = open('data/database2.json', encoding='utf-8')
    return json.load(f)


def search_by_price(min_price=0, max_price=1000000):
    data = get_data()
    filtered_data = list(filter(lambda x: min_price <= x["price"] <= max_price, data))
    return filtered_data
