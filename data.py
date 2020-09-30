from operator import eq
import jsonpickle, json
from city import City
from state import State
from states import States
from forecast import access


def get_data(city: object):
    data = {}
    with open('./Data/' + city.name + '.json') as target:
        data = json.load(target)
    return data


def get_world():
    #f = open('./Data/World.json')
    #json_str = f.read()
    #obj = jsonpickle.decode(json_str)
    #st = States()
    #st.set_dict(obj)
    #return st
    data = {}
    
    with open('./Data/World.json') as target:
        s = target.read()
        jp = jsonpickle.decode(s)
        data = jsonpickle.decode(jp)

    st = States()
    st.set_dict(data)
    return st




s = State('JP')

if s in d:
    print('he')

print(d.states.keys())

#print(get_data(City('Sapporo')))

