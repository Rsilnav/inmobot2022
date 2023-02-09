import datetime
import json
from json import JSONEncoder
from random import randint

from faker import Faker

Faker.seed(0)
fake = Faker('es_ES')


class House:
    def __init__(self):
        self.price = randint(10000, 1000000)
        self.address = fake.address()
        self.rooms = randint(1, 5)
        self.baths = randint(1, 3)
        self.phone = fake.phone_number()
        self.contact = fake.name()
        self.last_updated = fake.date_this_month()


class EmployeeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def json_default(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__


data = []

for _ in range(10000):
    h = House()
    data.append(h)

with open('database2.json', 'w', encoding='utf-8') as f:
    json_object = json.dumps(data, indent=4, cls=EmployeeEncoder, default=json_default)
    f.write(json_object)
