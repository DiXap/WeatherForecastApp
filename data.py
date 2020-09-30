import jsonpickle, json
from city import City
from state import State
from forecast import access


def get_data(city: object):
    data = {}
    with open('./Data/' + city.name + '.json') as target:
        data = json.load(target)
    return data


def get_world():
    f = open('./Data/Wolrd.json')
    json_str = f.read()
    obj = jsonpickle.decode(json_str)
    return obj

d = get_world()

s = State('JP')

print(d)

print(get_data(City('Sapporo')))

