import json, os, requests, jsonpickle
from os import name
from state import State
from city import City
from states import States

api = 'API'
#states = {}
#data = {}
cities = []
states = States()

def access(city: object):
    data = {}
    with open('./Data/' + city.name + '.json') as target:
        data = json.load(target)
    return data


def consult(city: object, state: object, states):
    """
    docstring
    """
    ow_url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric'.format(city.name, state, api)
    
    if city in state.cities:
        return access(city)
    
    try:
        response = requests.get(ow_url)   
    except requests.exceptions.RequestException:
        return

    data = json.loads(response.text)
    with open('./Data/' + city.name + '.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    try:
        city.set_dt(data['dt'])
    except:
        pass

    state.cities.append(city)
    state.cities.sort()
    #cities.update({ct.name : ct.dt})
    #jsonstate = StateEncoder().encode(state)

    #states[state] = state.cities;
    states.add(state)
    
    return data;
    

tokyo = City('Tokyo')
jp = State('JP')


print(consult(tokyo, jp, states))
consult(tokyo, jp, states)
consult(City('Sapporo'), jp, states)
consult(City('Okinawa'), jp, states)

consult(City('Cancun'), State('MX'), states)

c = City('Tokyo')
#c1 = City('Mom')
#d = [c, c1]

if jp in states:
    print(tokyo)

print(
    states
)

jsonpickle.set_encoder_options('simplejson', sort_keys = True)
js = jsonpickle.encode(states, unpicklable=False)

with open('./Data/World.json', 'w', encoding='utf-8') as outfile:
    json.dump(js, outfile)



print(js)